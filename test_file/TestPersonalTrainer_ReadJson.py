from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.PersonalTrainer import PersonalTrainer

jff=JsonFileFactory()
filename="../dataset/personaltrainer.json"
personal_trainer=jff.read_data(filename,PersonalTrainer)
print("Danh sách PT sau khi đọc file:")
for p in personal_trainer:
    print(p)