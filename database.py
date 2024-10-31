import os
import sys
import shutil
import sqlite3
from PyQt5.QtCore import QTimer
from pages_data import PagesData
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget

current_user_id = None


def reset_form(parent, ui, names_list):
    for name in names_list:
        element = getattr(ui, name, None)
        if isinstance(element, QtWidgets.QPlainTextEdit):
            element.clear()
        elif isinstance(element, QtWidgets.QLineEdit):
            element.clear()
        elif isinstance(element, QtWidgets.QPlainTextEdit):
            element.clear()
        elif isinstance(element, QtWidgets.QLabel):
            element.clear()
            element.setToolTip('')
            element.setText("img")
        elif isinstance(element, QtWidgets.QComboBox):
            element.setCurrentIndex(0)


class UserDialog(QDialog):
    def __init__(self, user_ids, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Lista de Planos Guardados")
        self.setStyleSheet("background-color: #f7c45f;")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)  # Set tighter margins
        self.layout.setSpacing(10)
        self.resize(500, 600)

        # Create QListWidget
        self.listWidget = QListWidget()
        self.listWidget.addItems(user_ids)

        # Set font size
        font = QFont()
        font.setPointSize(14)  # Adjust the font size as needed
        self.listWidget.setFont(font)

        # Add QListWidget to layout
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)


def popup_load_plan_dialog(parent, title, line):
    # Create a custom dialog window
    dialog = QtWidgets.QDialog(parent)
    dialog.setWindowTitle(title)

    # Set a soft white background color for the entire dialog
    dialog.setStyleSheet("background-color: #f7c45f;")  # Light grey background

    # Set dialog layout
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.setContentsMargins(20, 20, 20, 20)  # Set margins around the layout

    # Create and set the label
    label = QtWidgets.QLabel(line)
    font = QtGui.QFont()
    font.setPointSize(16)  # Set a larger font size
    label.setFont(font)

    # Align the label at the top
    label.setAlignment(QtCore.Qt.AlignTop)

    # Add the label to the layout with stretching
    layout.addStretch(1)
    layout.addWidget(label)

    # Create and set the QLineEdit
    line_edit = QtWidgets.QLineEdit(dialog)
    font2 = QtGui.QFont()
    font2.setPointSize(12)
    line_edit.setFont(font2)
    line_edit.setMinimumHeight(15)

    # Set a darker dirty white background color for the input field
    line_edit.setStyleSheet("background-color: #f3b25d;")
    layout.addWidget(line_edit)

    # Add stretching between the input field and buttons
    layout.addStretch(1)

    # Create buttons for OK and Cancel with larger sizes
    button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
    button_box.setFont(font)

    # Make buttons larger
    for button in button_box.buttons():
        button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setMinimumHeight(20)  # Increase button height
        button.setMinimumWidth(80)  # Increase button width

    button_box.layout().setSpacing(20)

    # Center the button box
    button_layout = QtWidgets.QHBoxLayout()
    button_layout.addStretch(1)
    button_layout.addWidget(button_box)
    button_layout.addStretch(1)
    layout.addLayout(button_layout)

    # Add stretching at the bottom
    layout.addStretch(1)

    # Connect the buttons
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    # Resize the dialog
    dialog.resize(400, 250)  # Adjust the size of the dialog for better spacing

    # Show the dialog and get the result
    result = dialog.exec_()
    if result == QtWidgets.QDialog.Accepted:
        return line_edit.text()  # Return the text from the input field if OK is pressed
    else:
        return None


def user_id_exists(user_id):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM form_data WHERE user_id = ?', (user_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists


def delete_plan(user_id):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM form_data WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()


def delete_plan_entry(parent):
    user_input = popup_load_plan_dialog(parent, "Apagar Plano", "Escreve o ID do plano:")
    if user_input:
        if user_id_exists(user_input):
            confirm = QtWidgets.QMessageBox.question(
                parent, "Confirmar",
                f"Tens a certeza que queres apagar o plano com o ID {user_input}?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            if confirm == QtWidgets.QMessageBox.Yes:
                delete_plan(user_input)
                QtWidgets.QMessageBox.information(parent, "Apagado!", f"Plano com o ID {user_input} foi apagado.")
            else:
                QtWidgets.QMessageBox.information(parent, "Cancelado", "Cancelado.")
        else:
            QtWidgets.QMessageBox.warning(parent, "Erro", f"Plano com ID {user_input} não existe.")


def fetch_user_ids(parent):
    # folder = 'database'
    # os.makedirs(folder, exist_ok=True)
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT user_id FROM form_data')
    user_ids = cursor.fetchall()
    conn.close()

    user_ids = [user_id[0] for user_id in user_ids]
    return user_ids


def resource_path(relative_path):
    """ Get absolute path to resource, works for both dev and for PyInstaller """
    try:
        # PyInstaller temporary folder
        base_path = sys._MEIPASS
    except AttributeError:
        # In development, base path is the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_all_image_paths():
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT image_path FROM image_paths')
    paths = cursor.fetchall()
    conn.close()
    return [path[0] for path in paths]


def add_image_path(image_path):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO images_paths (image_path)
        VALUES (?)
    ''', (image_path,))

    conn.commit()
    conn.close()


def init_db(names_list):
    # Folder where the database should be copied to (user-writable)
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')

    # Check if the database already exists
    if not os.path.exists(db_path):
        # If it doesn't exist, copy the empty database from the bundled resources
        bundled_db_path = resource_path("database/database.db")
        shutil.copyfile(bundled_db_path, db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='form_data';")
    if cursor.fetchone() is None:
        # If the table does not exist, create it
        columns = ",\n".join(f"{name} TEXT" for name in names_list if name != "user_id")
        cursor.execute(f'''
            CREATE TABLE form_data (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                {columns}
            )
        ''')

    # Check if images_paths table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='images_paths';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE images_paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT
            )
        ''')

    conn.commit()
    conn.close()


