class Account:
    def __init__(self,acctno,balance):
        self.acctno=acctno
        self.balance=balance
        
    def debit(self):
        d=int(input("Please enter the amount you want to debit from your acct:"))
        print(f"Account No : {self.acctno}")
        print(f"Your current balance is : {self.balance - d} ")
    
    def credit(self):
        c=int(input("Please enter the amount you want to credit to your acct:"))
        print(f"Account No : {self.acctno}")
        print(f"Your current balance is : {self.balance + c} ")
        
    def balance_check(self):
        print(f"Account No : {self.acctno}")
        print(f"Your current balance is : {self.balance}")
        
    
        
a1 = Account(12, 87566)
a2 = Account(13, 69006)

lst=[a1,a2]

def find_acct(acct_no):
    for i in lst:
        if i.acctno == acct_no:
            i.balance_check()
            choice=int(input("Please Enter your choice:\1. Credit\n2. Debit"))
            if choice==1:
                i.credit()
            elif choice==2:
                i.debit()
        return
    print("Account not found")

find_acct(int(input("Enter your acct No"))) 

    
