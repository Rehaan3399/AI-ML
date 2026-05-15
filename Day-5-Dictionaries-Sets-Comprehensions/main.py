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

#PROBLEM 1 — CHARACTER FREQUENCY
"""text="Hello Python"
frequency={}
for i in text:"""


#PROBLEM 2 — FIND COMMON ELEMENTS
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common_elements=[]
for i in list1:
    if i in list2:
        common_elements.append(i)
print(common_elements)   


#PROBLEM 3 — DICTIONARY FROM LISTS

names = ["Ali","Rahul","John"]
marks = [90,85,95]
result=zip(names, marks)
print(dict(result))

#PROBLEM 4 — SQUARE ONLY EVEN NUMBERS
numbers=[2,34,56,78,93,35,10,234,54,78]
even_squares=[i*i for i in numbers if i%2==0]
print(even_squares)

#PROBLEM 5 — WORD LENGTH DICTIONARY
words = ["apple","banana","kiwi"]

