from account import Account 

class Checking(Account):
    def __init__(self):
        super().__init__("Checking")
        self.over_draft = 1000 #Overdraft limit

    def get_overdraft_limit(self):
        return self.over_draft