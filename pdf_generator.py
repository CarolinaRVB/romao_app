import os
import sys
import os.path
import tempfile
from io import BytesIO
from collections import defaultdict
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter


def generate_pdf(linetext_entries, image_entries, template, output_filename, color):
    """Generates a PDF by drawing text and images onto a template and saving it to a file."""
    packet = BytesIO()
    page_width = 800
    page_height = 1500
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    can.setFillColorRGB(*color)
    draw_text(can, linetext_entries)
    draw_images(can, image_entries)
    can.save()

    target_folder = os.path.join(tempfile.gettempdir(), 'romao_pdfs')
    os.makedirs(target_folder, exist_ok=True)
    packet.seek(0)
    output_file = os.path.join(target_folder, output_filename)

    with open(template, "rb") as template_file:
        existing_pdf = PdfReader(template_file)
        output = PdfWriter()
        new_pdf = PdfReader(packet)
        if len(existing_pdf.pages) > 0 and len(new_pdf.pages) > 0:
            template_page = existing_pdf.pages[0]
            new_page = new_pdf.pages[0]
            template_page.merge_page(new_page)
            output.add_page(template_page)

        with open(output_file, "wb") as outputStream:
            output.write(outputStream)


def resource_path(relative_path):
    """Returns the absolute path to a resource, handling both development and PyInstaller modes."""
    if hasattr(sys, '_MEIPASS'):
        # The path where the files are bundled by PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # In development mode, just use the relative path
        return os.path.join(os.path.dirname(__file__), relative_path)


def wrap_text(text, max_width, font_name, font_size, can):
    """Wraps the input text to fit within the specified maximum width and returns the wrapped lines."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if can.stringWidth(current_line + word, font_name, font_size) <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines


def wrap_left_text_with_bullets(text, max_width, font_name, font_size, can, bullet_char="• "):
    """Wraps text with bullet points, handling indentation for sub-bullets."""
    lines = text.split('\n')
    wrapped_lines = []

    hollow_bullet = '-' + ' '
    for line in lines:
        leading_tabs = len(line) - len(line.lstrip('\t'))
        if leading_tabs > 0:
            indent = " " * (leading_tabs * 4)
            current_line = indent + hollow_bullet
        else:
            current_line = bullet_char
        words = line.lstrip().split()
        for word in words:
            if can.stringWidth(current_line + word, font_name, font_size) <= max_width:
                current_line += word + " "
            else:
                wrapped_lines.append(current_line.rstrip())
                current_line = indent + word + " " if leading_tabs > 0 else word + " "
        if current_line.strip():
            wrapped_lines.append(current_line.rstrip())

    return wrapped_lines


def adjust_line_height(lines, line_height, minimum_height, y):
    """Adjusts line height to ensure text fits within the available vertical space."""
    current_y = y
    for _ in lines:
        if current_y - line_height >= minimum_height:
            current_y -= line_height
        else:
            return False
    else:
        return True


def draw_centered_dyn_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height_ratio, can):
    """Dynamically adjusts text size and draws it centered within the specified dimensions."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    current_y = y
    line_height = font_size * line_height_ratio
    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.01
        line_height = font_size * line_height_ratio
        lines = wrap_text(text, max_width, font_name, font_size, can)
    can.setFont(font_name, font_size)
    for line in lines:
        line_width = can.stringWidth(line, font_name, font_size)
        centered_x = x + (max_width - line_width) / 2
        can.drawString(centered_x, current_y, line)
        current_y -= line_height


def draw_centered_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height, can):
    """Draws text centered within the specified space without adjusting font size dynamically."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    line_height = font_size * line_height
    current_y = y
    for line in lines:
        if current_y - line_height >= minimum_height:
            line_width = can.stringWidth(line, font_name, font_size)
            centered_x = x + (max_width - line_width) / 2
            can.drawString(centered_x, current_y, line)
            current_y -= line_height
        else:
            break


def draw_left_text_bullet(text, x, y, max_width, minimum_height, font_name, font_size, line_height_ratio, can, bullet_char):
    """Draws left-aligned bullet-pointed text, dynamically adjusting size to fit within constraints."""
    lines = wrap_left_text_with_bullets(text, max_width, font_name, font_size, can, bullet_char)
    line_height = font_size * line_height_ratio
    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.01
        line_height = font_size * line_height_ratio
        lines = wrap_left_text_with_bullets(text, max_width, font_name, font_size, can)
    can.setFont(font_name, font_size)
    current_y = y
    for line in lines:
        can.drawString(x, current_y, line)
        current_y -= line_height


def draw_left_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height_ratio, can):
    """Draws left-aligned text, dynamically adjusting size to fit within the available space."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    line_height = font_size * line_height_ratio
    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.1
        line_height = font_size * line_height_ratio
        lines = wrap_text(text, max_width, font_name, font_size, can)
    current_y = y
    for line in lines:
        can.drawString(x, current_y, line)
        current_y -= line_height


