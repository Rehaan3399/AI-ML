🐍 PYTHON CONTROL FLOW MASTER NOTES (ZERO → HERO)
1. if Statement
➤ Meaning:

Used when you want Python to do something only when a condition is true.

Real life:

If it rains → take umbrella.

Syntax:
if condition:
    statement
Example:
age = 20

if age >= 18:
    print("Eligible to vote")
How Python thinks:
Checks age >= 18
If True → print line
If False → skip
2. if else Statement
➤ Meaning:

When one condition is checked and Python must choose one of two paths.

Syntax:
if condition:
    statement1
else:
    statement2
Example:
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
Python thinking:

Condition true? → do if block
Condition false? → do else block

3. if elif else
➤ Meaning:

When there are multiple conditions.

Syntax:
if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
else:
    statement
Example:
marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
Important:

Python checks from top to bottom.
First true condition only executes.

4. Comparison Operators

Used to compare two values.
Result always True or False.

Operator	Meaning	Example
==	equal to	5 == 5
!=	not equal	5 != 3
>	greater than	8 > 2
<	less than	3 < 9
>=	greater or equal	5 >= 5
<=	less or equal	2 <= 4
Example:
a = 10
b = 20

print(a < b)   # True
print(a == b)  # False

These are mainly used inside if.

5. for Loop
➤ Meaning:

Repeat something fixed number of times OR loop through items.

Syntax:
for variable in sequence:
    statement
Example:
for i in range(5):
    print(i)

Output:

0
1
2
3
4
Python thinking:

Take one value from range → execute → repeat.

6. while Loop
➤ Meaning:

Repeat while condition remains true.

Syntax:
while condition:
    statement
Example:
i = 1

while i <= 5:
    print(i)
    i = i + 1
Important:

In while loop update is compulsory.
Otherwise infinite loop.

Bad:

while i <= 5:
    print(i)

This never stops.

7. range() Function

Used to generate numbers automatically.

Forms:
range(stop)
range(5)

→ 0 to 4

range(start, stop)
range(1, 6)

→ 1 to 5

range(start, stop, step)
range(1, 10, 2)

→ 1 3 5 7 9

Example:
for i in range(1, 6):
    print(i)
8. break
➤ Meaning:

Immediately stop the loop.

Example:
for i in range(1, 10):
    if i == 5:
        break
    print(i)

Output:

1
2
3
4

When i==5, loop dies.

9. continue
➤ Meaning:

Skip current iteration and go next.

Example:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5

3 skipped.

10. pass
➤ Meaning:

Do nothing temporarily.

Used when syntax requires block but logic not written yet.

Example:
for i in range(5):
    if i == 2:
        pass
    print(i)

No error. Python simply ignores.

Mostly used in:
future coding
empty functions
placeholders
11. Nested Loop Basics

Loop inside another loop.

Syntax:
for i in range(3):
    for j in range(2):
        print(i, j)
Output:
0 0
0 1
1 0
1 1
2 0
2 1
Real use:
patterns
tables
matrix
combinations
How it works:

Outer loop one time → inner loop full run.