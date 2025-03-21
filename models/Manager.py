from FinalProject.models.User import User


class Manager(User):
    def __init__(self, ID, Name, Gender, Username, Password):
        super().__init__(ID, Name, Gender, Username, Password)

    def __str__(self):
        infor = super().__str__()
        return infor
