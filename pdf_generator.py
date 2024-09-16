import os.path
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
import os

def wrap_text(text, max_width, font_name, font_size, can):
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
    lines = text.split('\n')
    wrapped_lines = []

    hollow_bullet = '-' + ' '
    for line in lines:
        # Check the number of leading tabs in the line
        leading_tabs = len(line) - len(line.lstrip('\t'))

        # If there are leading tabs, indent and use the hollow bullet
        if leading_tabs > 0:
            # Calculate the indentation space (assuming 4 spaces per tab)
            indent = " " * (leading_tabs * 4)
            current_line = indent + hollow_bullet
        else:
            current_line = bullet_char

        words = line.lstrip().split()  # Split the line into words, removing leading whitespace
        for word in words:
            # If the word fits in the current line, add it
            if can.stringWidth(current_line + word, font_name, font_size) <= max_width:
                current_line += word + " "
            else:
                # Add the current line to wrapped lines
                wrapped_lines.append(current_line.rstrip())
                # Start a new line with indentation and the word
                current_line = indent + word + " " if leading_tabs > 0 else word + " "

        if current_line.strip():
            wrapped_lines.append(current_line.rstrip())  # Add any remaining line to wrapped lines

    return wrapped_lines


def adjust_line_height(lines, line_height, minimum_height, y):
    current_y = y

    for line in lines:
        if current_y - line_height >= minimum_height:
            current_y -= line_height
        else:
            return False
    else:
        return True

def draw_centered_dyn_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height_ratio, can):
    lines = wrap_text(text, max_width, font_name, font_size, can)
    current_y = y

    # Calculate line height as a ratio of font size
    line_height = font_size * line_height_ratio

    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.01
        line_height = font_size * line_height_ratio  # Update line height consistently with new font size
        lines = wrap_text(text, max_width, font_name, font_size, can)  # Re-wrap the text with the new font size

    can.setFont(font_name, font_size)
    for line in lines:
        line_width = can.stringWidth(line, font_name, font_size)
        centered_x = x + (max_width - line_width) / 2
        can.drawString(centered_x, current_y, line)
        current_y -= line_height  # Decrease y by line_height to move to the next line




def draw_centered_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height, can):
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
    lines = wrap_left_text_with_bullets(text, max_width, font_name, font_size, can, bullet_char)
    line_height = font_size * line_height_ratio


    # Calculate line height as a ratio of font size
    line_height = font_size * line_height_ratio

    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.01
        line_height = font_size * line_height_ratio # Update line height consistently with new font size
        lines = wrap_left_text_with_bullets(text, max_width, font_name, font_size, can)  # Re-wrap the text with the new font size

    can.setFont(font_name, font_size)

    current_y = y
    for line in lines:
        can.drawString(x, current_y, line)
        current_y -= line_height

def draw_left_text(text, x, y, max_width, minimum_height, font_name, font_size, line_height_ratio, can):
    lines = wrap_text(text, max_width, font_name, font_size, can)
    line_height = font_size * line_height_ratio

    while not adjust_line_height(lines, line_height, minimum_height, y):
        font_size -= 0.1
        line_height = font_size * line_height_ratio # Update line height consistently with new font size
        lines = wrap_left_text_with_bullets(text, max_width, font_name, font_size, can)  # Re-wrap the text with the new font size

    current_y = y
    for line in lines:
        # if current_y - line_height >= minimum_height:
        can.drawString(x, current_y, line)
        current_y -= line_height
        # else:
        #     break

def adjust_line_width(can, line, font_name, font_size, max_width):
    sentence = ""

    for word in line:
        if can.stringWidth(sentence + word, font_name, font_size) <= max_width:
            sentence += word + " "
        else:
            return False
    return True

def draw_left(text, x, y, max_width, font_name, font_size, can):
    lines = wrap_text(text, max_width, font_name, font_size, can)

    while not adjust_line_width(can, lines, font_name, font_size, max_width):
        font_size -= 0.01
        lines = wrap_text(text, max_width, font_name, font_size, can)  # Re-wrap the text with the new font size

    can.setFont(font_name, font_size)
    for line in lines:
        line_width = can.stringWidth(line, font_name, font_size)
        centered_x = x + (max_width - line_width) / 2
        can.drawString(centered_x, y, line)
