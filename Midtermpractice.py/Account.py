class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance is ",self.get_balance())
    def credit (self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance is",self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1=Account(10000,67890)
acc1.debit(1000)
acc1.credit(600)
acc1.credit(40000)


