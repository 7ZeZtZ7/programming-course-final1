#chuẩn bị cho chương trình
import pandas as pd #module thêm chức năng tạo bảng
import os #module thêm chức năng từ hệ điều hành



#lập class HocSinh hỗ trợ cho việc lưu trữ và quản lý thông tin sinh viên
#lưu ý vai trò của từng đối tượng (chữ self trong cặp ngoặc của các Method) mà các Method sẽ được sử dụng lên:
#   đối tượng của truyxuat() chỉ cần mã sinh viên, sử dụng để rút thông tin sinh viên mang mã đó
#   đối tượng của them() cần có đầy đủ thông tin
#   đối tượng của xoa() chỉ cần mã sinh viên để xác định thông tin của ai sẽ bị xóa
#   đối tượng của chinhsua() cần đầy đủ thông tin, với mã sinh viên LÀ 1 mã PHẢI CÓ trong danh sách
class HocSinh:
    ThongTin={"MaSV":[],"HoTen":[],"DiemCoSo":[],"DiemChuyenNganh":[],"DiemCuoiKy":[]}



    #thiết lập Attribute cho thông tin sinh viên bao gồm định dạng thông tin & giá trị mặc định (None=...)
    def __init__(self,masv:str|None="X",hoten:str|None="X",diemcs:float|None=0,diemcn:float|None=0):
        self.masv=masv #mã sinh viên
        self.hoten=hoten #họ tên
        self.diemcs=diemcs #điểm cơ sở
        self.diemcn=diemcn #điểm chuyên ngành
        self.cuoiky=diemcs*0.4+diemcn*0.6 #điểm cuối kỳ



    #Method truy xuất thông tin sinh viên
    def truyxuat(self):
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            a=HocSinh.ThongTin["MaSV"][i]
            b=HocSinh.ThongTin["HoTen"][i]
            c=HocSinh.ThongTin["DiemCoSo"][i]
            d=HocSinh.ThongTin["DiemChuyenNganh"][i]
            e=HocSinh.ThongTin["DiemCuoiKy"][i]
            if self.masv not in HocSinh.ThongTin["MaSV"]:
                return print("Khong co sinh vien mang ma nay")
            elif self.masv==a:
                truy={"MaSV":[a],"HoTen":[b],"DiemCoSo":[c],"DiemChuyenNganh":[d],"DiemCuoiKy":[e]}
                print(pd.DataFrame(truy))



    #Method thêm thông tin sinh viên vào danh sách
    def them(self):
        #xét xem có trùng mã sinh viên với ai không
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            if self.masv=="X" or self.masv==HocSinh.ThongTin["MaSV"][i]:
                return print("Khong hop le")
        HocSinh.ThongTin["MaSV"].append(self.masv)
        HocSinh.ThongTin["HoTen"].append(self.hoten)
        HocSinh.ThongTin["DiemCoSo"].append(self.diemcs)
        HocSinh.ThongTin["DiemChuyenNganh"].append(self.diemcn)
        HocSinh.ThongTin["DiemCuoiKy"].append(self.cuoiky)



    #Method xóa thông tin sinh viên (chưa có backup, tính năng undo do đó xóa là mất, nên chọn cho đúng)
    def xoa(self):
        for i in range(len(HocSinh.ThongTin["MaSV"])): #hàm len khi này trả về độ dài ban đầu trước khi xóa
            if self.masv==HocSinh.ThongTin["MaSV"][i]: #lấy index trong danh sách ban đầu
                HocSinh.ThongTin["MaSV"].pop(i)
                HocSinh.ThongTin["HoTen"].pop(i)
                HocSinh.ThongTin["DiemCoSo"].pop(i)
                HocSinh.ThongTin["DiemChuyenNganh"].pop(i)
                HocSinh.ThongTin["DiemCuoiKy"].pop(i)
                return print("Da xoa") #ngưng ngay sau khi xóa, tránh tình trạng tràn index do lệnh for tiếp tục chạy đến khi hết độ dài danh sách cũ



    #Method chỉnh sửa (kèm truy xuất theo dõi) (chưa thể sửa mã sinh viên, nên nhập đúng từ đầu)
    def chinhsua(self):
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            if self.masv==HocSinh.ThongTin["MaSV"][i]:
                HocSinh.ThongTin["HoTen"][i]=self.hoten #sửa họ tên
                HocSinh.ThongTin["DiemCoSo"][i]=self.diemcs #sửa điểm cơ sở
                HocSinh.ThongTin["DiemChuyenNganh"][i]=self.diemcn #sửa điểm chuyên ngành
                HocSinh.ThongTin["DiemCuoiKy"][i]=self.cuoiky #sửa điểm cuối kỳ
                return self.truyxuat()



    #Method lập danh sách sinh viên
    def danhsach():
        if pd.DataFrame(HocSinh.ThongTin).empty:
            return print("Khong co thong tin")
        else:
            return print("Danh sach:\n",pd.DataFrame(HocSinh.ThongTin))



    #Method xác định sinh viên có điểm cuối kỳ cao nhất & thấp nhất
    def topbot():
        if len(HocSinh.ThongTin["DiemCuoiKy"])==0:
            return print("Chua co thong tin")
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
            if e==diemcao:
                hscao["MaSV"].append(a)
                hscao["HoTen"].append(b)
                hscao["DiemCoSo"].append(c)
                hscao["DiemChuyenNganh"].append(d)
                hscao["DiemCuoiKyCaoNhat"].append(e)

            #xác định thấp nhất
            if e==diemthap:
                hsthap["MaSV"].append(a)
                hsthap["HoTen"].append(b)
                hsthap["DiemCoSo"].append(c)
                hsthap["DiemChuyenNganh"].append(d)
                hsthap["DiemCuoiKyThapNhat"].append(e)

        #để phòng trường hợp có 2 người trở lên bằng điểm,
        #ta phải append (thêm) vào danh sách thay vì nhập thẳng attribute vào

        #VD: hscao={"MaSV":[a],"HoTen":[b],"DiemCoSo":[c],"DiemChuyenNganh":[d],"DiemCuoiKyCaoNhat":[e]}
        #    hsthap={"MaSV":[a],"HoTen":[b],"DiemCoSo":[c],"DiemChuyenNganh":[d],"DiemCuoiKyThapNhat":[e]}
        #khi này, danh sách được trả ra sẽ chỉ có 1 thông tin sinh viên và luôn là thông tin cuối cùng rút ra từ lệnh for và đáp ứng điều kiện của if

        #menu chọn xem học sinh điểm cao nhất hoặc thấp nhất
        while True:
            ans=input("[1]: Cao nhat | [2]: Thap nhat | [any]: Thoat | ")
            match ans:
                case "1":
                    print("Cao nhat:\n",pd.DataFrame(hscao))
                case "2":
                    print("Thap nhat:\n",pd.DataFrame(hsthap))
                case _:
                    break



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
            return print("Tat ca deu dat")
        else:
            return print("Khong dat:\n",pd.DataFrame(khongdat))



