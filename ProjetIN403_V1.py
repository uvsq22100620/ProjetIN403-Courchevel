###### 
## PROJET IN403 - Tout schuss a Courch !
## LE CORRE Camille, LEFEVRE Laura 
## LDDBI
######


### Import des librairies

import re

### Définition des variables globales

## Définition des dictionnaires


# Dictionnaire associant à chaque numéro de sommet un nom

sommets = {
    1 : "R_signal_",
    2 : "P_rochers-grandesbosses_1",
    3 : "B_rochers_1",
    4 : "B_rochers_2",
    5 : "TD_chapelets_",
    6 : "TF_ariondaz_",
    7 : "TF_granges_",
    8 : "P_granges-praline_1",
    9 : "P_carabosse-praline_1",
    10 : "P_carabosse-praline_2",
    11 : "TD_granges-stade_",
    12 : "TF_belvedere_",
    13 : "B_belvedere_1",
    14 : "TF_mickey_",
    15 : "V_courchevel-1650_",
    16 : "P_indiens-marquis_1",
    17 : "TF_steagathe_",
    18 : "P_indiens-pistebleue_1",
    19 : "TD_3vallees_",
    20 : "TF_marquis_",
    21 : "TF_3vallees_",
    22 : "TF_troika_",
    23 : "R_bosses_",
    24 : "TF_ptebosse_",
    25 : "B_praline_1",
    26 : "P_grandesbosses-praline_1",
    27 : "P_grandesbosses-pyramide_1",
    28 : "P_grandesbosses-pyramide_2",
    29 : "TF_combe_",
    30 : "P_montrusses-grandesbosses_",
    31 : "TF_rocmugnier_",
    32 : "TD_pyramide_",
    33 : "B_rocmugnier_1",
    34 : "P_montrusses-planmugnier_1",
    35 : "B_pyramide_1",
    36 : "P_montrusses-pyramide_1",
    37 : "TD_rocmerlet_",
    38 : "P_montrusses-pyramide_2",
    39 : "P_montrusses-planmugnier_2",
    40 : "TF_chanrossa-rocmerlet_",
    41 : "P_chanrossa-jeanpachod_1",
    42 : "TD_chanrossa-marmottes_",
    43 : "B_rocmugnier_2",
    44 : "B_rocmugnier_3",
    45 : "R_prameruel_",
    46 : "P_cavedescreux-mur-prameruel_1",
    47 : "P_altiport-mur_1",
    48 : "TD_suisses_",
    49 : "TF_gravelles_",
    50 : "P_laccreux-parkcity_1",
    51 : "P_parkcity-rama_1",
    52 : "P_laccreux-rama_1",
    53 : "B_rama_1",
    54 : "P_laccreux-rama_2",
    55 : "P_laccreux-parkcity-rama_1",
    56 : "TD_creuxnoirs_",
    57 : "P_creux-laccreux_1",
    58 : "P_rama-suisses-turcs_1",
    59 : "TF_aiguilledufruit_",
    60 : "P_suisses-turcs_1",
    61 : "R_vizelle_",
    62 : "P_creux-rochesgrises_1",
    63 : "B_rochesgrises_1",
    64 : "B_rochesgrises_2",
    65 : "TF_creuxnoirs_",
    66 : "B_rama_2",
    67 : "P_creux-rama_1",
    68 : "TF_saulire_",
    69 : "B_combesaulire_1",
    70 : "B_combesaulire_2",
    71 : "P_combepylones-combesaulire_1",
    72 : "P_combesaulire-m_1",
    73 : "P_combepylones-combesaulire_2",
    74 : "B_combesaulire_3",
    75 : "P_combesaulire-grandcouloir_1",
    76 : "B_combesaulire_4",
    77 : "P_combepylones-combesaulire_3",
    78 : "TF_rocherdelombre_",
    79 : "P_combepylones-combesaulire_4",
    80 : "TF_sources_",
    81 : "B_verdons_1",
    82 : "TD_saulire_",
    83 : "R_verdons_",
    84 : "B_verdons_2",
    85 : "P_biollayverdons-m_1",
    86 : "P_biollayverdons-m_2",
    87 : "B_m_1",
    88 : "TF_biollay-pralong_",
    89 : "P_biollay-biollayverdons_1",
    90 : "P_biollay-marquetty_1",
    91 : "B_biollay_1",
    92 : "B_pralong_1",
    93 : "P_altiport-pralong_1",
    94 : "B_pralong_2",
    95 : "TF_altiport_",
    96 : "TF_ferme_",
    97 : "TD_altiport-ferme_",
    98 : "TF_cospillot_",
    99 : "R_pralong_",
    100 : "P_biollay-titi_1",
    101 : "P_biollay-tit_2",
    102 : "TF_jardinalpin_",
    103 : "B_titi_1",
    104 : "TF_bellecote_",
    105 : "B_biollay_2",
    106 : "P_biollay-ryry_1",
    107 : "P_marquetty-ryry_1",
    108 : "P_marquetty-renard_1",
    109 : "P_biollay-renard_1",
    110 : "P_renard-titi_1",
    111 : "TD_cospillot_",
    112 : "T2_jardinalpin_",
    113 : "B_renard_1",
    114 : "TF_etoiles",
    115 : "T1_jardinalpin_",
    116 : "TD_etoiles_",
    117 : "TD_bellecote_",
    118 : "TD_jardin_alpin_",
    119 : "R_lac_",
    120 : "P_chenus-verdons_1",
    121 : "TD_rocherdelombre-sources_",
    122 : "P_renard-stadedescente-verdons_1",
    123 : "P_anemones-chenus-lozeest_1",
    124 : "P_renard-verdons_1",
    125 : "V_courchevel-1850_",
    126 : "TD_loze_",
    127 : "P_lozeest-jantzen_1",
    128 : "P_anemones-jantzen_1",
    129 : "P_anemones-chenus-lozeest_2",
    130 : "P_anemones-lacbleu-lozeest_1",
    131 : "P_lacbleu-lozeest_1",
    132 : "B_anemones_1",
    133 : "R_chenus_",
    134 : "TF_cretes_",
    135 : "R_loze_",
    136 : "TF_boucblanc_",
    137 : "B_doudumidi_1",
    138 : "TF_stade_",
    139 : "P_maumau-petitdou_1",
    140 : "TD_stade_",
    141 : "TD_jardindenfants_",
    142 : "P_maumau-proveres_1",
    143 : "TF_jardindenfants_",
    144 : "B_proveres_1",
    145 : "B_stade_1",
    146 : "P_proveres-stade_1",
    147 : "TF_roys_",
    148 : "TD_roys_",
    149 : "V_courchevel-1550_",
    150 : "TD_tovets_",
    151 : "P_deviation1550-doudumidi_1",
    152 : "P_brigues-deviation1550_1",
    153 : "TD_epicea_",
    154 : "TD_plantrey_",
    155 : "P_doudumidi-maumau_1",
    156 : "P_doudumidi-maumau_2",
    157 : "TF_praz_",
    158 : "P_doudumidi-maumau_3",
    159 : "TF_epicea_",
    160 : "B_doudumidi_2",
    161 : "P_doudumidi-jeanblanc_1",
    162 : "TD_cretes_",
    163 : "P_arollesboucblanc-lanches_1",
    164 : "TF_latania_",
    165 : "R_prazjuget_",
    166 : "B_doudeslanches_1",
    167 : "P_doudeslanches-lanches_1",
    168 : "B_doudeslanches_2",
    169 : "P_coldelaloze-doudeslanches_1",
    170 : "TF_coldelaloze-doudeslanches_",
    171 : "P_morettablanche-planfontaine_1",
    172 : "P_jockeys-murettes_1",
    173 : "P_morettablanche-murettes_1",
    174 : "TD_boucblanc_",
    175 : "TF_grosmurger_",
    176 : "B_folyeres_1",
    177 : "P_morettablanche-planfontaine_2",
    178 : "TD_grosmurger-latania_",
    179 : "V_latania-1400_",
    180 : "P_jockeys-murettes_2",
    181 : "V_courchevellepraz-1300_",
    182 : "B_brigues_1",
    183 : "B_brigues_2",
    184 : "P_brigues-jeanblanc_1",
    185 : "V_stbon-1100_",
    186 : "B_jeanblanc_1",
    187 : "TF_stade_",
    188 : "TD_combe_",
    }


