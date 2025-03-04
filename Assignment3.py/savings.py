from account import Account

class Savings(Account):
    def __init__(self):
        super().__init__("Savings")
        self.over_draft = 1200 #Overdraft limit

    def get_overdraft_limit(self):
        return self.over_draft
    
    def profit(self):
        self.current_balance *= 1.15 #Apply 15% profit
        print ("Profit applied! New Balance:", self.current_balance)
        
