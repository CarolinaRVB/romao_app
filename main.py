import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from PyQt5.QtCore import Qt

def main():
    app = QApplication(sys.argv)  # Initializes the application and processes command-line arguments
    window = MainWindow()         # Creates the main window
    window.setWindowState(Qt.WindowMaximized)
    window.show()                 # Shows the main window
    sys.exit(app.exec_())         # Starts the event loop and ensures proper exit

if __name__ == "__main__":
    main()