def show_user_ids(parent):
    user_ids = fetch_user_ids(parent)
    dialog = UserDialog(user_ids, parent)
    dialog.exec()


def save_form_data(parent, ui, names_list):
    global current_user_id

    user_input = current_user_id
    if not user_input:
        user_input = popup_load_plan_dialog(parent, "Guardar Plano", "ID do Plano: ")

    if user_input:
        data = {}
        if user_id_exists(user_input) and not current_user_id:
            confirm = QtWidgets.QMessageBox.question(
                parent, "AVISO: ID JÁ EXISTE!",
                f"Confirma se queres guardar com o ID: {user_input}?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            if confirm == QtWidgets.QMessageBox.No:
                return
        for name in names_list:

            if name != "user_id":
                element = getattr(ui, name, None)
                if isinstance(element, QtWidgets.QLineEdit):
                    data[name] = element.text()
                elif isinstance(element, QtWidgets.QPlainTextEdit):
                    data[name] = element.toPlainText()
                elif isinstance(element, QtWidgets.QLabel):
                    data[name] = element.toolTip()
                elif isinstance(element, QtWidgets.QComboBox):
                    data[name] = element.currentIndex()
                else:
                    data[name] = ""
        data['user_id'] = user_input

        if fetch_form_data(user_input):
            update_form_data(data)
        else:
            insert_form_data(data)


def setup_auto_save(parent, ui, names_list, interval=60000):
    timer = QTimer(parent)
    timer.timeout.connect(lambda: save_form_data(parent, ui, names_list))
    timer.start(interval)


def insert_new_id(parent, ui, names_list):
    global current_user_id
    user_id, ok = QtWidgets.QInputDialog.getText(parent, "Novo Plano", "Inserir ID do novo plano:")
    if ok:
        current_user_id = user_id
        data = {name: "" for name in names_list if name != "user_id"}
        data["user_id"] = user_id
        insert_form_data(data)

        setup_auto_save(parent, ui, names_list)


def insert_form_data(data):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))

    cursor.execute(f'''
        INSERT INTO form_data ({columns})
        VALUES ({placeholders})
    ''', tuple(data.values()))

    conn.commit()
    conn.close()


def update_form_data(data):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    columns = ', '.join(f"{key} = ?" for key in data.keys() if key != 'user_id')
    cursor.execute(f'''
        UPDATE form_data
        SET {columns}
        WHERE user_id = ?
    ''', tuple(value for key, value in data.items() if key != 'user_id') + (data['user_id'],))
    conn.commit()
    conn.close()


def set_image(label, image_path):
    if image_path:
        label.setToolTip(image_path)
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(50, 50)
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(False)
        else:
            label.setText("img")


def change_grid_visibility(element, value, grid_list, visible):
    index_map = {"1": 1, "2": 2, "3": 3}
    layout_map = {"1": 4, "2": 6, "3": 8}

    if value in index_map:
        element.setCurrentIndex(index_map[value])
        limit = layout_map[value]
        for layout in grid_list[:limit]:
            set_layout_visible(layout, visible)


def set_all_pages_visible(parent, name, element, value, visible):
    grid_names = {
        'pageSelection': 0,
        'pageSelectionM1': 1,
        'pageSelectionMM2': 2,
        'pageSelectionL': 3,
        'pageSelectionSN': 4,
        'pageSelectionSe': 5,
        'pageSelectionC': 6
    }
    if name in grid_names:
        index = grid_names[name]
        grid = PagesData.get_grid_names_PA(parent, index)
        change_grid_visibility(element, value, grid, visible)


def set_layout_visible(layout, visible):
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setVisible(visible)


def fetch_form_data(user_id):
    folder = os.path.join(os.path.expanduser("~"), 'romao_data')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM form_data WHERE user_id = ?', (user_id,))
    columns = [description[0] for description in cursor.description]
    data = cursor.fetchone()
    conn.close()
    return dict(zip(columns, data)) if data else None


def load_form_data(parent, ui):

    user_input = popup_load_plan_dialog(parent, "Recuperar Plano", "ID do Plano: ")
    if user_input:
        data = fetch_form_data(user_input)
        if data:
            for name, value in data.items():
                element = getattr(ui, name, None)
                if value and isinstance(element, QtWidgets.QLineEdit):
                    element.setText(value if value is not None else "")
                elif value and isinstance(element, QtWidgets.QPlainTextEdit):
                    element.setPlainText(value if value is not None else "")
                elif value and isinstance(element, QtWidgets.QLabel):
                    set_image(element, value)
                elif value and isinstance(element, QtWidgets.QComboBox):
                    set_all_pages_visible(parent, name, element, value, True)
        else:
            QtWidgets.QMessageBox.warning(parent, "Error", "No data found for the given plan ID.")
