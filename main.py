"""#Program 1 — Check positive or negative
num=int(input("Enter the number:"))
if num>0:
    print("Positive Number",num)
else:
    print("Negative Number",num)"""
"""
#Program 2 — Greatest of two numbers
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if num1>num2:
    print(num1," is bigger than ", num2)
else:
    print(num2, "is bigger than ",num1)"""

""" #Program 3 — Grade calculator using elif
marks=int(input("Enter the marks: "))
if marks>=90:
    print("A Garde")
elif marks>=80 and marks<90:
    print("B Grade")
elif marks>50 and marks<80:
    print("C Grade")
else:
    print("Fail")            """

""" #Program 4 — Print 1 to 10 using for loop
for i in range(1,11):
    print(i,end=", ")  """
""" #Program 5 — Print even numbers 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i,end=", ") """

"""#Program 6 — Sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum=sum+i
print("sum of first 10 natural numbers is ",sum)"""


"""
#Program 7 — Multiplication table
num=int(input("Enter the number to print the multiplication table:"))
for i in range(1,11):
    print(num, "*",i,"=",num*i)"""


"""#Nested Loops
for i in range(1,6):
    for j in range(0,i):
        print("*", end=" ")
    print(" ")    
    """
"""#Print numbers 1 to 20, but only multiples of 3.
for i in range(1,21):
    if i%3==0:
        print(i, end=" ")"""

"""#Print numbers from 1 to 30, but only odd numbers.
for i in range(1,31):
    if i%2!=0:
        print(i,end= " ")"""

"""#Print numbers from 10 down to 1
for i in range(10,0,-1): 
    print(i,end=" ")   """  

#Print numbers from 1 to 20 and beside each number print whether it is Even or Odd.
""" OutPut:
1 Odd
2 Even
3 Odd
4 Even
..."""  
""" for i in range(1,21):
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"odd")    """

"""#Print all numbers from 1 to 50 divisible by 5.
for i in range(1,51):
    if i%5==0:
        print(i, end=" ")"""

#Using while loop print 1 to 10.

"""a=10
i=1
while i<=a:
    print(i,end=" ")
    i=i+1"""

"""OP:
1
1 2
1 2 3
1 2 3 4"""
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print(' ') """  

#PART C — break
#STOP AT 5
"""for i in range(1,11):
    if i==5:
        break
    print(i, end=" ")"""
#PART D — continue
#skip 5
for i in range(1,11):
    if i==5:
        continue
    print(i, end=" ")

#PART E — pass
for i in range(1,6):
    if i==3:
        pass
    print(i)
    
#Solve 10 HackerRank Python problems (Introduction section)

