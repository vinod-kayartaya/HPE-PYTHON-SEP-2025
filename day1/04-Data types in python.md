# Data types in python

Python is one of the most popular programming languages in the world. One reason for its popularity is its **simplicity and flexibility with data types**. Unlike some languages where you must explicitly declare types, Python infers the type of a variable at runtime.

In this blog, we'll walk through the most common built-in data types in Python: **int, float, bool, str, list, tuple, dict, and set**. Each comes with powerful features, and as a developer (like myself, Vinod Kayartaya), you'll frequently use them in your applications.

## 1. Boolean (`bool`)

Booleans represent **True or False** values, often used in conditions.

```python
# Example by Vinod Kayartaya
is_trainer = True
is_student = False

print(is_trainer and not is_student)  # True
```

## 2. Integers (`int`)

An integer represents **whole numbers**, positive or negative, without decimals.

```python
# Example by Vinod Kayartaya
age = 52
year = 2025
score = -10

print(type(age))  # <class 'int'>
print(age + year) # 2077
```

## 3. Floating-Point Numbers (`float`)

Floats are **decimal numbers** used when precision matters.

```python
# Example by Vinod Kayartaya
pi = 3.14159
temperature = -5.6

print(type(pi))  # <class 'float'>
print(pi * 2)    # 6.28318
```

## 4. Strings (`str`)

Strings are **sequences of characters**, enclosed in single or double quotes.

```python
# Example by Vinod Kayartaya
name = "Vinod Kayartaya"
greeting = f"Hello, {name}!"

print(greeting)  # Hello, Vinod Kayartaya!
```

Strings support slicing and many methods:

```python
text = "Python Programming"
print(text.lower())    # python programming
print(text.upper())    # PYTHON PROGRAMMING
print(text[0:6])       # Python
```

## 5. Tuples (`tuple`)

Tuples are **ordered, immutable collections**. Once defined, you cannot modify them.

```python
# Example by Vinod Kayartaya
coordinates = (10.5, 20.3)
print(coordinates[0])  # 10.5
```

Tuples are useful when data should not change (e.g., database keys, configurations).

## 6. Lists (`list`)

Lists are **ordered, mutable collections** that can store different types of data.

```python
# Example by Vinod Kayartaya
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
```

### Common List Methods

```python
fruits.append("mango")   # add item
fruits.insert(1, "grape") # insert at index
fruits.remove("banana")  # remove item
fruits.sort()            # sort list
print(fruits)
```

### List Slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[::-1])  # reversed list
```

### List Comprehensions

A **Pythonic way** to create lists.

```python
# Squares of numbers 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

## 7. Sets (`set`)

Sets are **unordered collections of unique items**.

```python
# Example by Vinod Kayartaya
unique_numbers = {1, 2, 3, 3, 2, 1}
print(unique_numbers)  # {1, 2, 3}
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
```

## 8. Dictionaries (`dict`)

Dictionaries store **key-value pairs**. Keys must be unique and immutable.

```python
# Example by Vinod Kayartaya
student = {"name": "Vinod", "age": 52, "role": "Trainer"}
print(student["name"])  # Vinod
```

### Common Dictionary Methods

```python
print(student.keys())      # dict_keys(['name', 'age', 'role'])
print(student.values())    # dict_values(['Vinod', 52, 'Trainer'])
student["location"] = "Bengaluru"  # add new key
student.pop("age")         # remove key
print(student)
```

### Dictionary Comprehensions

```python
# Square dictionary
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Conclusion

Python data types form the backbone of programming. Whether you are handling numbers, text, or collections, understanding these types makes your code efficient and powerful.
