
"""def function_name():
    print("Mohammad Rehaan")"""


#PROGRAM 1 — SIMPLE FUNCTION USING def (Greet)
"""def greet(name):
    print("Hello", name, "Good Morning!")
greet("Mohammad")    
greet("Rahul")"""

#PROGRAM 3 — FUNCTION WITH RETURN
"""def add(a,b):
    return a+b
print(add(2,3))
"""
#PROGRAM 4 — POSITIONAL ARGUMENTS vs KEYWORD ARGUMENTS
"""
def greet(name, college, ID):
    return name, college, ID
print(greet("rise college", 1214, "mohan"))
print(greet("Mohammad", "Pace College", 1234))
print(greet("ravi", "Pace University", 2746))
print(greet( ID=1234, name="Mohammad", college="Harshini Degree College"))
"""

#Program 5 Default Arguments
"""
def greet(name="Other"):
    return name
print(greet("Mohammad"))    
print(greet())"""


#Program 6 *args
"""
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum 
print(add(1,2,3,4,5))"""

#Program 7 **kwargs
"""
def greet(**kwargs):
    return kwargs
print(greet(name="mohammad", college="rajasekhara", ID=18762))"""

"""#Program 8 Lambda Function
z=lambda a,b:a*b
print(z(2,3))"""

#Program 9 Nested Function (function inside a function)
"""def outer_function():
    print("This is an outer function")
    def inner_function():
        print("This is an inner functionn")
        inner_function()
ouuter_function()"""  

#bring factorial function from another file.(function_utils.py)
"""from function_utils import factorial
print(factorial(3))
"""
#bring Palindrome Checker from another file.(function_utils.py)
"""from function_utils import  is_palimdrome
print(is_palimdrome("Bye"))
print(is_palimdrome("level"))
"""

#bring Fibancaci series from another file(function_utils.py)
# 0 1 1 2 3 5 8 13...
"""
from function_utils import fibanacci
fibanacci(30)"""

#bring prime checker from another file
'''from function_utils import is_prime
print(is_prime(11))
print(is_prime(15))'''

#bring reverse from another file
"""from function_utils import reverse_string
print(reverse_string("Mohammad"))"""

"""#bring AVG from another file
from function_utils import find_average
print(find_average([10,2, 30]))"""

#bring Lambda Calculator from another file
from function_utils import sub
print(sub(50,50))

from function_utils import div
print(div(50,10))

from function_utils import mul
print(mul(3,5))