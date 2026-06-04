"""#Basic class
class student:
    #creating a method because its inside the class
    def greet(self):
        print("Hello Students")
s1=student()#creating an object of the class
s1.greet() #calling the method using the object """

"""#PROGRAM 2 — CONSTRUCTOR
class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)    
s1=student("Mohammad", 22) #created object
s1.display()#calling the method using object"""


#Instance variables VS Class variables
"""class student:
    def __init__(self, name):
        self.name=name 
s1=student("Mohammad") 
s2=student("Ravi") 
print(s1.name)
print(s2.name)
"""

class student:
    school='Harshini Degree College'
    def __init__(self,name):
        self.name=name

s1=student("Mohammad") 
s2=student("ravi")
print(s1.school)
print(s2.school)


#PROGRAM-5
#Instance method
class calculator:
    def add(self, a,b):
        return a+b
    def multiply(self, a,b):
        return a*b
obj=calculator()#created object
print(obj.add(3,4))
print(obj.multiply(2,3))


#BANK ACCOUNT SYSTEM PROJECT
class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input(
            "Hi, how can I help you?\n"
            "1) Enter 1 to create pin\n"
            "2) Enter 2 to change pin\n"
            "3) Enter 3 to check balance\n"
            "4) Enter 4 to withdraw money\n"
            "5) Enter 5 to exit\n"
        )
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw_money()
        else:
            exit()
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        self.balance = int(input("Enter the balance: "))
        print("Pin created successfully")
        self.menu()
    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            self.pin = input("Enter new pin: ")
            print("Pin changed successfully")
        else:
            print("Incorrect pin")
        self.menu()
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Incorrect pin")
        self.menu()
    def withdraw_money(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")
        self.menu()

        
obj = ATM()