import os, time
path = input("File path:")
"""
st_mode: int  # protection bits,
st_ino: int  # inode number,
st_dev: int  # device,
st_nlink: int  # number of hard links,
st_uid: int  # user id of owner,
st_gid: int  # group id of owner,
st_size: int  # size of file, in bytes,
st_atime: float  # time of most recent access,
st_mtime: float  # time of most recent content modification,
st_ctime: float  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows)
st_atime_ns: int  # time of most recent access, in nanoseconds
st_mtime_ns: int  # time of most recent content modification in nanoseconds
st_ctime_ns: int  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows) in nanoseconds
"""
fileStat = os.stat(path)

createdTime = time.strftime("%y%m%d %H%M%S",time.localtime(float(fileStat.st_mtime)))
print(createdTime)

modifiedTime = time.strftime("%y%m%d %H%M%S",time.localtime(float(fileStat.st_mtime)))
print(modifiedTime)

fileSize = round(float(fileStat.st_size)/1000000,3)
print(fileSize)

nfn = "fileName.taolao.txt"[:-len("txt")-1]+"-"+time.strftime("%y%m%d%H%M%S",time.localtime(float(fileStat.st_mtime)))+"."+"txt" 
print (nfn)

p = r"G:\003_OLD WORK\00-WORK FREE\120906 ELLE SHOP\DOC\HĐ Vincom-120917162622.doc"
print(p.split("\\")[-2])
print(p.split("\\")[-1].split("-")[-1].split(".")[0])