from FinalProject.libs.JsonFileFactory import JsonFileFactory
from FinalProject.models.PersonalTrainer import PersonalTrainer

personal_trainers=[]
personal_trainers.append(PersonalTrainer("P1","Đăng Béo","Nam","dangbeo","123","10","Gym","Hà Nội","huynhgiabaopy2006@gmail.com","0833456802","R1"))
personal_trainers.append(PersonalTrainer("P2","Quỳnh Anh","Nữ","quynhanh","1505","5","Yoga","Hồ Chí Minh","quynhanh@gmail.com","0850004822","R2"))
personal_trainers.append(PersonalTrainer("P3","Huỳnh Bảo","Nam","hbao","1811","5","Gym","Hà Nội","baohuynh@gmail.com","0912742837","R3"))
personal_trainers.append(PersonalTrainer("P4","Trân Lee","Nữ","tranle","123","7","Yoga","Hà Nội","tranlee@gmail.com","0983504600","R4"))
personal_trainers.append(PersonalTrainer("P5","Huy Nguyễn","Nam","huynguyen","456","20","Gym","Hồ Chí Minh","huynguyen@gmail.com","0802500409","R5"))
personal_trainers.append(PersonalTrainer("P6","Đại Đồng","Nam","daidong","789","15","Gym","Hồ Chí Minh","daidong@gmail.com","0914268533","R6"))

print("Danh sách các Khách Hàng:")
for p in personal_trainers:
    print(p)
jff=JsonFileFactory()
filename="../dataset/personaltrainer.json"
jff.write_data(personal_trainers,filename)