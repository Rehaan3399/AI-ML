
# Serialization & Deserialization (Zero to Hero Notes)

## What Problem Are We Solving?

Imagine you create a Python dictionary:

```python
student = {
    "name": "Mohammad",
    "marks": 95
}
```

This dictionary lives only in RAM (Memory).

```text
Python Program Running
        ↓
Dictionary in Memory
```

When the program closes:

```text
Program Ends
      ↓
Memory Cleared
      ↓
Dictionary Lost
```

Data is gone.

So we need a way to save Python data permanently in a file.

---

# What is Serialization?

## Definition

Serialization means:

```text
Python Object
      ↓
File Format
```

Converting a Python object into a format that can be stored in a file.

### Real-Life Example

Suppose you write a student's information on paper.

```text
Brain Memory
      ↓
Paper
```

You converted information into a storable form.

That is similar to Serialization.

---

# JSON (JavaScript Object Notation)

JSON is a popular format used to store data.

Example:

Python Dictionary:

```python
student = {
    "name": "Mohammad",
    "age": 24
}
```

JSON File:

```json
{
  "name": "Mohammad",
  "age": 24
}
```

JSON is simply a structured text format.

---

# json.dump()

## Purpose

Used to save Python data into a JSON file.

### Syntax

```python
json.dump(python_object, file_object)
```

### Example

```python
import json

student = {
    "name": "Mohammad",
    "age": 24
}

with open("student.json", "w") as file:
    json.dump(student, file)
```

### Internal Flow

```text
Python Dictionary
        ↓
    json.dump()
        ↓
student.json
```

File Content:

```json
{
  "name": "Mohammad",
  "age": 24
}
```

### Memory Trick

```text
dump = Drop data into file
```

---

# What is Deserialization?

## Definition

Deserialization means:

```text
File Data
      ↓
Python Object
```

Converting stored file data back into Python objects.

---

# json.load()

## Purpose

Used to read JSON data and convert it back to Python objects.

### Syntax

```python
json.load(file_object)
```

### Example

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

Output:

```python
{'name': 'Mohammad', 'age': 24}
```

### Check Type

```python
print(type(data))
```

Output:

```python
<class 'dict'>
```

Notice:

The data came back as a Python dictionary.

This is the power of Deserialization.

---

# Why Not Use Normal Text Files?

Example:

```python
with open("demo.txt", "w") as file:
    file.write(str(student))
```

Later:

```python
with open("demo.txt", "r") as file:
    data = file.read()
```

Output:

```python
"{'name':'Mohammad','age':24}"
```

Type:

```python
<class 'str'>
```

You get a string, not a dictionary.

With JSON:

```text
JSON File
      ↓
json.load()
      ↓
Dictionary
```

Original data structure is preserved.

---

# dump() vs dumps()

Students often confuse these.

## dump()

Writes directly to a file.

```python
json.dump(student, file)
```

Flow:

```text
Dictionary
    ↓
 File
```

---

## dumps()

Returns a JSON string.

```python
json_string = json.dumps(student)
```

Output:

```python
'{"name":"Mohammad","age":24}'
```

Type:

```python
<class 'str'>
```

No file is created.

### Memory Trick

```text
dump  = File

dumps = String
```

"s" means string.

---

# load() vs loads()

## load()

Reads from file.

```python
data = json.load(file)
```

---

## loads()

Reads from JSON string.

```python
json_string = '{"name":"Mohammad"}'

data = json.loads(json_string)
```

Output:

```python
{'name': 'Mohammad'}
```

---

# JSON Supported Data Types

JSON understands:

```text
dict
list
str
int
float
bool
None
```

Example:

```python
data = {
    "name":"Mohammad",
    "marks":[90,95,88]
}
```

Works perfectly.

---

# JSON Limitation

JSON does NOT understand custom classes.

Example:

```python
class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Mohammad")
```

Now:

```python
json.dump(s1,file)
```

Error:

```text
Object of type Student is not JSON serializable
```

Why?

Because JSON only understands:

```text
dict
list
str
int
float
bool
```

It does not know what a Student object is.

---

# Solution

Convert object into dictionary.

```python
data = {
    "name": s1.name
}

json.dump(data,file)
```

Now JSON understands it.

---

# Interview Questions

### What is Serialization?

Converting Python objects into a storable format.

### What is Deserialization?

Converting stored file data back into Python objects.

### Difference between dump() and dumps()?

```text
dump()  → File

dumps() → String
```

### Difference between load() and loads()?

```text
load()  → Reads File

loads() → Reads String
```

### Why use JSON?

* Data persistence
* API communication
* Configuration files
* Database interaction

---

# Quick Revision

```text
Serialization
Python Object → File

Deserialization
File → Python Object

dump()
Save to file

load()
Read from file

dumps()
Convert to JSON string

loads()
Convert JSON string to Python object

JSON understands:
dict, list, str, int, float, bool

JSON does not understand:
Custom Python Classes
```

## One-Line Memory Trick

```text
dump  = Save

load  = Read

Serialization = Python → File

Deserialization = File → Python
```

These notes are enough to understand JSON serialization even if you revisit them months later.