# Dictionnaire associant à chaque sommet un tuple de ses successeurs

# on retient qu'il faut proposer les 2 pistes bleues entre 39 et 34 (plan mugnier et mont russes)

successeurs = {
            1 : (2, 5),
            2 : (3, 27, 28),
            3 : (4, 6),
            4 : (5),
            5 : (1, 10),
            6 : (4, 5, 7, 188),
            7 : (8, 21),
            8 : (9, 11),
            9 : (5, 10),
            10 : (11),
            11 : (13, 187),
            12 : (11, 13),
            13 : (15),
            14 : (15),
            15 : (6, 12, 14, 17, 20),
            16 : (15),
            17 : (16),
            18 : (17, 19),
            19 : (15, 21),
            20 : (8, 18),
            21 : (20, 23),
            22 : (179),
            23 : (1, 18, 20, 24),
            24 : (23, 45),
            25 : (23, 24),
            26 : (23, 25),
            27 : (6),
            28 : (27, 29),
            29 : (30, 33),
            30 : (26),
            31 : (28),
            32 : (29, 30, 33, 37),
            33 : (43),
            34 : (32),
            35 : (31, 32),
            36 : (35),
            37 : (36, 38, 40),
            38 : (36, 39),
            39 : (34),           # 2 pistes bleues possibles
            40 : (37, 41),
            41 : (42),
            42 : (40, 45, 61),
            43 : (44),
            44 : (45),
            45 : (31, 49, 59),
            46 : (45),
            47 : (46, 93),
            48 : (47, 61),
            49 : (46, 48),
            50 : (49),
            51 : (50, 52),
            52 : (50, 53),
            53 : (42),
            54 : (52, 53),
            55 : (51, 54, 56),
            56 : (54, 65),
            57 : (42, 56),
            58 : (55, 59, 60),
            59 : (55, 60),
            60 : (48),
            61 : (58, 69, 70),
            62 : (57),
            63 : (62),
            64 : (63),
            65 : (64),
            66 : (61, 67),
            67 : (62),
            68 : (66, 67, 69, 75),
            69 : (74),
            70 : (69, 71),
            71 : (72, 73),
            72 : (73, 87),
            73 : (74, 77),
            74 : (75),
            75 : (76),
            76 : (77, 78),
            77 : (79),
            78 : (79, 122),
            79 : (80),
            80 : (81),
            81 : (82, 84),
            82 : (68, 83),
            83 : (61, 82, 84, 107, 108),
            84 : (122),
            85 : (83),
            86 : (85, 89),
            87 : (85, 86),
            88 : (48, 89, 92),
            89 : (90),
            90 : (91, 107),
            91 : (101, 106),
            92 : (48, 93),
            93 : (94, 101),
            94 : (95, 97),
            95 : (46),
            96 : (97),
            97 : (95, 96, 98),
            98 : (97, 99),
            99 : (88, 98),
            100 : (99),
            101 : (100, 104),
            102 : (101, 105),
            103 : (100, 118),
            104 : (103, 110),
            105 : (109),
            106 : (102, 105),
            107 : (106, 108),
            108 : (109, 122),
            109 : (110, 119),
            110 : (113),
            111 : (98),
            112 : (102, 114),
            113 : (112, 119),
            114 : (116),
            115 : (112, 116),
            116 : (114, 124),
            117 : (104, 118),
            118 : (117, 115, 125),
            119 : (88, 133),
            120 : (124),
            121 : (78, 80, 120, 123),
            122 : (121),
            123 : (120, 127),
            124 : (125),
            125 : (83, 118, 126, 133, 141, 142),
            126 : (125, 135),
            127 : (126),
            128 : (123, 127),
            129 : (123, 128, 130),
            130 : (131),
            131 : (123),
            132 : (129, 130),
            133 : (129, 132, 134, 167, 170),
            134 : (135),
            135 : (126, 129, 136, 137, 161, 162),
            136 : (163),
            137 : (138, 160),
            138 : (139),
            139 : (140),
            140 : (125, 138, 156),
            141 : (125),
            142 : (144, 155),
            143 : (141),
            144 : (145, 147),
            145 : (146, 147),
            146 : (150),
            147 : (146, 148, 149),
            148 : (147),
            149 : (125),
            150 : (125),
            151 : (150),
            152 : (151, 184),
            153 : (152, 159),
            154 : (135, 153),
            155 : (151, 154),
            156 : (154, 155),
            157 : (156),
            158 : (139, 156),
            159 : (153, 158),
            160 : (158),
            161 : (160, 186),
            162 : (134, 161, 163),
            163 : (164),
            164 : (172, 174, 175),
            165 : (133, 170),
            166 : (165),
            167 : (163, 166),
            168 : (166, 167),
            169 : (133, 168),
            170 : (169),
            171 : (174),
            172 : (173, 180),
            173 : (177, 180),
            174 : (136, 173, 176, 177),
            175 : (174, 176),
            176 : (179),
            177 : (178, 179),
            178 : (164, 175),
            179 : (22, 178),
            180 : (181),
            181 : (157, 162),
            182 : (181, 185),
            183 : (181, 182),
            184 : (183),
            185 : (),           # pas de successeur
            186: (152, 184),
            187 : (11, 16, 18),
            188 : (26, 29),
            }

