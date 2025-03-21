class User:
    def __init__(self,ID=None,Full_Name=None,Gender=None,Username=None,Password=None):
        self.ID=ID
        self.Full_Name=Full_Name
        self.Gender=Gender
        self.Username=Username
        self.Password=Password
    def __str__(self):
        return f"{self.ID}\t{self.Full_Name}\t{self.Gender}\t{self.Username}\t{self.Password}"