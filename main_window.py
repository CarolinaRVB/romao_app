from PyQt5.QtWidgets import QMainWindow, QTabWidget, QCheckBox
from PyQt5.QtCore import Qt
from main_window_ui import Ui_MainWindow
from pdf_generator import generate_pdf
from input_data import Input_Data
from database import init_db, show_user_ids, save_form_data, insert_new_id, load_form_data, delete_plan_entry, reset_form
from PyQt5.QtWidgets import QFileDialog
import os
from PyPDF2 import PdfReader, PdfWriter
from pages_data import Pages_Data

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
            pdf_path = "ui/resources/templates/pagina2_2.pdf"
        elif current_page == 2:
            for item in plaintext_entries:
                if item['text'] == text_type:
                    item['y'] = 990
                    break
            pdf_path = "ui/resources/templates/pagina2_4.pdf"
        elif current_page == 3:
            for item in plaintext_entries:
                if item['text'] == text_type:
                    item['y'] = 830
                    break
            pdf_path = "ui/resources/templates/pagina2_6.pdf"
        generate_pdf(plaintext_entries, image_entries, pdf_path, output_name, color)


def download_complex_PA(page_num, output_file):
    plaintext_entries = []
    plaintext_entries.extend(page_num.enter_text())
    # Get images inputs
    image_entries = []
    image_entries.extend(page_num.enter_images())
    color = (0, 0, 0)
    pdf_path = "ui/resources/templates/pagina2_8.pdf"
    output_name = output_file
    generate_pdf(plaintext_entries, image_entries, pdf_path, output_name, color)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowMaximized)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_page = 0

        pages_data = Pages_Data(self.ui, self)  # Create an instance of Pages_Data

        self.names_list = pages_data.get_names_list()  # Call the method on the instance
        init_db(self.names_list)

        # Lists for Geral page
        self.linetext_names_G = pages_data.get_linetext_names(-1)

        # Lists for PA page
        self.button_map_PA = pages_data.get_button_map(0)
        self.button_remove_PA = pages_data.get_button_remove(0)
        self.images_list_PA = pages_data.get_imgs_list(0)
        self.box_coords_PA = pages_data.get_box_coords(0)
        self.linetext_names_PA = pages_data.get_linetext_names(2)
        self.grid_names_PA = pages_data.get_grid_names_PA(0)

        #List for Almoço page
        self.button_map_A = pages_data.get_button_map(1)
        self.button_remove_A = pages_data.get_button_remove(1)
        self.images_list_A = pages_data.get_imgs_list(1)
        self.box_coords_A = pages_data.get_box_coords(1)
        self.linetext_names_A = pages_data.get_linetext_names(0)

        #List for Pequeno Almoço Especial
        self.button_map_PAS = pages_data.get_button_map(2)
        self.button_remove_PAS = pages_data.get_button_remove(2)
        self.images_list_PAS = pages_data.get_imgs_list(2)
        self.box_coords_PAS = pages_data.get_box_coords(2)
        self.linetext_names_PAS = pages_data.get_linetext_names(9)

        # List for Jantar page
        self.button_map_J = pages_data.get_button_map(3)
        self.button_remove_J = pages_data.get_button_remove(3)
        self.images_list_J = pages_data.get_imgs_list(3)
        self.box_coords_J = pages_data.get_box_coords(1)
        self.linetext_names_J = pages_data.get_linetext_names(1)

        #List for MM1
        self.button_map_MM1 = pages_data.get_button_map(4)
        self.button_remove_MM1 = pages_data.get_button_remove(4)
        self.images_list_MM1 = pages_data.get_imgs_list(4)
        self.box_coords_MM1 = pages_data.get_box_coords(0)
        self.linetext_names_MM1 = pages_data.get_linetext_names(3)
        self.grid_names_MM1 = pages_data.get_grid_names_PA(1)

        #List for MM2
        self.button_map_MM2 = pages_data.get_button_map(5)
        self.button_remove_MM2 = pages_data.get_button_remove(5)
        self.images_list_MM2 = pages_data.get_imgs_list(5)
        self.box_coords_MM2 = pages_data.get_box_coords(0)
        self.linetext_names_MM2 = pages_data.get_linetext_names(4)
        self.grid_names_MM2 = pages_data.get_grid_names_PA(2)

        #List for MC1
        self.button_map_MC1 = pages_data.get_button_map(6)
        self.button_remove_MC1 = pages_data.get_button_remove(6)
        self.images_list_MC1 = pages_data.get_imgs_list(6)
        self.box_coords_MC1 = pages_data.get_box_coords(2)
        self.linetext_names_MC1 = pages_data.get_linetext_names(10)

        #List for MC2
        self.button_map_MC2 = pages_data.get_button_map(7)
        self.button_remove_MC2 = pages_data.get_button_remove(7)
        self.images_list_MC2 = pages_data.get_imgs_list(7)
        self.box_coords_MC2 = pages_data.get_box_coords(2)
        self.linetext_names_MC2 = pages_data.get_linetext_names(11)

        #List for Lan
        self.button_map_L = pages_data.get_button_map(8)
        self.button_remove_L = pages_data.get_button_remove(8)
        self.images_list_L = pages_data.get_imgs_list(8)
        self.box_coords_L = pages_data.get_box_coords(0)
        self.linetext_names_L = pages_data.get_linetext_names(5)
        self.grid_names_L = pages_data.get_grid_names_PA(3)

        #List for LC
        self.button_map_LC = pages_data.get_button_map(9)
        self.button_remove_LC = pages_data.get_button_remove(9)
        self.images_list_LC = pages_data.get_imgs_list(9)
        self.box_coords_LC = pages_data.get_box_coords(2)
        self.linetext_names_LC = pages_data.get_linetext_names(12)

        #List for S
        self.button_map_SN = pages_data.get_button_map(10)
        self.button_remove_SN = pages_data.get_button_remove(10)
        self.images_list_SN = pages_data.get_imgs_list(10)
        self.box_coords_SN = pages_data.get_box_coords(0)
        self.linetext_names_SN = pages_data.get_linetext_names(6)
        self.grid_names_SN = pages_data.get_grid_names_PA(4)

        #List for SC
        self.button_map_SC = pages_data.get_button_map(11)
        self.button_remove_SC = pages_data.get_button_remove(11)
        self.images_list_SC = pages_data.get_imgs_list(11)
        self.box_coords_SC = pages_data.get_box_coords(2)
        self.linetext_names_SC = pages_data.get_linetext_names(13)

        #List for Se
        self.button_map_Se = pages_data.get_button_map(12)
        self.button_remove_Se = pages_data.get_button_remove(12)
        self.images_list_Se = pages_data.get_imgs_list(12)
        self.box_coords_Se = pages_data.get_box_coords(0)
        self.linetext_names_Se = pages_data.get_linetext_names(7)
        self.grid_names_Se = pages_data.get_grid_names_PA(5)

        #List for Sec
        self.button_map_Sec = pages_data.get_button_map(13)
        self.button_remove_Sec = pages_data.get_button_remove(13)
        self.images_list_Sec = pages_data.get_imgs_list(13)
        self.box_coords_Sec = pages_data.get_box_coords(2)
        self.linetext_names_Sec = pages_data.get_linetext_names(14)

        #List for C
        self.button_map_C = pages_data.get_button_map(14)
        self.button_remove_C = pages_data.get_button_remove(14)
        self.images_list_C = pages_data.get_imgs_list(14)
        self.box_coords_C = pages_data.get_box_coords(0)
        self.linetext_names_C = pages_data.get_linetext_names(8)
        self.grid_names_C = pages_data.get_grid_names_PA(6)

        #List for CC
        self.button_map_CC = pages_data.get_button_map(15)
        self.button_remove_CC = pages_data.get_button_remove(15)
        self.images_list_CC = pages_data.get_imgs_list(15)
        self.box_coords_CC = pages_data.get_box_coords(2)
        self.linetext_names_CC = pages_data.get_linetext_names(15)

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

        # FIXED PAGE
        self.page1 = Input_Data(self.ui, self, button_map=None, button_remove=None,
                            images_list=None, linetext_names=self.linetext_names_G,
                            grid_names=None, page_name_index=None)

        self.page2 = Input_Data(self.ui, self, button_map=self.button_map_PA, button_remove=self.button_remove_PA,
                            images_list=self.images_list_PA, box_coords=self.box_coords_PA,
                            linetext_names=self.linetext_names_PA, grid_names=self.grid_names_PA,
                            page_name_index=self.ui.pageSelection)

        self.page3 = Input_Data(self.ui, self, button_map=self.button_map_PAS, button_remove=self.button_remove_PAS,
                            images_list=self.images_list_PAS, box_coords=self.box_coords_PAS,
                            linetext_names=self.linetext_names_PAS, grid_names=None,
                            page_name_index=None)

        self.page4 = Input_Data(self.ui, self, button_map=self.button_map_MM1, button_remove=self.button_remove_MM1,
                            images_list=self.images_list_MM1, box_coords=self.box_coords_MM1,
                            linetext_names=self.linetext_names_MM1, grid_names=self.grid_names_MM1,
                            page_name_index=self.ui.pageSelectionM1)

        self.page5 = Input_Data(self.ui, self, button_map=self.button_map_MM2, button_remove=self.button_remove_MM2,
                            images_list=self.images_list_MM2, box_coords=self.box_coords_MM2,
                            linetext_names=self.linetext_names_MM2, grid_names=self.grid_names_MM2,
                            page_name_index=self.ui.pageSelectionMM2)

        self.page6 = Input_Data(self.ui, self, button_map=self.button_map_MC1, button_remove=self.button_remove_MC1,
                            images_list=self.images_list_MC1, box_coords=self.box_coords_MC1,
                            linetext_names=self.linetext_names_MC1, grid_names=None,
                            page_name_index=None)

        self.page7 = Input_Data(self.ui, self, button_map=self.button_map_MC2, button_remove=self.button_remove_MC2,
                            images_list=self.images_list_MC2, box_coords=self.box_coords_MC2,
                            linetext_names=self.linetext_names_MC2, grid_names=None,
                            page_name_index=None)

        # FIXED PAGE
        self.page8 = Input_Data(self.ui, self, button_map=self.button_map_A, button_remove=self.button_remove_A,
                            images_list=self.images_list_A, box_coords=self.box_coords_A,
                            linetext_names=self.linetext_names_A, grid_names=None, page_name_index=None)

        self.page9 = Input_Data(self.ui, self, button_map=self.button_map_L, button_remove=self.button_remove_L,
                            images_list=self.images_list_L, box_coords=self.box_coords_L,
                            linetext_names=self.linetext_names_L, grid_names=self.grid_names_L,
                            page_name_index=self.ui.pageSelectionL)

        self.page10 = Input_Data(self.ui, self, button_map=self.button_map_LC, button_remove=self.button_remove_LC,
                            images_list=self.images_list_LC, box_coords=self.box_coords_LC,
                            linetext_names=self.linetext_names_LC, grid_names=None,
                            page_name_index=None)

        self.page11 = Input_Data(self.ui, self, button_map=self.button_map_SN, button_remove=self.button_remove_SN,
                            images_list=self.images_list_SN, box_coords=self.box_coords_SN,
                            linetext_names=self.linetext_names_SN, grid_names=self.grid_names_SN,
                            page_name_index=self.ui.pageSelectionSN)

        self.page12 = Input_Data(self.ui, self, button_map=self.button_map_SC, button_remove=self.button_remove_SC,
                            images_list=self.images_list_SC, box_coords=self.box_coords_SC,
                            linetext_names=self.linetext_names_SC, grid_names=None,
                            page_name_index=None)

        self.page13 = Input_Data(self.ui, self, button_map=self.button_map_Se, button_remove=self.button_remove_Se,
                            images_list=self.images_list_Se, box_coords=self.box_coords_Se,
                            linetext_names=self.linetext_names_Se, grid_names=self.grid_names_Se,
                            page_name_index=self.ui.pageSelectionSe)

        self.page14 = Input_Data(self.ui, self, button_map=self.button_map_Sec, button_remove=self.button_remove_Sec,
                            images_list=self.images_list_Sec, box_coords=self.box_coords_Sec,
                            linetext_names=self.linetext_names_Sec, grid_names=None,
                            page_name_index=None)

        # FIXED PAGE
        self.page15 = Input_Data(self.ui, self, button_map=self.button_map_J, button_remove=self.button_remove_J,
                            images_list=self.images_list_J, box_coords=self.box_coords_J,
                            linetext_names=self.linetext_names_J, grid_names=None, page_name_index=None)

        self.page16 = Input_Data(self.ui, self, button_map=self.button_map_C, button_remove=self.button_remove_C,
                            images_list=self.images_list_C, box_coords=self.box_coords_C,
                            linetext_names=self.linetext_names_C, grid_names=self.grid_names_C,
                            page_name_index=self.ui.pageSelectionC)

        self.page17 = Input_Data(self.ui, self, button_map=self.button_map_CC, button_remove=self.button_remove_CC,
                            images_list=self.images_list_CC, box_coords=self.box_coords_CC,
                            linetext_names=self.linetext_names_CC, grid_names=None,
                            page_name_index=None)


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
        pdf_list = []
        color = (255, 255, 255)

        # Page 1 Geral (fixed)
        linetext_entries = self.page1.enter_text()
        image_entries = []
        generate_pdf(linetext_entries, image_entries, "ui/resources/templates/pagina1.pdf", "output1.pdf", color)
        pdf_list.append('pdfs/output1.pdf')

        # Page 2 PA (optional)
        if self.page2.has_content():
            download_simple_PA(self.ui.pageSelection.currentIndex(), self.page2, "output2.pdf",
                               self.ui.textNotasPA.toPlainText())
            pdf_list.append('pdfs/output2.pdf')

        # Page 3 PAS (optional)
        if self.page3.has_content():
            download_complex_PA(self.page3, "output3.pdf")
            pdf_list.append('pdfs/output3.pdf')

        # Page 4 MM1 (optional)
        if self.page4.has_content():  # Assume has_content checks if user entered any data on this page
            download_simple_PA(self.ui.pageSelectionM1.currentIndex(), self.page4, "output4.pdf",
                               self.ui.textNotasM1.toPlainText())
            pdf_list.append('pdfs/output4.pdf')

        # Page 5 MM2 (optional)
        if self.page5.has_content():
            download_simple_PA(self.ui.pageSelectionMM2.currentIndex(), self.page5, "output5.pdf",
                               self.ui.textNotasMM2.toPlainText())
            pdf_list.append('pdfs/output5.pdf')

        # Page 6 MMC1 (optional)
        if self.page6.has_content():
            download_complex_PA(self.page6, "output6.pdf")
            pdf_list.append('pdfs/output6.pdf')

        # Page 7 MMC2 (optional)
        if self.page7.has_content():
            download_complex_PA(self.page7, "output7.pdf")
            pdf_list.append('pdfs/output7.pdf')

        # Page 8 Alm (FIXED)
        if self.page8.has_content():
            linetext_entries = self.page8.enter_text()
            image_entries = self.page8.enter_images()
            generate_pdf(linetext_entries, image_entries, "ui/resources/templates/pagina3.pdf",
                         "output8.pdf", color)
            pdf_list.append('pdfs/output8.pdf')

        # Page 9 Lan (optional)
        if self.page9.has_content():
            download_simple_PA(self.ui.pageSelectionL.currentIndex(), self.page9, "output9.pdf",
                               self.ui.textNotasL.toPlainText())
            pdf_list.append('pdfs/output9.pdf')
        # Page 10 LanC (optional)
        if self.page10.has_content():
            download_complex_PA(self.page10, "output10.pdf")
            pdf_list.append('pdfs/output10.pdf')
        # Page 11 Snack (optional)
        if self.page11.has_content():
            download_simple_PA(self.ui.pageSelectionSN.currentIndex(), self.page11, "output11.pdf",
                               self.ui.textNotasSN.toPlainText())
            pdf_list.append('pdfs/output11.pdf')
        # Page 12 SnackC (optional)
        if self.page12.has_content():
            download_complex_PA(self.page12, "output12.pdf")
            pdf_list.append('pdfs/output12.pdf')
        # Page 13 Se (optional)
        if self.page13.has_content():
            download_simple_PA(self.ui.pageSelectionSe.currentIndex(), self.page13, "output13.pdf",
                               self.ui.textNotasSe.toPlainText())
            pdf_list.append('pdfs/output13.pdf')
        # Page 14 SeC (optional)
        if self.page14.has_content():
            download_complex_PA(self.page14, "output14.pdf")
            pdf_list.append('pdfs/output14.pdf')

        # Page 15 Jan (FIXED)
        if self.page15.has_content():
            linetext_entries = self.page15.enter_text()
            image_entries = self.page15.enter_images()
            generate_pdf(linetext_entries, image_entries, "ui/resources/templates/pagina3.pdf",
                         "output15.pdf", color)
            pdf_list.append('pdfs/output15.pdf')

        # Page 16 Ceia (optional)
        if self.page16.has_content():
            download_simple_PA(self.ui.pageSelectionC.currentIndex(), self.page16, "output16.pdf",
                               self.ui.textNotasC.toPlainText())
            pdf_list.append('pdfs/output16.pdf')
        # Page 17 CeiaC (optional)
        if self.page17.has_content():
            download_complex_PA(self.page17, "output17.pdf")
            pdf_list.append('pdfs/output17.pdf')


        # Merge PDFs
        merged_pdf_path = 'pdfs/merged_output.pdf'
        merge_pdfs(pdf_list, merged_pdf_path)

        # Prompt user for save location and move merged PDF
        final_save_path = select_save_location()
        if final_save_path:
            try:
                os.rename(merged_pdf_path, final_save_path)
                print(f"PDF saved successfully: {final_save_path}")
            except Exception as e:
                print(f"Error moving file: {e}")
        else:
            print("No file selected. PDF not saved.")
