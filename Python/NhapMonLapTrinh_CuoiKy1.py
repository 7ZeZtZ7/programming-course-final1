#import Module. Nếu máy chưa có, cần cài đặt qua cmd
#Module pandas cho tạo bảng
import pandas as pd

#lập class HocSinh hỗ trợ cho việc lưu trữ và quản lý thông tin sinh viên
class HocSinh:
    ThongTin={"MaSV":[],"HoTen":[],"DiemCoSo":[],"DiemChuyenNganh":[],"DiemCuoiKy":[]}



    #thiết lập Attribute cho thông tin sinh viên bao gồm định dạng thông tin & giá trị mặc định (None=...)
    def __init__(self,masv:str|None="X",hoten:str|None="X",diemcs:float|None=0,diemcn:float|None=0):
        self.masv=masv #mã sinh viên
        self.hoten=hoten #họ tên
        self.diemcs=diemcs #điểm cơ sở
        self.diemcn=diemcn #điểm chuyên ngành
        self.cuoiky=diemcs*0.4+diemcn*0.6 #điểm cuối kỳ



    #Method thêm thông tin sinh viên vào danh sách
    def them(self):
        HocSinh.ThongTin["MaSV"].append(self.masv)
        HocSinh.ThongTin["HoTen"].append(self.hoten)
        HocSinh.ThongTin["DiemCoSo"].append(self.diemcs)
        HocSinh.ThongTin["DiemChuyenNganh"].append(self.diemcn)
        HocSinh.ThongTin["DiemCuoiKy"].append(self.cuoiky)



    #Method xóa thông tin sinh viên (chưa có backup do đó xóa là mất, nên chọn cho đúng)
    def xoa(self):
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            if self.masv==HocSinh.ThongTin["MaSV"][i]:
                HocSinh.ThongTin["MaSV"].pop(i)
                HocSinh.ThongTin["HoTen"].pop(i)
                HocSinh.ThongTin["DiemCoSo"].pop(i)
                HocSinh.ThongTin["DiemChuyenNganh"].pop(i)
                HocSinh.ThongTin["DiemCuoiKy"].pop(i)



    #Method truy xuất thông tin sinh viên
    def truyxuat(self):
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            a=HocSinh.ThongTin["MaSV"][i]
            b=HocSinh.ThongTin["HoTen"][i]
            c=HocSinh.ThongTin["DiemCoSo"][i]
            d=HocSinh.ThongTin["DiemChuyenNganh"][i]
            e=HocSinh.ThongTin["DiemCuoiKy"][i]
            if self.masv==a:
                truy={"MaSV":[a],"HoTen":[b],"DiemCoSo":[c],"DiemChuyenNganh":[d],"DiemCuoiKy":[e]}
                print(pd.DataFrame(truy))



    #Method lập danh sách sinh viên
    def danhsach():
        print("Danh sach:\n",pd.DataFrame(HocSinh.ThongTin))



    #Method xác định sinh viên có điểm cuối kỳ cao nhất & thấp nhất
    def topbot():
        diemcao=max(HocSinh.ThongTin["DiemCuoiKy"]) #điểm số cao nhất
        diemthap=min(HocSinh.ThongTin["DiemCuoiKy"]) #điểm số thấp nhất
        hscao={"MaSV":[],"HoTen":[],"DiemCoSo":[],"DiemChuyenNganh":[],"DiemCuoiKyCaoNhat":[]}
        hsthap={"MaSV":[],"HoTen":[],"DiemCoSo":[],"DiemChuyenNganh":[],"DiemCuoiKyThapNhat":[]}

        #lấy thông tin từ danh sách sinh viên
        for i in range(len(HocSinh.ThongTin["DiemCuoiKy"])):
            a=HocSinh.ThongTin["MaSV"][i]
            b=HocSinh.ThongTin["HoTen"][i]
            c=HocSinh.ThongTin["DiemCoSo"][i]
            d=HocSinh.ThongTin["DiemChuyenNganh"][i]
            e=HocSinh.ThongTin["DiemCuoiKy"][i]

            #xác định cao nhất
            if HocSinh.ThongTin["DiemCuoiKy"][i]==diemcao:
                hscao["MaSV"].append(a)
                hscao["HoTen"].append(b)
                hscao["DiemCoSo"].append(c)
                hscao["DiemChuyenNganh"].append(d)
                hscao["DiemCuoiKyCaoNhat"].append(e)

            #xác định thấp nhất
            if HocSinh.ThongTin["DiemCuoiKy"][i]==diemthap:
                hsthap["MaSV"].append(a)
                hsthap["HoTen"].append(b)
                hsthap["DiemCoSo"].append(c)
                hsthap["DiemChuyenNganh"].append(d)
                hsthap["DiemCuoiKyThapNhat"].append(e)

        #menu chọn xem học sinh điểm cao nhất hoặc thấp nhất
        while True:
            ans=input("[1]: Cao nhat | [2]: Thap nhat | [X]: Thoat | ")
            if ans=="1":
                print("Cao nhat:\n",pd.DataFrame(hscao))
            elif ans=="2":
                print("Thap nhat:\n",pd.DataFrame(hsthap))
            elif ans=="X" or ans=="x":
                break
            else:
                print("Khong hop le")



    #Method lập danh sách sinh viên không đạt
    def khongdat():
        khongdat={"MaSV":[],"HoTen":[],"TenMonKhongDat":[],"DiemSoKhongDat":[]}

        #lấy thông tin sinh viên
        for i in range(len(HocSinh.ThongTin["HoTen"])):
            a=HocSinh.ThongTin["MaSV"][i]
            b=HocSinh.ThongTin["HoTen"][i]
            c=HocSinh.ThongTin["DiemCoSo"][i]
            d=HocSinh.ThongTin["DiemChuyenNganh"][i]

            #rớt cả 2 điểm
            if c<4 and d<4:
                khongdat["MaSV"].append(a)
                khongdat["HoTen"].append(b)
                khongdat["TenMonKhongDat"].append("Diem co so & chuyen nganh")
                khongdat["DiemSoKhongDat"].append([c,d])

            #rớt điểm cơ sở
            elif c<4:
                khongdat["MaSV"].append(a)
                khongdat["HoTen"].append(b)
                khongdat["TenMonKhongDat"].append("Diem co so")
                khongdat["DiemSoKhongDat"].append(c)

            #rớt điểm chuyên ngành
            elif d<4:
                khongdat["MaSV"].append(a)
                khongdat["HoTen"].append(b)
                khongdat["TenMonKhongDat"].append("Diem chuyen nganh")
                khongdat["DiemSoKhongDat"].append(d)

        #xét điều kiện nếu không có ai không đạt
        if pd.DataFrame(khongdat).empty:
            print("Tat ca deu dat")
        else:
            print("Khong dat:\n",pd.DataFrame(khongdat))