#hàm cho phép nhập thông tin liên tục
def nhaplieu():
    while True:
        a=input("Nhap ma so sinh vien: ")
        #xét mã có bị trùng mã có sẵn hay dạng mặc định không
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            if a=="X" or a==HocSinh.ThongTin["MaSV"][i]:
                return print("Khong hop le")
            
        b=input("Nhap ho ten: ")
        c=float(input("Nhap diem co so: "))
        d=float(input("Nhap diem chuyen nganh: "))
        sv=HocSinh(a,b,c,d)
        sv.them()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break



#hàm truy xuất thông tin liên tục
def truyhoi():
    while True:
        a=input("Nhap ma so sinh vien: ")
        sv=HocSinh(masv=a)
        sv.truyxuat()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break



#hàm cho phép xóa thông tin liên tục
def don():
    while True:
        a=input("Nhap ma so sinh vien: ")
        if a=="X":
            pass
        else:
            sv=HocSinh(masv=a)
            sv.xoa()

        ans=input("[X]: Thoat | Nhap bat ky de tiep tuc | ")
        if ans=="X" or ans=="x":
            break



#hàm cho phép chỉnh liên tục
def doi():
    while True:
        a=input("Nhap ma so sinh vien: ")
        b=str
        c=float
        d=float

        #giữ lại thông tin trường hợp không có sửa
        for i in range(len(HocSinh.ThongTin["MaSV"])):
            if HocSinh.ThongTin["MaSV"][i]==a:
                b=HocSinh.ThongTin["HoTen"][i]
                c=HocSinh.ThongTin["DiemCoSo"][i]
                d=HocSinh.ThongTin["DiemChuyenNganh"][i]

        #vào menu chỉnh sửa
        while True:
            ans=input("[1]: Nhap ho ten | [2]: Nhap diem co so | [3]: Nhap diem chuyen nganh | [X]: Xong | ")
            match ans:
                case "1":
                    b=input("Nhap ho ten: ")
                case "2":
                    c=float(input("Nhap diem co so: "))
                case "3":
                    d=float(input("Nhap diem chuyen nganh: "))
                case "X":
                    break
                case _:
                    pass
            
            sv=HocSinh(a,b,c,d)
            sv.chinhsua()

        ans=input("[X]: Thoat | Nhap bat ky de quay lai chinh sua | ")
        if ans=="X" or ans=="x":
            break



#menu quản lý danh sách
def truythemxoasua():
    while True:
        os.system("cls")
        HocSinh.danhsach()
        ans=input("[1]: Tim | [2]: Them | [3]: Xoa | [4]: Chinh sua | [any]: Thoat | ")
        match ans:
            case "1":
                truyhoi()
            case "2":
                nhaplieu()
            case "3":
                don()
            case "4":
                doi()
            case _:
                break



#biến tạo sẵn cho chạy thử nghiệm. Cú pháp: <var>=<Class>(<attribute>)
#Cú pháp cụ thể cho chương trình này: <var>=HocSinh( <MaSV> , <HoTen> , <DiemCoSo> , <DiemChuyenNganh> )
sv1=HocSinh("MS0001","Nguyen Van A",10,9)
sv2=HocSinh("MS0002","Hoang Thi B",3,6)
sv3=HocSinh("MS0003","Vo Tan C",6,3)
#chạy Method trực tiếp lên đối tượng, lấy đối tượng làm arg. Cú pháp: <var>.<Method>()
sv1.them()
sv2.them()
sv3.them()



#chạy chương trình
os.system("cls") #clear màn hình
while True:
    ans=input("[1]: Xem danh sach | [2]: Hoc sinh co diem cao nhat va thap nhat | [3]: Hoc sinh khong dat | [4]: Quan ly danh sach | [X]: Thoat | ")
    match ans:
        case "1":
            os.system("cls")
            HocSinh.danhsach()
        case "2":
            os.system("cls")
            HocSinh.topbot()
        case "3":
            os.system("cls")
            HocSinh.khongdat()
        case "4":
            truythemxoasua()
        case "X":
            break
        case _:
            print("Khong hop le")