from checking import Checking
from savings import Savings

class Person:
    def __init__(self,name,account_type):
        self.name= name 
        if account_type == "Checking":
            self.account = Checking()
        elif account_type == "Savings":
            self.account = Savings()

    def do_transaction(self):
        deposit_count = 0 

        for i in range(1,11): #Allow 10 transaction
            choice = input ("Enter 'D' to deposit or 'W' to withdraw:")
            amount = float (input("Enter amount:"))

            if choice == "D":
                self.account.deposit(amount)
                deposit_count += 1 
            elif choice == "W":
                self.account.withdraw(amount)
            else:
                print ("Invalid input!")
            # Apply profit every 10 deposits for Savings account
            if deposit_count == 10 and self.account.acct_type == "Savings":
                self.account.profit()
                deposit_count= 0

name = input ("Enter your name:")
acct_type = input ("Enter account type (Checking or Savings):")
person = Person(name , acct_type)
person.do_transaction()