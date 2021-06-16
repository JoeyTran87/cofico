import pandas as pd
import numpy as np
import os, sys, json
"""
---IN: DỮ LIỆU DẠNG BẢNG TỪ AUTOCAD (.csv, .txt, .xls)
---OUT: 
"""
#DATA CAD-MÓNG
class handleCadData_txt():
    def __init__(self):
        pass
    def start(self):
        self.cad_dat_path = input("---File Txt: ")#r"R:\BimESC\01_PROJECTS\MARUBENI SOLUBE\02-WIP 2\MARS-S-ZZ-ZZ-FD-FP-FOUNDATION FLOOR PLAN.txt"
        self.cad_dat = pd.read_csv(self.cad_dat_path, delimiter = "\t")
        print(self.cad_dat)
        self.cad_col_name = 'Value'
        self.cad_name_dic = {}
        for name in self.cad_dat[self.cad_col_name]:
            self.cad_name_dic[name] = ""

        print([n for n in self.cad_name_dic])
        print(" ".join([n for n in self.cad_name_dic]))
        print(len(self.cad_name_dic))

        self.cad_txt_file_name = input("---Tên file .txt (output): ")
        self.cad_txtpath = self.cad_dat_path[:len(self.cad_dat_path)-len(self.cad_dat_path.split("\\")[-1])]+ self.cad_txt_file_name+".txt"
        print(self.cad_txtpath)

        with open(self.cad_txtpath,'w') as cdf:
            cdf.write("\n".join([n for n in self.cad_name_dic]))
            print(f"--Thành công OUT txt: {self.cad_txtpath}")
        return self.cad_name_dic

# cad_FD_dat_path = r"R:\BimESC\01_PROJECTS\MARUBENI SOLUBE\02-WIP 2\MARS-S-ZZ-ZZ-FD-FP-FOUNDATION FLOOR PLAN.txt"
# cad_FD_dat = pd.read_csv(cad_FD_dat_path, delimiter = "\t")
# print(cad_FD_dat)
# cad_FD_col_name = 'Value'
# cad_FD_name_dic = {}
# for name in cad_FD_dat[cad_FD_col_name]:
#     cad_FD_name_dic[name] = ""

# print([n for n in cad_FD_name_dic])
# print(" ".join([n for n in cad_FD_name_dic]))
# print(len(cad_FD_name_dic))

# cad_txtpath = cad_FD_dat_path[:len(cad_FD_dat_path)-len(cad_FD_dat_path.split("\\")[-1])]+"cad_FD_name"+".txt"
# print(cad_txtpath)

# with open(cad_txtpath,'w') as FD_f:
#     FD_f.write("\n".join([n for n in cad_FD_name_dic]))
#     print(f"--Thành công ghi txt: {cad_txtpath}")
