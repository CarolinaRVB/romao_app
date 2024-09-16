class Pages_Data:
    def __init__(self, ui, parent):
        self.ui = ui
        self.parent = parent
        self.setup_ui()
        # self.names_list = []

    def setup_ui(self):
        self.names_list = [
            "user_id", "lineNome", "linePeso", "lineMG", "lineObj", "lineData", "lineMarc", "lineMax", "textNotasPA",
            "lineTipo",
            "lineHoras", "plain1", "plain2", "plain3", "plain4", "plain5", "plain6",
            "labelImg1_1", "labelImg1_2", "labelImg1_3", "labelImg1_4", "labelImg1_5",
            "labelImg2_1", "labelImg2_2", "labelImg2_3", "labelImg2_4", "labelImg2_5",
            "labelImg3_1", "labelImg3_2", "labelImg3_3", "labelImg3_4", "labelImg3_5",
            "labelImg4_1", "labelImg4_2", "labelImg4_3", "labelImg4_4", "labelImg4_5",
            "labelImg5_1", "labelImg5_2", "labelImg5_3", "labelImg5_4", "labelImg5_5",
            "labelImg6_1", "labelImg6_2", "labelImg6_3", "labelImg6_4", "labelImg6_5",
            "labelImgS1_1", "labelImgS1_2", "labelImgS1_3", "labelImgS1_4", "labelImgS1_5",
            "labelImgS2_1", "labelImgS2_2", "labelImgS2_3", "labelImgS2_4", "labelImgS2_5",
            "labelImgS3_1", "labelImgS3_2", "labelImgS3_3", "labelImgS3_4", "labelImgS3_5",
            "labelImgS4_1", "labelImgS4_2", "labelImgS4_3", "labelImgS4_4", "labelImgS4_5",
            "labelImgS5_1", "labelImgS5_2", "labelImgS5_3", "labelImgS5_4", "labelImgS5_5",
            "labelImgS6_1", "labelImgS6_2", "labelImgS6_3", "labelImgS6_4", "labelImgS6_5",
            "labelImgS7_1", "labelImgS7_2", "labelImgS7_3", "labelImgS7_4", "labelImgS7_5",
            "labelImgS8_1", "labelImgS8_2", "labelImgS8_3", "labelImgS8_4", "labelImgS8_5",
            "labelImgSe_1", "labelImgSe_2", "labelImgSe_3", "labelImgSe_4", "labelImgSe_5",
            "labelImgSe_6", "labelImgSe_7", "labelImgSe_8", "labelImgSe_9", "labelImgSe_10",
            "lineTipoS", "lineHorasS", "textExe", "textNotasPAS", "plainS1", "plainS2", "plainS3", "plainS4", "plainS5",
            "plainS6", "plainS7", "plainS8", "pageSelection",
            "labelImgA1_1", "labelImgA1_2", "labelImgA1_3", "labelImgA1_4", "labelImgA1_5", "labelImgA1_6",
            "labelImgA2_1", "labelImgA2_2", "labelImgA2_3", "labelImgA2_4", "labelImgA2_5", "labelImgA2_6",
            "labelImgA3_1", "labelImgA3_2", "labelImgA3_3", "labelImgA3_4", "labelImgA3_5", "labelImgA3_6",
            "labelImgA4_1", "labelImgA4_2", "labelImgA4_3", "labelImgA4_4", "labelImgA4_5", "labelImgA4_6",
            "labelImgA5_1", "labelImgA5_2", "labelImgA5_3", "labelImgA5_4", "labelImgA5_5", "labelImgA5_6",
            "labelImgAS_1", "labelImgAS_2", "labelImgAS_3", "labelImgAS_4",
            "lineTipoA", "lineHorasA", "lineVeg", "lineAze", "textNotasA", "plainA1_1", "plainA1_2",
            "plainA2_1", "plainA2_2", "plainA3_1", "plainA3_2", "plainA4_1", "plainA4_2",
            "plainA5_1", "plainA5_2", "plainAS",
            "labelImgJ1_1", "labelImgJ1_2", "labelImgJ1_3", "labelImgJ1_4", "labelImgJ1_5", "labelImgJ1_6",
            "labelImgJ2_1", "labelImgJ2_2", "labelImgJ2_3", "labelImgJ2_4", "labelImgJ2_5", "labelImgJ2_6",
            "labelImgJ3_1", "labelImgJ3_2", "labelImgJ3_3", "labelImgJ3_4", "labelImgJ3_5", "labelImgJ3_6",
            "labelImgJ4_1", "labelImgJ4_2", "labelImgJ4_3", "labelImgJ4_4", "labelImgJ4_5", "labelImgJ4_6",
            "labelImgJ5_1", "labelImgJ5_2", "labelImgJ5_3", "labelImgJ5_4", "labelImgJ5_5", "labelImgJ5_6",
            "labelImgJS_1", "labelImgJS_2", "labelImgJS_3", "labelImgJS_4",
            "lineTipoJ", "lineHorasJ", "lineVegJ", "lineAzeJ", "textNotasJ", "plainJ1_1", "plainJ1_2",
            "plainJ2_1", "plainJ2_2", "plainJ3_1", "plainJ3_2", "plainJ4_1", "plainJ4_2",
            "plainJ5_1", "plainJ5_2", "plainJS",
            # Added labels from button_map_MM1
            "labelImgM1_1", "labelImgM1_2", "labelImgM1_3", "labelImgM1_4", "labelImgM1_5",
            "labelImgM2_1", "labelImgM2_2", "labelImgM2_3", "labelImgM2_4", "labelImgM2_5",
            "labelImgM3_1", "labelImgM3_2", "labelImgM3_3", "labelImgM3_4", "labelImgM3_5",
            "labelImgM4_1", "labelImgM4_2", "labelImgM4_3", "labelImgM4_4", "labelImgM4_5",
            "labelImgM5_1", "labelImgM5_2", "labelImgM5_3", "labelImgM5_4", "labelImgM5_5",
            "labelImgM6_1", "labelImgM6_2", "labelImgM6_3", "labelImgM6_4", "labelImgM6_5",
            "lineTipoM1", "lineHorasM1", "textNotasM1", "plainM1", "plainM2", "plainM3", "plainM4", "plainM5",
            "plainM6", "pageSelectionM1",
            # Added labels from button_map_MM2
            "labelImgMM1_1", "labelImgMM1_2", "labelImgMM1_3", "labelImgMM1_4", "labelImgMM1_5",
            "labelImgMM2_1", "labelImgMM2_2", "labelImgMM2_3", "labelImgMM2_4", "labelImgMM2_5",
            "labelImgMM3_1", "labelImgMM3_2", "labelImgMM3_3", "labelImgMM3_4", "labelImgMM3_5",
            "labelImgMM4_1", "labelImgMM4_2", "labelImgMM4_3", "labelImgMM4_4", "labelImgMM4_5",
            "labelImgMM5_1", "labelImgMM5_2", "labelImgMM5_3", "labelImgMM5_4", "labelImgMM5_5",
            "labelImgMM6_1", "labelImgMM6_2", "labelImgMM6_3", "labelImgMM6_4", "labelImgMM6_5",
            "lineTipoMM2", "lineHorasMM2", "textNotasMM2", "plainMM1", "plainMM2", "plainMM3", "plainMM4", "plainMM5",
            "plainMM6", "pageSelectionMM2",
            #labels from MC1
            "labelImgMC1_1", "labelImgMC1_2", "labelImgMC1_3", "labelImgMC1_4", "labelImgMC1_5",
            "labelImgMC2_1", "labelImgMC2_2", "labelImgMC2_3", "labelImgMC2_4", "labelImgMC2_5",
            "labelImgMC3_1", "labelImgMC3_2", "labelImgMC3_3", "labelImgMC3_4", "labelImgMC3_5",
            "labelImgMC4_1", "labelImgMC4_2", "labelImgMC4_3", "labelImgMC4_4", "labelImgMC4_5",
            "labelImgMC5_1", "labelImgMC5_2", "labelImgMC5_3", "labelImgMC5_4", "labelImgMC5_5",
            "labelImgMC6_1", "labelImgMC6_2", "labelImgMC6_3", "labelImgMC6_4", "labelImgMC6_5",
            "labelImgMC7_1", "labelImgMC7_2", "labelImgMC7_3", "labelImgMC7_4", "labelImgMC7_5",
            "labelImgMC8_1", "labelImgMC8_2", "labelImgMC8_3", "labelImgMC8_4", "labelImgMC8_5",
            "labelImgMCe_1", "labelImgMCe_2", "labelImgMCe_3", "labelImgMCe_4", "labelImgMCe_5",
            "labelImgMCe_6", "labelImgMCe_7", "labelImgMCe_8", "labelImgMCe_9", "labelImgMCe_10",
            "lineTipoMC1", "lineHorasMC1", "textNotasMC1", "textExeMC1", "plainMC1", "plainMC2", "plainMC3", "plainMC4",
            "plainMC5", "plainMC6", "plainMC7", "plainMC8",
            #labels from MC2
            "labelImgMMC1_1", "labelImgMMC1_2", "labelImgMMC1_3", "labelImgMMC1_4", "labelImgMMC1_5",
            "labelImgMMC2_1", "labelImgMMC2_2", "labelImgMMC2_3", "labelImgMMC2_4", "labelImgMMC2_5",
            "labelImgMMC3_1", "labelImgMMC3_2", "labelImgMMC3_3", "labelImgMMC3_4", "labelImgMMC3_5",
            "labelImgMMC4_1", "labelImgMMC4_2", "labelImgMMC4_3", "labelImgMMC4_4", "labelImgMMC4_5",
            "labelImgMMC5_1", "labelImgMMC5_2", "labelImgMMC5_3", "labelImgMMC5_4", "labelImgMMC5_5",
            "labelImgMMC6_1", "labelImgMMC6_2", "labelImgMMC6_3", "labelImgMMC6_4", "labelImgMMC6_5",
            "labelImgMMC7_1", "labelImgMMC7_2", "labelImgMMC7_3", "labelImgMMC7_4", "labelImgMMC7_5",
            "labelImgMMC8_1", "labelImgMMC8_2", "labelImgMMC8_3", "labelImgMMC8_4", "labelImgMMC8_5",
            "labelImgMMCe_1", "labelImgMMCe_2", "labelImgMMCe_3", "labelImgMMCe_4", "labelImgMMCe_5",
            "labelImgMMCe_6", "labelImgMMCe_7", "labelImgMMCe_8", "labelImgMMCe_9", "labelImgMMCe_10",
            "lineTipoMMC2", "lineHorasMMC2", "textNotasMMC2", "textExeMMC2", "plainMMC1", "plainMMC2",
            "plainMMC3", "plainMMC4", "plainMMC5", "plainMMC6", "plainMMC7", "plainMMC8",
            #labels for L
            "labelImgL1_1", "labelImgL1_2", "labelImgL1_3", "labelImgL1_4", "labelImgL1_5",
            "labelImgL2_1", "labelImgL2_2", "labelImgL2_3", "labelImgL2_4", "labelImgL2_5",
            "labelImgL3_1", "labelImgL3_2", "labelImgL3_3", "labelImgL3_4", "labelImgL3_5",
            "labelImgL4_1", "labelImgL4_2", "labelImgL4_3", "labelImgL4_4", "labelImgL4_5",
            "labelImgL5_1", "labelImgL5_2", "labelImgL5_3", "labelImgL5_4", "labelImgL5_5",
            "labelImgL6_1", "labelImgL6_2", "labelImgL6_3", "labelImgL6_4", "labelImgL6_5",
            "lineTipoL", "lineHorasL", "textNotasL", "plainL1", "plainL2", "plainL3",
            "plainL4", "plainL5", "plainL6", "pageSelectionL",
            # labels for LC
            "labelImgLC1_1", "labelImgLC1_2", "labelImgLC1_3", "labelImgLC1_4", "labelImgLC1_5",
            "labelImgLC2_1", "labelImgLC2_2", "labelImgLC2_3", "labelImgLC2_4", "labelImgLC2_5",
            "labelImgLC3_1", "labelImgLC3_2", "labelImgLC3_3", "labelImgLC3_4", "labelImgLC3_5",
            "labelImgLC4_1", "labelImgLC4_2", "labelImgLC4_3", "labelImgLC4_4", "labelImgLC4_5",
            "labelImgLC5_1", "labelImgLC5_2", "labelImgLC5_3", "labelImgLC5_4", "labelImgLC5_5",
            "labelImgLC6_1", "labelImgLC6_2", "labelImgLC6_3", "labelImgLC6_4", "labelImgLC6_5",
            "labelImgLC7_1", "labelImgLC7_2", "labelImgLC7_3", "labelImgLC7_4", "labelImgLC7_5",
            "labelImgLC8_1", "labelImgLC8_2", "labelImgLC8_3", "labelImgLC8_4", "labelImgLC8_5",
            "labelImgLCe_1", "labelImgLCe_2", "labelImgLCe_3", "labelImgLCe_4", "labelImgLCe_5",
            "labelImgLCe_6", "labelImgLCe_7", "labelImgLCe_8", "labelImgLCe_9", "labelImgLCe_10",
            "lineTipoLC", "lineHorasLC", "textNotasLC", "textExeLC", "plainLC1", "plainLC2",
            "plainLC3", "plainLC4", "plainLC5", "plainLC6", "plainLC7", "plainLC8",
            # labels for SN
            "labelImgSN1_1", "labelImgSN1_2", "labelImgSN1_3", "labelImgSN1_4", "labelImgSN1_5",
            "labelImgSN2_1", "labelImgSN2_2", "labelImgSN2_3", "labelImgSN2_4", "labelImgSN2_5",
            "labelImgSN3_1", "labelImgSN3_2", "labelImgSN3_3", "labelImgSN3_4", "labelImgSN3_5",
            "labelImgSN4_1", "labelImgSN4_2", "labelImgSN4_3", "labelImgSN4_4", "labelImgSN4_5",
            "labelImgSN5_1", "labelImgSN5_2", "labelImgSN5_3", "labelImgSN5_4", "labelImgSN5_5",
            "labelImgSN6_1", "labelImgSN6_2", "labelImgSN6_3", "labelImgSN6_4", "labelImgSN6_5",
            "lineTipoSN", "lineHorasSN", "textNotasSN", "plainSN1", "plainSN2", "plainSN3",
            "plainSN4", "plainSN5", "plainSN6", "pageSelectionSN",
            # labels for SC
            "labelImgSC1_1", "labelImgSC1_2", "labelImgSC1_3", "labelImgSC1_4", "labelImgSC1_5",
            "labelImgSC2_1", "labelImgSC2_2", "labelImgSC2_3", "labelImgSC2_4", "labelImgSC2_5",
            "labelImgSC3_1", "labelImgSC3_2", "labelImgSC3_3", "labelImgSC3_4", "labelImgSC3_5",
            "labelImgSC4_1", "labelImgSC4_2", "labelImgSC4_3", "labelImgSC4_4", "labelImgSC4_5",
            "labelImgSC5_1", "labelImgSC5_2", "labelImgSC5_3", "labelImgSC5_4", "labelImgSC5_5",
            "labelImgSC6_1", "labelImgSC6_2", "labelImgSC6_3", "labelImgSC6_4", "labelImgSC6_5",
            "labelImgSC7_1", "labelImgSC7_2", "labelImgSC7_3", "labelImgSC7_4", "labelImgSC7_5",
            "labelImgSC8_1", "labelImgSC8_2", "labelImgSC8_3", "labelImgSC8_4", "labelImgSC8_5",
            "labelImgSCe_1", "labelImgSCe_2", "labelImgSCe_3", "labelImgSCe_4", "labelImgSCe_5",
            "labelImgSCe_6", "labelImgSCe_7", "labelImgSCe_8", "labelImgSCe_9", "labelImgSCe_10",
            "lineTipoSC", "lineHorasSC", "textNotasSC", "textExeSC", "plainSC1", "plainSC2",
            "plainSC3", "plainSC4", "plainSC5", "plainSC6", "plainSC7", "plainSC8",
            # labels for Se
            "labelImgSe1_1", "labelImgSe1_2", "labelImgSe1_3", "labelImgSe1_4", "labelImgSe1_5",
            "labelImgSe2_1", "labelImgSe2_2", "labelImgSe2_3", "labelImgSe2_4", "labelImgSe2_5",
            "labelImgSe3_1", "labelImgSe3_2", "labelImgSe3_3", "labelImgSe3_4", "labelImgSe3_5",
            "labelImgSe4_1", "labelImgSe4_2", "labelImgSe4_3", "labelImgSe4_4", "labelImgSe4_5",
            "labelImgSe5_1", "labelImgSe5_2", "labelImgSe5_3", "labelImgSe5_4", "labelImgSe5_5",
            "labelImgSe6_1", "labelImgSe6_2", "labelImgSe6_3", "labelImgSe6_4", "labelImgSe6_5",
            "lineTipoSe", "lineHorasSe", "textNotasSe", "plainSe1", "plainSe2", "plainSe3",
            "plainSe4", "plainSe5", "plainSe6", "pageSelectionSe",
            # labels for Sec
            "labelImgSec1_1", "labelImgSec1_2", "labelImgSec1_3", "labelImgSec1_4", "labelImgSec1_5",
            "labelImgSec2_1", "labelImgSec2_2", "labelImgSec2_3", "labelImgSec2_4", "labelImgSec2_5",
            "labelImgSec3_1", "labelImgSec3_2", "labelImgSec3_3", "labelImgSec3_4", "labelImgSec3_5",
            "labelImgSec4_1", "labelImgSec4_2", "labelImgSec4_3", "labelImgSec4_4", "labelImgSec4_5",
            "labelImgSec5_1", "labelImgSec5_2", "labelImgSec5_3", "labelImgSec5_4", "labelImgSec5_5",
            "labelImgSec6_1", "labelImgSec6_2", "labelImgSec6_3", "labelImgSec6_4", "labelImgSec6_5",
            "labelImgSec7_1", "labelImgSec7_2", "labelImgSec7_3", "labelImgSec7_4", "labelImgSec7_5",
            "labelImgSec8_1", "labelImgSec8_2", "labelImgSec8_3", "labelImgSec8_4", "labelImgSec8_5",
            "labelImgSece_1", "labelImgSece_2", "labelImgSece_3", "labelImgSece_4", "labelImgSece_5",
            "labelImgSece_6", "labelImgSece_7", "labelImgSece_8", "labelImgSece_9", "labelImgSece_10",
            "lineTipoSec", "lineHorasSec", "textNotasSec", "textExeSec", "plainSec1", "plainSec2",
            "plainSec3", "plainSec4", "plainSec5", "plainSec6", "plainSec7", "plainSec8",
            # labels for C
            "labelImgC1_1", "labelImgC1_2", "labelImgC1_3", "labelImgC1_4", "labelImgC1_5",
            "labelImgC2_1", "labelImgC2_2", "labelImgC2_3", "labelImgC2_4", "labelImgC2_5",
            "labelImgC3_1", "labelImgC3_2", "labelImgC3_3", "labelImgC3_4", "labelImgC3_5",
            "labelImgC4_1", "labelImgC4_2", "labelImgC4_3", "labelImgC4_4", "labelImgC4_5",
            "labelImgC5_1", "labelImgC5_2", "labelImgC5_3", "labelImgC5_4", "labelImgC5_5",
            "labelImgC6_1", "labelImgC6_2", "labelImgC6_3", "labelImgC6_4", "labelImgC6_5",
            "lineTipoC", "lineHorasC", "textNotasC", "plainC1", "plainC2", "plainC3", "plainC4",
            "plainC5", "plainC6", "pageSelectionC",
            # labels for CC
            "labelImgCC1_1", "labelImgCC1_2", "labelImgCC1_3", "labelImgCC1_4", "labelImgCC1_5",
            "labelImgCC2_1", "labelImgCC2_2", "labelImgCC2_3", "labelImgCC2_4", "labelImgCC2_5",
            "labelImgCC3_1", "labelImgCC3_2", "labelImgCC3_3", "labelImgCC3_4", "labelImgCC3_5",
            "labelImgCC4_1", "labelImgCC4_2", "labelImgCC4_3", "labelImgCC4_4", "labelImgCC4_5",
            "labelImgCC5_1", "labelImgCC5_2", "labelImgCC5_3", "labelImgCC5_4", "labelImgCC5_5",
            "labelImgCC6_1", "labelImgCC6_2", "labelImgCC6_3", "labelImgCC6_4", "labelImgCC6_5",
            "labelImgCC7_1", "labelImgCC7_2", "labelImgCC7_3", "labelImgCC7_4", "labelImgCC7_5",
            "labelImgCC8_1", "labelImgCC8_2", "labelImgCC8_3", "labelImgCC8_4", "labelImgCC8_5",
            "labelImgCCe_1", "labelImgCCe_2", "labelImgCCe_3", "labelImgCCe_4", "labelImgCCe_5",
            "labelImgCCe_6", "labelImgCCe_7", "labelImgCCe_8", "labelImgCCe_9", "labelImgCCe_10",
            "lineTipoCC", "lineHorasCC", "textNotasCC", "textExeCC",
            "plainCC1", "plainCC2", "plainCC3", "plainCC4", "plainCC5",
            "plainCC6", "plainCC7", "plainCC8"
        ]

        # Lists for Geral page
        self.linetext_names_G = [
            {'widget': self.ui.lineNome, 'x': 129, 'y': 1410, 'color': (255, 255, 255), 'font_size': 12,
             'font_name': "Montserrat-SemiBold", 'centered': "left", 'x_max': 450, 'y_max': 1375.9, 'line_height': 1.2},
            {'widget': self.ui.linePeso, 'x': 120, 'y': 1383, 'color': (255, 255, 255), 'font_size': 12,
             'font_name': "Montserrat-SemiBold", 'centered': "false", 'x_max': 33},
            {'widget': self.ui.lineMG, 'x': 188, 'y': 1356, 'color': (255, 255, 255), 'font_size': 12,
             'font_name': "Montserrat-SemiBold", 'centered': "false", 'x_max': 24},
            {'widget': self.ui.lineObj, 'x': 155, 'y': 1329.1, 'color': (255, 255, 255), 'font_size': 12,
             'font_name': "Montserrat-SemiBold", 'centered': "left", 'x_max': 450, 'y_max': 1295, 'line_height': 1.2},
            {'widget': self.ui.lineData, 'x': 120, 'y': 1296, 'color': (255, 255, 255), 'font_size': 12,
             'font_name': "Montserrat-SemiBold", 'centered':  "left", 'x_max': 450, 'y_max': 1375.9, 'line_height': 1.2},
            {'widget': self.ui.lineMarc, 'x': 405, 'y': 881, 'color': (0, 0, 0), 'font_size': 16.5,
             'font_name': "Montserrat-Bold", 'centered': "false", 'x_max': 140},
            {'widget': self.ui.lineMax, 'x': 430, 'y': 824, 'color': (0, 0, 0), 'font_size': 16.5,
             'font_name': "Montserrat-Bold", 'centered': "false", 'x_max': 140}
        ]

        # Lists for PA page
        self.button_map_PA = {
            "pushImg1_1": "labelImg1_1", "pushImg1_2": "labelImg1_2",
            "pushImg1_3": "labelImg1_3", "pushImg1_4": "labelImg1_4",
            "pushImg1_5": "labelImg1_5", "pushImg2_1": "labelImg2_1",
            "pushImg2_2": "labelImg2_2", "pushImg2_3": "labelImg2_3",
            "pushImg2_4": "labelImg2_4", "pushImg2_5": "labelImg2_5",
            "pushImg3_1": "labelImg3_1", "pushImg3_2": "labelImg3_2",
            "pushImg3_3": "labelImg3_3", "pushImg3_4": "labelImg3_4",
            "pushImg3_5": "labelImg3_5", "pushImg4_1": "labelImg4_1",
            "pushImg4_2": "labelImg4_2", "pushImg4_3": "labelImg4_3",
            "pushImg4_4": "labelImg4_4", "pushImg4_5": "labelImg4_5",
            "pushImg5_1": "labelImg5_1", "pushImg5_2": "labelImg5_2",
            "pushImg5_3": "labelImg5_3", "pushImg5_4": "labelImg5_4",
            "pushImg5_5": "labelImg5_5", "pushImg6_1": "labelImg6_1",
            "pushImg6_2": "labelImg6_2", "pushImg6_3": "labelImg6_3",
            "pushImg6_4": "labelImg6_4", "pushImg6_5": "labelImg6_5"
        }

        self.button_remove_PA = {
            "pushImg1_6": "labelImg1_1", "pushImg1_7": "labelImg1_2",
            "pushImg1_8": "labelImg1_3", "pushImg1_9": "labelImg1_4",
            "pushImg1_10": "labelImg1_5", "pushImg2_6": "labelImg2_1",
            "pushImg2_7": "labelImg2_2", "pushImg2_8": "labelImg2_3",
            "pushImg2_9": "labelImg2_4", "pushImg2_10": "labelImg2_5",
            "pushImg3_6": "labelImg3_1", "pushImg3_7": "labelImg3_2",
            "pushImg3_8": "labelImg3_3", "pushImg3_9": "labelImg3_4",
            "pushImg3_10": "labelImg3_5", "pushImg4_6": "labelImg4_1",
            "pushImg4_7": "labelImg4_2", "pushImg4_8": "labelImg4_3",
            "pushImg4_9": "labelImg4_4", "pushImg4_10": "labelImg4_5",
            "pushImg5_6": "labelImg5_1", "pushImg5_7": "labelImg5_2",
            "pushImg5_8": "labelImg5_3", "pushImg5_9": "labelImg5_4",
            "pushImg5_10": "labelImg5_5", "pushImg6_6": "labelImg6_1",
            "pushImg6_7": "labelImg6_2", "pushImg6_8": "labelImg6_3",
            "pushImg6_9": "labelImg6_4", "pushImg6_10": "labelImg6_5"
        }
        self.images_list_PA = [
            ["labelImg1_1", "labelImg1_2", "labelImg1_3", "labelImg1_4", "labelImg1_5"],
            ["labelImg2_1", "labelImg2_2", "labelImg2_3", "labelImg2_4", "labelImg2_5"],
            ["labelImg3_1", "labelImg3_2", "labelImg3_3", "labelImg3_4", "labelImg3_5"],
            ["labelImg4_1", "labelImg4_2", "labelImg4_3", "labelImg4_4", "labelImg4_5"],
            ["labelImg5_1", "labelImg5_2", "labelImg5_3", "labelImg5_4", "labelImg5_5"],
            ["labelImg6_1", "labelImg6_2", "labelImg6_3", "labelImg6_4", "labelImg6_5"]
        ]

        self.boxes_coords_PA = [
            # box0
            [
                [{'path': "", 'x': 140, 'y': 1290}],
                [{'path': "", 'x': 110, 'y': 1290}, {'path': "", 'x': 170, 'y': 1290}],
                [{'path': "", 'x': 80, 'y': 1290}, {'path': "", 'x': 140, 'y': 1290},
                 {'path': "", 'x': 200, 'y': 1290}],
                [{'path': "", 'x': 50, 'y': 1290}, {'path': "", 'x': 110, 'y': 1290}, {'path': "", 'x': 170, 'y': 1290},
                 {'path': "", 'x': 230, 'y': 1290}],
                [{'path': "", 'x': 45, 'y': 1290}, {'path': "", 'x': 95, 'y': 1290}, {'path': "", 'x': 145, 'y': 1290},
                 {'path': "", 'x': 195, 'y': 1290}, {'path': "", 'x': 245, 'y': 1290}]
            ],
            # box1
            [
                [{'path': "", 'x': 405, 'y': 1290}],
                [{'path': "", 'x': 375, 'y': 1290}, {'path': "", 'x': 435, 'y': 1290}],
                [{'path': "", 'x': 345, 'y': 1290}, {'path': "", 'x': 405, 'y': 1290},
                 {'path': "", 'x': 465, 'y': 1290}],
                [{'path': "", 'x': 315, 'y': 1290}, {'path': "", 'x': 375, 'y': 1290},
                 {'path': "", 'x': 435, 'y': 1290}, {'path': "", 'x': 495, 'y': 1290}],
                [{'path': "", 'x': 310, 'y': 1290}, {'path': "", 'x': 360, 'y': 1290},
                 {'path': "", 'x': 410, 'y': 1290}, {'path': "", 'x': 460, 'y': 1290},
                 {'path': "", 'x': 510, 'y': 1290}]
            ],
            # box2
            [
                [{'path': "", 'x': 140, 'y': 1130}],
                [{'path': "", 'x': 110, 'y': 1130}, {'path': "", 'x': 170, 'y': 1130}],
                [{'path': "", 'x': 80, 'y': 1130}, {'path': "", 'x': 140, 'y': 1130},
                 {'path': "", 'x': 200, 'y': 1130}],
                [{'path': "", 'x': 50, 'y': 1130}, {'path': "", 'x': 110, 'y': 1130}, {'path': "", 'x': 170, 'y': 1130},
                 {'path': "", 'x': 230, 'y': 1130}],
                [{'path': "", 'x': 45, 'y': 1130}, {'path': "", 'x': 95, 'y': 1130}, {'path': "", 'x': 145, 'y': 1130},
                 {'path': "", 'x': 195, 'y': 1130}, {'path': "", 'x': 245, 'y': 1130}]
            ],
            # box3
            [
                [{'path': "", 'x': 405, 'y': 1130}],
                [{'path': "", 'x': 375, 'y': 1130}, {'path': "", 'x': 435, 'y': 1130}],
                [{'path': "", 'x': 345, 'y': 1130}, {'path': "", 'x': 405, 'y': 1130},
                 {'path': "", 'x': 465, 'y': 1130}],
                [{'path': "", 'x': 315, 'y': 1130}, {'path': "", 'x': 375, 'y': 1130},
                 {'path': "", 'x': 435, 'y': 1130}, {'path': "", 'x': 495, 'y': 1130}],
                [{'path': "", 'x': 310, 'y': 1130}, {'path': "", 'x': 360, 'y': 1130},
                 {'path': "", 'x': 410, 'y': 1130}, {'path': "", 'x': 460, 'y': 1130},
                 {'path': "", 'x': 510, 'y': 1130}]
            ],
            # box4
            [
                [{'path': "", 'x': 140, 'y': 970}],
                [{'path': "", 'x': 110, 'y': 970}, {'path': "", 'x': 170, 'y': 970}],
                [{'path': "", 'x': 80, 'y': 970}, {'path': "", 'x': 140, 'y': 970}, {'path': "", 'x': 200, 'y': 970}],
                [{'path': "", 'x': 50, 'y': 970}, {'path': "", 'x': 110, 'y': 970}, {'path': "", 'x': 170, 'y': 970},
                 {'path': "", 'x': 230, 'y': 970}],
                [{'path': "", 'x': 45, 'y': 970}, {'path': "", 'x': 95, 'y': 970}, {'path': "", 'x': 145, 'y': 970},
                 {'path': "", 'x': 195, 'y': 970}, {'path': "", 'x': 245, 'y': 970}]
            ],
            # box5
            [
                [{'path': "", 'x': 405, 'y': 970}],
                [{'path': "", 'x': 375, 'y': 970}, {'path': "", 'x': 435, 'y': 970}],
                [{'path': "", 'x': 345, 'y': 970}, {'path': "", 'x': 405, 'y': 970}, {'path': "", 'x': 465, 'y': 970}],
                [{'path': "", 'x': 315, 'y': 970}, {'path': "", 'x': 375, 'y': 970}, {'path': "", 'x': 435, 'y': 970},
                 {'path': "", 'x': 495, 'y': 970}],
                [{'path': "", 'x': 310, 'y': 970}, {'path': "", 'x': 360, 'y': 970}, {'path': "", 'x': 410, 'y': 970},
                 {'path': "", 'x': 460, 'y': 970}, {'path': "", 'x': 510, 'y': 970}]
            ]
        ]

        self.grid_names_PA = [self.ui.gridLayout_7, self.ui.gridLayout_9, self.ui.gridLayout_46, self.ui.gridLayout_43,
                         self.ui.gridLayout_57, self.ui.gridLayout_58, self.ui.gridLayout_59, self.ui.gridLayout_60]

        self.button_map_Al = {
            "pushImgA1_1": "labelImgA1_1", "pushImgA1_2": "labelImgA1_2",
            "pushImgA1_3": "labelImgA1_3", "pushImgA1_4": "labelImgA1_4",
            "pushImgA1_5": "labelImgA1_5", "pushImgA1_6": "labelImgA1_6",

            "pushImgA2_1": "labelImgA2_1", "pushImgA2_2": "labelImgA2_2",
            "pushImgA2_3": "labelImgA2_3", "pushImgA2_4": "labelImgA2_4",
            "pushImgA2_5": "labelImgA2_5", "pushImgA2_6": "labelImgA2_6",

            "pushImgA3_1": "labelImgA3_1", "pushImgA3_2": "labelImgA3_2",
            "pushImgA3_3": "labelImgA3_3", "pushImgA3_4": "labelImgA3_4",
            "pushImgA3_5": "labelImgA3_5", "pushImgA3_6": "labelImgA3_6",

            "pushImgA4_1": "labelImgA4_1", "pushImgA4_2": "labelImgA4_2",
            "pushImgA4_3": "labelImgA4_3", "pushImgA4_4": "labelImgA4_4",
            "pushImgA4_5": "labelImgA4_5", "pushImgA4_6": "labelImgA4_6",

            "pushImgA5_1": "labelImgA5_1", "pushImgA5_2": "labelImgA5_2",
            "pushImgA5_3": "labelImgA5_3", "pushImgA5_4": "labelImgA5_4",
            "pushImgA5_5": "labelImgA5_5", "pushImgA5_6": "labelImgA5_6",

            "pushImgAS_1": "labelImgAS_1", "pushImgAS_2": "labelImgAS_2",
            "pushImgAS_3": "labelImgAS_3", "pushImgAS_4": "labelImgAS_4",
        }

        self.button_remove_Al = {
            "pushImgA1_7": "labelImgA1_1", "pushImgA1_8": "labelImgA1_2",
            "pushImgA1_9": "labelImgA1_3", "pushImgA1_10": "labelImgA1_4",
            "pushImgA1_11": "labelImgA1_5", "pushImgA1_12": "labelImgA1_6",

            "pushImgA2_7": "labelImgA2_1", "pushImgA2_8": "labelImgA2_2",
            "pushImgA2_9": "labelImgA2_3", "pushImgA2_10": "labelImgA2_4",
            "pushImgA2_11": "labelImgA2_5", "pushImgA2_12": "labelImgA2_6",

            "pushImgA3_7": "labelImgA3_1", "pushImgA3_8": "labelImgA3_2",
            "pushImgA3_9": "labelImgA3_3", "pushImgA3_10": "labelImgA3_4",
            "pushImgA3_11": "labelImgA3_5", "pushImgA3_12": "labelImgA3_6",

            "pushImgA4_7": "labelImgA4_1", "pushImgA4_8": "labelImgA4_2",
            "pushImgA4_9": "labelImgA4_3", "pushImgA4_10": "labelImgA4_4",
            "pushImgA4_11": "labelImgA4_5", "pushImgA4_12": "labelImgA4_6",

            "pushImgA5_7": "labelImgA5_1", "pushImgA5_8": "labelImgA5_2",
            "pushImgA5_9": "labelImgA5_3", "pushImgA5_10": "labelImgA5_4",
            "pushImgA5_11": "labelImgA5_5", "pushImgA5_12": "labelImgA5_6",

            "pushImgAS_5": "labelImgAS_1", "pushImgAS_6": "labelImgAS_2",
            "pushImgAS_7": "labelImgAS_3", "pushImgAS_8": "labelImgAS_4",
        }

        self.images_list_Al = [
            ["labelImgA1_1", "labelImgA1_2", "labelImgA1_3"],
            ["labelImgA1_4", "labelImgA1_5", "labelImgA1_6"],
            ["labelImgA2_1", "labelImgA2_2", "labelImgA2_3"],
            ["labelImgA2_4", "labelImgA2_5", "labelImgA2_6"],
            ["labelImgA3_1", "labelImgA3_2", "labelImgA3_3"],
            ["labelImgA3_4", "labelImgA3_5", "labelImgA3_6"],
            ["labelImgA4_1", "labelImgA4_2", "labelImgA4_3"],
            ["labelImgA4_4", "labelImgA4_5", "labelImgA4_6"],
            ["labelImgA5_1", "labelImgA5_2", "labelImgA5_3"],
            ["labelImgA5_4", "labelImgA5_5", "labelImgA5_6"],
            ["labelImgAS_1", "labelImgAS_2", "labelImgAS_3", "labelImgAS_4"]
        ]

        self.boxes_coords_Al = [
            # box0
            [
                [{'path': "", 'x': 140, 'y': 972}],
                [{'path': "", 'x': 110, 'y': 972}, {'path': "", 'x': 170, 'y': 972}],
                [{'path': "", 'x': 80, 'y': 972}, {'path': "", 'x': 140, 'y': 972}, {'path': "", 'x': 200, 'y': 972}]
            ],
            # box1
            [
                [{'path': "", 'x': 405, 'y': 972}],
                [{'path': "", 'x': 375, 'y': 972}, {'path': "", 'x': 435, 'y': 972}],
                [{'path': "", 'x': 345, 'y': 972}, {'path': "", 'x': 405, 'y': 972}, {'path': "", 'x': 465, 'y': 972}]
            ],
            # box2
            [
                [{'path': "", 'x': 140, 'y': 822}],
                [{'path': "", 'x': 110, 'y': 822}, {'path': "", 'x': 170, 'y': 822}],
                [{'path': "", 'x': 80, 'y': 822}, {'path': "", 'x': 140, 'y': 822}, {'path': "", 'x': 200, 'y': 822}]
            ],
            # box3
            [
                [{'path': "", 'x': 405, 'y': 822}],
                [{'path': "", 'x': 375, 'y': 822}, {'path': "", 'x': 435, 'y': 822}],
                [{'path': "", 'x': 345, 'y': 822}, {'path': "", 'x': 405, 'y': 822}, {'path': "", 'x': 465, 'y': 822}]
            ],
            # box4
            [
                [{'path': "", 'x': 140, 'y': 672}],
                [{'path': "", 'x': 110, 'y': 672}, {'path': "", 'x': 170, 'y': 672}],
                [{'path': "", 'x': 80, 'y': 672}, {'path': "", 'x': 140, 'y': 672}, {'path': "", 'x': 200, 'y': 672}]
            ],
            # box5
            [
                [{'path': "", 'x': 405, 'y': 672}],
                [{'path': "", 'x': 375, 'y': 672}, {'path': "", 'x': 435, 'y': 672}],
                [{'path': "", 'x': 345, 'y': 672}, {'path': "", 'x': 405, 'y': 672}, {'path': "", 'x': 465, 'y': 672}]
            ],
            # box6
            [
                [{'path': "", 'x': 140, 'y': 522}],
                [{'path': "", 'x': 110, 'y': 522}, {'path': "", 'x': 170, 'y': 522}],
                [{'path': "", 'x': 80, 'y': 522}, {'path': "", 'x': 140, 'y': 522}, {'path': "", 'x': 200, 'y': 522}]
            ],
            # box7
            [
                [{'path': "", 'x': 405, 'y': 522}],
                [{'path': "", 'x': 375, 'y': 522}, {'path': "", 'x': 435, 'y': 522}],
                [{'path': "", 'x': 345, 'y': 522}, {'path': "", 'x': 405, 'y': 522}, {'path': "", 'x': 465, 'y': 522}]
            ],
            # box8
            [
                [{'path': "", 'x': 140, 'y': 372}],
                [{'path': "", 'x': 110, 'y': 372}, {'path': "", 'x': 170, 'y': 372}],
                [{'path': "", 'x': 80, 'y': 372}, {'path': "", 'x': 140, 'y': 372}, {'path': "", 'x': 200, 'y': 372}]
            ],
            # box9
            [
                [{'path': "", 'x': 405, 'y': 372}],
                [{'path': "", 'x': 375, 'y': 372}, {'path': "", 'x': 435, 'y': 372}],
                [{'path': "", 'x': 345, 'y': 372}, {'path': "", 'x': 405, 'y': 372}, {'path': "", 'x': 465, 'y': 372}]
            ],
            # box10
            [
                [{'path': "", 'x': 275, 'y': 230}],
                [{'path': "", 'x': 245, 'y': 230}, {'path': "", 'x': 305, 'y': 230}],
                [{'path': "", 'x': 215, 'y': 230}, {'path': "", 'x': 275, 'y': 230}, {'path': "", 'x': 335, 'y': 230}],
                [{'path': "", 'x': 185, 'y': 230}, {'path': "", 'x': 245, 'y': 230}, {'path': "", 'x': 305, 'y': 230},
                 {'path': "", 'x': 365, 'y': 230}]
            ]
        ]

        # Lists for Pequeno Almoço Especial
        self.button_map_PAS = {
            "pushImgS1_1": "labelImgS1_1", "pushImgS1_2": "labelImgS1_2",
            "pushImgS1_3": "labelImgS1_3", "pushImgS1_4": "labelImgS1_4",
            "pushImgS1_5": "labelImgS1_5", "pushImgS2_1": "labelImgS2_1",
            "pushImgS2_2": "labelImgS2_2", "pushImgS2_3": "labelImgS2_3",
            "pushImgS2_4": "labelImgS2_4", "pushImgS2_5": "labelImgS2_5",
            "pushImgS3_1": "labelImgS3_1", "pushImgS3_2": "labelImgS3_2",
            "pushImgS3_3": "labelImgS3_3", "pushImgS3_4": "labelImgS3_4",
            "pushImgS3_5": "labelImgS3_5", "pushImgS4_1": "labelImgS4_1",
            "pushImgS4_2": "labelImgS4_2", "pushImgS4_3": "labelImgS4_3",
            "pushImgS4_4": "labelImgS4_4", "pushImgS4_5": "labelImgS4_5",
            "pushImgS5_1": "labelImgS5_1", "pushImgS5_2": "labelImgS5_2",
            "pushImgS5_3": "labelImgS5_3", "pushImgS5_4": "labelImgS5_4",
            "pushImgS5_5": "labelImgS5_5", "pushImgS6_1": "labelImgS6_1",
            "pushImgS6_2": "labelImgS6_2", "pushImgS6_3": "labelImgS6_3",
            "pushImgS6_4": "labelImgS6_4", "pushImgS6_5": "labelImgS6_5",
            "pushImgS7_1": "labelImgS7_1", "pushImgS7_2": "labelImgS7_2",
            "pushImgS7_3": "labelImgS7_3", "pushImgS7_4": "labelImgS7_4",
            "pushImgS7_5": "labelImgS7_5", "pushImgS8_1": "labelImgS8_1",
            "pushImgS8_2": "labelImgS8_2", "pushImgS8_3": "labelImgS8_3",
            "pushImgS8_4": "labelImgS8_4", "pushImgS8_5": "labelImgS8_5",
            "pushImgSe_1": "labelImgSe_1", "pushImgSe_2": "labelImgSe_2",
            "pushImgSe_3": "labelImgSe_3", "pushImgSe_4": "labelImgSe_4",
            "pushImgSe_5": "labelImgSe_5", "pushImgSe_11": "labelImgSe_6",
            "pushImgSe_12": "labelImgSe_7", "pushImgSe_13": "labelImgSe_8",
            "pushImgSe_14": "labelImgSe_9", "pushImgSe_15": "labelImgSe_10",
        }

        self.button_remove_PAS = {
            "pushImgS1_6": "labelImgS1_1", "pushImgS1_7": "labelImgS1_2",
            "pushImgS1_8": "labelImgS1_3", "pushImgS1_9": "labelImgS1_4",
            "pushImgS1_10": "labelImgS1_5", "pushImgS2_6": "labelImgS2_1",
            "pushImgS2_7": "labelImgS2_2", "pushImgS2_8": "labelImgS2_3",
            "pushImgS2_9": "labelImgS2_4", "pushImgS2_10": "labelImgS2_5",
            "pushImgS3_6": "labelImgS3_1", "pushImgS3_7": "labelImgS3_2",
            "pushImgS3_8": "labelImgS3_3", "pushImgS3_9": "labelImgS3_4",
            "pushImgS3_10": "labelImgS3_5", "pushImgS4_6": "labelImgS4_1",
            "pushImgS4_7": "labelImgS4_2", "pushImgS4_8": "labelImgS4_3",
            "pushImgS4_9": "labelImgS4_4", "pushImgS4_10": "labelImgS4_5",
            "pushImgS5_6": "labelImgS5_1", "pushImgS5_7": "labelImgS5_2",
            "pushImgS5_8": "labelImgS5_3", "pushImgS5_9": "labelImgS5_4",
            "pushImgS5_10": "labelImgS5_5", "pushImgS6_6": "labelImgS6_1",
            "pushImgS6_7": "labelImgS6_2", "pushImgS6_8": "labelImgS6_3",
            "pushImgS6_9": "labelImgS6_4", "pushImgS6_10": "labelImgS6_5",
            "pushImgS7_6": "labelImgS7_1", "pushImgS7_7": "labelImgS7_2",
            "pushImgS7_8": "labelImgS7_3", "pushImgS7_9": "labelImgS7_4",
            "pushImgS7_10": "labelImgS7_5", "pushImgS8_6": "labelImgS8_1",
            "pushImgS8_7": "labelImgS8_2", "pushImgS8_8": "labelImgS8_3",
            "pushImgS8_9": "labelImgS8_4", "pushImgS8_10": "labelImgS8_5",
            "pushImgSe_6": "labelImgSe_1", "pushImgSe_7": "labelImgSe_2",
            "pushImgSe_8": "labelImgSe_3", "pushImgSe_9": "labelImgSe_4",
            "pushImgSe_10": "labelImgSe_5", "pushImgSe_16": "labelImgSe_6",
            "pushImgSe_17": "labelImgSe_7", "pushImgSe_18": "labelImgSe_8",
            "pushImgSe_19": "labelImgSe_9", "pushImgSe_20": "labelImgSe_10",
        }

        self.images_list_PAS = [
            ["labelImgS1_1", "labelImgS1_2", "labelImgS1_3", "labelImgS1_4", "labelImgS1_5"],
            ["labelImgS2_1", "labelImgS2_2", "labelImgS2_3", "labelImgS2_4", "labelImgS2_5"],
            ["labelImgS3_1", "labelImgS3_2", "labelImgS3_3", "labelImgS3_4", "labelImgS3_5"],
            ["labelImgS4_1", "labelImgS4_2", "labelImgS4_3", "labelImgS4_4", "labelImgS4_5"],
            ["labelImgS5_1", "labelImgS5_2", "labelImgS5_3", "labelImgS5_4", "labelImgS5_5"],
            ["labelImgS6_1", "labelImgS6_2", "labelImgS6_3", "labelImgS6_4", "labelImgS6_5"],
            ["labelImgS7_1", "labelImgS7_2", "labelImgS7_3", "labelImgS7_4", "labelImgS7_5"],
            ["labelImgS8_1", "labelImgS8_2", "labelImgS8_3", "labelImgS8_4", "labelImgS8_5"],
            ["labelImgSe_1", "labelImgSe_2", "labelImgSe_3", "labelImgSe_4", "labelImgSe_5"],
            ["labelImgSe_6", "labelImgSe_7", "labelImgSe_8", "labelImgSe_9", "labelImgSe_10"]
        ]

        self.boxes_coords_PAS = [
            # Box 0
            [
                [{'path': "", 'x': 140, 'y': 1248}],
                [{'path': "", 'x': 110, 'y': 1248}, {'path': "", 'x': 170, 'y': 1248}],
                [{'path': "", 'x': 80, 'y': 1248}, {'path': "", 'x': 140, 'y': 1248},
                 {'path': "", 'x': 200, 'y': 1248}],
                [{'path': "", 'x': 50, 'y': 1248}, {'path': "", 'x': 110, 'y': 1248}, {'path': "", 'x': 170, 'y': 1248},
                 {'path': "", 'x': 230, 'y': 1248}],
                [{'path': "", 'x': 45, 'y': 1248}, {'path': "", 'x': 95, 'y': 1248}, {'path': "", 'x': 145, 'y': 1248},
                 {'path': "", 'x': 195, 'y': 1248}, {'path': "", 'x': 245, 'y': 1248}]
            ],
            # Box 1
            [
                [{'path': "", 'x': 405, 'y': 1248}],
                [{'path': "", 'x': 375, 'y': 1248}, {'path': "", 'x': 435, 'y': 1248}],
                [{'path': "", 'x': 345, 'y': 1248}, {'path': "", 'x': 405, 'y': 1248},
                 {'path': "", 'x': 465, 'y': 1248}],
                [{'path': "", 'x': 315, 'y': 1248}, {'path': "", 'x': 375, 'y': 1248},
                 {'path': "", 'x': 435, 'y': 1248}, {'path': "", 'x': 495, 'y': 1248}],
                [{'path': "", 'x': 310, 'y': 1248}, {'path': "", 'x': 360, 'y': 1248},
                 {'path': "", 'x': 410, 'y': 1248}, {'path': "", 'x': 460, 'y': 1248},
                 {'path': "", 'x': 510, 'y': 1248}]
            ],
            # Box 2
            [
                [{'path': "", 'x': 140, 'y': 1088}],
                [{'path': "", 'x': 110, 'y': 1088}, {'path': "", 'x': 170, 'y': 1088}],
                [{'path': "", 'x': 80, 'y': 1088}, {'path': "", 'x': 140, 'y': 1088},
                 {'path': "", 'x': 200, 'y': 1088}],
                [{'path': "", 'x': 50, 'y': 1088}, {'path': "", 'x': 110, 'y': 1088}, {'path': "", 'x': 170, 'y': 1088},
                 {'path': "", 'x': 230, 'y': 1088}],
                [{'path': "", 'x': 45, 'y': 1088}, {'path': "", 'x': 95, 'y': 1088}, {'path': "", 'x': 145, 'y': 1088},
                 {'path': "", 'x': 195, 'y': 1088}, {'path': "", 'x': 245, 'y': 1088}]
            ],
            # Box 3
            [
                [{'path': "", 'x': 405, 'y': 1088}],
                [{'path': "", 'x': 375, 'y': 1088}, {'path': "", 'x': 435, 'y': 1088}],
                [{'path': "", 'x': 345, 'y': 1088}, {'path': "", 'x': 405, 'y': 1088},
                 {'path': "", 'x': 465, 'y': 1088}],
                [{'path': "", 'x': 315, 'y': 1088}, {'path': "", 'x': 375, 'y': 1088},
                 {'path': "", 'x': 435, 'y': 1088}, {'path': "", 'x': 495, 'y': 1088}],
                [{'path': "", 'x': 310, 'y': 1088}, {'path': "", 'x': 360, 'y': 1088},
                 {'path': "", 'x': 410, 'y': 1088}, {'path': "", 'x': 460, 'y': 1088},
                 {'path': "", 'x': 510, 'y': 1088}]
            ],
            # Box 4
            [
                [{'path': "", 'x': 140, 'y': 883}],
                [{'path': "", 'x': 110, 'y': 883}, {'path': "", 'x': 170, 'y': 883}],
                [{'path': "", 'x': 80, 'y': 883}, {'path': "", 'x': 140, 'y': 883}, {'path': "", 'x': 200, 'y': 883}],
                [{'path': "", 'x': 50, 'y': 883}, {'path': "", 'x': 110, 'y': 883}, {'path': "", 'x': 170, 'y': 883},
                 {'path': "", 'x': 230, 'y': 883}],
                [{'path': "", 'x': 45, 'y': 883}, {'path': "", 'x': 95, 'y': 883}, {'path': "", 'x': 145, 'y': 883},
                 {'path': "", 'x': 195, 'y': 883}, {'path': "", 'x': 245, 'y': 883}]
            ],
            # Box 5
            [
                [{'path': "", 'x': 405, 'y': 883}],
                [{'path': "", 'x': 375, 'y': 883}, {'path': "", 'x': 435, 'y': 883}],
                [{'path': "", 'x': 345, 'y': 883}, {'path': "", 'x': 405, 'y': 883}, {'path': "", 'x': 465, 'y': 883}],
                [{'path': "", 'x': 315, 'y': 883}, {'path': "", 'x': 375, 'y': 883}, {'path': "", 'x': 435, 'y': 883},
                 {'path': "", 'x': 495, 'y': 883}],
                [{'path': "", 'x': 310, 'y': 883}, {'path': "", 'x': 360, 'y': 883}, {'path': "", 'x': 410, 'y': 883},
                 {'path': "", 'x': 460, 'y': 883}, {'path': "", 'x': 510, 'y': 883}]
            ],
            # Box 6
            [
                [{'path': "", 'x': 140, 'y': 718}],
                [{'path': "", 'x': 110, 'y': 718}, {'path': "", 'x': 170, 'y': 718}],
                [{'path': "", 'x': 80, 'y': 718}, {'path': "", 'x': 140, 'y': 718}, {'path': "", 'x': 200, 'y': 718}],
                [{'path': "", 'x': 50, 'y': 718}, {'path': "", 'x': 110, 'y': 718}, {'path': "", 'x': 170, 'y': 718},
                 {'path': "", 'x': 230, 'y': 718}],
                [{'path': "", 'x': 45, 'y': 718}, {'path': "", 'x': 95, 'y': 718}, {'path': "", 'x': 145, 'y': 718},
                 {'path': "", 'x': 195, 'y': 718}, {'path': "", 'x': 245, 'y': 718}]
            ],
            # Box 7
            [
                [{'path': "", 'x': 405, 'y': 718}],
                [{'path': "", 'x': 375, 'y': 718}, {'path': "", 'x': 435, 'y': 718}],
                [{'path': "", 'x': 345, 'y': 718}, {'path': "", 'x': 405, 'y': 718}, {'path': "", 'x': 465, 'y': 718}],
                [{'path': "", 'x': 315, 'y': 718}, {'path': "", 'x': 375, 'y': 718}, {'path': "", 'x': 435, 'y': 718},
                 {'path': "", 'x': 495, 'y': 718}],
                [{'path': "", 'x': 310, 'y': 718}, {'path': "", 'x': 360, 'y': 718}, {'path': "", 'x': 410, 'y': 718},
                 {'path': "", 'x': 460, 'y': 718}, {'path': "", 'x': 510, 'y': 718}]
            ],
            # Box 8
            [
                [{'path': "", 'x': 140, 'y': 538}],
                [{'path': "", 'x': 110, 'y': 538}, {'path': "", 'x': 170, 'y': 538}],
                [{'path': "", 'x': 80, 'y': 538}, {'path': "", 'x': 140, 'y': 538}, {'path': "", 'x': 200, 'y': 538}],
                [{'path': "", 'x': 50, 'y': 538}, {'path': "", 'x': 110, 'y': 538}, {'path': "", 'x': 170, 'y': 538},
                 {'path': "", 'x': 230, 'y': 538}],
                [{'path': "", 'x': 45, 'y': 538}, {'path': "", 'x': 95, 'y': 538}, {'path': "", 'x': 145, 'y': 538},
                 {'path': "", 'x': 195, 'y': 538}, {'path': "", 'x': 245, 'y': 538}]
            ],
            # Box 9
            [
                [{'path': "", 'x': 405, 'y': 538}],
                [{'path': "", 'x': 375, 'y': 538}, {'path': "", 'x': 435, 'y': 538}],
                [{'path': "", 'x': 345, 'y': 538}, {'path': "", 'x': 405, 'y': 538}, {'path': "", 'x': 465, 'y': 538}],
                [{'path': "", 'x': 315, 'y': 538}, {'path': "", 'x': 375, 'y': 538}, {'path': "", 'x': 435, 'y': 538},
                 {'path': "", 'x': 495, 'y': 538}],
                [{'path': "", 'x': 310, 'y': 538}, {'path': "", 'x': 360, 'y': 538}, {'path': "", 'x': 410, 'y': 538},
                 {'path': "", 'x': 460, 'y': 538}, {'path': "", 'x': 510, 'y': 538}]
            ]
        ]

        #List for MC1
        self.button_map_MC1 = {
            "pushImgMC1_1": "labelImgMC1_1", "pushImgMC1_2": "labelImgMC1_2",
            "pushImgMC1_3": "labelImgMC1_3", "pushImgMC1_4": "labelImgMC1_4",
            "pushImgMC1_5": "labelImgMC1_5", "pushImgMC2_1": "labelImgMC2_1",
            "pushImgMC2_2": "labelImgMC2_2", "pushImgMC2_3": "labelImgMC2_3",
            "pushImgMC2_4": "labelImgMC2_4", "pushImgMC2_5": "labelImgMC2_5",
            "pushImgMC3_1": "labelImgMC3_1", "pushImgMC3_2": "labelImgMC3_2",
            "pushImgMC3_3": "labelImgMC3_3", "pushImgMC3_4": "labelImgMC3_4",
            "pushImgMC3_5": "labelImgMC3_5", "pushImgMC4_1": "labelImgMC4_1",
            "pushImgMC4_2": "labelImgMC4_2", "pushImgMC4_3": "labelImgMC4_3",
            "pushImgMC4_4": "labelImgMC4_4", "pushImgMC4_5": "labelImgMC4_5",
            "pushImgMC5_1": "labelImgMC5_1", "pushImgMC5_2": "labelImgMC5_2",
            "pushImgMC5_3": "labelImgMC5_3", "pushImgMC5_4": "labelImgMC5_4",
            "pushImgMC5_5": "labelImgMC5_5", "pushImgMC6_1": "labelImgMC6_1",
            "pushImgMC6_2": "labelImgMC6_2", "pushImgMC6_3": "labelImgMC6_3",
            "pushImgMC6_4": "labelImgMC6_4", "pushImgMC6_5": "labelImgMC6_5",
            "pushImgMC7_1": "labelImgMC7_1", "pushImgMC7_2": "labelImgMC7_2",
            "pushImgMC7_3": "labelImgMC7_3", "pushImgMC7_4": "labelImgMC7_4",
            "pushImgMC7_5": "labelImgMC7_5", "pushImgMC8_1": "labelImgMC8_1",
            "pushImgMC8_2": "labelImgMC8_2", "pushImgMC8_3": "labelImgMC8_3",
            "pushImgMC8_4": "labelImgMC8_4", "pushImgMC8_5": "labelImgMC8_5",
            "pushImgMCe_1": "labelImgMCe_1", "pushImgMCe_2": "labelImgMCe_2",
            "pushImgMCe_3": "labelImgMCe_3", "pushImgMCe_4": "labelImgMCe_4",
            "pushImgMCe_5": "labelImgMCe_5", "pushImgMCe_11": "labelImgMCe_6",
            "pushImgMCe_12": "labelImgMCe_7", "pushImgMCe_13": "labelImgMCe_8",
            "pushImgMCe_14": "labelImgMCe_9", "pushImgMCe_15": "labelImgMCe_10",
        }

        self.button_remove_MC1 = {
            "pushImgMC1_6": "labelImgMC1_1", "pushImgMC1_7": "labelImgMC1_2",
            "pushImgMC1_8": "labelImgMC1_3", "pushImgMC1_9": "labelImgMC1_4",
            "pushImgMC1_10": "labelImgMC1_5", "pushImgMC2_6": "labelImgMC2_1",
            "pushImgMC2_7": "labelImgMC2_2", "pushImgMC2_8": "labelImgMC2_3",
            "pushImgMC2_9": "labelImgMC2_4", "pushImgMC2_10": "labelImgMC2_5",
            "pushImgMC3_6": "labelImgMC3_1", "pushImgMC3_7": "labelImgMC3_2",
            "pushImgMC3_8": "labelImgMC3_3", "pushImgMC3_9": "labelImgMC3_4",
            "pushImgMC3_10": "labelImgMC3_5", "pushImgMC4_6": "labelImgMC4_1",
            "pushImgMC4_7": "labelImgMC4_2", "pushImgMC4_8": "labelImgMC4_3",
            "pushImgMC4_9": "labelImgMC4_4", "pushImgMC4_10": "labelImgMC4_5",
            "pushImgMC5_6": "labelImgMC5_1", "pushImgMC5_7": "labelImgMC5_2",
            "pushImgMC5_8": "labelImgMC5_3", "pushImgMC5_9": "labelImgMC5_4",
            "pushImgMC5_10": "labelImgMC5_5", "pushImgMC6_6": "labelImgMC6_1",
            "pushImgMC6_7": "labelImgMC6_2", "pushImgMC6_8": "labelImgMC6_3",
            "pushImgMC6_9": "labelImgMC6_4", "pushImgMC6_10": "labelImgMC6_5",
            "pushImgMC7_6": "labelImgMC7_1", "pushImgMC7_7": "labelImgMC7_2",
            "pushImgMC7_8": "labelImgMC7_3", "pushImgMC7_9": "labelImgMC7_4",
            "pushImgMC7_10": "labelImgMC7_5", "pushImgMC8_6": "labelImgMC8_1",
            "pushImgMC8_7": "labelImgMC8_2", "pushImgMC8_8": "labelImgMC8_3",
            "pushImgMC8_9": "labelImgMC8_4", "pushImgMC8_10": "labelImgMC8_5",
            "pushImgMCe_6": "labelImgMCe_1", "pushImgMCe_7": "labelImgMCe_2",
            "pushImgMCe_8": "labelImgMCe_3", "pushImgMCe_9": "labelImgMCe_4",
            "pushImgMCe_10": "labelImgMCe_5", "pushImgMCe_16": "labelImgMCe_6",
            "pushImgMCe_17": "labelImgMCe_7", "pushImgMCe_18": "labelImgMCe_8",
            "pushImgMCe_19": "labelImgMCe_9", "pushImgMCe_20": "labelImgMCe_10",
        }

        self.images_list_MC1 = [
            ["labelImgMC1_1", "labelImgMC1_2", "labelImgMC1_3", "labelImgMC1_4", "labelImgMC1_5"],
            ["labelImgMC2_1", "labelImgMC2_2", "labelImgMC2_3", "labelImgMC2_4", "labelImgMC2_5"],
            ["labelImgMC3_1", "labelImgMC3_2", "labelImgMC3_3", "labelImgMC3_4", "labelImgMC3_5"],
            ["labelImgMC4_1", "labelImgMC4_2", "labelImgMC4_3", "labelImgMC4_4", "labelImgMC4_5"],
            ["labelImgMC5_1", "labelImgMC5_2", "labelImgMC5_3", "labelImgMC5_4", "labelImgMC5_5"],
            ["labelImgMC6_1", "labelImgMC6_2", "labelImgMC6_3", "labelImgMC6_4", "labelImgMC6_5"],
            ["labelImgMC7_1", "labelImgMC7_2", "labelImgMC7_3", "labelImgMC7_4", "labelImgMC7_5"],
            ["labelImgMC8_1", "labelImgMC8_2", "labelImgMC8_3", "labelImgMC8_4", "labelImgMC8_5"],
            ["labelImgMCe_1", "labelImgMCe_2", "labelImgMCe_3", "labelImgMCe_4", "labelImgMCe_5"],
            ["labelImgMCe_6", "labelImgMCe_7", "labelImgMCe_8", "labelImgMCe_9", "labelImgMCe_10"]
        ]

        #List for MC2
        self.button_map_MC2 = {
            "pushImgMMC1_1": "labelImgMMC1_1", "pushImgMMC1_2": "labelImgMMC1_2",
            "pushImgMMC1_3": "labelImgMMC1_3", "pushImgMMC1_4": "labelImgMMC1_4",
            "pushImgMMC1_5": "labelImgMMC1_5", "pushImgMMC2_1": "labelImgMMC2_1",
            "pushImgMMC2_2": "labelImgMMC2_2", "pushImgMMC2_3": "labelImgMMC2_3",
            "pushImgMMC2_4": "labelImgMMC2_4", "pushImgMMC2_5": "labelImgMMC2_5",
            "pushImgMMC3_1": "labelImgMMC3_1", "pushImgMMC3_2": "labelImgMMC3_2",
            "pushImgMMC3_3": "labelImgMMC3_3", "pushImgMMC3_4": "labelImgMMC3_4",
            "pushImgMMC3_5": "labelImgMMC3_5", "pushImgMMC4_1": "labelImgMMC4_1",
            "pushImgMMC4_2": "labelImgMMC4_2", "pushImgMMC4_3": "labelImgMMC4_3",
            "pushImgMMC4_4": "labelImgMMC4_4", "pushImgMMC4_5": "labelImgMMC4_5",
            "pushImgMMC5_1": "labelImgMMC5_1", "pushImgMMC5_2": "labelImgMMC5_2",
            "pushImgMMC5_3": "labelImgMMC5_3", "pushImgMMC5_4": "labelImgMMC5_4",
            "pushImgMMC5_5": "labelImgMMC5_5", "pushImgMMC6_1": "labelImgMMC6_1",
            "pushImgMMC6_2": "labelImgMMC6_2", "pushImgMMC6_3": "labelImgMMC6_3",
            "pushImgMMC6_4": "labelImgMMC6_4", "pushImgMMC6_5": "labelImgMMC6_5",
            "pushImgMMC7_1": "labelImgMMC7_1", "pushImgMMC7_2": "labelImgMMC7_2",
            "pushImgMMC7_3": "labelImgMMC7_3", "pushImgMMC7_4": "labelImgMMC7_4",
            "pushImgMMC7_5": "labelImgMMC7_5", "pushImgMMC8_1": "labelImgMMC8_1",
            "pushImgMMC8_2": "labelImgMMC8_2", "pushImgMMC8_3": "labelImgMMC8_3",
            "pushImgMMC8_4": "labelImgMMC8_4", "pushImgMMC8_5": "labelImgMMC8_5",
            "pushImgMMCe_1": "labelImgMMCe_1", "pushImgMMCe_2": "labelImgMMCe_2",
            "pushImgMMCe_3": "labelImgMMCe_3", "pushImgMMCe_4": "labelImgMMCe_4",
            "pushImgMMCe_5": "labelImgMMCe_5", "pushImgMMCe_11": "labelImgMMCe_6",
            "pushImgMMCe_12": "labelImgMMCe_7", "pushImgMMCe_13": "labelImgMMCe_8",
            "pushImgMMCe_14": "labelImgMMCe_9", "pushImgMMCe_15": "labelImgMMCe_10",
        }

        self.button_remove_MC2 = {
            "pushImgMMC1_6": "labelImgMMC1_1", "pushImgMMC1_7": "labelImgMMC1_2",
            "pushImgMMC1_8": "labelImgMMC1_3", "pushImgMMC1_9": "labelImgMMC1_4",
            "pushImgMMC1_10": "labelImgMMC1_5", "pushImgMMC2_6": "labelImgMMC2_1",
            "pushImgMMC2_7": "labelImgMMC2_2", "pushImgMMC2_8": "labelImgMMC2_3",
            "pushImgMMC2_9": "labelImgMMC2_4", "pushImgMMC2_10": "labelImgMMC2_5",
            "pushImgMMC3_6": "labelImgMMC3_1", "pushImgMMC3_7": "labelImgMMC3_2",
            "pushImgMMC3_8": "labelImgMMC3_3", "pushImgMMC3_9": "labelImgMMC3_4",
            "pushImgMMC3_10": "labelImgMMC3_5", "pushImgMMC4_6": "labelImgMMC4_1",
            "pushImgMMC4_7": "labelImgMMC4_2", "pushImgMMC4_8": "labelImgMMC4_3",
            "pushImgMMC4_9": "labelImgMMC4_4", "pushImgMMC4_10": "labelImgMMC4_5",
            "pushImgMMC5_6": "labelImgMMC5_1", "pushImgMMC5_7": "labelImgMMC5_2",
            "pushImgMMC5_8": "labelImgMMC5_3", "pushImgMMC5_9": "labelImgMMC5_4",
            "pushImgMMC5_10": "labelImgMMC5_5", "pushImgMMC6_6": "labelImgMMC6_1",
            "pushImgMMC6_7": "labelImgMMC6_2", "pushImgMMC6_8": "labelImgMMC6_3",
            "pushImgMMC6_9": "labelImgMMC6_4", "pushImgMMC6_10": "labelImgMMC6_5",
            "pushImgMMC7_6": "labelImgMMC7_1", "pushImgMMC7_7": "labelImgMMC7_2",
            "pushImgMMC7_8": "labelImgMMC7_3", "pushImgMMC7_9": "labelImgMMC7_4",
            "pushImgMMC7_10": "labelImgMMC7_5", "pushImgMMC8_6": "labelImgMMC8_1",
            "pushImgMMC8_7": "labelImgMMC8_2", "pushImgMMC8_8": "labelImgMMC8_3",
            "pushImgMMC8_9": "labelImgMMC8_4", "pushImgMMC8_10": "labelImgMMC8_5",
            "pushImgMMCe_6": "labelImgMMCe_1", "pushImgMMCe_7": "labelImgMMCe_2",
            "pushImgMMCe_8": "labelImgMMCe_3", "pushImgMMCe_9": "labelImgMMCe_4",
            "pushImgMMCe_10": "labelImgMMCe_5", "pushImgMMCe_16": "labelImgMMCe_6",
            "pushImgMMCe_17": "labelImgMMCe_7", "pushImgMMCe_18": "labelImgMMCe_8",
            "pushImgMMCe_19": "labelImgMMCe_9", "pushImgMMCe_20": "labelImgMMCe_10",
        }

        self.images_list_MC2 = [
            ["labelImgMMC1_1", "labelImgMMC1_2", "labelImgMMC1_3", "labelImgMMC1_4", "labelImgMMC1_5"],
            ["labelImgMMC2_1", "labelImgMMC2_2", "labelImgMMC2_3", "labelImgMMC2_4", "labelImgMMC2_5"],
            ["labelImgMMC3_1", "labelImgMMC3_2", "labelImgMMC3_3", "labelImgMMC3_4", "labelImgMMC3_5"],
            ["labelImgMMC4_1", "labelImgMMC4_2", "labelImgMMC4_3", "labelImgMMC4_4", "labelImgMMC4_5"],
            ["labelImgMMC5_1", "labelImgMMC5_2", "labelImgMMC5_3", "labelImgMMC5_4", "labelImgMMC5_5"],
            ["labelImgMMC6_1", "labelImgMMC6_2", "labelImgMMC6_3", "labelImgMMC6_4", "labelImgMMC6_5"],
            ["labelImgMMC7_1", "labelImgMMC7_2", "labelImgMMC7_3", "labelImgMMC7_4", "labelImgMMC7_5"],
            ["labelImgMMC8_1", "labelImgMMC8_2", "labelImgMMC8_3", "labelImgMMC8_4", "labelImgMMC8_5"],
            ["labelImgMMCe_1", "labelImgMMCe_2", "labelImgMMCe_3", "labelImgMMCe_4", "labelImgMMCe_5"],
            ["labelImgMMCe_6", "labelImgMMCe_7", "labelImgMMCe_8", "labelImgMMCe_9", "labelImgMMCe_10"],
        ]

        # List for MM1
        self.button_map_MM1 = {
            "pushImgM1_1": "labelImgM1_1", "pushImgM1_2": "labelImgM1_2",
            "pushImgM1_3": "labelImgM1_3", "pushImgM1_4": "labelImgM1_4",
            "pushImgM1_5": "labelImgM1_5", "pushImgM2_1": "labelImgM2_1",
            "pushImgM2_2": "labelImgM2_2", "pushImgM2_3": "labelImgM2_3",
            "pushImgM2_4": "labelImgM2_4", "pushImgM2_5": "labelImgM2_5",
            "pushImgM3_1": "labelImgM3_1", "pushImgM3_2": "labelImgM3_2",
            "pushImgM3_3": "labelImgM3_3", "pushImgM3_4": "labelImgM3_4",
            "pushImgM3_5": "labelImgM3_5", "pushImgM4_1": "labelImgM4_1",
            "pushImgM4_2": "labelImgM4_2", "pushImgM4_3": "labelImgM4_3",
            "pushImgM4_4": "labelImgM4_4", "pushImgM4_5": "labelImgM4_5",
            "pushImgM5_1": "labelImgM5_1", "pushImgM5_2": "labelImgM5_2",
            "pushImgM5_3": "labelImgM5_3", "pushImgM5_4": "labelImgM5_4",
            "pushImgM5_5": "labelImgM5_5", "pushImgM6_1": "labelImgM6_1",
            "pushImgM6_2": "labelImgM6_2", "pushImgM6_3": "labelImgM6_3",
            "pushImgM6_4": "labelImgM6_4", "pushImgM6_5": "labelImgM6_5"
        }

        self.button_remove_MM1 = {
            "pushImgM1_6": "labelImgM1_1", "pushImgM1_7": "labelImgM1_2",
            "pushImgM1_8": "labelImgM1_3", "pushImgM1_9": "labelImgM1_4",
            "pushImgM1_10": "labelImgM1_5", "pushImgM2_6": "labelImgM2_1",
            "pushImgM2_7": "labelImgM2_2", "pushImgM2_8": "labelImgM2_3",
            "pushImgM2_9": "labelImgM2_4", "pushImgM2_10": "labelImgM2_5",
            "pushImgM3_6": "labelImgM3_1", "pushImgM3_7": "labelImgM3_2",
            "pushImgM3_8": "labelImgM3_3", "pushImgM3_9": "labelImgM3_4",
            "pushImgM3_10": "labelImgM3_5", "pushImgM4_6": "labelImgM4_1",
            "pushImgM4_7": "labelImgM4_2", "pushImgM4_8": "labelImgM4_3",
            "pushImgM4_9": "labelImgM4_4", "pushImgM4_10": "labelImgM4_5",
            "pushImgM5_6": "labelImgM5_1", "pushImgM5_7": "labelImgM5_2",
            "pushImgM5_8": "labelImgM5_3", "pushImgM5_9": "labelImgM5_4",
            "pushImgM5_10": "labelImgM5_5", "pushImgM6_6": "labelImgM6_1",
            "pushImgM6_7": "labelImgM6_2", "pushImgM6_8": "labelImgM6_3",
            "pushImgM6_9": "labelImgM6_4", "pushImgM6_10": "labelImgM6_5"
        }

        self.images_list_MM1 = [
            ["labelImgM1_1", "labelImgM1_2", "labelImgM1_3", "labelImgM1_4", "labelImgM1_5"],
            ["labelImgM2_1", "labelImgM2_2", "labelImgM2_3", "labelImgM2_4", "labelImgM2_5"],
            ["labelImgM3_1", "labelImgM3_2", "labelImgM3_3", "labelImgM3_4", "labelImgM3_5"],
            ["labelImgM4_1", "labelImgM4_2", "labelImgM4_3", "labelImgM4_4", "labelImgM4_5"],
            ["labelImgM5_1", "labelImgM5_2", "labelImgM5_3", "labelImgM5_4", "labelImgM5_5"],
            ["labelImgM6_1", "labelImgM6_2", "labelImgM6_3", "labelImgM6_4", "labelImgM6_5"]
        ]

        self.grid_names_MM1 = [self.ui.gridLayout_32, self.ui.gridLayout_31, self.ui.gridLayoutM_1, self.ui.gridLayoutM_2,
                         self.ui.gridLayoutM_3, self.ui.gridLayoutM_4, self.ui.gridLayoutM_5, self.ui.gridLayoutM_6]

        # List for MM2
        self.button_map_MM2 = {
            "pushImgMM1_1": "labelImgMM1_1", "pushImgMM1_2": "labelImgMM1_2",
            "pushImgMM1_3": "labelImgMM1_3", "pushImgMM1_4": "labelImgMM1_4",
            "pushImgMM1_5": "labelImgMM1_5", "pushImgMM2_1": "labelImgMM2_1",
            "pushImgMM2_2": "labelImgMM2_2", "pushImgMM2_3": "labelImgMM2_3",
            "pushImgMM2_4": "labelImgMM2_4", "pushImgMM2_5": "labelImgMM2_5",
            "pushImgMM3_1": "labelImgMM3_1", "pushImgMM3_2": "labelImgMM3_2",
            "pushImgMM3_3": "labelImgMM3_3", "pushImgMM3_4": "labelImgMM3_4",
            "pushImgMM3_5": "labelImgMM3_5", "pushImgMM4_1": "labelImgMM4_1",
            "pushImgMM4_2": "labelImgMM4_2", "pushImgMM4_3": "labelImgMM4_3",
            "pushImgMM4_4": "labelImgMM4_4", "pushImgMM4_5": "labelImgMM4_5",
            "pushImgMM5_1": "labelImgMM5_1", "pushImgMM5_2": "labelImgMM5_2",
            "pushImgMM5_3": "labelImgMM5_3", "pushImgMM5_4": "labelImgMM5_4",
            "pushImgMM5_5": "labelImgMM5_5", "pushImgMM6_1": "labelImgMM6_1",
            "pushImgMM6_2": "labelImgMM6_2", "pushImgMM6_3": "labelImgMM6_3",
            "pushImgMM6_4": "labelImgMM6_4", "pushImgMM6_5": "labelImgMM6_5"
        }

        self.button_remove_MM2 = {
            "pushImgMM1_6": "labelImgMM1_1", "pushImgMM1_7": "labelImgMM1_2",
            "pushImgMM1_8": "labelImgMM1_3", "pushImgMM1_9": "labelImgMM1_4",
            "pushImgMM1_10": "labelImgMM1_5", "pushImgMM2_6": "labelImgMM2_1",
            "pushImgMM2_7": "labelImgMM2_2", "pushImgMM2_8": "labelImgMM2_3",
            "pushImgMM2_9": "labelImgMM2_4", "pushImgMM2_10": "labelImgMM2_5",
            "pushImgMM3_6": "labelImgMM3_1", "pushImgMM3_7": "labelImgMM3_2",
            "pushImgMM3_8": "labelImgMM3_3", "pushImgMM3_9": "labelImgMM3_4",
            "pushImgMM3_10": "labelImgMM3_5", "pushImgMM4_6": "labelImgMM4_1",
            "pushImgMM4_7": "labelImgMM4_2", "pushImgMM4_8": "labelImgMM4_3",
            "pushImgMM4_9": "labelImgMM4_4", "pushImgMM4_10": "labelImgMM4_5",
            "pushImgMM5_6": "labelImgMM5_1", "pushImgMM5_7": "labelImgMM5_2",
            "pushImgMM5_8": "labelImgMM5_3", "pushImgMM5_9": "labelImgMM5_4",
            "pushImgMM5_10": "labelImgMM5_5", "pushImgMM6_6": "labelImgMM6_1",
            "pushImgMM6_7": "labelImgMM6_2", "pushImgMM6_8": "labelImgMM6_3",
            "pushImgMM6_9": "labelImgMM6_4", "pushImgMM6_10": "labelImgMM6_5"
        }

        self.images_list_MM2 = [
            ["labelImgMM1_1", "labelImgMM1_2", "labelImgMM1_3", "labelImgMM1_4", "labelImgMM1_5"],
            ["labelImgMM2_1", "labelImgMM2_2", "labelImgMM2_3", "labelImgMM2_4", "labelImgMM2_5"],
            ["labelImgMM3_1", "labelImgMM3_2", "labelImgMM3_3", "labelImgMM3_4", "labelImgMM3_5"],
            ["labelImgMM4_1", "labelImgMM4_2", "labelImgMM4_3", "labelImgMM4_4", "labelImgMM4_5"],
            ["labelImgMM5_1", "labelImgMM5_2", "labelImgMM5_3", "labelImgMM5_4", "labelImgMM5_5"],
            ["labelImgMM6_1", "labelImgMM6_2", "labelImgMM6_3", "labelImgMM6_4", "labelImgMM6_5"]
        ]

        self.grid_names_MM2 = [self.ui.gridLayoutMM_1, self.ui.gridLayoutMM_2, self.ui.gridLayoutMM_3, self.ui.gridLayoutMM_4,
                         self.ui.gridLayoutMM_5, self.ui.gridLayoutMM_6, self.ui.gridLayoutMM_7, self.ui.gridLayoutMM_8]

        # List for L
        self.button_map_L = {
            "pushImgL1_1": "labelImgL1_1", "pushImgL1_2": "labelImgL1_2",
            "pushImgL1_3": "labelImgL1_3", "pushImgL1_4": "labelImgL1_4",
            "pushImgL1_5": "labelImgL1_5", "pushImgL2_1": "labelImgL2_1",
            "pushImgL2_2": "labelImgL2_2", "pushImgL2_3": "labelImgL2_3",
            "pushImgL2_4": "labelImgL2_4", "pushImgL2_5": "labelImgL2_5",
            "pushImgL3_1": "labelImgL3_1", "pushImgL3_2": "labelImgL3_2",
            "pushImgL3_3": "labelImgL3_3", "pushImgL3_4": "labelImgL3_4",
            "pushImgL3_5": "labelImgL3_5", "pushImgL4_1": "labelImgL4_1",
            "pushImgL4_2": "labelImgL4_2", "pushImgL4_3": "labelImgL4_3",
            "pushImgL4_4": "labelImgL4_4", "pushImgL4_5": "labelImgL4_5",
            "pushImgL5_1": "labelImgL5_1", "pushImgL5_2": "labelImgL5_2",
            "pushImgL5_3": "labelImgL5_3", "pushImgL5_4": "labelImgL5_4",
            "pushImgL5_5": "labelImgL5_5", "pushImgL6_1": "labelImgL6_1",
            "pushImgL6_2": "labelImgL6_2", "pushImgL6_3": "labelImgL6_3",
            "pushImgL6_4": "labelImgL6_4", "pushImgL6_5": "labelImgL6_5"
        }

        self.button_remove_L = {
            "pushImgL1_6": "labelImgL1_1", "pushImgL1_7": "labelImgL1_2",
            "pushImgL1_8": "labelImgL1_3", "pushImgL1_9": "labelImgL1_4",
            "pushImgL1_10": "labelImgL1_5", "pushImgL2_6": "labelImgL2_1",
            "pushImgL2_7": "labelImgL2_2", "pushImgL2_8": "labelImgL2_3",
            "pushImgL2_9": "labelImgL2_4", "pushImgL2_10": "labelImgL2_5",
            "pushImgL3_6": "labelImgL3_1", "pushImgL3_7": "labelImgL3_2",
            "pushImgL3_8": "labelImgL3_3", "pushImgL3_9": "labelImgL3_4",
            "pushImgL3_10": "labelImgL3_5", "pushImgL4_6": "labelImgL4_1",
            "pushImgL4_7": "labelImgL4_2", "pushImgL4_8": "labelImgL4_3",
            "pushImgL4_9": "labelImgL4_4", "pushImgL4_10": "labelImgL4_5",
            "pushImgL5_6": "labelImgL5_1", "pushImgL5_7": "labelImgL5_2",
            "pushImgL5_8": "labelImgL5_3", "pushImgL5_9": "labelImgL5_4",
            "pushImgL5_10": "labelImgL5_5", "pushImgL6_6": "labelImgL6_1",
            "pushImgL6_7": "labelImgL6_2", "pushImgL6_8": "labelImgL6_3",
            "pushImgL6_9": "labelImgL6_4", "pushImgL6_10": "labelImgL6_5"
        }

        self.images_list_L = [
            ["labelImgL1_1", "labelImgL1_2", "labelImgL1_3", "labelImgL1_4", "labelImgL1_5"],
            ["labelImgL2_1", "labelImgL2_2", "labelImgL2_3", "labelImgL2_4", "labelImgL2_5"],
            ["labelImgL3_1", "labelImgL3_2", "labelImgL3_3", "labelImgL3_4", "labelImgL3_5"],
            ["labelImgL4_1", "labelImgL4_2", "labelImgL4_3", "labelImgL4_4", "labelImgL4_5"],
            ["labelImgL5_1", "labelImgL5_2", "labelImgL5_3", "labelImgL5_4", "labelImgL5_5"],
            ["labelImgL6_1", "labelImgL6_2", "labelImgL6_3", "labelImgL6_4", "labelImgL6_5"]
        ]

        self.grid_names_L = [self.ui.gridLayoutL_1, self.ui.gridLayoutL_2, self.ui.gridLayoutL_3, self.ui.gridLayoutL_4,
                         self.ui.gridLayoutL_5, self.ui.gridLayoutL_6, self.ui.gridLayoutL_7, self.ui.gridLayoutL_8]


        #List for LC
        self.button_map_LC = {
            "pushImgLC1_1": "labelImgLC1_1", "pushImgLC1_2": "labelImgLC1_2",
            "pushImgLC1_3": "labelImgLC1_3", "pushImgLC1_4": "labelImgLC1_4",
            "pushImgLC1_5": "labelImgLC1_5", "pushImgLC2_1": "labelImgLC2_1",
            "pushImgLC2_2": "labelImgLC2_2", "pushImgLC2_3": "labelImgLC2_3",
            "pushImgLC2_4": "labelImgLC2_4", "pushImgLC2_5": "labelImgLC2_5",
            "pushImgLC3_1": "labelImgLC3_1", "pushImgLC3_2": "labelImgLC3_2",
            "pushImgLC3_3": "labelImgLC3_3", "pushImgLC3_4": "labelImgLC3_4",
            "pushImgLC3_5": "labelImgLC3_5", "pushImgLC4_1": "labelImgLC4_1",
            "pushImgLC4_2": "labelImgLC4_2", "pushImgLC4_3": "labelImgLC4_3",
            "pushImgLC4_4": "labelImgLC4_4", "pushImgLC4_5": "labelImgLC4_5",
            "pushImgLC5_1": "labelImgLC5_1", "pushImgLC5_2": "labelImgLC5_2",
            "pushImgLC5_3": "labelImgLC5_3", "pushImgLC5_4": "labelImgLC5_4",
            "pushImgLC5_5": "labelImgLC5_5", "pushImgLC6_1": "labelImgLC6_1",
            "pushImgLC6_2": "labelImgLC6_2", "pushImgLC6_3": "labelImgLC6_3",
            "pushImgLC6_4": "labelImgLC6_4", "pushImgLC6_5": "labelImgLC6_5",
            "pushImgLC7_1": "labelImgLC7_1", "pushImgLC7_2": "labelImgLC7_2",
            "pushImgLC7_3": "labelImgLC7_3", "pushImgLC7_4": "labelImgLC7_4",
            "pushImgLC7_5": "labelImgLC7_5", "pushImgLC8_1": "labelImgLC8_1",
            "pushImgLC8_2": "labelImgLC8_2", "pushImgLC8_3": "labelImgLC8_3",
            "pushImgLC8_4": "labelImgLC8_4", "pushImgLC8_5": "labelImgLC8_5",
            "pushImgLCe_1": "labelImgLCe_1", "pushImgLCe_2": "labelImgLCe_2",
            "pushImgLCe_3": "labelImgLCe_3", "pushImgLCe_4": "labelImgLCe_4",
            "pushImgLCe_5": "labelImgLCe_5", "pushImgLCe_11": "labelImgLCe_6",
            "pushImgLCe_12": "labelImgLCe_7", "pushImgLCe_13": "labelImgLCe_8",
            "pushImgLCe_14": "labelImgLCe_9", "pushImgLCe_15": "labelImgLCe_10",
        }

        self.button_remove_LC = {
            "pushImgLC1_6": "labelImgLC1_1", "pushImgLC1_7": "labelImgLC1_2",
            "pushImgLC1_8": "labelImgLC1_3", "pushImgLC1_9": "labelImgLC1_4",
            "pushImgLC1_10": "labelImgLC1_5", "pushImgLC2_6": "labelImgLC2_1",
            "pushImgLC2_7": "labelImgLC2_2", "pushImgLC2_8": "labelImgLC2_3",
            "pushImgLC2_9": "labelImgLC2_4", "pushImgLC2_10": "labelImgLC2_5",
            "pushImgLC3_6": "labelImgLC3_1", "pushImgLC3_7": "labelImgLC3_2",
            "pushImgLC3_8": "labelImgLC3_3", "pushImgLC3_9": "labelImgLC3_4",
            "pushImgLC3_10": "labelImgLC3_5", "pushImgLC4_6": "labelImgLC4_1",
            "pushImgLC4_7": "labelImgLC4_2", "pushImgLC4_8": "labelImgLC4_3",
            "pushImgLC4_9": "labelImgLC4_4", "pushImgLC4_10": "labelImgLC4_5",
            "pushImgLC5_6": "labelImgLC5_1", "pushImgLC5_7": "labelImgLC5_2",
            "pushImgLC5_8": "labelImgLC5_3", "pushImgLC5_9": "labelImgLC5_4",
            "pushImgLC5_10": "labelImgLC5_5", "pushImgLC6_6": "labelImgLC6_1",
            "pushImgLC6_7": "labelImgLC6_2", "pushImgLC6_8": "labelImgLC6_3",
            "pushImgLC6_9": "labelImgLC6_4", "pushImgLC6_10": "labelImgLC6_5",
            "pushImgLC7_6": "labelImgLC7_1", "pushImgLC7_7": "labelImgLC7_2",
            "pushImgLC7_8": "labelImgLC7_3", "pushImgLC7_9": "labelImgLC7_4",
            "pushImgLC7_10": "labelImgLC7_5", "pushImgLC8_6": "labelImgLC8_1",
            "pushImgLC8_7": "labelImgLC8_2", "pushImgLC8_8": "labelImgLC8_3",
            "pushImgLC8_9": "labelImgLC8_4", "pushImgLC8_10": "labelImgLC8_5",
            "pushImgLCe_6": "labelImgLCe_1", "pushImgLCe_7": "labelImgLCe_2",
            "pushImgLCe_8": "labelImgLCe_3", "pushImgLCe_9": "labelImgLCe_4",
            "pushImgLCe_10": "labelImgLCe_5", "pushImgLCe_16": "labelImgLCe_6",
            "pushImgLCe_17": "labelImgLCe_7", "pushImgLCe_18": "labelImgLCe_8",
            "pushImgLCe_19": "labelImgLCe_9", "pushImgLCe_20": "labelImgLCe_10",
        }

        self.images_list_LC = [
            ["labelImgLC1_1", "labelImgLC1_2", "labelImgLC1_3", "labelImgLC1_4", "labelImgLC1_5"],
            ["labelImgLC2_1", "labelImgLC2_2", "labelImgLC2_3", "labelImgLC2_4", "labelImgLC2_5"],
            ["labelImgLC3_1", "labelImgLC3_2", "labelImgLC3_3", "labelImgLC3_4", "labelImgLC3_5"],
            ["labelImgLC4_1", "labelImgLC4_2", "labelImgLC4_3", "labelImgLC4_4", "labelImgLC4_5"],
            ["labelImgLC5_1", "labelImgLC5_2", "labelImgLC5_3", "labelImgLC5_4", "labelImgLC5_5"],
            ["labelImgLC6_1", "labelImgLC6_2", "labelImgLC6_3", "labelImgLC6_4", "labelImgLC6_5"],
            ["labelImgLC7_1", "labelImgLC7_2", "labelImgLC7_3", "labelImgLC7_4", "labelImgLC7_5"],
            ["labelImgLC8_1", "labelImgLC8_2", "labelImgLC8_3", "labelImgLC8_4", "labelImgLC8_5"],
            ["labelImgLCe_1", "labelImgLCe_2", "labelImgLCe_3", "labelImgLCe_4", "labelImgLCe_5"],
            ["labelImgLCe_6", "labelImgLCe_7", "labelImgLCe_8", "labelImgLCe_9", "labelImgLCe_10"],
        ]

        # Lists for S
        self.button_map_SN = {
            "pushImgSN1_1": "labelImgSN1_1", "pushImgSN1_2": "labelImgSN1_2",
            "pushImgSN1_3": "labelImgSN1_3", "pushImgSN1_4": "labelImgSN1_4",
            "pushImgSN1_5": "labelImgSN1_5", "pushImgSN2_1": "labelImgSN2_1",
            "pushImgSN2_2": "labelImgSN2_2", "pushImgSN2_3": "labelImgSN2_3",
            "pushImgSN2_4": "labelImgSN2_4", "pushImgSN2_5": "labelImgSN2_5",
            "pushImgSN3_1": "labelImgSN3_1", "pushImgSN3_2": "labelImgSN3_2",
            "pushImgSN3_3": "labelImgSN3_3", "pushImgSN3_4": "labelImgSN3_4",
            "pushImgSN3_5": "labelImgSN3_5", "pushImgSN4_1": "labelImgSN4_1",
            "pushImgSN4_2": "labelImgSN4_2", "pushImgSN4_3": "labelImgSN4_3",
            "pushImgSN4_4": "labelImgSN4_4", "pushImgSN4_5": "labelImgSN4_5",
            "pushImgSN5_1": "labelImgSN5_1", "pushImgSN5_2": "labelImgSN5_2",
            "pushImgSN5_3": "labelImgSN5_3", "pushImgSN5_4": "labelImgSN5_4",
            "pushImgSN5_5": "labelImgSN5_5", "pushImgSN6_1": "labelImgSN6_1",
            "pushImgSN6_2": "labelImgSN6_2", "pushImgSN6_3": "labelImgSN6_3",
            "pushImgSN6_4": "labelImgSN6_4", "pushImgSN6_5": "labelImgSN6_5"
        }

        self.button_remove_SN = {
            "pushImgSN1_6": "labelImgSN1_1", "pushImgSN1_7": "labelImgSN1_2",
            "pushImgSN1_8": "labelImgSN1_3", "pushImgSN1_9": "labelImgSN1_4",
            "pushImgSN1_10": "labelImgSN1_5", "pushImgSN2_6": "labelImgSN2_1",
            "pushImgSN2_7": "labelImgSN2_2", "pushImgSN2_8": "labelImgSN2_3",
            "pushImgSN2_9": "labelImgSN2_4", "pushImgSN2_10": "labelImgSN2_5",
            "pushImgSN3_6": "labelImgSN3_1", "pushImgSN3_7": "labelImgSN3_2",
            "pushImgSN3_8": "labelImgSN3_3", "pushImgSN3_9": "labelImgSN3_4",
            "pushImgSN3_10": "labelImgSN3_5", "pushImgSN4_6": "labelImgSN4_1",
            "pushImgSN4_7": "labelImgSN4_2", "pushImgSN4_8": "labelImgSN4_3",
            "pushImgSN4_9": "labelImgSN4_4", "pushImgSN4_10": "labelImgSN4_5",
            "pushImgSN5_6": "labelImgSN5_1", "pushImgSN5_7": "labelImgSN5_2",
            "pushImgSN5_8": "labelImgSN5_3", "pushImgSN5_9": "labelImgSN5_4",
            "pushImgSN5_10": "labelImgSN5_5", "pushImgSN6_6": "labelImgSN6_1",
            "pushImgSN6_7": "labelImgSN6_2", "pushImgSN6_8": "labelImgSN6_3",
            "pushImgSN6_9": "labelImgSN6_4", "pushImgSN6_10": "labelImgSN6_5"
        }

        self.images_list_SN = [
            ["labelImgSN1_1", "labelImgSN1_2", "labelImgSN1_3", "labelImgSN1_4", "labelImgSN1_5"],
            ["labelImgSN2_1", "labelImgSN2_2", "labelImgSN2_3", "labelImgSN2_4", "labelImgSN2_5"],
            ["labelImgSN3_1", "labelImgSN3_2", "labelImgSN3_3", "labelImgSN3_4", "labelImgSN3_5"],
            ["labelImgSN4_1", "labelImgSN4_2", "labelImgSN4_3", "labelImgSN4_4", "labelImgSN4_5"],
            ["labelImgSN5_1", "labelImgSN5_2", "labelImgSN5_3", "labelImgSN5_4", "labelImgSN5_5"],
            ["labelImgSN6_1", "labelImgSN6_2", "labelImgSN6_3", "labelImgSN6_4", "labelImgSN6_5"]
        ]

        self.grid_names_SN = [self.ui.gridLayoutSN_1, self.ui.gridLayoutSN_2, self.ui.gridLayoutSN_3, self.ui.gridLayoutSN_4,
                         self.ui.gridLayoutSN_5, self.ui.gridLayoutSN_6, self.ui.gridLayoutSN_7, self.ui.gridLayoutSN_8]

        # Lists for SC
        self.button_map_SC = {
            "pushImgSC1_1": "labelImgSC1_1", "pushImgSC1_2": "labelImgSC1_2",
            "pushImgSC1_3": "labelImgSC1_3", "pushImgSC1_4": "labelImgSC1_4",
            "pushImgSC1_5": "labelImgSC1_5", "pushImgSC2_1": "labelImgSC2_1",
            "pushImgSC2_2": "labelImgSC2_2", "pushImgSC2_3": "labelImgSC2_3",
            "pushImgSC2_4": "labelImgSC2_4", "pushImgSC2_5": "labelImgSC2_5",
            "pushImgSC3_1": "labelImgSC3_1", "pushImgSC3_2": "labelImgSC3_2",
            "pushImgSC3_3": "labelImgSC3_3", "pushImgSC3_4": "labelImgSC3_4",
            "pushImgSC3_5": "labelImgSC3_5", "pushImgSC4_1": "labelImgSC4_1",
            "pushImgSC4_2": "labelImgSC4_2", "pushImgSC4_3": "labelImgSC4_3",
            "pushImgSC4_4": "labelImgSC4_4", "pushImgSC4_5": "labelImgSC4_5",
            "pushImgSC5_1": "labelImgSC5_1", "pushImgSC5_2": "labelImgSC5_2",
            "pushImgSC5_3": "labelImgSC5_3", "pushImgSC5_4": "labelImgSC5_4",
            "pushImgSC5_5": "labelImgSC5_5", "pushImgSC6_1": "labelImgSC6_1",
            "pushImgSC6_2": "labelImgSC6_2", "pushImgSC6_3": "labelImgSC6_3",
            "pushImgSC6_4": "labelImgSC6_4", "pushImgSC6_5": "labelImgSC6_5",
            "pushImgSC7_1": "labelImgSC7_1", "pushImgSC7_2": "labelImgSC7_2",
            "pushImgSC7_3": "labelImgSC7_3", "pushImgSC7_4": "labelImgSC7_4",
            "pushImgSC7_5": "labelImgSC7_5", "pushImgSC8_1": "labelImgSC8_1",
            "pushImgSC8_2": "labelImgSC8_2", "pushImgSC8_3": "labelImgSC8_3",
            "pushImgSC8_4": "labelImgSC8_4", "pushImgSC8_5": "labelImgSC8_5",
            "pushImgSCe_1": "labelImgSCe_1", "pushImgSCe_2": "labelImgSCe_2",
            "pushImgSCe_3": "labelImgSCe_3", "pushImgSCe_4": "labelImgSCe_4",
            "pushImgSCe_5": "labelImgSCe_5", "pushImgSCe_11": "labelImgSCe_6",
            "pushImgSCe_12": "labelImgSCe_7", "pushImgSCe_13": "labelImgSCe_8",
            "pushImgSCe_14": "labelImgSCe_9", "pushImgSCe_15": "labelImgSCe_10",
        }

        self.button_remove_SC = {
            "pushImgSC1_6": "labelImgSC1_1", "pushImgSC1_7": "labelImgSC1_2",
            "pushImgSC1_8": "labelImgSC1_3", "pushImgSC1_9": "labelImgSC1_4",
            "pushImgSC1_10": "labelImgSC1_5", "pushImgSC2_6": "labelImgSC2_1",
            "pushImgSC2_7": "labelImgSC2_2", "pushImgSC2_8": "labelImgSC2_3",
            "pushImgSC2_9": "labelImgSC2_4", "pushImgSC2_10": "labelImgSC2_5",
            "pushImgSC3_6": "labelImgSC3_1", "pushImgSC3_7": "labelImgSC3_2",
            "pushImgSC3_8": "labelImgSC3_3", "pushImgSC3_9": "labelImgSC3_4",
            "pushImgSC3_10": "labelImgSC3_5", "pushImgSC4_6": "labelImgSC4_1",
            "pushImgSC4_7": "labelImgSC4_2", "pushImgSC4_8": "labelImgSC4_3",
            "pushImgSC4_9": "labelImgSC4_4", "pushImgSC4_10": "labelImgSC4_5",
            "pushImgSC5_6": "labelImgSC5_1", "pushImgSC5_7": "labelImgSC5_2",
            "pushImgSC5_8": "labelImgSC5_3", "pushImgSC5_9": "labelImgSC5_4",
            "pushImgSC5_10": "labelImgSC5_5", "pushImgSC6_6": "labelImgSC6_1",
            "pushImgSC6_7": "labelImgSC6_2", "pushImgSC6_8": "labelImgSC6_3",
            "pushImgSC6_9": "labelImgSC6_4", "pushImgSC6_10": "labelImgSC6_5",
            "pushImgSC7_6": "labelImgSC7_1", "pushImgSC7_7": "labelImgSC7_2",
            "pushImgSC7_8": "labelImgSC7_3", "pushImgSC7_9": "labelImgSC7_4",
            "pushImgSC7_10": "labelImgSC7_5", "pushImgSC8_6": "labelImgSC8_1",
            "pushImgSC8_7": "labelImgSC8_2", "pushImgSC8_8": "labelImgSC8_3",
            "pushImgSC8_9": "labelImgSC8_4", "pushImgSC8_10": "labelImgSC8_5",
            "pushImgSCe_6": "labelImgSCe_1", "pushImgSCe_7": "labelImgSCe_2",
            "pushImgSCe_8": "labelImgSCe_3", "pushImgSCe_9": "labelImgSCe_4",
            "pushImgSCe_10": "labelImgSCe_5", "pushImgSCe_16": "labelImgSCe_6",
            "pushImgSCe_17": "labelImgSCe_7", "pushImgSCe_18": "labelImgSCe_8",
            "pushImgSCe_19": "labelImgSCe_9", "pushImgSCe_20": "labelImgSCe_10",
        }

        self.images_list_SC = [
            ["labelImgSC1_1", "labelImgSC1_2", "labelImgSC1_3", "labelImgSC1_4", "labelImgSC1_5"],
            ["labelImgSC2_1", "labelImgSC2_2", "labelImgSC2_3", "labelImgSC2_4", "labelImgSC2_5"],
            ["labelImgSC3_1", "labelImgSC3_2", "labelImgSC3_3", "labelImgSC3_4", "labelImgSC3_5"],
            ["labelImgSC4_1", "labelImgSC4_2", "labelImgSC4_3", "labelImgSC4_4", "labelImgSC4_5"],
            ["labelImgSC5_1", "labelImgSC5_2", "labelImgSC5_3", "labelImgSC5_4", "labelImgSC5_5"],
            ["labelImgSC6_1", "labelImgSC6_2", "labelImgSC6_3", "labelImgSC6_4", "labelImgSC6_5"],
            ["labelImgSC7_1", "labelImgSC7_2", "labelImgSC7_3", "labelImgSC7_4", "labelImgSC7_5"],
            ["labelImgSC8_1", "labelImgSC8_2", "labelImgSC8_3", "labelImgSC8_4", "labelImgSC8_5"],
            ["labelImgSCe_1", "labelImgSCe_2", "labelImgSCe_3", "labelImgSCe_4", "labelImgSCe_5"],
            ["labelImgSCe_6", "labelImgSCe_7", "labelImgSCe_8", "labelImgSCe_9", "labelImgSCe_10"],
        ]

        # Lists for Se
        self.button_map_Se = {
            "pushImgSe1_1": "labelImgSe1_1", "pushImgSe1_2": "labelImgSe1_2",
            "pushImgSe1_3": "labelImgSe1_3", "pushImgSe1_4": "labelImgSe1_4",
            "pushImgSe1_5": "labelImgSe1_5", "pushImgSe2_1": "labelImgSe2_1",
            "pushImgSe2_2": "labelImgSe2_2", "pushImgSe2_3": "labelImgSe2_3",
            "pushImgSe2_4": "labelImgSe2_4", "pushImgSe2_5": "labelImgSe2_5",
            "pushImgSe3_1": "labelImgSe3_1", "pushImgSe3_2": "labelImgSe3_2",
            "pushImgSe3_3": "labelImgSe3_3", "pushImgSe3_4": "labelImgSe3_4",
            "pushImgSe3_5": "labelImgSe3_5", "pushImgSe4_1": "labelImgSe4_1",
            "pushImgSe4_2": "labelImgSe4_2", "pushImgSe4_3": "labelImgSe4_3",
            "pushImgSe4_4": "labelImgSe4_4", "pushImgSe4_5": "labelImgSe4_5",
            "pushImgSe5_1": "labelImgSe5_1", "pushImgSe5_2": "labelImgSe5_2",
            "pushImgSe5_3": "labelImgSe5_3", "pushImgSe5_4": "labelImgSe5_4",
            "pushImgSe5_5": "labelImgSe5_5", "pushImgSe6_1": "labelImgSe6_1",
            "pushImgSe6_2": "labelImgSe6_2", "pushImgSe6_3": "labelImgSe6_3",
            "pushImgSe6_4": "labelImgSe6_4", "pushImgSe6_5": "labelImgSe6_5"
        }

        self.button_remove_Se = {
            "pushImgSe1_6": "labelImgSe1_1", "pushImgSe1_7": "labelImgSe1_2",
            "pushImgSe1_8": "labelImgSe1_3", "pushImgSe1_9": "labelImgSe1_4",
            "pushImgSe1_10": "labelImgSe1_5", "pushImgSe2_6": "labelImgSe2_1",
            "pushImgSe2_7": "labelImgSe2_2", "pushImgSe2_8": "labelImgSe2_3",
            "pushImgSe2_9": "labelImgSe2_4", "pushImgSe2_10": "labelImgSe2_5",
            "pushImgSe3_6": "labelImgSe3_1", "pushImgSe3_7": "labelImgSe3_2",
            "pushImgSe3_8": "labelImgSe3_3", "pushImgSe3_9": "labelImgSe3_4",
            "pushImgSe3_10": "labelImgSe3_5", "pushImgSe4_6": "labelImgSe4_1",
            "pushImgSe4_7": "labelImgSe4_2", "pushImgSe4_8": "labelImgSe4_3",
            "pushImgSe4_9": "labelImgSe4_4", "pushImgSe4_10": "labelImgSe4_5",
            "pushImgSe5_6": "labelImgSe5_1", "pushImgSe5_7": "labelImgSe5_2",
            "pushImgSe5_8": "labelImgSe5_3", "pushImgSe5_9": "labelImgSe5_4",
            "pushImgSe5_10": "labelImgSe5_5", "pushImgSe6_6": "labelImgSe6_1",
            "pushImgSe6_7": "labelImgSe6_2", "pushImgSe6_8": "labelImgSe6_3",
            "pushImgSe6_9": "labelImgSe6_4", "pushImgSe6_10": "labelImgSe6_5"
        }

        self.images_list_Se = [
            ["labelImgSe1_1", "labelImgSe1_2", "labelImgSe1_3", "labelImgSe1_4", "labelImgSe1_5"],
            ["labelImgSe2_1", "labelImgSe2_2", "labelImgSe2_3", "labelImgSe2_4", "labelImgSe2_5"],
            ["labelImgSe3_1", "labelImgSe3_2", "labelImgSe3_3", "labelImgSe3_4", "labelImgSe3_5"],
            ["labelImgSe4_1", "labelImgSe4_2", "labelImgSe4_3", "labelImgSe4_4", "labelImgSe4_5"],
            ["labelImgSe5_1", "labelImgSe5_2", "labelImgSe5_3", "labelImgSe5_4", "labelImgSe5_5"],
            ["labelImgSe6_1", "labelImgSe6_2", "labelImgSe6_3", "labelImgSe6_4", "labelImgSe6_5"]
        ]

        self.grid_names_Se = [self.ui.gridLayoutSe_1, self.ui.gridLayoutSe_2, self.ui.gridLayoutSe_3,
                              self.ui.gridLayoutSe_4,
                              self.ui.gridLayoutSe_5, self.ui.gridLayoutSe_6, self.ui.gridLayoutSe_7,
                              self.ui.gridLayoutSe_8]

        # Lists for Sec
        self.button_map_Sec = {
            "pushImgSec1_1": "labelImgSec1_1", "pushImgSec1_2": "labelImgSec1_2",
            "pushImgSec1_3": "labelImgSec1_3", "pushImgSec1_4": "labelImgSec1_4",
            "pushImgSec1_5": "labelImgSec1_5", "pushImgSec2_1": "labelImgSec2_1",
            "pushImgSec2_2": "labelImgSec2_2", "pushImgSec2_3": "labelImgSec2_3",
            "pushImgSec2_4": "labelImgSec2_4", "pushImgSec2_5": "labelImgSec2_5",
            "pushImgSec3_1": "labelImgSec3_1", "pushImgSec3_2": "labelImgSec3_2",
            "pushImgSec3_3": "labelImgSec3_3", "pushImgSec3_4": "labelImgSec3_4",
            "pushImgSec3_5": "labelImgSec3_5", "pushImgSec4_1": "labelImgSec4_1",
            "pushImgSec4_2": "labelImgSec4_2", "pushImgSec4_3": "labelImgSec4_3",
            "pushImgSec4_4": "labelImgSec4_4", "pushImgSec4_5": "labelImgSec4_5",
            "pushImgSec5_1": "labelImgSec5_1", "pushImgSec5_2": "labelImgSec5_2",
            "pushImgSec5_3": "labelImgSec5_3", "pushImgSec5_4": "labelImgSec5_4",
            "pushImgSec5_5": "labelImgSec5_5", "pushImgSec6_1": "labelImgSec6_1",
            "pushImgSec6_2": "labelImgSec6_2", "pushImgSec6_3": "labelImgSec6_3",
            "pushImgSec6_4": "labelImgSec6_4", "pushImgSec6_5": "labelImgSec6_5",
            "pushImgSec7_1": "labelImgSec7_1", "pushImgSec7_2": "labelImgSec7_2",
            "pushImgSec7_3": "labelImgSec7_3", "pushImgSec7_4": "labelImgSec7_4",
            "pushImgSec7_5": "labelImgSec7_5", "pushImgSec8_1": "labelImgSec8_1",
            "pushImgSec8_2": "labelImgSec8_2", "pushImgSec8_3": "labelImgSec8_3",
            "pushImgSec8_4": "labelImgSec8_4", "pushImgSec8_5": "labelImgSec8_5",
            "pushImgSece_1": "labelImgSece_1", "pushImgSece_2": "labelImgSece_2",
            "pushImgSece_3": "labelImgSece_3", "pushImgSece_4": "labelImgSece_4",
            "pushImgSece_5": "labelImgSece_5", "pushImgSece_11": "labelImgSece_6",
            "pushImgSece_12": "labelImgSece_7", "pushImgSece_13": "labelImgSece_8",
            "pushImgSece_14": "labelImgSece_9", "pushImgSece_15": "labelImgSece_10",
        }

        self.button_remove_Sec = {
            "pushImgSec1_6": "labelImgSec1_1", "pushImgSec1_7": "labelImgSec1_2",
            "pushImgSec1_8": "labelImgSec1_3", "pushImgSec1_9": "labelImgSec1_4",
            "pushImgSec1_10": "labelImgSec1_5", "pushImgSec2_6": "labelImgSec2_1",
            "pushImgSec2_7": "labelImgSec2_2", "pushImgSec2_8": "labelImgSec2_3",
            "pushImgSec2_9": "labelImgSec2_4", "pushImgSec2_10": "labelImgSec2_5",
            "pushImgSec3_6": "labelImgSec3_1", "pushImgSec3_7": "labelImgSec3_2",
            "pushImgSec3_8": "labelImgSec3_3", "pushImgSec3_9": "labelImgSec3_4",
            "pushImgSec3_10": "labelImgSec3_5", "pushImgSec4_6": "labelImgSec4_1",
            "pushImgSec4_7": "labelImgSec4_2", "pushImgSec4_8": "labelImgSec4_3",
            "pushImgSec4_9": "labelImgSec4_4", "pushImgSec4_10": "labelImgSec4_5",
            "pushImgSec5_6": "labelImgSec5_1", "pushImgSec5_7": "labelImgSec5_2",
            "pushImgSec5_8": "labelImgSec5_3", "pushImgSec5_9": "labelImgSec5_4",
            "pushImgSec5_10": "labelImgSec5_5", "pushImgSec6_6": "labelImgSec6_1",
            "pushImgSec6_7": "labelImgSec6_2", "pushImgSec6_8": "labelImgSec6_3",
            "pushImgSec6_9": "labelImgSec6_4", "pushImgSec6_10": "labelImgSec6_5",
            "pushImgSec7_6": "labelImgSec7_1", "pushImgSec7_7": "labelImgSec7_2",
            "pushImgSec7_8": "labelImgSec7_3", "pushImgSec7_9": "labelImgSec7_4",
            "pushImgSec7_10": "labelImgSec7_5", "pushImgSec8_6": "labelImgSec8_1",
            "pushImgSec8_7": "labelImgSec8_2", "pushImgSec8_8": "labelImgSec8_3",
            "pushImgSec8_9": "labelImgSec8_4", "pushImgSec8_10": "labelImgSec8_5",
            "pushImgSece_6": "labelImgSece_1", "pushImgSece_7": "labelImgSece_2",
            "pushImgSece_8": "labelImgSece_3", "pushImgSece_9": "labelImgSece_4",
            "pushImgSece_10": "labelImgSece_5", "pushImgSece_16": "labelImgSece_6",
            "pushImgSece_17": "labelImgSece_7", "pushImgSece_18": "labelImgSece_8",
            "pushImgSece_19": "labelImgSece_9", "pushImgSece_20": "labelImgSece_10",
        }

        self.images_list_Sec = [
            ["labelImgSec1_1", "labelImgSec1_2", "labelImgSec1_3", "labelImgSec1_4", "labelImgSec1_5"],
            ["labelImgSec2_1", "labelImgSec2_2", "labelImgSec2_3", "labelImgSec2_4", "labelImgSec2_5"],
            ["labelImgSec3_1", "labelImgSec3_2", "labelImgSec3_3", "labelImgSec3_4", "labelImgSec3_5"],
            ["labelImgSec4_1", "labelImgSec4_2", "labelImgSec4_3", "labelImgSec4_4", "labelImgSec4_5"],
            ["labelImgSec5_1", "labelImgSec5_2", "labelImgSec5_3", "labelImgSec5_4", "labelImgSec5_5"],
            ["labelImgSec6_1", "labelImgSec6_2", "labelImgSec6_3", "labelImgSec6_4", "labelImgSec6_5"],
            ["labelImgSec7_1", "labelImgSec7_2", "labelImgSec7_3", "labelImgSec7_4", "labelImgSec7_5"],
            ["labelImgSec8_1", "labelImgSec8_2", "labelImgSec8_3", "labelImgSec8_4", "labelImgSec8_5"],
            ["labelImgSece_1", "labelImgSece_2", "labelImgSece_3", "labelImgSece_4", "labelImgSece_5", "labelImgSece_6",
             "labelImgSece_7", "labelImgSece_8", "labelImgSece_9", "labelImgSece_10"]
        ]

        # Lists for Jantar
        self.button_map_J = {
            "pushImgJ1_1": "labelImgJ1_1", "pushImgJ1_2": "labelImgJ1_2",
            "pushImgJ1_3": "labelImgJ1_3", "pushImgJ1_4": "labelImgJ1_4",
            "pushImgJ1_5": "labelImgJ1_5", "pushImgJ1_6": "labelImgJ1_6",

            "pushImgJ2_1": "labelImgJ2_1", "pushImgJ2_2": "labelImgJ2_2",
            "pushImgJ2_3": "labelImgJ2_3", "pushImgJ2_4": "labelImgJ2_4",
            "pushImgJ2_5": "labelImgJ2_5", "pushImgJ2_6": "labelImgJ2_6",

            "pushImgJ3_1": "labelImgJ3_1", "pushImgJ3_2": "labelImgJ3_2",
            "pushImgJ3_3": "labelImgJ3_3", "pushImgJ3_4": "labelImgJ3_4",
            "pushImgJ3_5": "labelImgJ3_5", "pushImgJ3_6": "labelImgJ3_6",

            "pushImgJ4_1": "labelImgJ4_1", "pushImgJ4_2": "labelImgJ4_2",
            "pushImgJ4_3": "labelImgJ4_3", "pushImgJ4_4": "labelImgJ4_4",
            "pushImgJ4_5": "labelImgJ4_5", "pushImgJ4_6": "labelImgJ4_6",

            "pushImgJ5_1": "labelImgJ5_1", "pushImgJ5_2": "labelImgJ5_2",
            "pushImgJ5_3": "labelImgJ5_3", "pushImgJ5_4": "labelImgJ5_4",
            "pushImgJ5_5": "labelImgJ5_5", "pushImgJ5_6": "labelImgJ5_6",

            "pushImgJS_1": "labelImgJS_1", "pushImgJS_2": "labelImgJS_2",
            "pushImgJS_3": "labelImgJS_3", "pushImgJS_4": "labelImgJS_4",
        }

        self.button_remove_J = {
            "pushImgJ1_7": "labelImgJ1_1", "pushImgJ1_8": "labelImgJ1_2",
            "pushImgJ1_9": "labelImgJ1_3", "pushImgJ1_10": "labelImgJ1_4",
            "pushImgJ1_11": "labelImgJ1_5", "pushImgJ1_12": "labelImgJ1_6",

            "pushImgJ2_7": "labelImgJ2_1", "pushImgJ2_8": "labelImgJ2_2",
            "pushImgJ2_9": "labelImgJ2_3", "pushImgJ2_10": "labelImgJ2_4",
            "pushImgJ2_11": "labelImgJ2_5", "pushImgJ2_12": "labelImgJ2_6",

            "pushImgJ3_7": "labelImgJ3_1", "pushImgJ3_8": "labelImgJ3_2",
            "pushImgJ3_9": "labelImgJ3_3", "pushImgJ3_10": "labelImgJ3_4",
            "pushImgJ3_11": "labelImgJ3_5", "pushImgJ3_12": "labelImgJ3_6",

            "pushImgJ4_7": "labelImgJ4_1", "pushImgJ4_8": "labelImgJ4_2",
            "pushImgJ4_9": "labelImgJ4_3", "pushImgJ4_10": "labelImgJ4_4",
            "pushImgJ4_11": "labelImgJ4_5", "pushImgJ4_12": "labelImgJ4_6",

            "pushImgJ5_7": "labelImgJ5_1", "pushImgJ5_8": "labelImgJ5_2",
            "pushImgJ5_9": "labelImgJ5_3", "pushImgJ5_10": "labelImgJ5_4",
            "pushImgJ5_11": "labelImgJ5_5", "pushImgJ5_12": "labelImgJ5_6",

            "pushImgJS_5": "labelImgJS_1", "pushImgJS_6": "labelImgJS_2",
            "pushImgJS_7": "labelImgJS_3", "pushImgJS_8": "labelImgJS_4",
        }

        self.images_list_J = [
            ["labelImgJ1_1", "labelImgJ1_2", "labelImgJ1_3"],
            ["labelImgJ1_4", "labelImgJ1_5", "labelImgJ1_6"],
            ["labelImgJ2_1", "labelImgJ2_2", "labelImgJ2_3"],
            ["labelImgJ2_4", "labelImgJ2_5", "labelImgJ2_6"],
            ["labelImgJ3_1", "labelImgJ3_2", "labelImgJ3_3"],
            ["labelImgJ3_4", "labelImgJ3_5", "labelImgJ3_6"],
            ["labelImgJ4_1", "labelImgJ4_2", "labelImgJ4_3"],
            ["labelImgJ4_4", "labelImgJ4_5", "labelImgJ4_6"],
            ["labelImgJ5_1", "labelImgJ5_2", "labelImgJ5_3"],
            ["labelImgJ5_4", "labelImgJ5_5", "labelImgJ5_6"],
            ["labelImgJS_1", "labelImgJS_2", "labelImgJS_3", "labelImgJS_4"]
        ]

        self.boxes_coords_J = [
            # box0
            [
                [{'path': "", 'x': 140, 'y': 970}],
                [{'path': "", 'x': 110, 'y': 970}, {'path': "", 'x': 170, 'y': 970}],
                [{'path': "", 'x': 80, 'y': 970}, {'path': "", 'x': 140, 'y': 970}, {'path': "", 'x': 200, 'y': 970}]
            ],
            # box1
            [
                [{'path': "", 'x': 405, 'y': 970}],
                [{'path': "", 'x': 375, 'y': 970}, {'path': "", 'x': 435, 'y': 970}],
                [{'path': "", 'x': 345, 'y': 970}, {'path': "", 'x': 405, 'y': 970}, {'path': "", 'x': 465, 'y': 970}]
            ],
            # box2
            [
                [{'path': "", 'x': 140, 'y': 820}],
                [{'path': "", 'x': 110, 'y': 820}, {'path': "", 'x': 170, 'y': 820}],
                [{'path': "", 'x': 80, 'y': 820}, {'path': "", 'x': 140, 'y': 820}, {'path': "", 'x': 200, 'y': 820}]
            ],
            # box3
            [
                [{'path': "", 'x': 405, 'y': 820}],
                [{'path': "", 'x': 375, 'y': 820}, {'path': "", 'x': 435, 'y': 820}],
                [{'path': "", 'x': 345, 'y': 820}, {'path': "", 'x': 405, 'y': 820}, {'path': "", 'x': 465, 'y': 820}]
            ],
            # box4
            [
                [{'path': "", 'x': 140, 'y': 670}],
                [{'path': "", 'x': 110, 'y': 670}, {'path': "", 'x': 170, 'y': 670}],
                [{'path': "", 'x': 80, 'y': 670}, {'path': "", 'x': 140, 'y': 670}, {'path': "", 'x': 200, 'y': 670}]
            ],
            # box5
            [
                [{'path': "", 'x': 405, 'y': 670}],
                [{'path': "", 'x': 375, 'y': 670}, {'path': "", 'x': 435, 'y': 670}],
                [{'path': "", 'x': 345, 'y': 670}, {'path': "", 'x': 405, 'y': 670}, {'path': "", 'x': 465, 'y': 670}]
            ],
            # box6
            [
                [{'path': "", 'x': 140, 'y': 520}],
                [{'path': "", 'x': 110, 'y': 520}, {'path': "", 'x': 170, 'y': 520}],
                [{'path': "", 'x': 80, 'y': 520}, {'path': "", 'x': 140, 'y': 520}, {'path': "", 'x': 200, 'y': 520}]
            ],
            # box7
            [
                [{'path': "", 'x': 405, 'y': 520}],
                [{'path': "", 'x': 375, 'y': 520}, {'path': "", 'x': 435, 'y': 520}],
                [{'path': "", 'x': 345, 'y': 520}, {'path': "", 'x': 405, 'y': 520}, {'path': "", 'x': 465, 'y': 520}]
            ],
            # box8
            [
                [{'path': "", 'x': 140, 'y': 370}],
                [{'path': "", 'x': 110, 'y': 370}, {'path': "", 'x': 170, 'y': 370}],
                [{'path': "", 'x': 80, 'y': 370}, {'path': "", 'x': 140, 'y': 370}, {'path': "", 'x': 200, 'y': 370}]
            ],
             # box9
            [
                [{'path': "", 'x': 405, 'y': 370}],
                [{'path': "", 'x': 375, 'y': 370}, {'path': "", 'x': 435, 'y': 370}],
                [{'path': "", 'x': 345, 'y': 370}, {'path': "", 'x': 405, 'y': 370}, {'path': "", 'x': 465, 'y': 370}]
            ],
            # box10
            [
                [{'path': "", 'x': 275, 'y': 230}],
                [{'path': "", 'x': 245, 'y': 230}, {'path': "", 'x': 305, 'y': 230}],
                [{'path': "", 'x': 215, 'y': 230}, {'path': "", 'x': 275, 'y': 230}, {'path': "", 'x': 335, 'y': 230}],
                [{'path': "", 'x': 185, 'y': 230}, {'path': "", 'x': 245, 'y': 230}, {'path': "", 'x': 305, 'y': 230},
                 {'path': "", 'x': 365, 'y': 230}]
            ]
        ]

        # Lists for C
        self.button_map_C = {
            "pushImgC1_1": "labelImgC1_1", "pushImgC1_2": "labelImgC1_2",
            "pushImgC1_3": "labelImgC1_3", "pushImgC1_4": "labelImgC1_4",
            "pushImgC1_5": "labelImgC1_5", "pushImgC2_1": "labelImgC2_1",
            "pushImgC2_2": "labelImgC2_2", "pushImgC2_3": "labelImgC2_3",
            "pushImgC2_4": "labelImgC2_4", "pushImgC2_5": "labelImgC2_5",
            "pushImgC3_1": "labelImgC3_1", "pushImgC3_2": "labelImgC3_2",
            "pushImgC3_3": "labelImgC3_3", "pushImgC3_4": "labelImgC3_4",
            "pushImgC3_5": "labelImgC3_5", "pushImgC4_1": "labelImgC4_1",
            "pushImgC4_2": "labelImgC4_2", "pushImgC4_3": "labelImgC4_3",
            "pushImgC4_4": "labelImgC4_4", "pushImgC4_5": "labelImgC4_5",
            "pushImgC5_1": "labelImgC5_1", "pushImgC5_2": "labelImgC5_2",
            "pushImgC5_3": "labelImgC5_3", "pushImgC5_4": "labelImgC5_4",
            "pushImgC5_5": "labelImgC5_5", "pushImgC6_1": "labelImgC6_1",
            "pushImgC6_2": "labelImgC6_2", "pushImgC6_3": "labelImgC6_3",
            "pushImgC6_4": "labelImgC6_4", "pushImgC6_5": "labelImgC6_5"
        }

        self.button_remove_C = {
            "pushImgC1_6": "labelImgC1_1", "pushImgC1_7": "labelImgC1_2",
            "pushImgC1_8": "labelImgC1_3", "pushImgC1_9": "labelImgC1_4",
            "pushImgC1_10": "labelImgC1_5", "pushImgC2_6": "labelImgC2_1",
            "pushImgC2_7": "labelImgC2_2", "pushImgC2_8": "labelImgC2_3",
            "pushImgC2_9": "labelImgC2_4", "pushImgC2_10": "labelImgC2_5",
            "pushImgC3_6": "labelImgC3_1", "pushImgC3_7": "labelImgC3_2",
            "pushImgC3_8": "labelImgC3_3", "pushImgC3_9": "labelImgC3_4",
            "pushImgC3_10": "labelImgC3_5", "pushImgC4_6": "labelImgC4_1",
            "pushImgC4_7": "labelImgC4_2", "pushImgC4_8": "labelImgC4_3",
            "pushImgC4_9": "labelImgC4_4", "pushImgC4_10": "labelImgC4_5",
            "pushImgC5_6": "labelImgC5_1", "pushImgC5_7": "labelImgC5_2",
            "pushImgC5_8": "labelImgC5_3", "pushImgC5_9": "labelImgC5_4",
            "pushImgC5_10": "labelImgC5_5", "pushImgC6_6": "labelImgC6_1",
            "pushImgC6_7": "labelImgC6_2", "pushImgC6_8": "labelImgC6_3",
            "pushImgC6_9": "labelImgC6_4", "pushImgC6_10": "labelImgC6_5"
        }

        self.images_list_C = [
            ["labelImgC1_1", "labelImgC1_2", "labelImgC1_3", "labelImgC1_4", "labelImgC1_5"],
            ["labelImgC2_1", "labelImgC2_2", "labelImgC2_3", "labelImgC2_4", "labelImgC2_5"],
            ["labelImgC3_1", "labelImgC3_2", "labelImgC3_3", "labelImgC3_4", "labelImgC3_5"],
            ["labelImgC4_1", "labelImgC4_2", "labelImgC4_3", "labelImgC4_4", "labelImgC4_5"],
            ["labelImgC5_1", "labelImgC5_2", "labelImgC5_3", "labelImgC5_4", "labelImgC5_5"],
            ["labelImgC6_1", "labelImgC6_2", "labelImgC6_3", "labelImgC6_4", "labelImgC6_5"]
        ]

        self.grid_names_C = [self.ui.gridLayoutC_1, self.ui.gridLayoutC_2, self.ui.gridLayoutC_3,
                              self.ui.gridLayoutC_4,
                              self.ui.gridLayoutC_5, self.ui.gridLayoutC_6, self.ui.gridLayoutC_7,
                              self.ui.gridLayoutC_8]

        # Lists for CC
        self.button_map_CC = {
            "pushImgCC1_1": "labelImgCC1_1", "pushImgCC1_2": "labelImgCC1_2",
            "pushImgCC1_3": "labelImgCC1_3", "pushImgCC1_4": "labelImgCC1_4",
            "pushImgCC1_5": "labelImgCC1_5", "pushImgCC2_1": "labelImgCC2_1",
            "pushImgCC2_2": "labelImgCC2_2", "pushImgCC2_3": "labelImgCC2_3",
            "pushImgCC2_4": "labelImgCC2_4", "pushImgCC2_5": "labelImgCC2_5",
            "pushImgCC3_1": "labelImgCC3_1", "pushImgCC3_2": "labelImgCC3_2",
            "pushImgCC3_3": "labelImgCC3_3", "pushImgCC3_4": "labelImgCC3_4",
            "pushImgCC3_5": "labelImgCC3_5", "pushImgCC4_1": "labelImgCC4_1",
            "pushImgCC4_2": "labelImgCC4_2", "pushImgCC4_3": "labelImgCC4_3",
            "pushImgCC4_4": "labelImgCC4_4", "pushImgCC4_5": "labelImgCC4_5",
            "pushImgCC5_1": "labelImgCC5_1", "pushImgCC5_2": "labelImgCC5_2",
            "pushImgCC5_3": "labelImgCC5_3", "pushImgCC5_4": "labelImgCC5_4",
            "pushImgCC5_5": "labelImgCC5_5", "pushImgCC6_1": "labelImgCC6_1",
            "pushImgCC6_2": "labelImgCC6_2", "pushImgCC6_3": "labelImgCC6_3",
            "pushImgCC6_4": "labelImgCC6_4", "pushImgCC6_5": "labelImgCC6_5",
            "pushImgCC7_1": "labelImgCC7_1", "pushImgCC7_2": "labelImgCC7_2",
            "pushImgCC7_3": "labelImgCC7_3", "pushImgCC7_4": "labelImgCC7_4",
            "pushImgCC7_5": "labelImgCC7_5", "pushImgCC8_1": "labelImgCC8_1",
            "pushImgCC8_2": "labelImgCC8_2", "pushImgCC8_3": "labelImgCC8_3",
            "pushImgCC8_4": "labelImgCC8_4", "pushImgCC8_5": "labelImgCC8_5",
            "pushImgCCe_1": "labelImgCCe_1", "pushImgCCe_2": "labelImgCCe_2",
            "pushImgCCe_3": "labelImgCCe_3", "pushImgCCe_4": "labelImgCCe_4",
            "pushImgCCe_5": "labelImgCCe_5", "pushImgCCe_11": "labelImgCCe_6",
            "pushImgCCe_12": "labelImgCCe_7", "pushImgCCe_13": "labelImgCCe_8",
            "pushImgCCe_14": "labelImgCCe_9", "pushImgCCe_15": "labelImgCCe_10",
        }

        self.button_remove_CC = {
            "pushImgCC1_6": "labelImgCC1_1", "pushImgCC1_7": "labelImgCC1_2",
            "pushImgCC1_8": "labelImgCC1_3", "pushImgCC1_9": "labelImgCC1_4",
            "pushImgCC1_10": "labelImgCC1_5", "pushImgCC2_6": "labelImgCC2_1",
            "pushImgCC2_7": "labelImgCC2_2", "pushImgCC2_8": "labelImgCC2_3",
            "pushImgCC2_9": "labelImgCC2_4", "pushImgCC2_10": "labelImgCC2_5",
            "pushImgCC3_6": "labelImgCC3_1", "pushImgCC3_7": "labelImgCC3_2",
            "pushImgCC3_8": "labelImgCC3_3", "pushImgCC3_9": "labelImgCC3_4",
            "pushImgCC3_10": "labelImgCC3_5", "pushImgCC4_6": "labelImgCC4_1",
            "pushImgCC4_7": "labelImgCC4_2", "pushImgCC4_8": "labelImgCC4_3",
            "pushImgCC4_9": "labelImgCC4_4", "pushImgCC4_10": "labelImgCC4_5",
            "pushImgCC5_6": "labelImgCC5_1", "pushImgCC5_7": "labelImgCC5_2",
            "pushImgCC5_8": "labelImgCC5_3", "pushImgCC5_9": "labelImgCC5_4",
            "pushImgCC5_10": "labelImgCC5_5", "pushImgCC6_6": "labelImgCC6_1",
            "pushImgCC6_7": "labelImgCC6_2", "pushImgCC6_8": "labelImgCC6_3",
            "pushImgCC6_9": "labelImgCC6_4", "pushImgCC6_10": "labelImgCC6_5",
            "pushImgCC7_6": "labelImgCC7_1", "pushImgCC7_7": "labelImgCC7_2",
            "pushImgCC7_8": "labelImgCC7_3", "pushImgCC7_9": "labelImgCC7_4",
            "pushImgCC7_10": "labelImgCC7_5", "pushImgCC8_6": "labelImgCC8_1",
            "pushImgCC8_7": "labelImgCC8_2", "pushImgCC8_8": "labelImgCC8_3",
            "pushImgCC8_9": "labelImgCC8_4", "pushImgCC8_10": "labelImgCC8_5",
            "pushImgCCe_6": "labelImgCCe_1", "pushImgCCe_7": "labelImgCCe_2",
            "pushImgCCe_8": "labelImgCCe_3", "pushImgCCe_9": "labelImgCCe_4",
            "pushImgCCe_10": "labelImgCCe_5", "pushImgCCe_16": "labelImgCCe_6",
            "pushImgCCe_17": "labelImgCCe_7", "pushImgCCe_18": "labelImgCCe_8",
            "pushImgCCe_19": "labelImgCCe_9", "pushImgCCe_20": "labelImgCCe_10",
        }

        self.images_list_CC = [
            ["labelImgCC1_1", "labelImgCC1_2", "labelImgCC1_3", "labelImgCC1_4", "labelImgCC1_5"],
            ["labelImgCC2_1", "labelImgCC2_2", "labelImgCC2_3", "labelImgCC2_4", "labelImgCC2_5"],
            ["labelImgCC3_1", "labelImgCC3_2", "labelImgCC3_3", "labelImgCC3_4", "labelImgCC3_5"],
            ["labelImgCC4_1", "labelImgCC4_2", "labelImgCC4_3", "labelImgCC4_4", "labelImgCC4_5"],
            ["labelImgCC5_1", "labelImgCC5_2", "labelImgCC5_3", "labelImgCC5_4", "labelImgCC5_5"],
            ["labelImgCC6_1", "labelImgCC6_2", "labelImgCC6_3", "labelImgCC6_4", "labelImgCC6_5"],
            ["labelImgCC7_1", "labelImgCC7_2", "labelImgCC7_3", "labelImgCC7_4", "labelImgCC7_5"],
            ["labelImgCC8_1", "labelImgCC8_2", "labelImgCC8_3", "labelImgCC8_4", "labelImgCC8_5"],
            ["labelImgCCe_1", "labelImgCCe_2", "labelImgCCe_3", "labelImgCCe_4", "labelImgCCe_5"],
            ["labelImgCCe_6", "labelImgCCe_7", "labelImgCCe_8", "labelImgCCe_9", "labelImgCCe_10"],
        ]

    def get_names_list(self):
        return self.names_list

    def get_button_map(self, index):
        if index == 0:
            return self.button_map_PA
        elif index == 1:
            return self.button_map_Al
        elif index == 2:
            return self.button_map_PAS
        elif index == 3:
            return self.button_map_J
        elif index == 4:
            return self.button_map_MM1
        elif index == 5:
            return self.button_map_MM2
        elif index == 6:
            return self.button_map_MC1
        elif index == 7:
            return self.button_map_MC2
        elif index == 8:
            return self.button_map_L
        elif index == 9:
            return self.button_map_LC
        elif index == 10:
            return self.button_map_SN
        elif index == 11:
            return self.button_map_SC
        elif index == 12:
            return self.button_map_Se
        elif index == 13:
            return self.button_map_Sec
        elif index == 14:
            return self.button_map_C
        elif index == 15:
            return self.button_map_CC

    def get_button_remove(self, index):
        if index == 0:
            return self.button_remove_PA
        elif index == 1:
            return self.button_remove_Al
        elif index == 2:
            return self.button_remove_PAS
        elif index == 3:
            return self.button_remove_J
        elif index == 4:
            return self.button_remove_MM1
        elif index == 5:
            return self.button_remove_MM2
        elif index == 6:
            return self.button_remove_MC1
        elif index == 7:
            return self.button_remove_MC2
        elif index == 8:
            return self.button_remove_L
        elif index == 9:
            return self.button_remove_LC
        elif index == 10:
            return self.button_remove_SN
        elif index == 11:
            return self.button_remove_SC
        elif index == 12:
            return self.button_remove_Se
        elif index == 13:
            return self.button_map_Sec
        elif index == 14:
            return self.button_remove_C
        elif index == 15:
            return self.button_remove_CC


    def get_imgs_list(self, index):
        if index == 0:
            return self.images_list_PA
        elif index == 1:
            return self.images_list_Al
        elif index == 2:
            return self.images_list_PAS
        elif index == 3:
            return self.images_list_J
        elif index == 4:
            return self.images_list_MM1
        elif index == 5:
            return self.images_list_MM2
        elif index == 6:
            return self.images_list_MC1
        elif index == 7:
            return self.images_list_MC2
        elif index == 8:
            return self.images_list_L
        elif index == 9:
            return self.images_list_LC
        elif index == 10:
            return self.images_list_SN
        elif index == 11:
            return self.images_list_SC
        elif index == 12:
            return self.images_list_Se
        elif index == 13:
            return self.images_list_Sec
        elif index == 14:
            return self.images_list_C
        elif index == 15:
            return self.images_list_CC

    def get_box_coords(self, index):
        if index == 0:
            return self.boxes_coords_PA
        elif index == 1:
            return self.boxes_coords_Al
        elif index == 2:
            return self.boxes_coords_PAS


    def get_linetext(self, index, label_list):
        line_text = []
        if index in range(2):
            line_text = [
                {'widget': label_list[0], 'x': 243, 'y': 1395, 'color': (255, 255, 255), 'font_size': 19,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 6, 'x_max': 100},
                {'widget': label_list[1], 'x': 498, 'y': 1398, 'color': (255, 255, 255), 'font_size': 14,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 3, 'x_max': 50},
                {'widget': label_list[2], 'x': 288, 'y': 1240, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'centered': "false", 'x_max': 30},
                {'widget': label_list[3], 'x': 238, 'y': 1153, 'color': (0, 0, 0), 'font_size': 14,
                 'font_name': "Montserrat-SemiBold", 'centered': "false", 'x_max': 10},
                {'widget': label_list[4], 'x': 45, 'y': 137, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.4, 'centered': "left_bullet", 'x_max': 518,
                 'y_max': 40},
                {'widget': label_list[5], 'x': 38, 'y': 960, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 912},
                {'widget': label_list[6], 'x': 305, 'y': 960, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 912},
                {'widget': label_list[7], 'x': 38, 'y': 810, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 762},
                {'widget': label_list[8], 'x': 305, 'y': 810, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 762},
                {'widget': label_list[9], 'x': 38, 'y': 660, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 612},
                {'widget': label_list[10], 'x': 305, 'y': 660, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 612},
                {'widget': label_list[11], 'x': 38, 'y': 510, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 462},
                {'widget': label_list[12], 'x': 305, 'y': 510, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 462},
                {'widget': label_list[13], 'x': 38, 'y': 340, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 292},
                {'widget': label_list[14], 'x': 305, 'y': 340, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 292},
                {'widget': label_list[15], 'x': 50, 'y': 215, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.3, 'centered': "true_dyn", 'x_max': 500,
                 'y_max': 190}
            ]
        elif index in range(2, 9):
           line_text = [
                {'widget': label_list[0], 'x': 230, 'y': 1399, 'color': (255, 255, 255), 'font_size': 19,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 6, 'x_max': 80},

                {'widget': label_list[1], 'x': 498, 'y': 1401, 'color': (255, 255, 255), 'font_size': 14,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 3, 'x_max': 50},

                {'widget': label_list[2], 'x': 45, 'y': 900, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.8, 'centered': "left_bullet", 'x_max': 518,
                 'y_max': 475},

                {'widget': label_list[3], 'x': 38, 'y': 1276, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 1210},

                {'widget': label_list[4], 'x': 303, 'y': 1276, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 1210},

                {'widget': label_list[5], 'x': 38, 'y': 1116, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 1055},

                {'widget': label_list[6], 'x': 303, 'y': 1116, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 1055},

                {'widget': label_list[7], 'x': 38, 'y': 956, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 890},

                {'widget': label_list[8], 'x': 303, 'y': 956, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 250,
                 'y_max': 890}
            ]
        else:
            line_text = [
                {'widget': label_list[0], 'x': 230, 'y': 1399, 'color': (255, 255, 255), 'font_size': 19,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 6, 'x_max': 80},
                {'widget': label_list[1], 'x': 498, 'y': 1401, 'color': (255, 255, 255), 'font_size': 14,
                 'font_name': "BebasNeue-Regular", 'centered': "spacing", 'letter_spacing': 3, 'x_max': 50},
                {'widget': label_list[2], 'x': 45, 'y': 380, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.8, 'centered': "left_bullet", 'x_max': 518,
                 'y_max': 70},
                {'widget': label_list[3], 'x': 40, 'y': 477, 'color': (0, 0, 0), 'font_size': 13,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.2, 'centered': "left", 'x_max': 500,
                 'y_max': 430},
                {'widget': label_list[4], 'x': 38, 'y': 1233, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 1168},
                {'widget': label_list[5], 'x': 305, 'y': 1233, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 1168},
                {'widget': label_list[6], 'x': 38, 'y': 1075, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 1010},
                {'widget': label_list[7], 'x': 305, 'y': 1075, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 1010},
                {'widget': label_list[8], 'x': 38, 'y': 867, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 804},
                {'widget': label_list[9], 'x': 305, 'y': 867, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 804},
                {'widget': label_list[10], 'x': 38, 'y': 705, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 644},
                {'widget': label_list[11], 'x': 305, 'y': 705, 'color': (0, 0, 0), 'font_size': 12,
                 'font_name': "Montserrat-SemiBold", 'line_height': 1.5, 'centered': "true_dyn", 'x_max': 255,
                 'y_max': 644}
            ]
        return line_text

    def get_linetext_names(self, index):
        index_list = [
                        [self.ui.lineTipoA, self.ui.lineHorasA, self.ui.lineVeg, self.ui.lineAze, self.ui.textNotasA,
                        self.ui.plainA1_1, self.ui.plainA1_2, self.ui.plainA2_1, self.ui.plainA2_2, self.ui.plainA3_1,
                        self.ui.plainA3_2, self.ui.plainA4_1, self.ui.plainA4_2, self.ui.plainA5_1, self.ui.plainA5_2,
                        self.ui.plainAS],
                        [self.ui.lineTipoJ, self.ui.lineHorasJ, self.ui.lineVegJ, self.ui.lineAzeJ, self.ui.textNotasJ,
                        self.ui.plainJ1_1, self.ui.plainJ1_2, self.ui.plainJ2_1, self.ui.plainJ2_2,
                        self.ui.plainJ3_1, self.ui.plainJ3_2, self.ui.plainJ4_1, self.ui.plainJ4_2, self.ui.plainJ5_1,
                        self.ui.plainJ5_2, self.ui.plainJS],
                        [self.ui.lineTipo, self.ui.lineHoras, self.ui.textNotasPA, self.ui.plain1,  self.ui.plain2,
                         self.ui.plain3, self.ui.plain4, self.ui.plain5, self.ui.plain6],
                        [self.ui.lineTipoM1, self.ui.lineHorasM1, self.ui.textNotasM1, self.ui.plainM1, self.ui.plainM2,
                         self.ui.plainM3, self.ui.plainM4, self.ui.plainM5, self.ui.plainM6],
                        [self.ui.lineTipoMM2, self.ui.lineHorasMM2, self.ui.textNotasMM2, self.ui.plainMM1,
                         self.ui.plainMM2, self.ui.plainMM3, self.ui.plainMM4, self.ui.plainMM5, self.ui.plainMM6],
                        [self.ui.lineTipoL, self.ui.lineHorasL, self.ui.textNotasL, self.ui.plainL1, self.ui.plainL2,
                         self.ui.plainL3, self.ui.plainL4, self.ui.plainL5, self.ui.plainL6],
                        [self.ui.lineTipoSN, self.ui.lineHorasSN, self.ui.textNotasSN, self.ui.plainSN1, self.ui.plainSN2,
                         self.ui.plainSN3, self.ui.plainSN4, self.ui.plainSN5, self.ui.plainSN6],
                        [self.ui.lineTipoSe, self.ui.lineHorasSe, self.ui.textNotasSe, self.ui.plainSe1, self.ui.plainSe2,
                         self.ui.plainSe3, self.ui.plainSe4, self.ui.plainSe5, self.ui.plainSe6],
                        [self.ui.lineTipoC, self.ui.lineHorasC, self.ui.textNotasC, self.ui.plainC1, self.ui.plainC2,
                         self.ui.plainC3, self.ui.plainC4, self.ui.plainC5, self.ui.plainC6],
                        [self.ui.lineTipoS, self.ui.lineHorasS, self.ui.textNotasPAS, self.ui.textExe, self.ui.plainS1,
                         self.ui.plainS2, self.ui.plainS3, self.ui.plainS4, self.ui.plainS5, self.ui.plainS6,
                         self.ui.plainS7, self.ui.plainS8],
                        [self.ui.lineTipoMC1, self.ui.lineHorasMC1, self.ui.textNotasMC1, self.ui.textExeMC1, self.ui.plainMC1,
                         self.ui.plainMC2, self.ui.plainMC3, self.ui.plainMC4, self.ui.plainMC5, self.ui.plainMC6,
                         self.ui.plainMC7, self.ui.plainMC8],
                        [self.ui.lineTipoMC2, self.ui.lineHorasMC2, self.ui.textNotasMC2, self.ui.textExeMC2, self.ui.plainMMC1,
                         self.ui.plainMMC2, self.ui.plainMMC3, self.ui.plainMMC4, self.ui.plainMMC5, self.ui.plainMMC6,
                         self.ui.plainMMC7, self.ui.plainMMC8],
                        [self.ui.lineTipoLC, self.ui.lineHorasLC, self.ui.textNotasLC, self.ui.textExeLC, self.ui.plainMC1,
                         self.ui.plainLC2, self.ui.plainLC3, self.ui.plainLC4, self.ui.plainLC5, self.ui.plainLC6,
                         self.ui.plainLC7, self.ui.plainLC8],
                        [self.ui.lineTipoSC, self.ui.lineHorasSC, self.ui.textNotasSC, self.ui.textExeSC, self.ui.plainSC1,
                         self.ui.plainSC2, self.ui.plainSC3, self.ui.plainSC4, self.ui.plainSC5, self.ui.plainSC6,
                         self.ui.plainSC7, self.ui.plainSC8],
                        [self.ui.lineTipoSec, self.ui.lineHorasSec, self.ui.textNotasSec, self.ui.textExeSec, self.ui.plainSec1,
                         self.ui.plainSec2, self.ui.plainSec3, self.ui.plainSec4, self.ui.plainSec5, self.ui.plainSec6,
                         self.ui.plainSec7, self.ui.plainSec8],
                        [self.ui.lineTipoCC, self.ui.lineHorasCC, self.ui.textNotasCC, self.ui.textExeCC, self.ui.plainCC1,
                         self.ui.plainCC2, self.ui.plainCC3, self.ui.plainCC4, self.ui.plainCC5, self.ui.plainCC6,
                         self.ui.plainCC7, self.ui.plainCC8],
        ]

        if index == -1:
            return self.linetext_names_G
        else:
            return self.get_linetext(index, index_list[index])

    def get_grid_names_PA(self, index):
        if index == 0:
            return self.grid_names_PA
        elif index == 1:
            return self.grid_names_MM1
        elif index == 2:
            return self.grid_names_MM2
        elif index == 3:
            return self.grid_names_L
        elif index == 4:
            return self.grid_names_SN
        elif index == 5:
            return self.grid_names_Se
        elif index == 6:
            return self.grid_names_C
