import pandas as pd
import re,os,json
from seach_methods import *
from commands import *
import unidecode


def main():
    user_name = input("Vui lòng cho biết tên của bạn: ")#.upper()
    spinWaiting()
    print (f"Hi {user_name} !!")
    print(f"""------------------------------------------------------------------
        Chào mừng {user_name} đến với 
                CHƯƠNG TRÌNH 
        E-LOGISTIC PHIÊN BẢN COMMAND LINE
------------------------------------------------------------------
""")
    time_use = time.strftime("%y%m%d %H%M%S",time.localtime(time.time()))
    spinWaiting()
    promp = f"""
------------------------------------------------------------------
                            Menu Chương Trình
------------------------------------------------------------------
    1.  Tra cứu Mã, Loại, Tên và Thông tin vật tư
    1.1 Lưu Mã vật tư vào Bộ sưu tập
    2.  Xem chi tiết vật tư
    2.1 Xem chi tiết vật tư Nâng cao
    3.  Lập Phiếu Yêu cầu Vật tư
    4.  Lập Phiếu Xuất vật tư
    5.  Lập Phiếu Nhập vật tư
    6.  Lập Phiếu Vận tải
    7.  Lập phiếu Giao nhận
    8.  In Biên lai
    9.  Xem Hồ sơ
    10. Thiết đặt Dữ liệu

    0. Thoát chương trình
<{user_name}>: """
    askMenu = input(promp)
    spinWaiting()
    data_path = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\EquipmentList_24-02-2021.xlsx" # input("---Vui lòng nhập Đường dẫn Root: Bước 10")
    spinWaiting()
    # data = pd.read_excel(data_path)
    # print(data)
    column_heads = ['MaLoaiThietBi','TenLoaiThietBi','MaThietBi','TenThietBi','DonVi','KhoiLuong']
    store_dir = data_path[:-len(data_path.split("\\")[-1])-1]
    data_name = "data"#data_path.split("\\")[-1].split(".")[0]
    json_path = store_dir+"\\"+data_name+".json"
    data_search_name = "data_seach"#data_path.split("\\")[-1].split(".")[0]
    json_search_path = store_dir+"\\"+data_search_name+".json"
    # print(json_path)
    search_data = None
    newdata = None
    if not os.path.isfile(json_path):
        newdata = pd.read_excel(data_path)[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3','Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:]#pd.DataFrame(new_series,columns=column_heads)
        newdata.columns = column_heads
        newdata.index = range(len(newdata))
        newdata.to_json(json_path,orient='records')
    else:
        newdata = pd.read_json(json_path, orient='records')
    if not os.path.isfile(json_search_path):
        search_data = pd.DataFrame([unidecode.unidecode("___".join(str(newdata.loc[i][c]) for c in column_heads)).upper() for i in newdata.index], index = range(len(newdata)),columns = ["Search string"],dtype="string")
        search_data.to_json(json_search_path,orient='records')
    else:
        search_data = pd.read_json(json_search_path, orient='records')
    # print(newdata.head())
    # print(search_data.head())
    while askMenu != "0":        

        # print(data[2:])
        # print(data.columns) #['DANH SÁCH THIẾT BỊ', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3','Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']
        # print(data[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3','Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:])

        spinWaiting()
        if askMenu == "1":
            value = input("Seach Value:").upper()
            # search(value,newdata,column_heads)
            # str_row = "___".join(str(newdata.loc[0][c]) for c in column_heads)
            # print(str_row)
            # line = unidecode.unidecode(str_row).lower()
            # print(line)
            spinWaiting()
            print(newdata.loc[[ii for ii in search_data.index if re.search(value,str(search_data.loc[ii]))]])

        if askMenu == "2":
            detail_id = input("Index:(Là số hiệu Cột đầu tiên của các bảng Thông tin) ")
            spinWaiting()
            if int(detail_id):
                print(f"---Bạn đang xem thông tin chi tiết của \n{newdata.loc[int(detail_id)]}")
                pass
            else:
                print("---Bạn nhập sai kiểu dữ liệu, cần là Số Nguyên")
                pass
        if askMenu == "2.1":
            try:
                detail_id, column_name = input("Index,Column:(Số hiệu,Tên cột) ").split(",")
                spinWaiting()
                if int(detail_id) and column_name:
                    print(f"---Bạn đang xem thông tin chi tiết của \n{newdata.loc[int(detail_id)][column_name]}")
                    pass
                else:
                    print("---Bạn nhập sai dữ liệu, cần là 1 chuỗi :Số Nguyên,Tên Cột")
                    pass
            except:
                pass        
        if askMenu == "1.1":
            try:
                user_data_path = store_dir + "\\userdata\\" + user_name +"-"+time_use+".json"
                saved_selection = input("---Hãy nhập Mã Vật Tư bạn Muốn lưu: ")
                #verify
                flag_exist = True
                if flag_exist:
                    time_select = round(time.time())
                    user_selection = {"MaVatTu":saved_selection,"Time":time_select}           
                if not os.path.exists(user_data_path):
                    with open(user_data_path,'w') as wud:
                        wud.write(json.dumps(user_selection,indent=4,sort_keys=True))
                    spinWaiting()
                    print (f"---Thành công lưu thông tin tại {user_data_path}")
            except Exception as ex:
                print (ex)
                print("---Có lỗi gì đó xảy ra, vui lòng thử lại")
                pass
        spinWaiting()
        askMenu = input(promp)
    time_end = time.strftime("%H:%M:%S %a %d %b %Y ",time.localtime(time.time()))
    print(f"---Bạn đang thoát chương trình vào lúc {time_end}")
    spinWaiting()
    spinWaiting()
    quit()

#START PROGRAM
main()

def test():
    data_path = r"C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\py_logistic\EquipmentList_24-02-2021.xlsx"


    store_dir = data_path[:-len(data_path.split("\\")[-1])-1]
    data_name = "data"#data_path.split("\\")[-1].split(".")[0]
    json_path = store_dir+"\\"+data_name+".json"

    newdata = pd.read_json(json_path, orient='records')
    print (newdata.loc[14222])
# test()


   