# Dictionnaire contenant les données du graphe
# Rappel : chaque arête est définie par ses 2 sommets, son type, sa longueur et son nom

graphe = {
        (1, 2, 'b') : [0.2, 'grandes bosses'],
        (1, 2, 'r') : [0.2, 'rochers'],
        (1, 5, 'r') : [2, 'chapelets'],
        (2, 3, 'r') : [1, 'rochers'],
        (2, 27, 'b') : [1, 'ariondaz'],
        (2, 28, 'b') : [0.7, 'grandes bosses'],
        (3, 4, 'r') : [0.2, 'rochers'],
        (3, 6, 'r') : [0.2, 'rochers'],
        (4, 5, 'r') : [1, 'rochers'],
        (5, 1, 'ts') : [2, 'chapelets'],
        (5, 10, 'v') : [1, 'praline'],
        (6, 4, 'r') : [0.2, 'rochers'],
        (6, 5, 'r') : [1, 'bel air'],
        (6, 7, 'b') : [0.5, 'ariondaz'],
        (6, 188, 'v') : [0.3, 'praline'],
        (7, 8, 'b') : [0.2, 'granges'],
        (7, 21, 'b') : [0.2, 'ariondaz'],
        (8, 9, 'v') : [0.2, 'praline'],
        (8, 11, 'b') : [0.6,'granges'],
        (9, 5, 'v') : [0.8, 'praline'],
        (9, 10, 'b') : [0.5, 'carabosse'],
        (10, 11, 'v') : [0.1, 'praline'],
        (11, 13, 'v') : [0.5, 'praline'],
        (11, 187, 'tf') : [0.5, 'stade'],
        (12, 11, 'v') : [0.5, 'belvédère'],
        (12, 13, 'v') : [0.3, 'belvédère'],
        (13, 15, 'v') : [1, 'belvédère'],
        (14, 15, 'c') : [0.3, 'zen'],
        (15, 6, 'tc') : [3.5, 'ariondaz'],
        (15, 12, 'rg') : [1.5, 'belvédère'],
        (15, 14, 'rg') : [0.3, 'mickey'],
        (15, 17, 'tf') : [0.7, 'ste agathe'],
        (15, 20, 'tf') : [2, 'marquis'],
        (16, 15, 'b') : [0.4, 'marquis'],
        (17, 16, 'b') : [0.2, 'indiens'],
        (18, 17, 'b') : [0.1, 'indiens'],
        (18, 19, 'b') : [0.8, 'piste bleue'],
        (19, 15, 'v') : [0.2, 'chemin'],
        (19, 21, 'ts') : [2, '3 Vallées'],
        (20, 8, 'v') : [0.1, 'praline'],
        (20, 18, 'b') : [1.5, 'piste bleue'],
        (21, 20, 'b') : [0.1, 'piste bleue'],
        (21, 23, 'b') : [0.1, 'ariondaz'],
        (22, 179, 'v') : [0.1, 'plan fontaine'],
        (23, 1, 'ts') : [2.1, 'signal'],
        (23, 18, 'b') : [1, 'indiens'],
        (23, 20, 'v') : [1, 'praline'],
        (23, 24, 'tf') : [0.6, 'pte bosse'],
        (24, 23, 'v') : [0.6, 'praline'],
        (24, 45, 'b') : [0.3, 'gravelles'],
        (25, 23, 'v') : [0.5, 'praline'],
        (25, 24, 'v') : [0.3, 'praline'],
        (26, 23, 'b') : [0.5, 'grandes bosses'],
        (26, 25, 'v') : [0.2, 'praline'],
        (27, 6, 'b') : [0.5, 'pyramide'],
        (28, 27, 'b') : [0.2, 'pyramide'],
        (28, 29, 'b') : [0.1, 'grandes bosses'],
        (29, 30, 'b') : [0.1, 'grandes bosses'],
        (29, 33, 'r') : [0.1, 'roc mugnier'],
        (30, 26, 'b') : [0.7, 'grandes bosses'],
        (31, 28, 'b') : [0.1, 'pyramide'],
        (32, 29, 'b') : [0.1, 'mont russes'],
        (32, 30, 'b') : [0.2, 'mont russes'],
        (32, 33, 'r') : [0.1, 'roc mugnier'],
        (32, 37, 'tf') : [1.5, 'pyramide'],
        (33, 43, 'r') : [0.7, 'roc mugnier'],
        (34, 32, 'b') : [0.1, 'mont russes'],
        (35, 31, 'b') : [0.8, 'pyramide'],
        (35, 32, 'b') : [0.8, 'pyramide'],
        (36, 35, 'b') : [0.4, 'pyramide'],
        (37, 36, 'b') : [0.3, 'pyramide'],
        (37, 38, 'b') : [0.2, 'mont russes'],
        (37, 40, 'ts') : [0.7, 'roc merlet'],
        (38, 36, 'b') : [0.1, 'mont russes'],
        (38, 39, 'b') : [0.4, 'mont russes'],
        (39, 34, 'b') : [0.7, 'mont russes ou plan mugnier'],
        (40, 37, 'r') : [0.7, 'roc merlet'],
        (40, 41, 'r') : [0.3, 'jean pachod'],
        (41, 42, 'r') : [1.7, 'jean pachod'],
        (41, 42, 'n') : [1.7, 'chanrossa'],
        (42, 40, 'ts') : [2.3, 'chanrossa'],
        (42, 45, 'r') : [1.5, 'creux'],
        (42, 61, 'ts') : [2.2, 'marmottes'],
        (43, 44, 'r') : [0.4, 'roc mugnier'],
        (44, 45, 'r') : [0.7, 'roc mugnier'],
        (45, 31, 'ts') : [2, 'roc mugnier'],
        (45, 49, 'ts') : [1.2, 'gravelles'],
        (45, 59, 'ts') : [2.4, 'aiguille du fruit'],
        (46, 45, 'b') : [0.5, 'prameruel'],
        (47, 46, 'r') : [1.1, 'mur'],
        (47, 93, 'b') : [0.6, 'altiport'],
        (48, 47, 'b') : [0.2, 'altiport'],
        (48, 61, 'ts') : [2.2, 'suisses'],
        (49, 46, 'r') : [1.2, 'cave des creux'],
        (49, 48, 'b') : [0.5, 'altiport'],
        (50, 49, 'r') : [0.4, 'park city'],
        (51, 50, 'r') : [0.5, 'park city'],
        (51, 52, 'r') : [0.2, 'rama'],
        (52, 50, 'r') : [0.5, 'lac creux'],
        (52, 53, 'r') : [0.4, 'rama'],
        (53, 42, 'r') : [0.2, 'rama'],
        (54, 52, 'r') : [0.2, 'lac creux'],
        (54, 53, 'r') : [0.4, 'rama'],
        (55, 51, 'r') : [0.4, 'park city'],
        (55, 54, 'r') : [0.4, 'rama'],
        (55, 56, 'r') : [0.5, 'rama'],
        (56, 54, 'r') : [0.5, 'lac creux'],
        (56, 65, 'ts') : [2, 'creux noirs'],
        (57, 42, 'r') : [1.5, 'creux'],
        (57, 56, 'r') : [0.7, 'lac creux'],
        (58, 55, 'r') : [1, 'rama'],
        (58, 59, 'n') : [0.8, 'turcs'],
        (58, 60, 'n') : [1, 'suisses'],
        (59, 55, 'r') : [0.5, 'park city'],
        (59, 60, 'n') : [0.3, 'turcs'],
        (60, 48, 'n') : [1.7, 'suisses'],
        (61, 58, 'r') : [0.3, 'rama'],
        (61, 69, 'r') : [0.2, 'combe saulire'],
        (61, 70, 'r') : [0.2, 'combe saulire'],
        (62, 57, 'r') : [0.9, 'creux'],
        (63, 62, 'r') : [0.7, 'roches grises'],
        (63, 62, 'n') : [0.5, 'roches grises'],
        (64, 63, 'r') : [0.5, 'roches grises'],
        (65, 64, 'r') : [0.2, 'roches grises'],
        (66, 61, 'r') : [0.2, 'rama'],
        (66, 67, 'r') : [0.2, 'rama'],
        (67, 62, 'r') : [1, 'creux'],
        (68, 66, 'r') : [0.3, 'rama'],
        (68, 67, 'r') : [0.3, 'creux'],
        (68, 69, 'r') : [0.6, 'combe saulire'],
        (68, 75, 'n') : [1.5, 'grand couloir'],
        (69, 74, 'r') : [0.6, 'combe saulire'],
        (70, 69, 'r') : [0.2, 'combe saulire'],
        (70, 71, 'r') : [0.1, 'combe saulire'],
        (71, 72, 'r') : [0.1, 'combe saulire'],
        (71, 73, 'n') : [0.3, 'combe pylones'],
        (72, 73, 'r') : [0.4, 'combe saulire'],
        (72, 87, 'n') : [1.2, 'm'],
        (73, 74, 'r') : [0.2, 'combe saulire'],
        (73, 77, 'n') : [1, 'combe pylones'],
        (74, 75, 'r') : [0.6, 'combe saulire'],
        (75, 76, 'r') : [0.3, 'combe saulire'],
        (76, 77, 'r') : [0.3, 'combe saulire'],
        (76, 78, 'r') : [0.3, 'combe saulire'],
        (77, 79, 'r') : [0.1, 'combe pylones'],
        (78, 79, 'r') : [0.1, 'combe saulire'],
        (78, 122, 'r') : [1.7, 'stade descente'],
        (79, 80, 'r') : [0.4, 'combe saulire'],
        (80, 81, 'v') : [0.1, 'verdons'],
        (81, 82, 'v') : [0.1, 'verdons'],
        (81, 84, 'v') : [0.2, 'verdons'],
        (82, 68, 'tp') : [2, 'saulire'],
        (82, 83, 'v') : [0.1, 'verdons'],
        (83, 61, 'tc') : [1.9, 'vizelle'],
        (83, 82, 'v') : [0.1, 'verdons'],
        (83, 84, 'v') : [0.2, 'verdons'],
        (83, 107, 'b') : [0.4, 'ryry'],
        (83, 108, 'v') : [0.6, 'renard'],
        (84, 122, 'v') : [0.8, 'verdons'],
        (85, 83, 'b') : [0.3, 'biollay verdons'],
        (86, 85, 'b') : [0.1, 'biollay verdons'],
        (86, 89, 'b') : [0.5, 'biollay verdons'],
        (87, 85, 'n') : [0.5, 'm'],
        (87, 86, 'n') : [0.4, 'm'],
        (88, 48, 'b') : [0.8, 'super pralong'],
        (88, 89, 'b') : [0.1, 'biollay'],
        (88, 92, 'b') : [0.3, 'pralong'],
        (89, 90, 'b') : [0.2, 'biollay'],
        (90, 91, 'b') : [0.4, 'biollay'],
        (90, 107, 'r') : [0.6, 'marquetty'],
        (91, 101, 'b') : [0.4, 'biollay'],
        (91, 106, 'b') : [0.4, 'biollay'],
        (92, 48, 'b') : [0.7, 'pralong'],
        (92, 93, 'b') : [0.6, 'pralong'],
        (93, 94, 'b') : [0.1, 'pralong'],
        (93, 101, 'b') : [0.6, 'altiport'],
        (94, 95, 'b') : [0.2, 'praméruel'],
        (94, 97, 'b') : [0.9, 'pralong'],
        (95, 46, 'b') : [1.2, 'praméruel'],
        (96, 97, 'c') : [0.4, 'zen'],
        (97, 95, 'tf') : [0.8, 'altiport'],
        (97, 96, 'tf') : [0.4, 'ferme'],
        (97, 98, 'c') : [0.2, 'chemin'],
        (98, 97, 'c') : [0.2, 'chemin'],
        (98, 99, 'c') : [0.1, 'chemin'],
        (99, 88, 'ts') : [2, 'pralong'],
        (99, 98, 'c') : [0.1, 'chemin'],
        (100, 99, 'v') : [0.3, "titi"],
        (101, 100, 'b') : [0.3, 'biollay'],
        (101, 104, 'v') : [0.3, 'titi'],
        (102, 101, 'v') : [0.1, 'titi'],
        (102, 105, 'b') : [0.2, 'biollay'],
        (103, 100, 'v') : [0.1, 'titi'],
        (103, 118, 'v') : [2, 'titi'],
        (104, 103, 'v') : [0.1, 'titi'],
        (104, 110, 'v') : [0.2, 'titi'],
        (105, 109, 'b') : [0.2, 'biollay'],
        (106, 102, 'b') : [0.1, 'ryry'],
        (106, 105, 'b') : [0.1, 'biollay'],
        (107, 106, 'b') : [0.7, 'ryry'],
        (107, 108, 'r') : [0.5, 'marquetty'],
        (108, 109, 'v') : [0.3, 'renard'],
        (108, 122, 'v') : [0.4, 'renard'],
        (109, 110, 'v') : [0.1, 'renard'],
        (109, 119, 'b') : [0.6, 'biollay'],
        (110, 113, 'v') : [0.3, 'renard'],
        (111, 98, 'rg') : [1.2, 'cospillot'],
        (112, 102, 'tc') : [1, 'jardin alpin'],
        (112, 114, 'v') : [0.1, 'renard'],
        (113, 112, 'v') : [0.1, 'renard'],
        (113, 119, 'v') : [0.3, 'renard'],
        (114, 116, 'v') : [0.3, 'renard'],
        (115, 112, 'tc') : [0.3, 'jardin alpin'],
        (115, 116, 'c') : [0.1, 'chemin'],
        (116, 114, 'rg') : [0.3, 'etoiles'],
        (116, 124, 'v') : [0.8, 'renard'],
        (117, 104, 'rg') : [1.6, 'bellecote'],
        (117, 118, 'c') : [0.2, 'chemin'],
        (118, 117, 'c') : [0.2, 'chemin'],
        (118, 115, 'tc') : [0.7, 'jardin alpin'],
        (118, 125, 'c') : [0.1, 'chemin'],
        (119, 88, 'ts') : [2.1, 'biollay'],
        (119, 133, 'ts') : [2, 'coqs'],
        (120, 124, 'v') : [0.5, 'verdons'],
        (121, 78, 'ts') : [1.5, "rocher de l'ombre"],
        (121, 80, 'ts') : [1, 'sources'],
        (121, 120, 'v') : [0.1, 'verdons'],
        (121, 123, 'v') : [0.3, 'verdons'],
        (122, 121, 'v') : [0.1, 'verdons'],
        (123, 120, 'r') : [0.3, 'chenus'],
        (123, 127, 'b') : [0.5, 'loze est'],
        (124, 125, 'v') : [0.4, 'verdons'],
        (125, 83, 'tc') : [2, 'verdons'],
        (125, 118, 'c') : [0.1, 'chemin'],
        (125, 126, 'c') : [0.1, 'chemin'],
        (125, 133, 'tc') : [2.2, 'chenus'],
        (125, 141, 'c') : [0.1, 'chemin'],
        (125, 142, 'b') : [0.1, 'proveres'],
        (126, 125, 'c') : [0.1, 'chemin'],
        (126, 135, 'ts') : [1.6, 'loze'],
        (127, 126, 'b') : [0.2, 'loze est'],
        (128, 123, 'b') : [0.5, 'anémones'],
        (128, 127, 'r') : [0.5, 'jantzen'],
        (129, 123, 'r') : [0.8, 'chenus'],
        (129, 128, 'b') : [0.7, 'anémones'],
        (129, 130, 'v') : [0.3, 'loze est'],
        (130, 131, 'b') : [0.3, 'lac bleu'],
        (130, 131, 'v') : [0.5, 'loze est'],
        (131, 123, 'v') : [0.6, 'loze est'],
        (132, 129, 'b') : [0.2, 'anémones'],
        (132, 130, 'b') : [0.3, 'anémones'],
        (133, 129, 'r') : [0.4, 'chenus'],
        (133, 132, 'b') : [0.3, 'anémones'],
        (133, 134, 'b') : [0.2, 'crêtes'],
        (133, 167, 'r') : [1.5, 'lanches'],
        (133, 170, 'ts') : [1.3, 'col de la loze'],
        (134, 135, 'b') : [0.2, 'crêtes'],
        (135, 126, 'r') : [1.8, 'loze'],
        (135, 129, 'v') : [0.5, 'loze est'],
        (135, 136, 'r') : [0.1, 'bouc blanc'],
        (135, 137, 'r') : [0.3, 'dou du midi'],
        (135, 161, 'n') : [0.8, 'jean blanc'],
        (135, 162, 'b') : [0.8, 'crêtes'],
        (136, 163, 'r') : [0.9, 'bouc blanc'],
        (137, 138, 'r') : [0.3, 'petit dou'],
        (137, 160, 'r') : [0.3, 'dou du midi'],
        (138, 139, 'r') : [0.6, 'petit dou'],
        (139, 140, 'v') : [0.3, 'maumau'],
        (140, 125, 'v') : [0.4, 'maumau'],
        (140, 138, 'ts') : [1, 'stade'],
        (140, 156, 'b') : [0.8, 'maumau'],
        (141, 125, 'c') : [0.1, 'chemin'],
        (142, 144, 'b') : [0.2, 'proveres'],
        (142, 155, 'v') : [0.8, 'maumau'],
        (143, 141, 'ts') : [0.6, "jardin d'enfants"],
        (144, 145, 'b') : [0.1, 'stade'],
        (144, 147, 'b') : [1, 'proveres'],
        (145, 146, 'b') : [0.6, 'stade'],
        (145, 147, 'b') : [0.5, 'tovets'],
        (146, 150, 'b') : [0.3, 'proveres'],
        (147, 146, 'b') : [0.4, 'proveres'],
        (147, 148, 'v') : [0.4, 'roys'],
        (147, 149, 'b') : [0.4, 'tovets'],
        (148, 147, 'rg') : [0.3, 'roys'],
        (149, 125, 'tc') : [1.2, 'grangettes'],
        (150, 125, 'ts') : [1.1, 'tovets'],
        (151, 150, 'r') : [0.4, 'déviation 1550'],
        (152, 151, 'r') : [0.9, 'déviation 1550'],
        (152, 184, 'r') : [0.6, 'brigues'],
        (153, 152, 'r') : [0.3, 'brigues'],
        (153, 159, 'ts') : [1, 'epicea'],
        (154, 135, 'ts') : [2.4, 'plantrey'],
        (154, 153, 'v') : [0.1, 'maumau'],
        (155, 151, 'r') : [0.8, 'dou du midi'],
        (155, 154, 'v') : [0.1, 'maumau'],
        (156, 154, 'b') : [0.1, 'maumau'],
        (156, 155, 'r') : [0.1, 'dou du midi'],
        (157, 156, 'b') : [0.4, 'maumau'],
        (158, 139, 'v') : [0.7, 'maumau'],
        (158, 156, 'r') : [0.8, 'dou du midi'],
        (159, 153, 'v') : [1, 'tothor'],
        (159, 158, 'v') : [0.3, 'maumau'],
        (160, 158, 'r') : [0.5, 'dou du midi'],
        (161, 160, 'r') : [0.5, 'dou du midi'],
        (161, 186, 'n') : [1.3, 'jean blanc'],
        (162, 134, 'ts') : [1.1, 'crêtes'],
        (162, 161, 'r') : [0.1, 'dou du midi'],
        (162, 163, 'b') : [0.6, 'arolles'],
        (163, 164, 'b') : [0.5, 'arolles'],
        (163, 164, 'r') : [0.5, 'bouc blanc'],      ####WE GOT A PB
        (164, 172, 'n') : [0.7, 'jockeys'],
        (164, 174, 'r') : [1, 'bouc blanc'],
        (164, 175, 'b') : [1, 'folyères'],
        (165, 133, 'tf') : [1.8, 'praz juget'],
        (165, 170, 'ts') : [1.4, 'dou des lanches'],
        (166, 165, 'n') : [0.4, 'dou des lanches'],
        (167, 163, 'r') : [0.4, 'lanches'],
        (167, 166, 'n') : [0.2, 'dou des lanches'],
        (168, 166, 'n') : [0.3, 'dou des lanches'],
        (168, 167, 'n') : [0.2, 'dou des lanches'],
        (169, 133, 'b') : [0.7, 'col de la loze'],
        (169, 168, 'n') : [1, 'dou des lanches'],
        (170, 169, 'b') : [0.6, 'col de la loze'],
        (171, 174, 'r') : [0.7, 'moretta blanche'],
        (172, 173, 'r') : [0.7, 'murettes'],
        (172, 180, 'n') : [1.2, 'jockeys'],
        (173, 177, 'v') : [1.7, 'plan fontaine'],
        (173, 180, 'r') : [1.1, 'murettes'],
        (174, 136, 'tf') : [2, 'bouc blanc'],
        (174, 173, 'v') : [0.4, 'plan fontaine'],
        (174, 176, 'b') : [0.2, 'folyères'],
        (174, 177, 'r') : [1, 'moretta blanche'],
        (175, 174, 'b') : [0.2, 'folyères'],
        (175, 176, 'b') : [0.3, 'folyères'],
        (176, 179, 'b') : [1.8, 'folyères'],
        (177, 178, 'r') : [0.7, 'moretta blanche'],
        (177, 179, 'v') : [1, 'plan fontaine'],
        (178, 164, 'tc') : [2.5, 'la tania'],
        (178, 175, 'tf') : [1.6, 'gros murger'],
        (179, 22, 'tf') : [0.3, 'troika'],
        (179, 178, 'v') : [0.4, 'plan fontaine'],    #a verifier pour le nom
        (180, 181, 'r') : [0.8, 'murettes'],
        (181, 157, 'tc') : [2.4, 'praz'],
        (181, 162, 'tc') : [2.1, 'forêt'],
        (182, 181, 'r') : [0.9, 'brigues'],
        (182, 185, 'r') : [2, 'saint bon'],
        (183, 181, 'r') : [0.8, 'amoureux'],
        (183, 182, 'r') : [0.3, 'brigues'],
        (184, 183, 'r') : [0.4, 'brigues'],
        (186, 152, 'r') : [0.4, 'deviation 1550'],
        (186, 184, 'n') : [0.8, 'jean blanc'],
        (187, 11, 'r') : [0.6, 'stade'],
        (187, 16, 'b') : [1.1, 'marquis'],
        (187, 18, 'b') : [1, 'piste bleue'],
        (188, 26, 'v') : [0.1, 'praline'],
        (188, 29, 'v') : [0.9, 'combe']
        }


