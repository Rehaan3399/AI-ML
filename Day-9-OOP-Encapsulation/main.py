
#If there is agregation bbetween the two classes then we can use getters and setters to access the private members of  the class. 
class Customer:
    def __init__(self, name, gender, adress):
        self.name=name
        self.gender=gender
        self.adress=adress
    def print_address(self):
        print(self.adress.city, self.adress.pin, self.adress.state)    
class Adress:
    def __init__(self, city, pin, state):
        self.__city=city
        self.pin=pin
        self.state=state
add1=Adress('Singarayakonda', 23456, 'haryana')
cust=Customer("nitish","male",add1 )
 

# In the below code we have made city as private member of the class Adress and we are accessing it in the class Customer using getter method get_city().
class Customer:
    def __init__(self, name, gender, address):
        self.name=name
        self.gender=gender
        self.address=address
    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)    
class Adress:
    def __init__(self, city, pin, state):
        self.__city=city
        self.pin=pin
        self.state=state
    def get_city(self):
        return self.__city   
add1=Adress('Singarayakonda', 23456, 'haryana')
cust=Customer("nitish","male",add1 )
cust.print_address()



###################INHERITANCE############

# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class SmartPhone(Phone):
    pass
SmartPhone(1000,"Apple","13px").buy()


# multilevel
class Product:
    def review(self):
        print ("Product customer review")
class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class SmartPhone(Phone):
    pass
s=SmartPhone(20000, "Apple", 12)
s.buy()
s.review()


# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class SmartPhone(Phone):
    pass
class FeaturePhone(Phone):
    pass
SmartPhone(1000,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()


# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class Product:
    def review(self):
        print ("Customer review")
class SmartPhone(Phone, Product):
    pass
s=SmartPhone(20000, "Apple", 12)
s.buy()
s.review()


class Parent:
    def __init___(self):
        self.name="Mohammad"
    def login(self):
        print("login")

#Child class    
class Student(Parent):
    def __init__(self):
        self.rollno=13452
    def enroll(self):
        print("Enroll into the course") 
s=Student()      
print(s.name)



class phone: #parent class
    def __init___(self, price, brand):
        self.price=price
        self.brand=brand
    def buy(self):
        print("Buying a phone")
class Smartphone(phone): #child class
    pass
#creating an object
s1=Smartphone(20000, "apple") #child class object
print(s1.brand)
s1.buy()


################################   METHOD OVERRIDING     ##########################

class Phone: #parent class
    def __init__(self, price, brand):
        self.price=price
        self.brand=brand
    def buy(self):
        print("Buying a phone")    
class Smartphone(Phone): #child class inheriting parent class
    pass   
#object creation
s1=Smartphone(2000, "apple")
print(s1.brand) #using parent property
s1.buy() #using parent method 








## the diamond problem
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class Product:
    def buy(self):
        print ("Product buy method")
# Method resolution order
class SmartPhone(Phone,Product):
    pass
s=SmartPhone(20000, "Apple", 12)
s.buy()



class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
class C(B):
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj2.m2()+obj3.m2())    
    


#POLYMORPHISM
"Method Overriding"
"method Overloading"
"Operator Overloading"
 class shape:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a*
        else:
            return a*b    
s=shape()
print(s.area(2))
print(s.area(3,4))


print('Hello'+'world')
print([1,2,3]+[4,5])





class phone:
    def buy(self):
        print("Buying a normal phone")

class Smartphone(phone):
    def buy(self):
        print("Buying a smartphone") #override
s=Smartphone()
s.buy()       



class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)



# object without a reference
class Person:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

p = Person()
q = p


class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print('Hi my name is',person.name,'and I am a',person.gender)
  p1 = Person('ankit','male')
  return p1

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)


class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print(id(person))
  person.name = 'ankit'
  print(person.name)

p = Person('nitish','male')
print(id(p))
greet(p)
print(p.name)


#Object Mutability
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  person.name = 'ankit'
  return person
p = Person('nitish','male')
print(id(p))
p1 = greet(p)
print(id(p1))



# instance var -> python tutor
class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

p1 = Person('nitish','india')
p2 = Person('steve','australia')




class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    #self.menu()

  def get_balance(self):
    return self.__balance

  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')


# need for static vars
class Atm:
  __counter = 1
  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    self.cid = Atm.__counter
    Atm.__counter = Atm.__counter + 1
    #self.menu()

  # utility functions
  @staticmethod
  def get_counter():
    return Atm.__counter
  def get_balance(self):
    return self.__balance

  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')