#hàm cho phép nhập thông tin liên tục
def nhaplieu():
    while True:
        a=input("Nhap ma so sinh vien: ")
        b=input("Nhap ho ten: ")
        c=float(input("Nhap diem co so: "))
        d=float(input("Nhap diem chuyen nganh: "))
        sv=HocSinh(a,b,c,d)
        sv.them()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break
        else:
            pass



#hàm truy xuất thông tin liên tục
def truyhoi():
    while True:
        a=input("Nhap ma so sinh vien hoac ho ten sinh vien: ")
        sv=HocSinh(masv=a,hoten=a)
        sv.truyxuat()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break
        else:
            pass



#hàm cho phép xóa thông tin liên tục
def don():
    while True:
        a=input("Nhap ma so sinh vien hoac ho ten sinh vien: ")
        sv=HocSinh(masv=a,hoten=a)
        sv.xoa()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break
        else:
            pass



#menu tìm/thêm/xóa (có thể có sửa)
def findaddrem():
    while True:
        ans=input("[1]: Tim | [2]: Them | [3]: Xoa | [X]: Thoat | ")
        if ans=="1":
            truyhoi()
        elif ans=="2":
            nhaplieu()
        elif ans=="3":
            don()
        elif ans=="X" or ans=="x":
            break
        else:
            print("Khong hop le")


#chạy chương trình
while True:
    ans=input("[1]: Danh sach sinh vien | [2]: Hoc sinh co diem cao nhat va thap nhat | [3]: Hoc sinh khong dat | [4]: Quan ly danh sach | [X]: Thoat | ")
    if ans=="1":
        HocSinh.danhsach()
    elif ans=="2":
        HocSinh.topbot()
    elif ans=="3":
        HocSinh.khongdat()
    elif ans=="4":
        findaddrem()
    elif ans=="X" or ans=="x":
        break
    else:
        print("Khong hop le")