# Dictionnaire des temps de descente des pistes en fonction de leur couleur et du niveau du skieur
# Le 1er élément du tuple correspond au temps pour un skieur de niveau débutant,
# le 2ème élement pour un skieur de niveau intermédiaire et le dernier pour un skieur téméraire 

temps_pistes = {
        'v' : (4.5, 3, 2),      # piste verte
        'b' : (8, 4, 2),        # piste bleue
        'r' : (12.5, 5, 2),     # piste rouge
        'n' : (24.5, 7, 2)      # piste noire
        }

# Dictionnaire des temps des remontées mécaniques

temps_remontees = {
        'temps_moyen_attente' : 5,
        'tp' : 0.5,     # téléphérique
        'tc' : 1,       # télécabine
        'ts' : 1.5,     # télésiège
        'tf' : 2,       # téléski
        'rg' : 2,       # remontée gratuite
        'c' : 3         # à pied
        }


## Définition des autres variables

niveau_skieur = 0


### Fonctions pour trouver le plus court chemin (algorithme de Dijkstra)


def calculTemps(sA, sB):
    ''' Calcule le temps nécessaire au skieur pour aller de sA à sB'''

    global graphe, niveau_skieur, temps_pistes, temps_remontees
    
    # On cherche dans le dictionnaire les informations concernant l'arc (sA, sB)
    for key in graphe.keys():
        if key[0] == sA and key[1] == sB:
            arc = (key, graphe[key])
            type_arc = arc[0][2]        # le type d'un arc est la couleur de la piste ou le type de remontée mécanique
            longueur_arc = arc[1][0]
    
            if type_arc in temps_pistes:
                # s'il s'agit d'une piste, le temps est calculé en fonction de
                # sa couleur, de sa longueur et du niveau du skieur
                temps = longueur_arc * temps_pistes[type_arc][niveau_skieur]
            else:
                if type_arc == 'c':
                    # s'il s'agit d'un arc de type chemin (à pied), il n'y a pas de temps d'attente
                    temps = longueur_arc * temps_remontees['c']     
                else:
                    # s'il s'agit d'une remontée mécanique, le temps est calculé en fonction du
                    # temps moyen d'attente, du type de remontée et de sa longueur
                    temps = temps_remontees['temps_moyen_attente'] + (longueur_arc * temps_remontees[type_arc])

            return temps 


