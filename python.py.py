
#If there is agregation bbetween the two classes then we can use getters and setters to access the private members of  the class. 
"""class Customer:
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
 
 """
"""
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
"""
 




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


"""
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
print(s.name)"""


"""
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
s1.buy()"""


################################   METHOD OVERRIDING     ##########################
"""
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
s1.buy() #using parent method """








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
























"""

class phone:
    def buy(self):
        print("Buying a normal phone")

class Smartphone(phone):
    def buy(self):
        print("Buying a smartphone") #override
s=Smartphone()
s.buy()        """