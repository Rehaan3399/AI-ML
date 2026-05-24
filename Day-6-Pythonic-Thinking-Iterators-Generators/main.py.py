###########################PHASE 1 — ITERATORS###########################
#2. Magic Methods Under the Hood: __iter__ and __next__
###check if something is an Iterable or an Iterator? We use Python's built-in dir() function

my_list=[1,2,3]
print("__iter__" in dir(my_list))
print("__next__" in dir(my_list))

## Transforming Iterable into an Iterator using iter() function
my_iterator=iter(my_list)
print("__iter__" in dir(my_list))
print("__next__" in dir(my_iterator))


#PROGRAM 1 — iter() + next()
numbers = [10,20,30]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))

nums=[1,2,3,4,556,6]
z=iter(nums)
print(next(z))
print(next(z))


#creating my own for loop
def mera_khudka_for_loop(iterable):
while True:
    try:
        print(next(iterable))
    except Stopiteration:
        break  

"""












######################################################generators######################################################
L=[x for x in range(1000000000)]
import sys
sys.getsizeof(L)


x=range(1000000000)
import sys
sys.getsizeof(x)


def gen_demo():
    yield 1
    yield 2
    yield 3
gen=gen_demo()
print(next(gen))
print(next(gen))
print(next(gen))

#OR

def gen_demo():
    yield 1
    yield 2
    yield 3
gen=gen_demo()
for i in gen:
    print(i)


#PHASE 3 — BASIC GENERATOR
def numbers():
    yield 1
    yield 2
    yield 3  
result=numbers()     
print(next(result))  
print(next(result))
print(next(result))

#Looping through Generators
#program 4:
def fruits():
    yield "banana"
    yield "mango"
    yield "grapes"
    yield "orange"
for i in fruits():
    print(i)  

  
 

    





################################################### SHALLOW COPY VS DEEP COPY #######################################
import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1+5)
print(arr1*2)

#vectorized addition of two arrays
arr2=np.array([3,5,6,8,9])
print(arr1+arr2)
print(np.sum(arr1))
print(np.sin(arr2))
print(np.cos(arr1))
print(np.min(arr2))
print(np.sqrt(arr2))

#Aliasing (New name, Same Memory Point)
a=np.array([1,2,3])
b=a
print(id(a))
print(id(b))
b[0]=100
print(a) #modifying b also modifies a because they point to the same memory location

#Shallow Copy Using view() method
a=np.array([1,2,3,4,5])
b=a.view()
print(id(a)==id(b)) #False because they are different objects in memory
b[0]=100
print(a) #modifying b also modifies a

#Deep copy using copy() method
a=np.array([1,2,3,4,5,6,9])
b=a.copy()
print(id(a)==id(b)) #false because they are different objects in memory
b[0]=100
print(a) #modyfying b doesnot modify a because they are different objects in memory

