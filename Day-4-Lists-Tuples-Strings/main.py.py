#Creating The List
"""my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))

#Acceessing elements of the list
my_list=[1,2,3,4,5]
print(my_list[1]) #OP:2

#List Slicing
my_list=[2,7,45, 9, 23, 90, 88]
print(my_list[2:5]) #OP:[45,9, 23]
print(my_list[:3]) #OP:[2,7,45]
print(my_list[::-1]) #OP:[88, 90, 23, 9, 45, 7, 2]

#Using Append() method to add on element to the list
my_list=[2,3,4,5,85,45,4,35]
my_list.append(100)
print(my_list)
"""
"""
#PROGRAM 5 — INSERTing element in the list
my_list=[1,2, 56, 35, 35, 6, 35, 45]
my_list.insert(0, 100)
print(my_list)

#PROGRAM 6 — POP (Deleting values from the list using index)
my_list=[1,2, 56, 35, 35, 6, 35, 45]
my_list.pop(7)
print(my_list)

#Deleting Values from the list
my_list1=[1,2, 56, 35, 35, 6, 35, 45]
my_list.remove(56)
print(my_list)"""

"""
my_list2=["Mohammad", "Jasmine", "Sana", "Ayesha"]
my_list2.remove("Jasmine")
print(my_list2)
#pop() → by index
#remove() → by value


#PROGRAM 8 — SORTing a List
my_list1=[1,2, 56, 35, 35, 6, 35, 45]
my_list1.sort()
print(my_list1)

#Program 9- revese a List
my_list2=["Monalisa", "Jaffa", "Robo", "chitty"]
my_list2.reverse()
print(my_list2)

#PROGRAM 10 — LIST ITERATION
my_list3=[2, 7, 89, "john", "deisel"]
for i in my_list3:
    print(i)

"""
###########################################PART 2 — TUPLES#####################################
#create Tuple
"""
tup=(10,20,30,32,45)
print(tup)
print(type(tup))"""


#PROGRAM 12 — TUPLE IMMUTABILITY
"""
numbers=(12,34,5,6,68)
number[0]=100
print(numbers)
"""
#PART 3 — STRINGS
#PROGRAM 13 — STRING SLICING
"""text="Python"
print(text[1:3])
print(text[::-1])
print(text[0:5:2])
"""

#PROGRAM 14 — UPPER LOWER
text="Mohammad"
print(text.upper())

#COnverting to Lowercase
text="REHAAN"
print(text.lower())

#PROGRAM 15 — REPLACE
text2="I love Python"
print(text2.replace("I", "YOU"))

#PROGRAM 16 — SPLIT
text44="My name is Mohammad Rehaan"
print(text44.split())

#PROGRAM 17 — JOIN
text5="Mohammad", "Rehaan", "is", "The", "best"
print(" ".join(text5))

#PROGRAM 18 — STRIP
text6="      Mohamma     "
z="     Rehaan     "
print(text6.strip())
print(z)

#PROGRAM 19 — F-STRINGS
Age=22
name="Mohammad"
info=f"My age is {Age} and my name is {name} "
print(info)

#PROGRAM 20 — STRING ITERATION
sample="Rehhaaa"
for i in sample:
    print(i)

#DAY 4 — HACKERRANK STYLE PROBLEMS
#PROBLEM 1 — COUNT EVEN NUMBERS
"""numbers=[10, 30, 5, 6, 78, 9, 44]
count=0
for i in numbers:
    if i%2==0:
        count+=1
print(count)    """

#PROBLEM 2 — FIND LARGEST STRING
"""words=["Mohammad", "Jaswanth", "rehman", "haramee"]
for i in words:
    if len(i)>words[i+1]
        print(i)
     else:
        print(words[i+1])   """

#PROBLEM 3 — REVERSE EACH WORD
"""words=["Mohammad", "Jaswanth", "rehman", "haramee"]
for i in words:
    print(i[::-1])"""

#PROBLEM 4 — REMOVE DUPLICATES
"""numbers = [1,2,2,3,4,4,5]
nil=[]
for i in numbers:
    if i not in nil:
        nil.append(i)
print(nil)"""

#PROBLEM 5 — PALINDROME STRING
"""
a="Madam"
z=a.lower()
m=z[::-1]
if z==m:
    print("palimdrome")
else:
    print("Not a Palimdrome")    

text55="Rehaan"
z=a.lower()
m=a[::-1]
if z==m:
    print("palimdrome")
else:
    print("Not a Palimdrome")   
"""

#PROBLEM 6 — COUNT VOWELS
"""letters="Mohammad"
count=0
z=[]
for i in letters:
    if i=="a" or  i=="e" or i=="i" or i=="o" or i=="u":
       if i  not in z:
           z.append(i)
           count+=1
print(count,z)    
"""

#PROBLEM 7 — SECOND LARGEST NUMBER
"""numbers = [10,20,5,40,30]
for i in numbers:
    numbers.sort()
print(numbers[1])""" 

#PROBLEM 8 — WORD COUNTER
"""inp="My name is Mohammad rehaan"
count=0
z=inp.split()
for i in z:
    count+=1
print(count)"""

#PROBLEM 9 — CHARACTER FREQUENCY
text = "pythonn"
count=0
for i in text:
    print(text.count(i))

#PROBLEM 10 — MERGE LISTS
a=["Mohammad"]
z=["Rehaan"]
print(a+z)