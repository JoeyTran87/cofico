import pandas as pd
import numpy as np
import os, sys, json



# print(bim_projects_data)
def bim_projects_data(bim_dir):
    data = {}
    project_data_file_path = bim_dir+"\\"+"bim_projects_data.json"
    with open(project_data_file_path,'r',encoding='utf-8') as jdf:
        data =  json.loads(jdf.read(),)
    return data

def project_info_template(bim_dir):
    #project_info_template = {}
    data = {}
    project_info_file_path = bim_dir+"\\"+"_template\\project_info_template.json"
    with open(project_info_file_path,'r',encoding='utf-8') as jf:
        data =  json.loads(jf.read(),)#json.dumps(jf.read()),)
    return data

# print(len([project_info_template()]*4))
# print(type([project_info_template()]) == list)



