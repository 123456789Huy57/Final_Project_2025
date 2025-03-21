from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Client import Client

jff=JsonFileFactory()
filename="../dataset/client.json"
clients=jff.read_data(filename,Client)
print("Danh sách khách hàng sau khi đọc file:")
for c in clients:
    print(c)