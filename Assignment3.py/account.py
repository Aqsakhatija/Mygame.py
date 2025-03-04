class Account:
    def __init__(self,acct_type):
        self.acct_type = acct_type
        self.current_balance= 500 #default balance
        self.min_balance= 500 # minimum balance
    
    def withdraw(self,amount):
        if self.current_balance - amount < -self.get_overdraft_limit():
            print ("Transaction denied! Overdraft limit exceed.")
        else:
            self.current_balance -= amount
            print ("Withdrawal successful. New balance:",self.current_balance)

    def deposit(self,amount):
        self.current_balance += amount
        print ("Deposit successful. New balance:",self.current_balance)
    
    def get_overdraft_limit(self):
        return 0 