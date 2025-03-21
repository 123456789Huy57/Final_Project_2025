from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Manager import Manager

jff=JsonFileFactory()
filename="../dataset/manager.json"
managers=jff.read_data(filename,Manager)
print("Danh sách quản lý sau khi đọc file:")
for m in managers:
    print(m)