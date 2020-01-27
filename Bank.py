print("This is a bank application program, which doesnt contain private variable")
class bank:
    def __init__(self):
        self.accno=""
        self.acctype=""
        self.accname=""
        self.balance="" 
    def display(self):
        print("The account number is ",self.accno)
        print("The account type is ",self.acctype)
        print("The name of the account holder is ",self.accname)
        print("The balance amount is ",self.balance)
    def TakeInput(self):
        self.accno=input("Enter the account number: ")
        self.acctype=input("Enter the account type: ")
        self.accname=input("Enter the account name: ")
        self.balance=input("Enter the balance: ")
#Driver code:        
b1=bank()
b1.TakeInput()
b1.display()