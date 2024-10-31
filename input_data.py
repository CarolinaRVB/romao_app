import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from image_bank_dialog import ImageBankDialog


class Input_Data:
    def __init__(self, ui, parent, button_map=None, button_remove=None, images_list=None, box_coords=None,
                 linetext_names=None, grid_names=None, page_name_index=None):
        self.ui = ui
        self.parent = parent
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
        index_map = [0, 4, 6, 8]

        selected = index_map[index]
        self.currentIndex = index
        for i in range(selected):
            self.set_layout_visible(self.grid_names[i], True)
        for i in range(selected, 8):
            self.set_layout_visible(self.grid_names[i], False)

    def set_all_pages_visible(self):
        for i in range(8):
            self.set_layout_visible(self.grid_names[i], False)

    def set_layout_visible(self, layout, visible):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(visible)

    def enter_text(self):
        self.text_entries = []
        for entry in self.linetext_names:
            widget = entry['widget']
            centered = entry['centered']
            if isinstance(widget, QtWidgets.QLineEdit):
                text = widget.text()
            elif isinstance(widget, QtWidgets.QTextEdit):
                text = widget.toPlainText()
            elif isinstance(widget, QtWidgets.QPlainTextEdit):
                text = widget.toPlainText()
            else:
                break
            self.text_entries.append({'text': text, 'x': entry['x'], 'y': entry['y'], 'color': entry['color'],
                                      'font_size': entry['font_size'], 'font_name': entry['font_name'],
                                      'centered': centered, 'x_max': entry['x_max']})
            if centered == "true" or centered == "left" or centered == "left_bullet" or centered == "true_dyn":
                self.text_entries[-1]['y_max'] = entry['y_max']
                self.text_entries[-1]['line_height'] = entry['line_height']
            elif centered == "spacing":
                self.text_entries[-1]['letter_spacing'] = entry['letter_spacing']

        return self.text_entries

    def append_img_paths(self, images_list, box_list, number_imgs):
        for index, label in enumerate(images_list[:number_imgs]):
            lbl = getattr(self.ui, label)
            path = lbl.toolTip()
            box_list[index]['path'] = path
            if index > len(box_list):
                break

    def set_coords(self, img_box, number_imgs):
        box_id = f'box_{img_box}'
        if img_box == 10:
            x = 185
        elif img_box % 2 == 0:
            x = 45
        else:
            x = 310
        self.append_img_paths(self.images_list[img_box], self.box_coords[img_box][number_imgs - 1], number_imgs)
        for lst in self.box_coords[img_box][(number_imgs - 1)]:
            self.image_entries.append({'box_id': box_id, 'start_x': x, **lst})

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
        image_folder = 'app_imgs'
        os.makedirs(image_folder, exist_ok=True)
        dialog = ImageBankDialog(image_folder, self.parent)
        if dialog.exec() == QDialog.Accepted:
            self.ui.image_path = dialog.selected_image_path
            pixmap = QPixmap(self.ui.image_path)
            scaled_pixmap = pixmap.scaled(50, 50)
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(False)
            label.setToolTip(self.ui.image_path)

    def remove_img_path(self, label):
        label.clear()
        label.setToolTip('')
        label.setText("img")

    def has_content(self):
        text_entries = self.enter_text()
        for entry in text_entries:
            if entry['text']:
                return True
        return False