def adjust_line_width(can, line, font_name, font_size, max_width):
    """Adjusts text width by reducing font size until the line fits within the specified width."""
    sentence = ""
    for word in line:
        if can.stringWidth(sentence + word, font_name, font_size) <= max_width:
            sentence += word + " "
        else:
            return False
    return True


def draw_left(text, x, y, max_width, font_name, font_size, can):
    """Draws left-aligned text, adjusting font size to fit the specified width."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    while not adjust_line_width(can, lines, font_name, font_size, max_width):
        font_size -= 0.01
        lines = wrap_text(text, max_width, font_name, font_size, can)

    can.setFont(font_name, font_size)
    for line in lines:
        line_width = can.stringWidth(line, font_name, font_size)
        centered_x = x + (max_width - line_width) / 2
        can.drawString(centered_x, y, line)


def draw_spaced_letters(x, y, letter_spacing, max_width, font_name, font_size, text, can):
    """Draws text with custom spacing between letters, adjusting font size if necessary."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    while not adjust_line_width(can, lines, font_name, font_size, max_width):
        font_size -= 0.01
        lines = wrap_text(text, max_width, font_name, font_size, can)

    current_x = x
    for char in text:
        can.drawString(current_x, y, char)
        current_x += can.stringWidth(char) + letter_spacing

    can.setFont(font_name, font_size)


def extract_width_height(file_name):
    """Extracts width and height from the image file name based on the naming convention."""
    file_base, _ = os.path.splitext(file_name)
    parts = file_base.split('_')
    if len(parts) >= 3:
        width = int(parts[-2])
        height = int(parts[-1])
        return width, height
    return None, None


def get_total_images_width(image_entries, gap=4):
    """Calculates the total width of all images when scaled, including custom spacing."""
    total_width = 0
    for entry in image_entries:
        image_path = entry['path']
        scaled_width, _ = extract_width_height(image_path)
        total_width += scaled_width
    total_width += gap * (len(image_entries) - 1)
    return total_width


def draw_images(can, image_entries):
    """Draws a set of images on the canvas, dynamically adjusting gaps to fit within available space."""
    max_width = 235
    initial_gap = 4
    boxes = defaultdict(list)
    for entry in image_entries:
        boxes[entry['box_id']].append(entry)
    for box_id, entries in boxes.items():
        total_imgs_width = get_total_images_width(entries) if entries else 0
        rest_space = max_width - total_imgs_width
        gap = initial_gap
        while rest_space > 10 and gap <= 10:
            total_imgs_width = get_total_images_width(entries, gap)
            rest_space = max_width - total_imgs_width
            if rest_space > 10:
                gap += 2
        if entries and 'start_x' in entries[0]:
            start_x = entries[0]['start_x'] + rest_space / 2
        for image_entry in entries:
            image_path = image_entry['path']
            if not image_path or image_path == "img":
                continue
            scaled_width, scaled_height = extract_width_height(image_path)
            can.drawImage(image_path, start_x, image_entry['y'], width=scaled_width, height=scaled_height,
                          mask='auto')
            start_x += scaled_width + gap


def draw_text(can, linetext_entries):
    """Draws text entries on the canvas based on their defined attributes, such as font, position, and alignment."""
    for entry in linetext_entries:
        text = entry['text']
        if not text:
            continue
        can.setFont(entry['font_name'], entry['font_size'])
        can.setFillColorRGB(*entry['color'])
        centered = entry['centered']
        if centered == "true_dyn":
            draw_centered_dyn_text(text, entry['x'], entry['y'], entry['x_max'], entry['y_max'], entry['font_name'],
                                   entry['font_size'], entry['line_height'], can)
        elif centered == 'left_bullet':
            draw_left_text_bullet(text, entry['x'], entry['y'], entry['x_max'], entry['y_max'], entry['font_name'],
                                  entry['font_size'], entry['line_height'], can, bullet_char="• ")
        elif centered == 'left':
            draw_left_text(text, entry['x'], entry['y'], entry['x_max'], entry['y_max'], entry['font_name'],
                           entry['font_size'], entry['line_height'], can)
        elif centered == 'spacing':
            draw_spaced_letters(entry['x'], entry['y'], entry['letter_spacing'], entry['x_max'], entry['font_name'],
                                entry['font_size'], text, can)
        elif centered == 'false':
            draw_left(text, entry['x'], entry['y'], entry['x_max'], entry['font_name'], entry['font_size'], can)
