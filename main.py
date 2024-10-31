import os
import sys
from PyQt5.QtCore import Qt
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from img_folder_watcher import stop_image_watcher
from img_folder_watcher import start_image_watcher

def main():
    app = QApplication(sys.argv)  # Initializes the application and processes command-line arguments
    window = MainWindow()         # Creates the main window
    window.setWindowState(Qt.WindowMaximized)
    window.show()                 # Shows the main window
    sys.exit(app.exec_())         # Starts the event loop and ensures proper exit

if __name__ == "__main__":
    image_folder = 'app_imgs'
    os.makedirs(image_folder, exist_ok=True)
    observer = start_image_watcher(image_folder)
    try:
        main()  # Start the main app (no loop needed)
    except KeyboardInterrupt:
        stop_image_watcher(observer)
