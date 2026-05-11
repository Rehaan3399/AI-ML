#Function 1 Factorial
"""def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))"""

#Function 2 Palindrome Checker
"""def is_palimdrome(s.lower()):
    z=s[::-1]
    if s==z:
        return "palimdrome"
    else:
        return "not a polimdrome"
print(is_palimdrome("mam"))
print(is_palimdrome("hello"))"""

#Function 3 Fibonacci Series
#0 1 1 2 3 5 8 13 ...
"""def fibanacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print(c)
fibanacci(10)  
"""
#Function 4 Prime Checker
"""def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "prime"
    else:
        return "not a prime"
print(is_prime(7))
"""
#Reversing a String 
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

#Finding the max  number in the list
"""def find_max(lst):
    return max(lst)
z=find_max([10, 20, 2, 5, 7, 15])    
print(z)
"""

#Finding the AVERAGE of the numbers in the list
"""def find_average(lst):
    for i in range(len(lst)):
        sum=0
        sum=sum+i
    return sum/len(lst)
print(find_average([10,2,34,88,9]))    """

#Function 9 Flatten List




"""#Function 10 Lambda Calculator
add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div =lambda a,b:a/b
print(add(10,20))
print(sub(5,4))"""