'''Create a class Account
accno
type account (Current, Savings, Loan)
branch
city
balance

deposit(amount)
- if savings, currnet - add to balance
- if loan - decuct from balance

withdraw(amount)
- if savings, currnet - deduct from balance
- if loan -add to balance

showDetails()'''
class NegativeBalance(Exception):
    def __init__(self,message):
        self.message = message

class Account:
    def __init__(self,acc,branch,city,balance):
        self.acctype = acc
        self.branch = branch
        self.city = city
        self.balance = balance

    def Deposite(self,amount):
        #amount = int(input("enter the amount to deposite:"))
        if (self.acctype=="current" or self.acctype=="savings"):
            tobalance=self.balance+amount
            return tobalance
        elif(self.acctype=="loan"):
            tobalance=self.balance-amount
            return tobalance
        else:
             #self.balance-=amount
            print("invalid acc type")

    def withdraw(self,amount):
        #amount = int(input("enter the amount to withdraw:"))
        if (self.balance <=0):
            raise NegativeBalance("balance is <=")
        elif (self.acctype == "current" or self.acctype == "savings"):
            tobalance = self.balance-amount
            return tobalance
        else:
            print("invalid acc type")

    def showdetails(self):
        print("acc type:",self.acctype)
        print("branch:", self.branch)
        print("city:", self.city)
        print("balance:", self.balance)

accA = Account("savings","vaslane","mangalore",1000)
acc1=accA.Deposite(100)
acc12=accA.showdetails()
print("balance after deposite:",acc1)
accB = Account("current","vaslane","mangalore",1000)
acc2=accB.withdraw(50)
acc123=accB.showdetails()
print("balance after withdrawal:",acc2)
try:
    print(accB.withdraw(300))
    accB.showdetails()
except NegativeBalance:
    print("withdraw not possible")
