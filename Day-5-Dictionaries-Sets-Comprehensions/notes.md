# Day 5 — Dictionaries + Sets + Comprehensions

## Topics Learned
- Dictionary CRUD
- .get()
- .keys()
- .values()
- .items()
- Sets
- union()
- intersection()
- difference()
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- zip()
- enumerate()
- map()
- filter()

---

# Dictionary Concepts

## Dictionary
Stores data in key-value pairs.

Example:
```python
student = {
    "name":"Mohammad",
    "age":22
}
```

---

## .get()

Safely accesses value from dictionary.

Example:
```python id="w1q8pn"
student.get("name")
```

Returns None if key not found.

---

## .keys()

Returns all dictionary keys.

---

## .values()

Returns all dictionary values.

---

## .items()

Returns key-value pairs.

Used in loops.

Example:
```python id="g5m2ra"
for key,value in student.items():
```

---

# Word Frequency Counter

Used dictionary to count repeated words.

Example output:
```python id="r7k4tm"
{
 'python':2,
 'is':2
}
```

---

# Set Concepts

## Set
Stores unique values only.

Example:
```python id="j3v9qa"
numbers = {1,2,3}
```

---

## union()

Combines values from two sets.

---

## intersection()

Finds common values.

---

## difference()

Finds values present in first set but not second.

---

# Comprehensions

## List Comprehension

Example:
```python id="x8m1pn"
[i*i for i in range(1,6)]
```

---

## Dictionary Comprehension

Example:
```python id="n6q7tm"
{i:i*i for i in range(1,6)}
```

---

## Set Comprehension

Example:
```python id="p4k2ra"
{i*i for i in range(1,6)}
```

---

# zip()

Combines multiple iterables together.

Example:
```python id="u9v5tm"
zip(names,marks)
```

---

# enumerate()

Returns index and value together.

Example:
```python id="m2q8pn"
enumerate(fruits)
```

---

# map()

Transforms all values using function.

Example:
```python id="k7m4ra"
map(lambda x:x*x, numbers)
```

---

# filter()

Filters values based on condition.

Example:
```python id="d1v9tm"
filter(lambda x:x%2==0, numbers)
```

---

# Problems Solved
1. Character frequency
2. Common elements
3. Dictionary from lists
4. Square even numbers
5. Word length dictionary

---

# Mistakes I Made
- confusion between map and filter
- forgot set uniqueness sometimes
- comprehension syntax mistakes initially

---

# Things I Understood Well
- dictionary iteration
- zip()
- enumerate()
- list comprehensions
- word frequency logic

---

# Overall Learning
Today I learned Pythonic ways to process and manipulate collections using dictionaries, sets, comprehensions, map, and filter.