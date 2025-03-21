from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Client import Client

clients=[]
clients.append(Client("C0", "Tèo", "Nam", "teo", "123", "Newbie", "Hà Nội", "nhatkhoaledang@gmail.com", "09284783578", "S1", "R1",1))
clients.append(Client("C1", "Nguyễn Văn Anh", "Nam", "anhnv", "123456", "Experienced", "Hà Nội", "anhnv@gmail.com", "0912345678", "S1", "R2",60))
clients.append(Client("C2", "Trần Thị Bình", "Nữ", "binhtt", "123456", "Newbie", "Hà Nội", "binhtt@gmail.com", "0923456789", "S2", "R3",720))
clients.append(Client("C3", "Lê Minh Cường", "Nam", "cuonglm", "123456", "Newbie", "Hà Nội", "cuonglm@gmail.com", "0934567890", "S3", "R4",60))
clients.append(Client("C4", "Phạm Thanh Dung", "Nữ", "dungpt", "123456", "Newbie", "Hà Nội", "dungpt@gmail.com", "0945678901", "S4", "R4",60))
clients.append(Client("C5", "Hoàng Văn Em", "Nam", "emhv", "123456", "Newbie", "Hà Nội", "emhv@gmail.com", "0956789012", "S5", "R5",600))
clients.append(Client("C6", "Vũ Thị Phương", "Nữ", "phuongvt", "123456", "Newbie", "Hà Nội", "phuongvt@gmail.com", "0967890123", "S1", "R6",60))
clients.append(Client("C7", "Đặng Minh Quân", "Nam", "quandm", "123456", "Experienced", "Hà Nội", "quandm@gmail.com", "0978901234", "S2", "None",60))
clients.append(Client("C8", "Bùi Thị Hoa", "Nữ", "hoabt", "123456", "Newbie", "Hà Nội", "hoabt@gmail.com", "0989012345", "S3", "R1",120))
clients.append(Client("C9", "Đỗ Văn Hùng", "Nam", "hungdv", "123456", "Newbie", "Hà Nội", "hungdv@gmail.com", "0990123456", "S4", "R2",75))
clients.append(Client("C10", "Ngô Thị Lan", "Nữ", "lannt", "123456", "Experienced", "Hà Nội", "lannt@gmail.com", "0901234567", "S5", "R3",60))
clients.append(Client("C11", "Dương Văn Mạnh", "Nam", "manhdv", "123456", "Experienced", "Hà Nội", "manhdv@gmail.com", "0912345679", "S1", "R4",50))
clients.append(Client("C12", "Lý Thị Ngọc", "Nữ", "ngoclt", "123456", "Newbie", "Hà Nội", "ngoclt@gmail.com", "0923456780", "S2", "R5",45))
clients.append(Client("C13", "Hồ Văn Phúc", "Nam", "phuchv", "123456", "Newbie", "Hà Nội", "phuchv@gmail.com", "0934567891", "S3", "R6","60 "))
clients.append(Client("C14", "Trương Thị Quỳnh", "Nữ", "quynhtt", "123456", "Newbie", "Hà Nội", "quynhtt@gmail.com", "0945678902", "S4", "None","60 "))
clients.append(Client("C15", "Võ Văn Sơn", "Nam", "sonvv", "123456", "Experienced", "Hà Nội", "sonvv@gmail.com", "0956789013", "S5", "R4"))
clients.append(Client("C16", "Mai Thị Thảo", "Nữ", "thaomt", "123456", "Experienced", "Hà Nội", "thaomt@gmail.com", "0967890124", "S1", "R3","720 "))
clients.append(Client("C17", "Lâm Văn Tuấn", "Nam", "tuanlv", "123456", "Newbie", "Hà Nội", "tuanlv@gmail.com", "0978901235", "S2", "R2","60 "))
clients.append(Client("C18", "Đinh Thị Uyên", "Nữ", "uyendt", "123456", "Experienced", "Hà Nội", "uyendt@gmail.com", "0989012346", "S3", "R5","35 "))
clients.append(Client("C19", "Phan Văn Vinh", "Nam", "vinhpv", "123456", "Newbie", "Hà Nội", "vinhpv@gmail.com", "0990123457", "S4", "R6","25 "))
clients.append(Client("C20", "Tạ Thị Xuân", "Nữ", "xuantt", "123456", "Experienced", "Hà Nội", "xuantt@gmail.com", "0901234568", "S5", "R4","720 "))

# Ghi chú về các mã đăng ký:
# R1, R3, R4 thuộc Hà Nội
# R3, R5, R6 thuộc Hồ Chí Minh



print("Danh sách các Khách Hàng:")
for c in clients:
    print(c)
jff=JsonFileFactory()
filename="../dataset/client.json"
jff.write_data(clients,filename)