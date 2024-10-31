class PagesData:
    def __init__(self, ui, parent):
        self.ui = ui
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.page_suffixes = ['PA', 'Al', 'PAS', 'J', 'MM1', 'MM2', 'MC1', 'MC2', 'L','LC', 'SN', 'SC', 'Se', 'Sec',
                               'C', 'CC']
        suffixes = ['S', 'A', 'J', 'M1', 'MM2', 'MC1', 'MMC1', 'L', 'LC', 'SN', 'SC', 'Se', 'Sec', 'C', 'CC']
        cp_suffixed = ['S', 'MC1', 'MMC1', 'LC', 'SC', 'Sec', 'CC']
        spn_suffix = ['', 'M1', 'MM2', 'L', 'SN', 'Se', 'C']
        sp_suffix = ['', 'M', 'MM', 'L', 'SN', 'Se', 'C']
        aj_suffix = ['A', 'J']
        se_suffix = ['Se_', 'AS_', 'JS_', 'MCe_', 'MMCe_', 'LCe_', 'SCe_', 'Sece_', 'CCe_']
        self.names_list = ["user_id", "lineNome", "linePeso", "lineMG", "lineObj", "lineData", "lineMarc",
                           "lineMax", "textNotasPA", "lineTipo", "lineHoras"]

        self.names_list += self.add_suffixed_names(suffixes, ['lineTipo{}', 'lineHoras{}', 'textNotas{}'])
        self.names_list += self.add_suffixed_names(spn_suffix, ['pageSelection{}'])
        self.names_list += self.add_suffixed_names(cp_suffixed, ['textExe{}'])

        spc_patterns = [(f'labelImg{suf}', [(1, 6), (1, 5)]) for suf in sp_suffix]
        sps_patterns = [(f'plain{suf}', [(1, 6)]) for suf in sp_suffix]
        cp_patterns = [(f'labelImg{suf}', [(1, 8), (1, 5)]) for suf in cp_suffixed]
        cps_patterns = [(f'plain{suf}', [(1, 8)]) for suf in cp_suffixed]
        se_patterns = [(f'labelImg{suf}', [(1, 10)]) for suf in se_suffix]
        aj_patterns = [(f'labelImg{suf}', [(1, 5), (1, 6)]) for suf in aj_suffix] + \
                      [(f'plain{suf}', [(1, 5), (1, 2)]) for suf in aj_suffix]

        self.names_list += self.gen_patterns(cp_patterns, 1)
        self.names_list += self.gen_patterns(cps_patterns, 0)
        self.names_list += self.gen_patterns(spc_patterns, 1)
        self.names_list += self.gen_patterns(sps_patterns, 0)
        self.names_list += self.gen_patterns(se_patterns, 0)
        self.names_list += self.gen_patterns(aj_patterns, 1)

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
            {'widget': self.ui.lineMarc, 'x': 380, 'y': 881, 'color': (0, 0, 0), 'font_size': 16.5,
             'font_name': "Montserrat-Bold", 'centered': "false", 'x_max': 140},
            {'widget': self.ui.lineMax, 'x': 430, 'y': 824, 'color': (0, 0, 0), 'font_size': 16.5,
             'font_name': "Montserrat-Bold", 'centered': "false", 'x_max': 140}
        ]

        self.button_map_PA = {
            f"pushImg{i}_{j}": f"labelImg{i}_{j}"
            for i in range(1, 7)
            for j in range(1, 6)
        }

        self.button_remove_PA = {
            f"pushImg{i}_{j+5}": f"labelImg{i}_{j}"
            for i in range(1, 7)
            for j in range(1, 6)
        }

        self.images_list_PA = [
            [f"labelImg{i}_{j}" for j in range(1, 6)]
            for i in range(1, 7)
        ]

        # Define the y-values for each box
        y_values = [1290, 1290, 1130, 1130, 970, 970]

        # Generate the structure automatically
        self.boxes_coords_PA = [
            [
                [{'path': "", 'y': y_values[i]} for _ in range(j)]
                for j in range(1, 6)  # Range for number of coordinates in each row
            ]
            for i in range(6)  # Number of boxes (from 0 to 5)
        ]

        self.grid_names_PA = [self.ui.gridLayout_7, self.ui.gridLayout_9, self.ui.gridLayout_46, self.ui.gridLayout_43,
                         self.ui.gridLayout_57, self.ui.gridLayout_58, self.ui.gridLayout_59, self.ui.gridLayout_60]

        # For pushImgA1_ to pushImgA5_ series
        self.button_map_Al = {
            f"pushImgA{i}_{j}": f"labelImgA{i}_{j}"
            for i in range(1, 6)
            for j in range(1, 7)
        }

        self.button_remove_Al = {
            f"pushImgA{i}_{j}": f"labelImgA{i}_{j - 6}"
            for i in range(1, 6)
            for j in range(7, 13)
        }

        # For pushImgAS series
        self.button_map_Al.update({
            f"pushImgAS_{i}": f"labelImgAS_{i}"
            for i in range(1, 5)
        })

        self.button_remove_Al.update({
            f"pushImgAS_{i}": f"labelImgAS_{i - 4}"
            for i in range(5, 9)
        })

        self.images_list_Al = [
                 [f"labelImgA{i}_1", f"labelImgA{i}_2", f"labelImgA{i}_3"] for i in range(1, 6)
             ] + [
                 [f"labelImgA{i}_4", f"labelImgA{i}_5", f"labelImgA{i}_6"] for i in range(1, 6)
             ] + [
                 [f"labelImgAS_{i}" for i in range(1, 5)]
             ]

        # y_values = [972, 972, 822, 822, 672, 672, 522, 522, 372, 372, 230]

        # self.boxes_coords_Al = [
        #                            [
        #                                [{'path': "", 'y': y_values[i]} for _ in range(num_items)]
        #                                for num_items in range(1, 4)
        #                            ]
        #                            for i in range(10)
        #                        ] + [
        #                            [{'path': "", 'y': 230} for _ in range(4)]
        #                        ]

        self.boxes_coords_Al = [
            # box0
            [
                [{'path': "", 'y': 972}],
                [{'path': "", 'y': 972}, {'path': "", 'y': 972}],
                [{'path': "", 'y': 972}, {'path': "", 'y': 972}, {'path': "", 'y': 972}]
            ],
            # box1
            [
                [{'path': "", 'y': 972}],
                [{'path': "", 'y': 972}, {'path': "", 'y': 972}],
                [{'path': "", 'y': 822}, {'path': "", 'y': 972}, {'path': "", 'y': 972}]
            ],
            # box2
            [
                [{'path': "", 'y': 822}],
                [{'path': "", 'y': 822}, {'path': "", 'y': 822}],
                [{'path': "", 'y': 822}, {'path': "", 'y': 822}, {'path': "", 'y': 822}]
            ],
            # box3
            [
                [{'path': "", 'y': 822}],
                [{'path': "", 'y': 822}, {'path': "", 'y': 822}],
                [{'path': "", 'y': 822}, {'path': "", 'y': 822}, {'path': "", 'y': 822}]
            ],
            # box4
            [
                [{'path': "", 'y': 672}],
                [{'path': "", 'y': 672}, {'path': "", 'y': 672}],
                [{'path': "", 'y': 672}, {'path': "", 'y': 672}, {'path': "", 'y': 672}]
            ],
            # box5
            [
                [{'path': "", 'y': 672}],
                [{'path': "", 'y': 672}, {'path': "", 'y': 672}],
                [{'path': "", 'y': 672}, {'path': "", 'y': 672}, {'path': "", 'y': 672}]
            ],
            # box6
            [
                [{'path': "", 'y': 522}],
                [{'path': "", 'y': 522}, {'path': "", 'y': 522}],
                [{'path': "", 'y': 522}, {'path': "", 'y': 522}, {'path': "", 'y': 522}]
            ],
            # box7
            [
                [{'path': "", 'y': 522}],
                [{'path': "", 'y': 522}, {'path': "", 'y': 522}],
                [{'path': "", 'y': 522}, {'path': "", 'y': 522}, {'path': "", 'y': 522}]
            ],
            # box8
            [
                [{'path': "", 'y': 372}],
                [{'path': "", 'y': 372}, {'path': "", 'y': 372}],
                [{'path': "", 'y': 372}, {'path': "", 'y': 372}, {'path': "", 'y': 372}]
            ],
            # box9
            [
                [{'path': "", 'y': 372}],
                [{'path': "", 'y': 372}, {'path': "", 'y': 372}],
                [{'path': "", 'y': 372}, {'path': "", 'y': 372}, {'path': "", 'y': 372}]
            ],
            # box10
            [
                [{'path': "", 'y': 230}],
                [{'path': "", 'y': 230}, {'path': "", 'y': 230}],
                [{'path': "", 'y': 230}, {'path': "", 'y': 230}, {'path': "", 'y': 230}],
                [{'path': "", 'y': 230}, {'path': "", 'y': 230}, {'path': "", 'y': 230}, {'path': "", 'y': 230}]
            ]
        ]

        self.button_map_J = {
            f"pushImgJ{i}_{j}": f"labelImgJ{i}_{j}"
            for i in range(1, 6)
            for j in range(1, 7)
        }

        self.button_remove_J = {
            f"pushImgJ{i}_{j}": f"labelImgJ{i}_{j - 6}"
            for i in range(1, 6)
            for j in range(7, 13)
        }

        # For pushImgAS series
        self.button_map_J.update({
            f"pushImgJS_{i}": f"labelImgJS_{i}"
            for i in range(1, 5)
        })

        self.button_remove_J.update({
            f"pushImgJS_{i}": f"labelImgJS_{i - 4}"
            for i in range(5, 9)
        })

        self.images_list_J = [
                 [f"labelImgJ{i}_1", f"labelImgJ{i}_2", f"labelImgJ{i}_3"] for i in range(1, 6)
             ] + [
                 [f"labelImgJ{i}_4", f"labelImgJ{i}_5", f"labelImgJ{i}_6"] for i in range(1, 6)
             ] + [
                 [f"labelImgJS_{i}" for i in range(1, 5)]
             ]

        self.button_map_PAS = {
            f"pushImgS{i}_{j}": f"labelImgS{i}_{j}"
            for i in range(1, 9)  # Adjust range for S1 to S8
            for j in range(1, 6)  # Adjust range for 1 to 5
        }.update({
            f"pushImgSe_{k}": f"labelImgSe_{k}"
            for k in range(1, 16)  # Adjust range for Se_1 to Se_15
        })

        self.button_remove_PAS = {
            f"pushImgS{i}_{j}": f"labelImgS{i}_{j - 5}"
            for i in range(1, 9) for j in range(6, 11)
        }

        self.button_remove_PAS.update({
            f"pushImgSe_{i}": f"labelImgSe_{i - 5}"
            for i in range(6, 11)
        })

        self.button_remove_PAS.update({
            f"pushImgSe_{i}": f"labelImgSe_{i - 10}"
            for i in range(16, 21)
        })

        # Automating the images_list_PAS list
        self.images_list_PAS = [
                                   [f"labelImgS{i}_{j}" for j in range(1, 6)] for i in range(1, 9)
                               ] + [
                                   [f"labelImgSe_{j}" for j in range(1, 6)],
                                   [f"labelImgSe_{j}" for j in range(6, 11)]
                               ]

        # Predefined y-values for each box
        y_values = [1248, 1248, 1088, 1088, 883, 883, 718, 718, 593, 593]

        # Automating the boxes_coords_PAS generation
        self.boxes_coords_PAS = [
            [[{'path': "", 'y': y_values[box_index]} for _ in range(row_index + 1)] for row_index in range(5)]
            for box_index in range(10)
        ]

        #List for MC1
        # Automate button_map_MC1
        self.button_map_MC1 = {f"pushImgMC{i}_{j}": f"labelImgMC{i}_{j}"
                               for i in range(1, 9)
                               for j in range(1, 6)}
        self.button_map_MC1.update({f"pushImgMCe_{j}": f"labelImgMCe_{j}"
                                    for j in range(1, 11)})

        # Automate button_remove_MC1
        self.button_remove_MC1 = {f"pushImgMC{i}_{j}": f"labelImgMC{i}_{j - 5}"
                                  for i in range(1, 9)
                                  for j in range(6, 11)}
        self.button_remove_MC1.update({f"pushImgMCe_{j}": f"labelImgMCe_{j - 5}"
                                       for j in range(6, 11)})
        self.button_remove_MC1.update({f"pushImgMCe_{j}": f"labelImgMCe_{j - 10}"
                                       for j in range(16, 21)})

        # Automate images_list_MC1
        self.images_list_MC1 = [[f"labelImgMC{i}_{j}" for j in range(1, 6)]
                                 for i in range(1, 9)
                                ] + \
                               [[f"labelImgMCe_{j}" for j in range(1, 6)]
                                 for j in range(1, 11)
                               ]

        #List for MC2
        # Automate button_map_MC2
        self.button_map_MC2 = {f"pushImgMMC{i}_{j}": f"labelImgMMC{i}_{j}" for i in range(1, 9) for j in range(1, 6)}
        self.button_map_MC2.update({f"pushImgMMCe_{j}": f"labelImgMMCe_{j}" for j in range(1, 6)})
        self.button_map_MC2.update({f"pushImgMMCe_{j + 10}": f"labelImgMMCe_{j + 5}" for j in range(1, 6)})

        # Automate button_remove_MC2
        self.button_remove_MC2 = {f"pushImgMMC{i}_{j}": f"labelImgMMC{i}_{j - 5}" for i in range(1, 9) for j in
                                  range(6, 11)}
        self.button_remove_MC2.update({f"pushImgMMCe_{j}": f"labelImgMMCe_{j - 5}"
                                       for j in range(6, 11)})
        self.button_remove_MC2.update({f"pushImgMMCe_{j}": f"labelImgMMCe_{j - 10}"
                                       for j in range(16, 21)})

        # Automate images_list_MC2
        self.images_list_MC2 = [[f"labelImgMMC{i}_{j}" for j in range(1, 6)] for i in range(1, 9)] + \
                               [[f"labelImgMMCe_{j}" for j in range(1, 6)] for j in range(1, 11, 5)]

        # List for MM1
        # Dynamically generate mappings and lists
        self.button_map_MM1 = {f"pushImgM{i + 1}_{j + 1}": f"labelImgM{i + 1}_{j + 1}" for i in range(6) for j in
                               range(5)}
        self.button_remove_MM1 = {f"pushImgM{i + 1}_{j + 6}": f"labelImgM{i + 1}_{j + 1}" for i in range(6) for j in
                                  range(5)}
        self.images_list_MM1 = [[f"labelImgM{i + 1}_{j + 1}" for j in range(5)] for i in range(6)]

        self.grid_names_MM1 = [self.ui.gridLayout_32, self.ui.gridLayout_31, self.ui.gridLayoutM_1, self.ui.gridLayoutM_2,
                         self.ui.gridLayoutM_3, self.ui.gridLayoutM_4, self.ui.gridLayoutM_5, self.ui.gridLayoutM_6]

        # List for MM2
        # Automating the creation of button_map_MM2
        self.button_map_MM2 = {
            f"pushImgMM{i}_{j}": f"labelImgMM{i}_{j}"
            for i in range(1, 7)
            for j in range(1, 6)
        }

        # Automating the creation of button_remove_MM2
        self.button_remove_MM2 = {
            f"pushImgMM{i}_{j}": f"labelImgMM{i}_1"
            for i in range(1, 7)
            for j in range(6, 11)
        }

        # Automating the creation of images_list_MM2
        self.images_list_MM2 = [
            [f"labelImgMM{i}_{j}" for j in range(1, 6)]
            for i in range(1, 7)
        ]

        self.grid_names_MM2 = [self.ui.gridLayoutMM_1, self.ui.gridLayoutMM_2, self.ui.gridLayoutMM_3, self.ui.gridLayoutMM_4,
                         self.ui.gridLayoutMM_5, self.ui.gridLayoutMM_6, self.ui.gridLayoutMM_7, self.ui.gridLayoutMM_8]

        # List for L
        # Automating button_map_L
        self.button_map_L = {
            f"pushImgL{i}_{j}": f"labelImgL{i}_{j}"
            for i in range(1, 7)  # i represents rows 1 to 6
            for j in range(1, 6)  # j represents columns 1 to 5
        }

        # Automating button_remove_L
        self.button_remove_L = {
            f"pushImgL{i}_{j + 5}": f"labelImgL{i}_{j}"
            for i in range(1, 7)  # i represents rows 1 to 6
            for j in range(1, 6)  # j represents columns 1 to 5 (j+5 represents columns 6 to 10)
        }

        # Automating images_list_L
        self.images_list_L = [
            [f"labelImgL{i}_{j}" for j in range(1, 6)]  # j represents columns 1 to 5
            for i in range(1, 7)  # i represents rows 1 to 6
        ]

        self.grid_names_L = [self.ui.gridLayoutL_1, self.ui.gridLayoutL_2, self.ui.gridLayoutL_3, self.ui.gridLayoutL_4,
                         self.ui.gridLayoutL_5, self.ui.gridLayoutL_6, self.ui.gridLayoutL_7, self.ui.gridLayoutL_8]


        #List for LC
        # Generate the button_map_LC dictionary
        self.button_map_LC = {
            f"pushImgLC{i}_{j}": f"labelImgLC{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }
        self.button_map_LC.update({
            f"pushImgLCe_{i}": f"labelImgLCe_{j}"
            for i, j in zip(range(1, 16), range(1, 11))
            if i != 11  # Exclude i=11
        })

        # Generate the button_remove_LC dictionary
        self.button_remove_LC = {
            f"pushImgLC{i}_{j - 1 + 6}": f"labelImgLC{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }
        self.button_remove_LC.update({
            f"pushImgLCe_{i + 6}": f"labelImgLCe_{j}"
            for i, j in zip(range(1, 21), range(1, 11))
            if i != 16  # Exclude i=16
        })

        # Generate the images_list_LC list
        self.images_list_LC = [
                                  [f"labelImgLC{i}_{j}" for j in range(1, 6)]
                                  for i in range(1, 9)
                              ] + [
                                  [f"labelImgLCe_{i}" for i in range(1, 11)]
                              ]

        # Lists for S
        # Generate button mappings for the SN category
        self.button_map_SN = {
            f"pushImgSN{i}_{j}": f"labelImgSN{i}_{j}"
            for i in range(1, 7)  # Assuming there are 6 groups
            for j in range(1, 6)  # Assuming there are 5 images per group
        }

        # Generate button mappings for removing images in the SN category
        self.button_remove_SN = {
            f"pushImgSN{i}_{j + 5}": f"labelImgSN{i}_{j}"
            for i in range(1, 7)  # Assuming there are 6 groups
            for j in range(1, 6)  # Assuming there are 5 images per group
        }

        # Create the images list for the SN category
        self.images_list_SN = [
            [f"labelImgSN{i}_{j}" for j in range(1, 6)]
            for i in range(1, 7)  # Assuming there are 6 groups
        ]

        self.grid_names_SN = [self.ui.gridLayoutSN_1, self.ui.gridLayoutSN_2, self.ui.gridLayoutSN_3, self.ui.gridLayoutSN_4,
                         self.ui.gridLayoutSN_5, self.ui.gridLayoutSN_6, self.ui.gridLayoutSN_7, self.ui.gridLayoutSN_8]

        # Lists for SC
        # Automating button_map_SC
        self.button_map_SC = {
            f"pushImgSC{i}_{j}": f"labelImgSC{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }
        self.button_map_SC.update({
            f"pushImgSCe_{i}": f"labelImgSCe_{j}"
            for i, j in zip(range(1, 16), range(1, 11))
        })

        # Automating button_remove_SC
        self.button_remove_SC = {
            f"pushImgSC{i}_{j + 5}": f"labelImgSC{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }
        self.button_remove_SC.update({
            f"pushImgSCe_{i + 5}": f"labelImgSCe_{j}"
            for i, j in zip(range(1, 21), range(1, 11))
        })

        # Automating images_list_SC
        self.images_list_SC = [
                                  [f"labelImgSC{i}_{j}" for j in range(1, 6)]
                                  for i in range(1, 9)
                              ] + [
                                  [f"labelImgSCe_{i}" for i in range(1, 11)]
                              ]

        self.grid_names_Se = [self.ui.gridLayoutSe_1, self.ui.gridLayoutSe_2, self.ui.gridLayoutSe_3,
                              self.ui.gridLayoutSe_4,
                              self.ui.gridLayoutSe_5, self.ui.gridLayoutSe_6, self.ui.gridLayoutSe_7,
                              self.ui.gridLayoutSe_8]

        # Create button_map_Se using a dictionary comprehension
        self.button_map_Se = {
            f"pushImgSe{i}_{j}": f"labelImgSe{i}_{j}"
            for i in range(1, 7) for j in range(1, 6)
        }

        # Create button_remove_Se using a dictionary comprehension
        self.button_remove_Se = {
            f"pushImgSe{i}_{j + 5}": f"labelImgSe{i}_{j}"
            for i in range(1, 7) for j in range(1, 6)
        }

        # Create images_list_Se using a list comprehension
        self.images_list_Se = [
            [f"labelImgSe{i}_{j}" for j in range(1, 6)]
            for i in range(1, 7)
        ]

        # Lists for Sec
        # Automating button maps for Section
        self.button_map_Sec = {
            f"pushImgSec{i}_{j}": f"labelImgSec{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }.update({
            f"pushImgSece_{k}": f"labelImgSece_{k}"
            for k in range(1, 16)
        })

        self.button_remove_Sec = {
            f"pushImgSec{i}_{j + 6}": f"labelImgSec{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }.update({
            f"pushImgSece_{k + 6}": f"labelImgSece_{k}"
            for k in range(1, 11)
        })

        # Creating images list for Section
        self.images_list_Sec = [
                                   [f"labelImgSec{i}_{j}" for j in range(1, 6)]
                                   for i in range(1, 9)
                               ] + [
                                   [f"labelImgSece_{k}" for k in range(1, 11)]
                               ]

        # Lists for C
        # Create button_map_C using a dictionary comprehension
        self.button_map_C = {
            f"pushImgC{i}_{j}": f"labelImgC{i}_{j}"
            for i in range(1, 7) for j in range(1, 6)
        }

        # Create button_remove_C using a dictionary comprehension
        self.button_remove_C = {
            f"pushImgC{i}_{j + 5}": f"labelImgC{i}_{j}"
            for i in range(1, 7) for j in range(1, 6)
        }

        # Create images_list_C using a list comprehension
        self.images_list_C = [
            [f"labelImgC{i}_{j}" for j in range(1, 6)]
            for i in range(1, 7)
        ]

        self.grid_names_C = [self.ui.gridLayoutC_1, self.ui.gridLayoutC_2, self.ui.gridLayoutC_3,
                              self.ui.gridLayoutC_4,
                              self.ui.gridLayoutC_5, self.ui.gridLayoutC_6, self.ui.gridLayoutC_7,
                              self.ui.gridLayoutC_8]

        # Lists for CC
        # Button map for CC
        self.button_map_CC = {
            f"pushImgCC{i}_{j}": f"labelImgCC{i}_{j}"
            for i in range(1, 9) for j in range(1, 6)
        }.update({
            f"pushImgCCe_{i}": f"labelImgCCe_{j}"
            for i, j in zip(range(1, 16), range(1, 11))
            if i != 11  # Exclude i=11
        })

        # Button remove map for CC
        self.button_remove_CC = {
            f"pushImgCC{i}_{j + 5}": f"labelImgCC{i}_{j + 1}"  # j+5 for push buttons, j+1 for labels
            for i in range(1, 9) for j in range(1, 6)
        }.update({
            f"pushImgCCe_{i + 5}": f"labelImgCCe_{j}"  # Adjust for e buttons as well
            for i, j in zip(range(1, 16), range(1, 11))
            if i != 11  # Exclude i=11
        })

        # Images list for CC
        self.images_list_CC = [
                                  [f"labelImgCC{i}_{j}" for j in range(1, 6)]
                                  for i in range(1, 9)
                              ] + [
                                  [f"labelImgCCe_{i}" for i in range(1, 11)]
                              ]

        # Merging the images of CCe into the last sublist
        self.images_list_CC.append([f"labelImgCCe_{i}" for i in range(6, 16)])

    def get_names_list(self):
        return self.names_list

    def get_button_map(self, index):
        return getattr(self, f"button_map_{self.page_suffixes[index]}")

    def get_button_remove(self, index):
        return getattr(self, f"button_remove_{self.page_suffixes[index]}")

    def get_imgs_list(self, index):
        return getattr(self, f"images_list_{self.page_suffixes[index]}")

    def get_box_coords(self, index):
        box_list = ['PA', 'Al', 'PAS']
        return getattr(self, f"boxes_coords_{box_list[index]}")

    def get_grid_names_PA(self, index):
        suffixes = ['PA', 'MM1', 'MM2', 'L', 'SN', 'Se', 'C']
        return getattr(self, f"grid_names_{suffixes[index]}")

    def generate_boxes_coords(self, y_values, offsets):
        boxes_coords = []
        for box_index in range(len(y_values)):
            box_coords = []
            for i in range(len(offsets)):
                if i == 0:
                    box_coords.append([{'path': "", 'y': y_values[box_index]}])
                else:
                    coords = [{'path': "", 'y': y_values[box_index]}]
                    for offset in offsets[i]:
                        coords.append({'path': "", 'y': y_values[box_index]})
                    box_coords.append(coords)
            boxes_coords.append(box_coords)
        return boxes_coords
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
        if index == -1:
            return self.linetext_names_G
        else:
            index_list = [
                [self.ui.lineTipoA, self.ui.lineHorasA, self.ui.lineVeg, self.ui.lineAze, self.ui.textNotasA] +
                self.gen_list('plainA', complex_ranges=[(1, 5), (1, 2)], attr=True) + [self.ui.plainAS],
                [self.ui.lineTipoJ, self.ui.lineHorasJ, self.ui.lineVegJ, self.ui.lineAzeJ, self.ui.textNotasJ] +
                self.gen_list('plainJ', complex_ranges=[(1, 5), (1, 2)], attr=True) + [self.ui.plainJS],
                [self.ui.lineTipo, self.ui.lineHoras, self.ui.textNotasPA] +
                self.gen_list('plain', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoM1, self.ui.lineHorasM1, self.ui.textNotasM1] +
                self.gen_list('plainM', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoMM2, self.ui.lineHorasMM2, self.ui.textNotasMM2, self.ui.plainMM1] +
                self.gen_list('plainMM', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoL, self.ui.lineHorasL, self.ui.textNotasL] +
                self.gen_list('plainL', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoSN, self.ui.lineHorasSN, self.ui.textNotasSN] +
                self.gen_list('plainSN', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoSe, self.ui.lineHorasSe, self.ui.textNotasSe] +
                self.gen_list('plainSe', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoC, self.ui.lineHorasC, self.ui.textNotasC] +
                self.gen_list('plainC', simple_ranges=[(1, 6)], attr=True),
                [self.ui.lineTipoS, self.ui.lineHorasS, self.ui.textNotasPAS, self.ui.textExe] +
                self.gen_list('plainS', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoMC1, self.ui.lineHorasMC1, self.ui.textNotasMC1, self.ui.textExeMC1] +
                self.gen_list('plainMC', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoMC2, self.ui.lineHorasMC2, self.ui.textNotasMC2, self.ui.textExeMC2] +
                self.gen_list('plainMMC', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoLC, self.ui.lineHorasLC, self.ui.textNotasLC, self.ui.textExeLC] +
                self.gen_list('plainLC', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoSC, self.ui.lineHorasSC, self.ui.textNotasSC, self.ui.textExeSC] +
                self.gen_list('plainSC', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoSec, self.ui.lineHorasSec, self.ui.textNotasSec, self.ui.textExeSec] +
                self.gen_list('plainSec', simple_ranges=[(1, 8)], attr=True),
                [self.ui.lineTipoCC, self.ui.lineHorasCC, self.ui.textNotasCC, self.ui.textExeCC] +
                self.gen_list('plainCC', simple_ranges=[(1, 8)], attr=True),
            ]
            return self.get_linetext(index, index_list[index])

    def gen_patterns(self, pattern_list, flag):
        names_list = []
        for pattern, ranges in pattern_list:
            if flag:
                names_list += self.gen_list(pattern, complex_ranges=ranges)
            else:
                names_list += self.gen_list(pattern, simple_ranges=ranges)

        return names_list

    def gen_list(self, base_name, simple_ranges=None, complex_ranges=None, attr=False):
        elements = []

        # Handle simple cases
        if simple_ranges:
            for single_range in simple_ranges:
                for i in range(single_range[0], single_range[1] + 1):
                    element_name = f"{base_name}{i}"
                    if attr:
                        elements.append(getattr(self.ui, element_name))
                    else:
                        elements.append(element_name)

        # Handle complex cases
        if complex_ranges:
            for part1 in range(complex_ranges[0][0], complex_ranges[0][1] + 1):
                for part2 in range(complex_ranges[1][0], complex_ranges[1][1] + 1):
                    element_name = f"{base_name}{part1}_{part2}"
                    if attr:
                        elements.append(getattr(self.ui, element_name))
                    else:
                        elements.append(element_name)

        return elements

    def add_suffixed_names(self, suffixes, templates):
        return [template.format(suffix) for suffix in suffixes for template in templates]

