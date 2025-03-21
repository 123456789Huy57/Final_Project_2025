from FinalProject.models.User import User

class Client(User):
    def __init__(self, ID=None, Full_Name=None, Gender=None, Username=None, Password=None, TypeofPT=None,
                 Branch=None, Email=None, Phone=None, Schedule=None, RegisID=None, Remaining_days=None,
                 Package_Registration_Date=None, Package_Name=None, Package_Price=None):
        super().__init__(ID, Full_Name, Gender, Username, Password)
        self.TypeofPT = TypeofPT
        self.Branch = Branch
        self.Schedule = Schedule
        self.Email = Email
        self.Phone = Phone
        self.Remaining_days = Remaining_days
        self.Schedule = Schedule  # Lưu ý: Có thể có lỗi gán lại Schedule, kiểm tra lại logic
        self.RegisID = RegisID
        self.Package_Registration_Date = Package_Registration_Date
        self.Package_Name = Package_Name
        self.Package_Price = Package_Price

        if Remaining_days is None:
            self.Remaining_days = 0
        elif isinstance(Remaining_days, (int, float)):
            self.Remaining_days = int(Remaining_days)
        else:
            try:
                self.Remaining_days = int(str(Remaining_days).strip())
            except (ValueError, TypeError):
                self.Remaining_days = 0

    def __str__(self):
        return (f"{super().__str__()}\t{self.TypeofPT}\t{self.Remaining_days}\t{self.Branch}\t"
                f"{self.Email}\t{self.Phone}\t{self.Schedule}\t{self.RegisID}\t"
                f"{self.Package_Registration_Date}\t{self.Package_Name}\t{self.Package_Price}")

    def to_dict(self):
        return {
            "ID": self.ID,
            "Full_Name": self.Full_Name,
            "Gender": self.Gender,
            "Username": self.Username,
            "Password": self.Password,
            "TypeofPT": self.TypeofPT,
            "Branch": self.Branch,
            "Email": self.Email,
            "Phone": self.Phone,
            "Schedule": self.Schedule,
            "RegisID": self.RegisID,
            "Remaining_days": self.Remaining_days,
            "Package_Registration_Date": self.Package_Registration_Date,
            "Package_Name": self.Package_Name,
            "Package_Price": self.Package_Price
        }