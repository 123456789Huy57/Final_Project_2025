from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Manager import Manager

managers=[]
managers.append(Manager("M1","Lâm Hồng Thanh","Nu","thanhlh","123"))
managers.append(Manager("M2","Lê Thị Kim Hiền","Nu","hienltk","456"))
managers.append(Manager("M3","Trần Duy Thanh","Nam","thanhtd","789"))

print("Danh sách các Manager:")
for m in managers:
    print(m)
jff=JsonFileFactory()
filename="../dataset/manager.json"
jff.write_data(managers,filename)