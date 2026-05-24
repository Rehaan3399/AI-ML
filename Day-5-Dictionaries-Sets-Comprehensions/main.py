############################################PHASE 1 — DICTIONARIES############################################
#Program 1 Creating AND Accessing 
"""student={
    "name":"Mohammad",
    "age":24,
    "Course":"MCA",
}
print(student["name"])
print(student["age"])
"""
"""
office={
    "company":"Soyasis",
    "Location":"Vijayawada",
    "Phone":96655454,
}
print(office["company"])
"""

#PROGRAM 2 — .get()
"""
Details={
    "lastname":"Mohammad",
    "surname":"Shaik",
}
print(Details.get("lastname"))
print(Details.get("surname"))"""

#PROGRAM 3 — .keys() .values() .items()
"""
office={
    "company":"Soyasis",
    "Location":"Vijayawada",
    "Phone":96655454,
}
print(office.values())
print(office.keys())
print(office.items())
"""
#PROGRAM 4 — LOOP THROUGH DICTIONARY
"""
names={
    "name":"Rajiya",
    "age":78,
    "ID":122
}
for i,j in names.items():
    print(i,j)
"""
#PROGRAM 5 — WORD FREQUENCY COUNTER



#############################################PHASE 2 — SETS#########################################
#CReating SET
"""numbers={1,2,34,66}
print(numbers)
print(type(numbers))"""

#PROGRAM 7 — REMOVE DUPLICATES
numbers=[1,3,89,77,33, 33]
print(set(numbers))

#PROGRAM 8 — ADD + REMOVE
"""numbers={1,2,4,0,5,4}
numbers.add(66)
numbers.remove(4)
print(numbers)
"""
#PROGRAM 9 — UNION
pro1={1,2,4}
pro2={2,5,6}
print(pro1.union(pro2))

#PROGRAM 10 — INTERSECTION
"""pro1={1,2,4}
pro2={2,5,6}
print(pro1.intersection(pro2))"""

#PROGRAM 11 — DIFFERENCE
"""pro1={1,2,4}
pro2={2,5,6}
print(pro1.difference(pro2))"""

######################################PHASE 3 — LIST COMPREHENSION##########################################
#PROGRAM 12 — NORMAL LOOP VERSION
squares=[]
for i in range(1,6):
    squares.append(i*i)
print(squares)    


#PROGRAM 13 — LIST COMPREHENSION VERSION
#[expression for variable in iterable]
square=[i*i for i in range(1,6)]
print(square)

#ROGRAM 14 — CONDITION IN COMPREHENSION
#[expression for variable in iterable if condition]
even_squares=[i*i for i in range(1,11) if i%2==0]
print(even_squares)

############################################PHASE 4 — DICTIONARY COMPREHENSION######################################
#PROGRAM 15
numbers={1,2,3,4,5}
squares={i:i*i for i in numbers}
print(squares)

details={"name":"Mohammad",
         "age":"Twenty four",
         "course":"MCA"}
upper_details={a:b.upper() for a,b in details.items()}
print(upper_details)

##########################################PHASE 5 — SET COMPREHENSION#######################################
#program 16
set={i*i for i in range(1,11)}
print(set)

"""
list
dict
set
Tuple comprehension doesn't truly exis"""

##############################################PHASE 6 — ZIP######################################################
#PROGRAM 17
names = ["Ali","Rahul","John"]
marks = [90,85,95]
result=zip(names,marks)
print(list(result))

#PHASE 7 — ENUMERATE
#PROGRAM 18
names=["Mohammad", "Rehaan", "Shaik"]
for index, value in enumerate(names):
    print(index, value)


##############################################################PHASE 8 — MAP######################################
#PROGRAM 19
numbers=[1,2,3,45,6]
squares=map(lambda i:i*i, numbers)
print(list(squares))


###########################################################PHASE 9 — FILTER#########################################
numbers=[1,2,3,4,5,6,78,9,9845]
even_numbers=filter(lambda i:i%2==0, numbers)
print(list(even_numbers))


#######################################FINAL PHASE — HACKERRANK STYLE PROBLEMS########################################
#PROBLEM 1 — CHARACTER FREQUENCY
from collections import Counter
x="Python"
print(Counter(x))
       
from collections import Counter
sentence="Koding Caravan"
print(Counter(sentence))

#PROBLEM 2 — FIND COMMON ELEMENTS
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print(common)


#Dictionary From List
names = ["Ali","Rahul","John"]
marks = [90,85,95]
student_data = dict(zip(names,marks))
print(student_data)

#Squares only Even Numbers
numbers = [1,2,3,4,5,6]
result = [i*i for i in numbers if i%2==0]
print(result)


#Word Length Dictionary
words = ["apple","banana","kiwi"]
lengths = {
    word:len(word) for word in words
}
print(lengths)




