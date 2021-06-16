import pandas as pd
import numpy as np
import os, sys, json, time

from project_data import *
from commands import *

def informationViewer (dic):
    # lines = ""
    # for d in dic:
    #     line = f"{d}     :{dic[d]}"
    #     lines += line + "\n"
    # print (lines)
    if type(dic) == dict:
        info = pd.DataFrame(dic,index=[0])
        print (info.T)
    if type(dic) == list:
        info = pd.DataFrame.from_dict(dic,)
        print (info)

# informationViewer (bim_projects_data[0])
# informationViewer(bim_projects_data)
# print(bim_projects_data)
# data = pd.DataFrame.from_dict(bim_projects_data)
# print(data)

class info_viewer ():
    def __init__(self) -> None:
        pass