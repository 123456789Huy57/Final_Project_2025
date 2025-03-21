from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.Location import Location

locations=[]
locations.append(Location("1","Hà Nội"))
locations.append(Location("2","Hồ Chí Minh"))


print("Danh sách các chi nhánh:")
for l in locations:
    print(l)
jff=JsonFileFactory()
filename="../dataset/location.json"
jff.write_data(locations,filename)