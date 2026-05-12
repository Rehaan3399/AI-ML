# Day 4 — Lists + Tuples + Strings

## Topics Learned
- List CRUD operations
- list slicing
- append()
- insert()
- pop()
- remove()
- sort()
- reverse()
- tuples
- tuple immutability
- string slicing
- upper()
- lower()
- replace()
- split()
- join()
- strip()
- f-strings

---

# List Concepts

## append()
Adds item at end of list.

Example:
```python
fruits.append("mango")
```

## insert()
Adds item at specific index.

Example:
```python id="d9k4tm"
fruits.insert(1,"orange")
```

## pop()
Removes item using index.

Example:
```python id="r6m1qa"
fruits.pop()
```

## remove()
Removes item using value.

Example:
```python id="j3v8pn"
fruits.remove("banana")
```

## sort()
Sorts list in ascending order.

## reverse()
Reverses list order.

---

# Tuple Concepts

## Tuple
Tuple is immutable collection.

Example:
```python id="x8q5tm"
numbers = (10,20,30)
```

Cannot modify tuple values.

---

# String Concepts

## String Slicing

Example:
```python id="w4m7qa"
text[::-1]
```

Used for reversing string.

---

## split()

Converts string into list.

Example:
```python id="u1k9pn"
text.split()
```

---

## join()

Converts list into string.

Example:
```python id="e5v2tm"
" ".join(words)
```

---

## strip()

Removes extra spaces.

Example:
```python id="f7q3ra"
text.strip()
```

---

## replace()

Replaces old text with new text.

Example:
```python id="p8m4qa"
text.replace("Java","Python")
```

---

## f-strings

Modern string formatting.

Example:
```python id="z2v6pn"
print(f"My name is {name}")
```

---

# Problems Solved
1. Count even numbers
2. Find largest string
3. Reverse each word
4. Remove duplicates
5. Palindrome checker
6. Count vowels
7. Second largest number
8. Word counter
9. Character frequency
10. Merge lists

---

# Mistakes I Made
- forgot indexes sometimes
- confused pop and remove
- slicing confusion initially
- tuple immutability confusion

---

# Things I Understood Well
- list methods
- slicing
- palindrome logic
- split and join
- loops with strings

---

# Overall Learning
Today I learned how Python handles collections and strings using lists, tuples, and string methods.