def algoDijkstra(dict_sommets, dict_successeurs, dict_graphe, s_depart, s_arrivee):
    ''' Fonction réalisant l'algorithme de Dijkstra afin de trouver le plus court 
        chemin entre les sommets s_depart et s_arrivee dans le graphe représenté
        dans le dictionnaire dict_graphe'''


    # Création des listes
    taille_tableau = len(dict_sommets)
    tableau = [0 for k in range(taille_tableau + 1)]

    sommets_marques = [s_depart]        # on ajoutera un par un les sommets dans cette liste une fois qu'ils on été marqués

    s = s_depart
    for i in range(taille_tableau):
        suc = list(dict_successeurs[s])
        for sommet in suc:
            nv_temps = calculTemps(s, sommet)
            #print(tableau[sommet], tableau)
            if (nv_temps < tableau[sommet]) or (tableau[sommet] == 0):
                tableau[sommet] = nv_temps
            #elif:
                # si égal
        
        # Recherche du prochain sommet à traiter
        l_candidats = []
        for k in range(len(tableau)):
            if (tableau[k] != 0) and (k not in sommets_marques):
                l_candidats.append(tableau[k])
        s = tableau.index(min(l_candidats))
        if s not in sommets_marques:
            sommets_marques.append(s)

        
    return sommets_marques


# Quand on demande au skieur son niveau, on stocke le résultat dans niveau_skieur, qui est une variable globale.
# Il peut être débutant (0), intermédiaire (1) ou bien téméraire (2)


### Fonction pour donner l'itinéraire au skieur


def recupNomsFromSommet(nom_s):
    ''' Récupère le nom de la ou des pistes ou remontées mécaniques
        à partir du nom du sommet'''
   
    while nom_s[0] != '_':     # suppression de la ou des lettres majuscules indiquant le type du sommet:
        nom_s = nom_s[1:]
    nom_s = nom_s[1:]

    # Création d'une regex récupérant les noms des pistes ou des remontées :
    # on veut récupérer ce qui est entouré des caractères '-' et/ou de '_'
    regex = re.compile("[-_]?([A-Za-z0-9]+)[-_]")

    return regex.findall(nom_s)

