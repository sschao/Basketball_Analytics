import pandas as pd
import numpy as np
import csv
from PIL import Image
from PIL import ImageDraw
import shutil


class Bracket:
    def __init__(self, bracketm, pmatrix):
        self.bracket = pd.read_csv(bracketm)
        p = pd.read_csv(pmatrix)
        self.teams = list(p.columns.values)
        self.bracket['Teams'] = np.array(self.teams)
        self.bracket = self.bracket[['Teams', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6']]
        self.matrix_list = [[], [], [], [], [], [], []]
        self.bracket_list()
        self.csvData = [['Round of 64', 'Round of 32', 'Sweet Sixteen', 'Elite Eight', 'Final Four',
                    'Championship', 'Champion']]
        self.create_csv('Bracket.csv')
        self.make_bracket('Bracket02.jpg')

    def bracket_list(self):
        for index, row in self.bracket.iterrows():
            if row['x6'] == 1:
                self.is_1(row['Teams'])
            elif row['x5'] == 1:
                self.is_2(row['Teams'])
            elif row['x4'] == 1:
                self.is_4(row['Teams'])
            elif row['x3'] == 1:
                self.is_8(row['Teams'])
            elif row['x2'] == 1:
                self.is_16(row['Teams'])
            elif row['x1'] == 1:
                self.is_32(row['Teams'])
            else:
                self.is_64(row['Teams'])

    def is_1(self, team):
        self.matrix_list[6].append(team)
        self.matrix_list[5].append(team)
        self.matrix_list[4].append(team)
        self.matrix_list[3].append(team)
        self.matrix_list[2].append(team)
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_2(self, team):
        self.matrix_list[5].append(team)
        self.matrix_list[4].append(team)
        self.matrix_list[3].append(team)
        self.matrix_list[2].append(team)
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_4(self, team):
        self.matrix_list[4].append(team)
        self.matrix_list[3].append(team)
        self.matrix_list[2].append(team)
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_8(self, team):
        self.matrix_list[3].append(team)
        self.matrix_list[2].append(team)
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_16(self, team):
        self.matrix_list[2].append(team)
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_32(self, team):
        self.matrix_list[1].append(team)
        self.matrix_list[0].append(team)

    def is_64(self, team):
        self.matrix_list[0].append(team)

    def create_csv(self, name):
        """Creates a csv 'name' that helps visualize bracket"""
        for team in self.teams:
            if team in self.matrix_list[6]:
                self.csvData.append([team, team, team, team, team, team, team])
            elif team in self.matrix_list[5]:
                self.csvData.append([team, team, team, team, team, team, None])
            elif team in self.matrix_list[4]:
                self.csvData.append([team, team, team, team, team, None, None])
            elif team in self.matrix_list[3]:
                self.csvData.append([team, team, team, team, None, None, None])
            elif team in self.matrix_list[2]:
                self.csvData.append([team, team, team, None, None, None, None])
            elif team in self.matrix_list[1]:
                self.csvData.append([team, team, None, None, None, None, None])
            else:
                self.csvData.append([team, None, None, None, None, None, None])

        with open(name, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.csvData)

        csvFile.close()

    def make_bracket(self, name, empty_bracket='empty_bracket.jpg'):
        shutil.copy(empty_bracket, name)
        img = Image.open(name)
        draw = ImageDraw.Draw(img)

        # Slots are the coordinates to put each team
        # Regions W, X, Y, Z
        slots = {1:  (30, 370), # W1
         2: (30, 388),
         3: (30, 406),
         4: (30, 424),
         5: (30, 442),
         6: (30, 460),
         7: (30, 478),
         8: (30, 496),
         9: (30, 514),
         10: (30, 532),
         11: (30, 550),
         12: (30, 567),
         13: (30, 586),
         14: (30, 604),
         15: (30, 622),
         16: (30, 640),
         17: (30, 38),# X1
         18: (30, 55),
         19: (30, 74),
         20: (30, 92),
         21: (30, 110),
         22: (30, 128),
         23: (30, 146),
         24: (30, 164),
         25: (30, 182),
         26: (30, 199),
         27: (30, 218),
         28: (30, 236),
         29: (30, 254),
         30: (30, 272),
         31: (30, 290),
         32: (30, 308),
         33: (815, 370),# Y1
         34: (815, 388),
         35: (815, 406),
         36: (815, 424),
         37: (815, 442),
         38: (815, 460),
         39: (815, 478),
         40: (815, 496),
         41: (815, 514),
         42: (815, 532),
         43: (815, 550),
         44: (815, 567),
         45: (815, 586),
         46: (815, 604),
         47: (815, 622),
         48: (815, 640),
         49: (815, 38),# Z1
         50: (815, 55),
         51: (815, 74),
         52: (815, 92),
         53: (815, 110),
         54: (815, 128),
         55: (815, 146),
         56: (815, 164),
         57: (815, 182),
         58: (815, 199),
         59: (815, 218),
         60: (815, 236),
         61: (815, 254),
         62: (815, 272),
         63: (815, 290),
         64: (815, 308),
         65: (155, 379),# W2
         66: (155, 415),
         67: (155, 451),
         68: (155, 487),
         69: (155, 523),
         70: (155, 559),
         71: (155, 595),
         72: (155, 631),
         73: (155, 47),# X2
         74: (155, 83),
         75: (155, 119),
         76: (155, 155),
         77: (155, 191),
         78: (155, 227),
         79: (155, 263),
         80: (155, 299),
         81: (735, 379),# Y2
         82: (735, 415),
         83: (735, 451),
         84: (735, 487),
         85: (735, 523),
         86: (735, 559),
         87: (735, 595),
         88: (735, 631),
         89: (735, 47),# Z2
         90: (735, 83),
         91: (735, 119),
         92: (735, 155),
         93: (735, 191),
         94: (735, 227),
         95: (735, 263),
         96: (735, 299),
         97: (232, 397),# W3
         98: (232, 469),
         99: (232, 541),
         100: (232, 613),
         101: (232, 65),# X3
         102: (232, 137),
         103: (232, 209),
         104: (232, 281),
         105: (668, 397),# Y3
         106: (668, 469),
         107: (668, 541),
         108: (668, 613),
         109: (668, 65),# Z3
         110: (668, 137),
         111: (668, 209),
         112: (668, 281),
         113: (298, 432),# W4
         114: (298, 576),
         115: (298, 100),# X4
         116: (298, 244),
         117: (601, 432),# Y4
         118: (601, 576),
         119: (601, 100),# Z4
         120: (601, 244),
         121: (358, 504),# W5
         122: (358, 172),# X5
         123: (540, 504),# Y5
         124: (540, 172),# Z5
         125: (420, 457),# WX6
         126: (435, 219),# YZ6
         127: (435, 339) # CH
            }

        added = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        columns = list(self.csvData)
        copy_columns = columns[:]
        del copy_columns[0]
        for result in copy_columns:
            for index in range(len(result)):
                if result[index] is None:
                    break
                else:
                    if index == 0:
                        point = slots[1 + added[1]]
                        added[1] += 1
                    elif index == 1:
                        point = slots[65 + added[2]]
                        added[2] += 1
                    elif index == 2:
                        point = slots[97 + added[3]]
                        added[3] += 1
                    elif index == 3:
                        point = slots[113 + added[4]]
                        added[4] += 1
                    elif index == 4:
                        point = slots[121 + added[5]]
                        added[5] += 1
                    elif index == 5:
                        point = slots[125 + added[6]]
                        added[6] += 1
                    else:
                        point = slots[127]
                    draw.text(point, result[index], (0, 0, 0))
        img.save('Bracket02.jpg')




if __name__ == '__main__':
    b = Bracket('ExampleBracket2018.csv', 'P2018.csv')


