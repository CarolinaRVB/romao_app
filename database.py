import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
import sys
import os

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
    folder = 'database'
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM form_data WHERE user_id = ?', (user_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def delete_plan(user_id):
    folder = 'database'
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
    folder = 'database'
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT user_id FROM form_data')
    user_ids = cursor.fetchall()
    conn.close()

    user_ids = [user_id[0] for user_id in user_ids]
    return user_ids


def init_db(names_list):
    folder = 'database'
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')
    # db_path = 'ui/database/form_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    columns = ",\n".join(f"{name} TEXT" for name in names_list if name != "user_id")

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS form_data (
            id INTEGER PRIMARY KEY,
            user_id TEXT,
            {columns}
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
    folder = 'database'
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
    folder = 'database'
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
        label.setToolTip(image_path)  # Store the image path in the toolTip
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(60, 50, aspectRatioMode=1)
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(True)
        else:
            label.setText("img")


def change_grid_visibility(element,  value, grid_list, visible):
    if value == "1":
        element.setCurrentIndex(1)
        set_layout_visible(grid_list[0], visible)
        set_layout_visible(grid_list[1], visible)
        set_layout_visible(grid_list[2], visible)
        set_layout_visible(grid_list[3], visible)
    elif value == "2":
        element.setCurrentIndex(2)
        set_layout_visible(grid_list[0], visible)
        set_layout_visible(grid_list[1], visible)
        set_layout_visible(grid_list[2], visible)
        set_layout_visible(grid_list[3], visible)
        set_layout_visible(grid_list[4], visible)
        set_layout_visible(grid_list[5], visible)
    elif value == "3":
        element.setCurrentIndex(3)
        set_layout_visible(grid_list[0], visible)
        set_layout_visible(grid_list[1], visible)
        set_layout_visible(grid_list[2], visible)
        set_layout_visible(grid_list[3], visible)
        set_layout_visible(grid_list[4], visible)
        set_layout_visible(grid_list[5], visible)
        set_layout_visible(grid_list[6], visible)
        set_layout_visible(grid_list[7], visible)

def set_all_pages_visible(ui, name, element, value, visible):

    grid_pa = [ui.gridLayout_7, ui.gridLayout_9, ui.gridLayout_46, ui.gridLayout_43,
                         ui.gridLayout_57, ui.gridLayout_58, ui.gridLayout_59, ui.gridLayout_60]
    grid_MM1 = [ui.gridLayout_32, ui.gridLayout_31, ui.gridLayoutM_1, ui.gridLayoutM_2,
                           ui.gridLayoutM_3, ui.gridLayoutM_4, ui.gridLayoutM_5, ui.gridLayoutM_6]
    grid_MM2 = [ui.gridLayoutMM_1, ui.gridLayoutMM_2, ui.gridLayoutMM_3, ui.gridLayoutMM_4,
                      ui.gridLayoutMM_5, ui.gridLayoutMM_6, ui.gridLayoutMM_7, ui.gridLayoutMM_8]
    grid_L = [ui.gridLayoutL_1, ui.gridLayoutL_2, ui.gridLayoutL_3, ui.gridLayoutL_4,
                    ui.gridLayoutL_5, ui.gridLayoutL_6, ui.gridLayoutL_7, ui.gridLayoutL_8]
    grid_SN = [ui.gridLayoutSN_1, ui.gridLayoutSN_2, ui.gridLayoutSN_3, ui.gridLayoutSN_4,
                         ui.gridLayoutSN_5, ui.gridLayoutSN_6, ui.gridLayoutSN_7, ui.gridLayoutSN_8]
    grid_Se = [ui.gridLayoutSe_1, ui.gridLayoutSe_2, ui.gridLayoutSe_3, ui.gridLayoutSe_4, ui.gridLayoutSe_5,
               ui.gridLayoutSe_6, ui.gridLayoutSe_7, ui.gridLayoutSe_8]
    grid_C = [ui.gridLayoutC_1, ui.gridLayoutC_2, ui.gridLayoutC_3, ui.gridLayoutC_4,
              ui.gridLayoutC_5, ui.gridLayoutC_6, ui.gridLayoutC_7, ui.gridLayoutC_8]

    if name == "pageSelection":
        change_grid_visibility(element, value, grid_pa, visible)
    elif name == "pageSelectionM1":
        change_grid_visibility(element, value, grid_MM1, visible)
    elif name == "pageSelectionMM2":
        change_grid_visibility(element, value, grid_MM2, visible)
    elif name == "pageSelectionL":
        change_grid_visibility(element, value, grid_L, visible)
    elif name == "pageSelectionSN":
        change_grid_visibility(element, value, grid_SN, visible)
    elif name == "pageSelectionSe":
        change_grid_visibility(element, value, grid_Se, visible)
    elif name == "pageSelectionC":
        change_grid_visibility(element, value, grid_C, visible)



def set_layout_visible(layout, visible):
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.setVisible(visible)


def fetch_form_data(user_id):
    folder = 'database'
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
                    set_all_pages_visible(ui, name, element, value, True)
        else:
            QtWidgets.QMessageBox.warning(parent, "Error", "No data found for the given plan ID.")