def draw_spaced_letters(x, y, letter_spacing, max_width, font_name, font_size, text, can):
    lines = wrap_text(text, max_width, font_name, font_size, can)

    while not adjust_line_width(can, lines, font_name, font_size, max_width):
        font_size -= 0.01
        lines = wrap_text(text, max_width, font_name, font_size, can)  # Re-wrap the text with the new font size

    current_x = x
    for char in text:
        can.drawString(current_x, y, char)
        current_x += can.stringWidth(char) + letter_spacing

    can.setFont(font_name, font_size)

def generate_pdf(linetext_entries, image_entries, template, output_filename, color, image_position=None):
    # Create a PDF with the text and optionally the image
    packet = BytesIO()

    # Set the custom page size
    page_width = 800
    page_height = 1500
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))

    # Set text color to white
    can.setFillColorRGB(*color)  # RGB values for white

    # Set font and font size
    fonts_path = "ui/fonts/static"
    font_list = ["Montserrat-Medium.ttf", "Montserrat-SemiBold.ttf", "Montserrat-Bold.ttf", "Montserrat-ExtraBold.ttf",
                 "Montserrat-Black.ttf", "Montserrat-Thin.ttf", "Montserrat-Regular.ttf", "BebasNeue-Regular.ttf"]

    for item in font_list:
        font_path = os.path.join(fonts_path, item)
        font = item.strip(".ttf")
        pdfmetrics.registerFont(TTFont(font, font_path))

    font_name = "Montserrat-Medium"
    font_size = 12  # Adjust font size as needed

    can.setFont(font_name, font_size)

    for entry in linetext_entries:
        text = entry['text']
        if not text:
            continue
        x = entry['x']
        y = entry['y']
        color = entry['color']
        font_name = entry['font_name']
        font_size = entry['font_size']
        can.setFont(font_name, font_size)
        can.setFillColorRGB(*color)
        centered = entry['centered']
        if centered == "true_dyn":
            x_max = entry['x_max']
            y_max = entry['y_max']
            line_height = entry['line_height']
            draw_centered_dyn_text(text, x, y, x_max, y_max, font_name, font_size, line_height, can)
        elif centered == 'left_bullet':
            x_max = entry['x_max']
            y_max = entry['y_max']
            line_height = entry['line_height']
            draw_left_text_bullet(text, x, y, x_max, y_max, font_name, font_size, line_height, can, bullet_char="• ")
        elif centered == 'left':
            x_max = entry['x_max']
            y_max = entry['y_max']
            line_height = entry['line_height']
            draw_left_text(text, x, y, x_max, y_max, font_name, font_size, line_height, can)
        elif centered == 'spacing':
            x_max = entry['x_max']
            letter_spacing = entry['letter_spacing']
            draw_spaced_letters(x, y, letter_spacing, x_max, font_name, font_size, text, can)
        elif centered == 'false':
            x_max = entry['x_max']
            draw_left(text, x, y, x_max, font_name, font_size, can)

    # If an image is selected, draw it on the PDF at the specified position
    for image_entry in image_entries:
        image_path = image_entry['path']
        if not image_path or image_path == "img":
            continue
        image_x = image_entry['x']
        image_y = image_entry['y']
        image_size = 50
        can.drawImage(image_path, image_x, image_y, width=image_size, height=image_size, mask='auto')

    can.save()

    target_folder = 'pdfs'

    os.makedirs(target_folder, exist_ok=True)
    # Move to the beginning of the StringIO buffer
    packet.seek(0)

    output_file = os.path.join(target_folder, output_filename)
    # Read the existing PDF template
    template_path = os.path.join(os.path.dirname(__file__), template)
    with open(template_path, "rb") as template_file:
        existing_pdf = PdfReader(template_file)
        output = PdfWriter()

        # Read the new PDF
        new_pdf = PdfReader(packet)

        if len(existing_pdf.pages) > 0 and len(new_pdf.pages) > 0:
            template_page = existing_pdf.pages[0]
            new_page = new_pdf.pages[0]
            template_page.merge_page(new_page)
            output.add_page(template_page)

        # Write output to a real file
        with open(output_file, "wb") as outputStream:
            output.write(outputStream)
