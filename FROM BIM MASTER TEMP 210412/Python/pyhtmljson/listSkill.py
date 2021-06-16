list1 = [1,2,3,4]
list2 = [1]


pathdir = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pyBIM2\BimProjectsBool\file.txt"
print(pathdir)
res = pathdir.split("\\")
p = ""
p = '\\'.join(res[:-1])
print("pyBIM2".lower() in p.lower())