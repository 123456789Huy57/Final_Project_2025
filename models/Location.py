class Location:
    def __init__(self,Address=None,Branch=None):
        self.Address=Address
        self.Branch=Branch
    def __str__(self):
        return f"{self.Address}\t{self.Branch}"
