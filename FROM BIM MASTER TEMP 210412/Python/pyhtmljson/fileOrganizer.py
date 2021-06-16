import os, shutil,time
import fileExplorer
from fileExplorer import *
# print(fileExplorer().exts)

dirpath = input("Đường dẫn ROOT:")#r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_html_json\organizer"#r"C:\Users\tvpduy\py_html_json\organizer"
childLevel = int(input("Subfolder mode: ")) # 0 = ROOT
listExt = []
exts = fileExplorer().exts
needExts = fileExplorer().needExts#['dwg', 'dwf','rvt', 'rfa', 'rte', 'skp','pdf', 'json', 'txt','csv','xml', 'xls', 'xlsx', 'xlsm', 'doc' , 'docx', 'ai', 'tif','jpg','png', 'gif','bmp','psd', 'jpeg', 'tga', 'ies', 'max']

#-------------------------------------------------#
# TẠO FOLDER CHỨA CÁC LOẠI ĐUÔI FILE TRONG TỪNG CHILD CỦA ROOT
#-------------------------------------------------#
def createEXTfolders (dirpath,needExts):
    for e in needExts:
        try:
            extFolderDir = dirpath + "\\" + e.upper()
            if not os.path.exists(extFolderDir):
                os.mkdir(extFolderDir)
        except:
            pass
    print("---Hoàn tất tạo Folder chứa tập tin")
def createEXTfolders2 (extFolderDir):
    try:
        if not os.path.exists(extFolderDir):
            os.mkdir(extFolderDir)
            print("---Hoàn tất tạo Folder: ",extFolderDir)
    except:
        pass
    
def handleFiles(newFp,newDir,fp,copyFp):    
    if not os.path.exists(newFp): # NẾU FILE CHƯA TỒN TAI --> THỰC HIEN COPY TẬP TIN + THÔNG TIN NGÀY MODIFIED CUỐI CÙNG
        if os.path.exists(newDir):
            try:
                modTimeNameField = fp.split("\\")[-1].split("-")[-1].split(".")[0]
                if len(modTimeNameField) == 12:
                    newFp = copyFp                    
            finally:
                shutil.copy(fp,newDir)
                os.rename(copyFp,newFp)
                try:
                    os.remove(fp)
                except:
                    pass

def deleteZeroSizeFolder(dirpath):
    pass
def organizer(dirpath):
    flagIsDir = False
    if os.path.isdir(dirpath):
        flagIsDir = True
        print (f"---Thư mục có tồn tại {dirpath}")
    if flagIsDir:
        # createEXTfolders (dirpath,exts)
        for (path,dir,files) in os.walk(dirpath):
            try:            
                for f in files:
                    try:
                        ext = f.split(".")[-1] # ĐUÔI FILE - EXTENSION   
                        prp = path.split("\\")[-2]# TÊN FOLDER CHỨA (PARENT)        
                        flagNoNeed = prp == ext.upper()
                        fp = path + "\\" + f # FULL TÊN FILE + PATH
                    # if ext.lower() in needExts.lower() and flagNoNeed == False:                   
                        
                        nfn = f[:-len(ext)-1]+"-"+time.strftime("%y%m%d%H%M%S",time.localtime(float(os.stat(fp).st_mtime)))+"."+ext # TÊN MỚI + THỜI GIAN LƯU LAST
                        newDir = dirpath + "\\" + ext.upper() #TÊN FOLDER MỚI THEO EXT
                        createEXTfolders2 (newDir) # TAO FOLDER
                        copyFp = newDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
                        newFp =  newDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
                        if flagNoNeed == False: # NẾU FOLDER DANG CHỨA KHÔNG PHẢI TÊN DUÔI FILE UPPER
                            handleFiles(newFp,newDir,fp,copyFp)
                        else:
                            pass

                    # else:
                    except Exception as exx:
                        print(f"======LỖI: {exx}")  
                        if not "are the same file" in f"{exx}":
                            unsortDir = dirpath + "\\" + "UNSORT"
                            createEXTfolders2 (unsortDir)
                            copyFp = unsortDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
                            newFp =  unsortDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
                            handleFiles(newFp,unsortDir,fp,copyFp)
                        else:
                            pass
                    finally:
                        pass

            except Exception as ex:
                print(f"======LỖI: {ex}")
                pass

if childLevel == 0:
    organizer(dirpath)
if childLevel == 1:
    for d in os.listdir(dirpath):
        organizer(dirpath+"\\"+d)

    # flagIsDir = False
    # if os.path.isdir(dirpath):
    #     flagIsDir = True
    #     print (f"---Thư mục có tồn tại {dirpath}")
    # if flagIsDir:
    #     # createEXTfolders (dirpath,exts)
    #     for (path,dir,files) in os.walk(dirpath):
    #         try:            
    #             for f in files:
    #                 try:
    #                     ext = f.split(".")[-1] # ĐUÔI FILE - EXTENSION   
    #                     prp = path.split("\\")[-2]# TÊN FOLDER CHỨA (PARENT)        
    #                     flagNoNeed = prp == ext.upper()
    #                     fp = path + "\\" + f # FULL TÊN FILE + PATH
    #                 # if ext.lower() in needExts.lower() and flagNoNeed == False:                   
                        
    #                     nfn = f[:-len(ext)-1]+"-"+time.strftime("%y%m%d%H%M%S",time.localtime(float(os.stat(fp).st_mtime)))+"."+ext # TÊN MỚI + THỜI GIAN LƯU LAST
    #                     newDir = dirpath + "\\" + ext.upper() #TÊN FOLDER MỚI THEO EXT
    #                     createEXTfolders2 (newDir) # TAO FOLDER
    #                     copyFp = newDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
    #                     newFp =  newDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
    #                     if flagNoNeed == False: # NẾU FOLDER DANG CHỨA KHÔNG PHẢI TÊN DUÔI FILE UPPER
    #                         handleFiles(newFp,newDir,fp,copyFp)
    #                     else:
    #                         pass

    #                 # else:
    #                 except Exception as exx:
    #                     print(f"======LỖI: {exx}")  
    #                     if not "are the same file" in f"{exx}":
    #                         unsortDir = dirpath + "\\" + "UNSORT"
    #                         createEXTfolders2 (unsortDir)
    #                         copyFp = unsortDir + "\\" + f # TÊN CŨ TRONG FOLDER MỚI
    #                         newFp =  unsortDir + "\\" + nfn # TÊN MỚI TRONG FOLDER MỚI
    #                         handleFiles(newFp,unsortDir,fp,copyFp)
    #                     else:
    #                         pass
    #                 finally:
    #                     pass

    #         except Exception as ex:
    #             print(f"======LỖI: {ex}")
    #             pass