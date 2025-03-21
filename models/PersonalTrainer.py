from FinalProject.models.User import User


class PersonalTrainer(User):
    def __init__(self, ID=None,Full_Name=None, Gender=None, Username=None, Password=None, Experience=None, TypeofPT=None, Branch=None,Email=None,Phone=None,RegisID=None):
        super().__init__(ID,Full_Name, Gender, Username, Password)
        self.Experience = Experience
        self.TypeofPT = TypeofPT
        self.Branch = Branch
        self.Email=Email
        self.Phone=Phone
        self.RegisID = RegisID
    def __str__(self):
        return f"{super().__str__()}\t{self.Experience}\t{self.TypeofPT}\t{self.Branch}\t{self.Email}\t{self.Phone}\t{self.RegisID}"