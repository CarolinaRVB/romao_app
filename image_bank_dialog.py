import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap

class ImageBankDialog(QDialog):
    def __init__(self, image_folder, parent=None):
        super(ImageBankDialog, self).__init__(parent)
        self.image_folder = image_folder
        self.selected_image_path = None

        self.setWindowTitle("Seleciona uma Imagem")

        # Set a similar background color to popup_load_plan_dialog
        self.setStyleSheet("background-color: #f7c45f;")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)  # Set tighter margins
        self.layout.setSpacing(1)
        self.resize(800, 600)

        # Modify search bar styling
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Pequisar Imagens ... ")
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        self.search_bar.setFont(font2)
        self.search_bar.setStyleSheet("background-color: #f3b25d;")  # Match input field color
        self.search_bar.textChanged.connect(self.filter_images)
        self.layout.addWidget(self.search_bar)

        # Create image grid layout
        self.image_grid = QGridLayout()
        self.layout.addLayout(self.image_grid)

        self.setLayout(self.layout)
        self.layout.addStretch(1)
        self.load_images()
    def load_images(self):
        self.images = []
        for file_name in os.listdir(self.image_folder):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.images.append(file_name)
            self.display_images(self.images)

    def display_images(self, images):
        for i in reversed(range(self.image_grid.count())):
            widget = self.image_grid.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        for index, image_name in enumerate(images):
            image_path = os.path.join(self.image_folder, image_name)
            pixmap = QPixmap(image_path).scaled(100, 100, aspectRatioMode=1)  # Scale images to 100x100 pixels
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.mousePressEvent = self.get_image_click_handler(image_path)
            row = index // 4
            col = index % 4
            self.image_grid.addWidget(label, row, col)

    def filter_images(self, text):
        filtered_images = [img for img in self.images if text.lower() in img.lower()]
        self.display_images(filtered_images)

    def get_image_click_handler(self, image_path):
        def handler(event):
            self.selected_image_path = image_path
            self.accept()
        return handler
