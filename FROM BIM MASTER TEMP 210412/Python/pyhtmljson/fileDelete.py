import os, sys, json
import pandas as pd

class FileDelete():
    def __init__(self,jsonPathSorted,deleteExts) -> None:
        #------------------------------------------------------#
        # LOAD DỮ LIỆU JSON THÀNH PANDAS DATAFRAME
        #------------------------------------------------------#
        self.data = pd.read_json(jsonPathSorted)
        self.deleteExts = deleteExts
    def delete(self):
        for i in self.data.index:
            if self.data['File Extension'][i] in self.deleteExts:
                try:
                    os.remove(self.data['Full Path'][i])
                except:
                    pass

# askDir = input("Đường dẫn:")
# jsonPathSorted = askDir + "\\fileManager.json"
# deleteExts = ['bak', 'zip', 'rar', 'pcp'
# , 'db', 'mpp', 'log', 'mat', 'rws', 'slog', 'dat'
# , 'vrmesh', 'tmp', 'vrlmap', 'vrmap', 'eps'
# , 'dropbox', 'ini', 'ctb', '7z', 'pc3', 'fmp', 'fas', 'dwl', 'err', 'skb']

# exts =['dwg', 'dwf','rvt', 'rfa', 'rte', 'skp','pdf', 'json', 'txt', 'xls', 'xlsx', 'xlsm', 'doc' , 'docx', 'ai', 'tif','jpg','png', 'gif','bmp','psd', 'jpeg', 'tga', 'ies', 'max']
# detroyer = FileDelete(jsonPathSorted,deleteExts)
# detroyer.delete()

def deleteZeroSizeFolder(dirpath):
    # print(os.listdir(dirpath))
    for d in os.listdir(dirpath):
        path = dirpath+"\\"+d
        stat = os.stat(path)
        size = round((float(stat.st_size)),3)     
        print(f"{path} : {size}")
        
        if size == 0:
            try:           
                os.remove(path)
                print("---Thành công xóa thư mục Zero size: ",path)
            except Exception as ex:
                print(ex)
                pass



dirpath = input("Đường dẫn:")
deleteZeroSizeFolder(dirpath)