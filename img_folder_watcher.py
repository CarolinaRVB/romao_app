import os
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image, ImageFilter
import time
import sqlite3

# image_folder = Path("user_images")  # Folder where users add images

processing_images = set()  # To track actively processing images


def is_image_processed(image_path):
    """Check if the image path exists in the database."""
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"image: {image_path}")
    cursor.execute('SELECT image_path FROM images_paths WHERE image_path = ?', (image_path,))
    result = cursor.fetchone()
    conn.close()

    return result is not None


def update_processed_image_path(image_path):
    """Add the processed image path to the database."""
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images_paths (image_path)
        VALUES (?)
    ''', (image_path,))
    conn.commit()
    conn.close()


class ImageHandler(FileSystemEventHandler):
    """Handles image folder events for new or modified images."""

    def on_created(self, event):
        if event.is_directory or not event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        # Check if the image is being processed already
        if event.src_path in processing_images:
            return  # Skip if already processing

        process_image(event.src_path)  # Process the newly added image

    def on_modified(self, event):
        if event.is_directory or not event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        # Check if the image is being processed already
        if event.src_path in processing_images:
            return  # Skip if already processing

        process_image(event.src_path)


def wait_for_file_ready(image_path):
    """Wait until the file is accessible."""
    while True:
        try:
            with Image.open(image_path):
                break  # Exit if the file opens successfully
        except (IOError, FileNotFoundError):
            time.sleep(0.5)  # Wait and retry


def calculate_scaled_dimensions(img, max_width, max_height):
    """Calculates the scaled width and height while preserving aspect ratio."""
    width, height = img.size

    # Calculate the scaling factor
    scale_factor = min(max_width / width, max_height / height)

    # Calculate new width and height
    scaled_width = int(width * scale_factor)
    scaled_height = int(height * scale_factor)

    return scaled_width, scaled_height, scale_factor
def process_image(image_path):
    """Process the image in place."""
    global processing_images
    try:
        # Wait for the file to be ready
        wait_for_file_ready(image_path)

        if image_path in processing_images:
            return  # Already processing this image

        # Add the image to the processing set
        processing_images.add(image_path)

        # Check if file has already been processed
        if is_image_processed(image_path):
            print(f"Skipped already processed image: {image_path}")
            return  # Skip reprocessing the image

        # Open and process the image
        img = Image.open(image_path)
        processed_image = remove_background(img)  # Assume remove_background is defined

        scaled_width, scaled_height, _ = calculate_scaled_dimensions(processed_image, 50, 50)
        # resized_img = processed_image.resize((scaled_width, scaled_height))

        # Determine the format based on the file extension
        file_dir, file_name = os.path.split(image_path)
        file_base, file_ext = os.path.splitext(file_name)

        # Modify the original file name to include the width, but only if it's not already included
        if f"_{scaled_width}" not in file_base:
            new_file_name = f"{file_base}_{scaled_width}_{scaled_height}{file_ext}"
        else:
            new_file_name = file_name  # Keep the original if width is already included

        new_file_path = os.path.join(file_dir, new_file_name)

        # Save the resized image with good quality
        os.remove(image_path)  # Remove the original file

        if file_ext in ['.jpg', '.jpeg']:
            processed_image = processed_image.convert("RGB")  # Convert to RGB for JPEG
            processed_image.save(new_file_path, format='JPEG', quality=90)  # Save with high quality
        elif file_ext == '.png':
            processed_image.save(new_file_path, format='PNG', compress_level=1)  # Save with minimal compression for better quality
        else:
            processed_image.save(new_file_path)  # Save in the default format

        img.close()

        # Mark the image as processed in the database
        update_processed_image_path(image_path)
        print(f"Processed: {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
    finally:
        # Remove the image from processing set
        processing_images.discard(image_path)


def start_image_watcher(image_folder):
    """Start watching the image folder for changes."""
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, str(image_folder), recursive=True)  # Set recursive to True
    observer.start()

    # Process existing images in the folder and its subfolders
    for root, dirs, files in os.walk(image_folder):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, filename)
                process_image(image_path)  # Process existing images

    return observer


def stop_image_watcher(observer):
    """Stop the image watcher."""
    observer.stop()
    observer.join()


def remove_background(image: Image.Image) -> Image.Image:
    """Removes the white background or transparent areas from the image and crops excess space."""
    image = image.convert('RGBA')
    datas = image.getdata()
    new_data = []
    tolerance = 240

    for item in datas:
        if item[0] >= tolerance and item[1] >= tolerance and item[2] >= tolerance:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)
    bbox = image.getbbox()
    image = image.filter(ImageFilter.GaussianBlur(1))

    if bbox:
        cropped_image = image.crop(bbox)
        return cropped_image

    return image
