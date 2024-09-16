import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from image_bank_dialog import ImageBankDialog


class Input_Data:
    def __init__(self, ui, parent, button_map=None, button_remove=None, images_list=None, box_coords=None,
                 linetext_names=None, grid_names=None, page_name_index=None):
        self.ui = ui
        self.parent = parent
        # self.images_list = [[] for _ in range(11)]
        self.button_map = button_map
        self.button_remove = button_remove
        self.images_list = images_list
        self.box_coords = box_coords
        self.linetext_names = linetext_names
        self.grid_names = grid_names
        self.page_name_index = page_name_index

        self.image_entries = []
        self.text_entries = []
        self.setup_ui()

    def setup_ui(self):
        if (self.page_name_index):
            self.set_all_pages_visible()
            self.page_name_index.currentIndexChanged.connect(self.on_combobox_changed)

        if self.button_map:
            for button_name, label_name in self.button_map.items():
                button = getattr(self.ui, button_name)
                label = getattr(self.ui, label_name)
                button.clicked.connect(lambda _, lbl=label: self.open_image_bank(lbl))
        if self.button_remove:
            for button_name, label_name in self.button_remove.items():
                button = getattr(self.ui, button_name)
                label = getattr(self.ui, label_name)
                button.clicked.connect(lambda _, lbl=label: self.remove_img_path(lbl))
    def on_combobox_changed(self, index):
        if index == 0:
            self.currentIndex = 0
            self.set_layout_visible(self.grid_names[0], False)
            self.set_layout_visible(self.grid_names[1], False)
            self.set_layout_visible(self.grid_names[2], False)
            self.set_layout_visible(self.grid_names[3], False)
            self.set_layout_visible(self.grid_names[4], False)
            self.set_layout_visible(self.grid_names[5], False)
            self.set_layout_visible(self.grid_names[6], False)
            self.set_layout_visible(self.grid_names[7], False)
        elif index == 1:  # Option 2
            self.currentIndex = 1
            self.set_layout_visible(self.grid_names[0], True)
            self.set_layout_visible(self.grid_names[1], True)
            self.set_layout_visible(self.grid_names[2], True)
            self.set_layout_visible(self.grid_names[3], True)
            self.set_layout_visible(self.grid_names[4], False)
            self.set_layout_visible(self.grid_names[5], False)
            self.set_layout_visible(self.grid_names[6], False)
            self.set_layout_visible(self.grid_names[7], False)
        elif index == 2:  # Option 3
            self.currentIndex = 2
            self.set_layout_visible(self.grid_names[0], True)
            self.set_layout_visible(self.grid_names[1], True)
            self.set_layout_visible(self.grid_names[2], True)
            self.set_layout_visible(self.grid_names[3], True)
            self.set_layout_visible(self.grid_names[4], True)
            self.set_layout_visible(self.grid_names[5], True)
            self.set_layout_visible(self.grid_names[6], False)
            self.set_layout_visible(self.grid_names[7], False)
        elif index == 3:  # Option 3
            self.currentIndex = 3
            self.set_layout_visible(self.grid_names[0], True)
            self.set_layout_visible(self.grid_names[1], True)
            self.set_layout_visible(self.grid_names[2], True)
            self.set_layout_visible(self.grid_names[3], True)
            self.set_layout_visible(self.grid_names[4], True)
            self.set_layout_visible(self.grid_names[5], True)
            self.set_layout_visible(self.grid_names[6], True)
            self.set_layout_visible(self.grid_names[7], True)
    def set_all_pages_visible(self):
        self.set_layout_visible(self.grid_names[0], False)
        self.set_layout_visible(self.grid_names[1], False)
        self.set_layout_visible(self.grid_names[2], False)
        self.set_layout_visible(self.grid_names[3], False)
        self.set_layout_visible(self.grid_names[4], False)
        self.set_layout_visible(self.grid_names[5], False)
        self.set_layout_visible(self.grid_names[6], False)
        self.set_layout_visible(self.grid_names[7], False)

    def set_layout_visible(self, layout, visible):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(visible)

    def enter_text(self):
        self.text_entries = []
        for entry in self.linetext_names:
            widget = entry['widget']
            x = entry['x']
            y = entry['y']
            color = entry['color']
            font_size = entry['font_size']
            font_name = entry['font_name']
            centered = entry['centered']
            # Retrieve text based on widget type
            if isinstance(widget, QtWidgets.QLineEdit):
                text = widget.text()
            elif isinstance(widget, QtWidgets.QTextEdit):
                text = widget.toPlainText()
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                text = widget.toPlainText()
            else:
                break
            if centered == "true" or centered == "left" or centered == "left_bullet" or centered == "true_dyn":
                x_max = entry['x_max']
                y_max = entry['y_max']
                line_height = entry['line_height']
                self.text_entries.append({'text': text, 'x': x, 'y': y, 'color': color, 'font_size': font_size,
                                          'font_name': font_name, 'line_height': line_height,
                                          'centered': centered, 'x_max': x_max, 'y_max': y_max})
            elif centered == "spacing":
                x_max = entry['x_max']
                letter_spacing = entry['letter_spacing']
                self.text_entries.append({'text': text, 'x': x, 'y': y, 'color': color, 'font_size': font_size,
                                         'font_name': font_name, 'centered': centered, 'letter_spacing': letter_spacing,
                                          'x_max': x_max})
            else:
                x_max = entry['x_max']
                self.text_entries.append({'text': text, 'x': x, 'y': y, 'color': color, 'font_size': font_size,
                                          'font_name': font_name, 'centered': centered, 'x_max': x_max})

        return self.text_entries

    def append_img_paths(self, images_list, box_list, number_imgs):
        for index, label in enumerate(images_list[:number_imgs]):
            lbl = getattr(self.ui, label)
            path = lbl.toolTip()
            box_list[index]['path'] = path
            if index > len(box_list):
                break

    def set_coords(self, img_box, number_imgs):
        if img_box == 0:
            self.append_img_paths(self.images_list[0], self.box_coords[0][number_imgs - 1], number_imgs)
            for lst in self.box_coords[0][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 1:
            self.append_img_paths(self.images_list[1], self.box_coords[1][number_imgs - 1], number_imgs)
            for lst in self.box_coords[1][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 2:
            self.append_img_paths(self.images_list[2], self.box_coords[2][number_imgs - 1], number_imgs)
            for lst in self.box_coords[2][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 3:
            self.append_img_paths(self.images_list[3], self.box_coords[3][number_imgs - 1], number_imgs)
            for lst in self.box_coords[3][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 4:
            self.append_img_paths(self.images_list[4], self.box_coords[4][number_imgs - 1], number_imgs)
            for lst in self.box_coords[4][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 5:
            self.append_img_paths(self.images_list[5], self.box_coords[5][number_imgs - 1], number_imgs)
            for lst in self.box_coords[5][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 6:
            self.append_img_paths(self.images_list[6], self.box_coords[6][number_imgs - 1], number_imgs)
            for lst in self.box_coords[6][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 7:
            self.append_img_paths(self.images_list[7], self.box_coords[7][number_imgs - 1], number_imgs)
            for lst in self.box_coords[7][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 8:
            self.append_img_paths(self.images_list[8], self.box_coords[8][number_imgs - 1], number_imgs)
            for lst in self.box_coords[8][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 9:
            self.append_img_paths(self.images_list[9], self.box_coords[9][number_imgs - 1], number_imgs)
            for lst in self.box_coords[9][(number_imgs - 1)]:
                self.image_entries.append(lst)
        elif img_box == 10:
            self.append_img_paths(self.images_list[10], self.box_coords[10][number_imgs - 1], number_imgs)
            for lst in self.box_coords[10][(number_imgs - 1)]:
                self.image_entries.append(lst)

    def get_number_of_imgs(self, i):
        number = 0
        for label in self.images_list[i]:
            lbl = getattr(self.ui, label)
            if lbl.toolTip():
                number += 1
            else:
                continue
        return number

    def enter_images(self):
        self.image_entries = []
        for i in range(len(self.images_list)):
            number_imgs = self.get_number_of_imgs(i)
            if number_imgs > 0:
                self.set_coords(i, number_imgs)
        return self.image_entries

    def open_image_bank(self, label):
        # image_folder = os.path.join(os.path.dirname(__file__), 'ui/resources/logos')
        image_folder = 'app_imgs'
        os.makedirs(image_folder, exist_ok=True)
        dialog = ImageBankDialog(image_folder, self.parent)
        if dialog.exec() == QDialog.Accepted:
            self.ui.image_path = dialog.selected_image_path
            pixmap = QPixmap(self.ui.image_path)
            scaled_pixmap = pixmap.scaled(50, 50, aspectRatioMode=1)  # Scale the pixmap to a smaller size
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(True)

            label.setToolTip(self.ui.image_path)

    def remove_img_path(self, label):
        label.clear()
        label.setToolTip('')
        label.setText("img")

    def has_content(self):
        # Check if there is any text or image content
        text_entries = self.enter_text()
        for entry in text_entries:
            if entry['text']:
                return True
        return False
