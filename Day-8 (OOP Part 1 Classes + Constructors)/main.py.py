#Creating ATM MACHINE
class ATM: #class name should in Pascal
    def __init__(self): #this is constructor when object is creatied it automatically runs
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input("""
Hello, how would you like to proceed?
1. Enter 1 to create a new pin
2. enter 2 to pin deposit           
3.enter 3 to check balancce
4. enter 4 to withdraw moneyt """)
    
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            pass
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            print("EXIST")

    def create_pin(self):
        self.pin=input("Enter your PIN:")
        self.balance=int(input("Enter the initial balance: "))
        print("PIN is Created Successfull")
    def check_balance(self):
        pin=input("Enter your pin:")
        if pin==self.pin:
            print("your balance is:", self.balance)
        else:
            print("incorrect pin")
    def withdraw(self):
        pin=input("Enter your pin number:")
        if pin==self.pin:
            amount=int("Enter the amount:")
            if amount<=self.balance:
                self.balance=amount-self.balance
                print("Withdrwal Successfull")
            else:
                print("INCORRECT PIN")
  
#CREATING OBJECT
sbi=ATM()   



                  
