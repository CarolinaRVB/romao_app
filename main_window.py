import os
import re
import sys
import tempfile
from PyQt5.QtCore import Qt
from pages_data import PagesData
from input_data import Input_Data
from pdf_generator import generate_pdf
from PyQt5.QtWidgets import QFileDialog
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from main_window_ui import Ui_MainWindow
from reportlab.pdfbase.ttfonts import TTFont
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QCheckBox
from database import (init_db, show_user_ids, save_form_data, insert_new_id, load_form_data, delete_plan_entry,
                      reset_form)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowMaximized)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_page = 0

        pages_data = PagesData(self.ui, self)
        self.names_list = pages_data.get_names_list()
        init_db(self.names_list)
        # Lists for Geral page
        self.linetext_names_G = pages_data.get_linetext_names(-1)

        item_list1 = ['button_map', 'button_remove', 'imgs_list']
        page_suffixes = [
                    'PA', 'A', 'PAS', 'J', 'MM1', 'MM2', 'MC1', 'MC2', 'L',
                    'LC', 'SN', 'SC', 'Se', 'Sec', 'C', 'CC'
                ]
        linetext_nums = [2, 0, 9, 1, 3, 4, 10, 11, 5, 12, 6, 13, 7, 14, 8, 15]

        for index, suf in enumerate(page_suffixes):
            for item in item_list1:
                getter_function = getattr(pages_data, f"get_{item}")
                setattr(self, f"{item}_{suf}", getter_function(index))

        item_dict1 = {0: ['PA', 'MM1', 'MM2', 'L', 'SN', 'Se', 'C'],
                     1: ['A', 'J'],
                     2: ['PAS', 'MC1', 'MC2', 'LC', 'SC', 'Sec', 'CC']}

        for index, suf in item_dict1.items():
            box_getter = getattr(pages_data, "get_box_coords")
            for item in suf:
                setattr(self, f"box_coords_{item}", box_getter(index))

        item_dict2 = dict(zip(linetext_nums, page_suffixes))
        line_text_getter = getattr(pages_data, "get_linetext_names")
        for index, suf in item_dict2.items():
            setattr(self, f"linetext_names_{suf}", line_text_getter(index))

        item_dict3 = dict(zip(list(range(0, 7)), item_dict1[0]))
        grid_getter = getattr(pages_data, f"get_grid_names_PA")
        for index, suf in item_dict3.items():
            setattr(self, f"grid_names_{suf}", grid_getter(index))

        # Hiding Tabs
        self.tabWidget = self.findChild(QTabWidget, 'tabHome')
        self.checkBoxSimple = self.findChild(QCheckBox, 'checkBoxS')
        self.checkBoxComplex = self.findChild(QCheckBox, 'checkBoxC')

        self.tabsToShowSimple = [2,3,4,9,11,13,16]
        self.tabsToShowComplex = [5,6,7,10,12,14,17]
        for i in self.tabsToShowSimple + self.tabsToShowComplex:
            self.tabWidget.setTabVisible(i, False)

        self.checkBoxSimple.stateChanged.connect(self.toggle_box_simple)
        self.checkBoxComplex.stateChanged.connect(self.toggle_box_complex)

        # Define the parameters for each page in a list of dictionaries
        pages_config = [
            {"name": "page1", "button_map": None, "button_remove": None, "images_list": None,
             "box_coords": None, "linetext_names": self.linetext_names_G, "grid_names": None,
             "page_name_index": None},

            {"name": "page2", "button_map": self.button_map_PA, "button_remove": self.button_remove_PA,
             "images_list": self.imgs_list_PA, "box_coords": self.box_coords_PA,
             "linetext_names": self.linetext_names_PA, "grid_names": self.grid_names_PA,
             "page_name_index": self.ui.pageSelection},

            {"name": "page3", "button_map": self.button_map_PAS, "button_remove": self.button_remove_PAS,
             "images_list": self.imgs_list_PAS, "box_coords": self.box_coords_PAS,
             "linetext_names": self.linetext_names_PAS, "grid_names": None, "page_name_index": None},

            {"name": "page4", "button_map": self.button_map_MM1, "button_remove": self.button_remove_MM1,
             "images_list": self.imgs_list_MM1, "box_coords": self.box_coords_MM1,
             "linetext_names": self.linetext_names_MM1, "grid_names": self.grid_names_MM1,
             "page_name_index": self.ui.pageSelectionM1},

            {"name": "page5", "button_map": self.button_map_MM2, "button_remove": self.button_remove_MM2,
             "images_list": self.imgs_list_MM2, "box_coords": self.box_coords_MM2,
             "linetext_names": self.linetext_names_MM2, "grid_names": self.grid_names_MM2,
             "page_name_index": self.ui.pageSelectionMM2},

            {"name": "page6", "button_map": self.button_map_MC1, "button_remove": self.button_remove_MC1,
             "images_list": self.imgs_list_MC1, "box_coords": self.box_coords_MC1,
             "linetext_names": self.linetext_names_MC1, "grid_names": None, "page_name_index": None},

            {"name": "page7", "button_map": self.button_map_MC2, "button_remove": self.button_remove_MC2,
             "images_list": self.imgs_list_MC2, "box_coords": self.box_coords_MC2,
             "linetext_names": self.linetext_names_MC2, "grid_names": None, "page_name_index": None},

            {"name": "page8", "button_map": self.button_map_A, "button_remove": self.button_remove_A,
             "images_list": self.imgs_list_A, "box_coords": self.box_coords_A,
             "linetext_names": self.linetext_names_A, "grid_names": None, "page_name_index": None},

            {"name": "page9", "button_map": self.button_map_L, "button_remove": self.button_remove_L,
             "images_list": self.imgs_list_L, "box_coords": self.box_coords_L,
             "linetext_names": self.linetext_names_L, "grid_names": self.grid_names_L,
             "page_name_index": self.ui.pageSelectionL},

            {"name": "page10", "button_map": self.button_map_LC, "button_remove": self.button_remove_LC,
             "images_list": self.imgs_list_LC, "box_coords": self.box_coords_LC,
             "linetext_names": self.linetext_names_LC, "grid_names": None, "page_name_index": None},

            {"name": "page11", "button_map": self.button_map_SN, "button_remove": self.button_remove_SN,
             "images_list": self.imgs_list_SN, "box_coords": self.box_coords_SN,
             "linetext_names": self.linetext_names_SN, "grid_names": self.grid_names_SN,
             "page_name_index": self.ui.pageSelectionSN},

            {"name": "page12", "button_map": self.button_map_SC, "button_remove": self.button_remove_SC,
             "images_list": self.imgs_list_SC, "box_coords": self.box_coords_SC,
             "linetext_names": self.linetext_names_SC, "grid_names": None, "page_name_index": None},

            {"name": "page13", "button_map": self.button_map_Se, "button_remove": self.button_remove_Se,
             "images_list": self.imgs_list_Se, "box_coords": self.box_coords_Se,
             "linetext_names": self.linetext_names_Se, "grid_names": self.grid_names_Se,
             "page_name_index": self.ui.pageSelectionSe},

            {"name": "page14", "button_map": self.button_map_Sec, "button_remove": self.button_remove_Sec,
             "images_list": self.imgs_list_Sec, "box_coords": self.box_coords_Sec,
             "linetext_names": self.linetext_names_Sec, "grid_names": None, "page_name_index": None},

            {"name": "page15", "button_map": self.button_map_J, "button_remove": self.button_remove_J,
             "images_list": self.imgs_list_J, "box_coords": self.box_coords_J,
             "linetext_names": self.linetext_names_J, "grid_names": None, "page_name_index": None},

            {"name": "page16", "button_map": self.button_map_C, "button_remove": self.button_remove_C,
             "images_list": self.imgs_list_C, "box_coords": self.box_coords_C,
             "linetext_names": self.linetext_names_C, "grid_names": self.grid_names_C,
             "page_name_index": self.ui.pageSelectionC},

            {"name": "page17", "button_map": self.button_map_CC, "button_remove": self.button_remove_CC,
             "images_list": self.imgs_list_CC, "box_coords": self.box_coords_CC,
             "linetext_names": self.linetext_names_CC, "grid_names": None, "page_name_index": None},
        ]

        # Create pages dynamically
        for page in pages_config:
            setattr(self, page["name"], Input_Data(self.ui, self,
                                                   button_map=page["button_map"],
                                                   button_remove=page["button_remove"],
                                                   images_list=page["images_list"],
                                                   box_coords=page["box_coords"],
                                                   linetext_names=page["linetext_names"],
                                                   grid_names=page["grid_names"],
                                                   page_name_index=page["page_name_index"]))

        self.ui.pushDownload.clicked.connect(self.download_pdf)
        self.ui.pushSave.clicked.connect(lambda: save_form_data(self, self.ui, self.names_list))
        self.ui.pushRecover.clicked.connect(lambda: load_form_data(self, self.ui))
        self.ui.pushDelete.clicked.connect(lambda: delete_plan_entry(self))
        self.ui.pushVer.clicked.connect(lambda: show_user_ids(self))
        self.ui.pushNovo.clicked.connect(lambda: insert_new_id(self, self.ui, self.names_list))
        self.ui.pushApagarEntr.clicked.connect(lambda: reset_form(self, self.ui, self.names_list))

    def toggle_box_simple(self, state):
        if state == 2:
            for index in self.tabsToShowSimple:
                self.tabWidget.setTabVisible(index, True)
        else:
            for index in self.tabsToShowSimple:
                self.tabWidget.setTabVisible(index, False)

    def toggle_box_complex(self, state):
        if state == 2:
            for index in self.tabsToShowComplex:
                self.tabWidget.setTabVisible(index, True)
        else:
            for index in self.tabsToShowComplex:
                self.tabWidget.setTabVisible(index, False)

    def download_pdf(self):
        temp_dir = os.path.join(tempfile.gettempdir(), 'romao_pdfs')
        os.makedirs(temp_dir, exist_ok=True)
        pdf_list = []
        color = (255, 255, 255)
        fonts_path = resource_path("fonts" + "/" + "static")
        font_list = ["Montserrat-Medium.ttf", "Montserrat-SemiBold.ttf", "Montserrat-Bold.ttf",
                     "Montserrat-ExtraBold.ttf",
                     "Montserrat-Black.ttf", "Montserrat-Thin.ttf", "Montserrat-Regular.ttf", "BebasNeue-Regular.ttf"]

        for item in font_list:
            font_path = resource_path(fonts_path + "/" + item)
            font = item.strip(".ttf")
            pdfmetrics.registerFont(TTFont(font, font_path))

        simple_list = {num: getattr(self, f"page{num}") for num in self.tabsToShowSimple}
        complex_list = {num: getattr(self, f"page{num}") for num in self.tabsToShowComplex}
        notes = {2: self.ui.textNotasPA, 3: self.ui.textNotasM1, 4: self.ui.textNotasMM2, 9: self.ui.textNotasL,
                 11: self.ui.textNotasSN, 13: self.ui.textNotasSe, 16: self.ui.textNotasC}
        notes_list = {num: notes[num] for num in self.tabsToShowSimple}

        for num, page in simple_list.items():
            if page.has_content():
                download_simple_PA(page.page_name_index.currentIndex(), page, f"output{num}.pdf",
                                   notes_list[num].toPlainText())
                pdf_list.append(os.path.join(temp_dir, f"output{num}.pdf"))

        for num, page in complex_list.items():
            if page.has_content():
                download_complex_PA(page, f"output{num}.pdf")
                pdf_list.append(os.path.join(temp_dir, f"output{num}.pdf"))

        special_cases = {1: resource_path("templates" + "/" + "pagina1.pdf"),
                         8: resource_path("templates" + "/" + "pagina3.pdf"),
                         15: resource_path("templates" + "/" + "pagina3.pdf")}

        for num, pdf in special_cases.items():
            page = getattr(self, f"page{num}")
            if page.has_content():
                linetext_entries = page.enter_text()
                if num == 1:
                    image_entries = []
                else:
                    image_entries = page.enter_images()
                generate_pdf(linetext_entries, image_entries, special_cases[num], f"output{num}.pdf", color)
                pdf_list.append(os.path.join(temp_dir, f"output{num}.pdf"))

        def natural_sort_key(path):
            file_name = os.path.basename(path)
            return [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', file_name)]

        pdf_list_sorted = sorted(pdf_list, key=natural_sort_key)
        merged_pdf_path = os.path.join(temp_dir, "merged_output.pdf")
        merge_pdfs(pdf_list_sorted, merged_pdf_path)
        final_save_path = select_save_location()
        if final_save_path:
            try:
                os.rename(merged_pdf_path, final_save_path)
                print(f"PDF saved successfully: {final_save_path}")
            except Exception as e:
                print(f"Error moving file: {e}")
        else:
            print("No file selected. PDF not saved.")


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for both dev and PyInstaller package """
    if hasattr(sys, '_MEIPASS'):
        # The path where the files are bundled by PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # In development mode, just use the relative path
        return os.path.join(os.path.dirname(__file__), relative_path)


def select_save_location():
    file_path, _ = QFileDialog.getSaveFileName(
        None,
        "Save PDF as",
        "",
        "PDF Files (*.pdf);;All Files (*)"
    )
    if file_path:
        return file_path
    else:
        print("No file selected or dialog canceled.")
        return None


def merge_pdfs(pdf_list, output_pdf_path):
    output = PdfWriter()
    for pdf_path in pdf_list:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                output.add_page(pdf_reader.pages[page_num])
    with open(output_pdf_path, "wb") as output_file:
        output.write(output_file)
    for pdf_path in pdf_list:
        os.remove(pdf_path)


def download_simple_PA(curr_page, page_num, output_name, text_type):
    current_page = curr_page
    if current_page != 0:
        plaintext_entries = []
        plaintext_entries.extend(page_num.enter_text())
        # Get images inputs
        image_entries = []
        image_entries.extend(page_num.enter_images())
        color = (0, 0, 0)
        pdf_path = ""
        output_name = output_name
        if current_page == 1:
            for item in plaintext_entries:
                if item['text'] == text_type:
                    item['y'] = 1150
                    break
            pdf_path = resource_path("templates" + "/" + "pagina2_2.pdf")
        elif current_page == 2:
            for item in plaintext_entries:
                if item['text'] == text_type:
                    item['y'] = 990
                    break
            pdf_path = resource_path("templates" + "/" + "pagina2_4.pdf")
        elif current_page == 3:
            for item in plaintext_entries:
                if item['text'] == text_type:
                    item['y'] = 830
                    break
            pdf_path = resource_path("templates" + "/" + "pagina2_6.pdf")
        generate_pdf(plaintext_entries, image_entries, pdf_path, output_name, color)


def download_complex_PA(page_num, output_file):
    plaintext_entries = []
    plaintext_entries.extend(page_num.enter_text())
    # Get images inputs
    image_entries = []
    image_entries.extend(page_num.enter_images())
    color = (0, 0, 0)
    pdf_path = resource_path("templates" + "/" + "pagina2_8.pdf")
    output_name = output_file
    generate_pdf(plaintext_entries, image_entries, pdf_path, output_name, color)