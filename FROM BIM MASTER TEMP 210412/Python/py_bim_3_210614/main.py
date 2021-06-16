
import os, sys, json
import pandas as pd
import numpy as np

from cad_data_handler import *
from project_data import *
from project_editor import *
from project_viewer import *
from commands import *
from utilities import *

def main():
    bim_dir = input("---Vui lòng nhập đường dẫn tới Kho dữ liệu BIM: ")

    #----------------------------------------------------------------#
    # LỜI CHÀO
    #----------------------------------------------------------------#
    program_version = "1.0 - 14/06/2021"
    welcome_promp = f"""
    #----------------------------------------------------------------#
        CHÀO MỪNG ĐẾN CHƯƠNG TRÌNH : MÔ HÌNH THÔNG TIN TÒA NHÀ
            Version :   {program_version}
            Author  :   tvpduy
    #----------------------------------------------------------------#"""
    print(welcome_promp)
    spinWaiting()
    bim_projects_database = bim_projects_data(bim_dir)
    #----------------------------------------------------------------#
    # HỎI ? DỰ ÁN MỚI ?
    #----------------------------------------------------------------#
    isNewProject = input(f"""
    <ASK>           :   BẠN MUỐN TẠO DỰ ÁN MỚI hay TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI??
    1   TẠO DỰ ÁN MỚI
    2   TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI
    3   THOÁT
    <IN>   :   """)

    if isNewProject == "1":
        print("---Bạn đã chọn TẠO DỰ ÁN MỚI, Template dự án mới đang được TẢI...")
        spinWaiting()
        project_number = input("---Vui lòng chọn Mã dự án muốn tạo mới:<IN> ")
        print(f"---Bạn đã chọn TẠO DỰ ÁN MỚI với Mã {project_number} --- Đang kiểm tra với Cơ sở dữ liệu Dự án Đã tồn tại")
        spinWaiting()
        
        flag_exist = [project_number != proj['ProjectNumber'] for proj in bim_projects_database]
        # print(flag_exist)
        if False in flag_exist:
            print(f"<--!--> MÃ DỰ ÁN ĐÃ TỒN TẠI, vui lòng đặt lại mã khác <--!-->")
            #do something
        else:
            project_creator = projectCreator(bim_dir,project_number)
            project_creator.start()
            project_creator.end()

    if isNewProject == "2":
        print("---Bạn đã chọn TRUY CẬP VÀO DỰ ÁN ĐÃ TỒN TẠI, Cơ sở dữ liệu dự án đang được TẢI...")    
        spinWaiting()
        print("---Danh sách các dự án: ",[proj['ProjectNumber'] for proj in bim_projects_database])
        informationViewer (bim_projects_database)        
        project_number = input("---Vui lòng chọn Mã dự án muốn truy cập:<IN> ")
        project = [proj for proj in bim_projects_database if proj['ProjectNumber'] == project_number][0]
        project_name = project['ProjectName']
        print(f"---Bạn đã chọn dự án {project_number} - {project_name} --- Dữ liệu dự án đang được TẢI...")
        spinWaiting()
        informationViewer (project)

        project_editor()
        pass
    if isNewProject == "3":
        print(f"---Bạn đang thoát chương trình, hy vọng bạn hài lòng với việc sử dụng thông tin từ chương trình này...")    
        spinWaiting()
        quit()

try:
    main()
except KeyboardInterrupt:
    print("Bạn đang thoát chương trình ...")
    spinWaiting()
    quit()