import pandas as pd
import numpy as np
import os, sys, json, time

from project_data import *
from project_viewer import *
from commands import *

class projectCreator ():
    def __init__ (self,bim_dir,project_number):
        self.bim_dir = bim_dir
        self.project_number = project_number
        self.project_data = project_info_template( self.bim_dir)
        self.project_data["ProjectNumber"] = self.project_number
    def start(self):
        print("---Tiến trình khai báo thông tin dự án (Ctrl + 1 trở về Main menu)")
        spinWaiting()
        # self.project_name = input("Project Name: ")
        # self.project_client = input("Project Client: ")
        # self.project_address = input("Project Address: ")
        # self.project_scale = input("Project Scale: ")
        # self.project_type = input("Project Type: ")
        # self.project_duration = input("Project Duration: ")
        # self.project_data["ProjectName"] = self.project_name
        # self.project_data["ProjectClient"] = self.project_client
        # self.project_data["ProjectAddress"] = self.project_address
        # self.project_data["ProjectScale"] = self.project_scale
        # self.project_data["ProjectType"] = self.project_type
        # self.project_data["ProjectDuration"] = self.project_duration
        for d in self.project_data:
            if d != "ProjectNumber":
                self.project_data[d] = input(f"{self.project_data.get(d)}: ")

        askContinue = input("---Bạn muốn quay lại khai báo (y/n):<IN> ").lower()
        if askContinue == "y":
            spinWaiting()
            self.start()
        else:
            spinWaiting()
            print(f"---Bạn đã hoàn tất khai báo thông tin dự án mới:")
            informationViewer (self.project_data)
            pass

    def end(self):
        askUploadProject = input("---Bạn có muốn Tải dữ liệu dự án Mới lên Cơ sở dữ liệu dự án BIM (y/n):<IN> ").lower()
        if askUploadProject == "y":
            print(f"---Dự án mới đang được cập nhật dữ liệu vào Cơ sở dữ liệu dự án ...")
            # timeCreated = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime(time.time()))
            #function
            spinWaiting()
            writeInfo(self.bim_dir,self.project_data,"update")
            # print(f"---Thành công cập nhật Cơ sở dữ liệu dự án , tại: {timeCreated}")


def writeInfo(bim_dir,dic,file_name):
    data_path = bim_dir + "\\_wip\\" + file_name + "-"+time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))+".json"
    with open(data_path,'w') as jfw:
        jfw.write(json.dumps(dic,indent=4,sort_keys=True))
    print("---Thành công ghi dữ liệu, --> Chờ dữ liệu được Duyệt, và Merge với Cơ sở dữ liệu BIM")


class project_editor():
    def __init__(self) -> None:
        pass



