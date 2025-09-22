# Built-in Modules in Python

One of the biggest strengths of Python is its **standard library** – a collection of built-in modules that provide ready-made functionality. Instead of writing everything from scratch, Python developers can **reuse these built-in tools**.

This article will guide you through the **most commonly used built-in modules in Python**, along with examples.

## 1. `math` – Mathematical Functions

The `math` module provides advanced mathematical operations.

```python
import math

print(math.sqrt(25))     # 5.0
print(math.factorial(5)) # 120
print(math.pi)           # 3.141592653589793
print(math.sin(math.radians(90)))  # 1.0
```

✅ Use case: Scientific calculations, geometry, trigonometry.

## 2. `random` – Random Numbers

The `random` module helps in generating random numbers and selections.

```python
import random

print(random.randint(1, 10))     # Random int between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Random choice
print(random.sample(range(10), 3))  # 3 unique numbers
```

✅ Use case: Games, simulations, testing.

## 3. `datetime` – Date and Time Handling

```python
from datetime import datetime, timedelta

now = datetime.now()
print("Current Time:", now)

future = now + timedelta(days=5)
print("5 days later:", future)
```

✅ Use case: Logging, scheduling, event timestamps.

## 4. `os` – Operating System Interaction

The `os` module allows Python to interact with the operating system.

```python
import os

print(os.name)                   # posix / nt
print(os.getcwd())               # Current directory
os.mkdir("new_folder")           # Create folder
print(os.listdir("."))           # List files
```

✅ Use case: File handling, automation scripts.

## 5. `sys` – System-Specific Parameters

```python
import sys

print(sys.version)          # Python version
print(sys.platform)         # Platform info
print(sys.path)             # Module search paths
```

✅ Use case: Accessing interpreter details, command-line arguments.

## 6. `json` – Working with JSON Data

```python
import json

person = {"name": "Vinod", "age": 52, "city": "Bengaluru"}

# Convert dict → JSON
json_data = json.dumps(person)
print(json_data)   # {"name": "Vinod", "age": 52, "city": "Bengaluru"}

# Convert JSON → dict
python_data = json.loads(json_data)
print(python_data["name"])  # Vinod
```

✅ Use case: APIs, configuration files, data exchange.

## 7. `re` – Regular Expressions

```python
import re

text = "My email is vinod@example.com"
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # vinod@example.com
```

✅ Use case: Searching, validation, pattern matching.

## 8. `collections` – Advanced Data Structures

```python
from collections import Counter, defaultdict, namedtuple

# Counter
nums = [1, 2, 2, 3, 3, 3]
print(Counter(nums))   # Counter({3: 3, 2: 2, 1: 1})

# defaultdict
d = defaultdict(int)
d["apple"] += 1
print(d)  # defaultdict(<class 'int'>, {'apple': 1})

# namedtuple
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y)   # 10 20
```

✅ Use case: Specialized containers beyond lists/dicts.

## 9. `statistics` – Statistics Functions

```python
import statistics

data = [10, 20, 30, 40, 50]
print(statistics.mean(data))   # 30
print(statistics.median(data)) # 30
print(statistics.stdev(data))  # 15.811...
```

✅ Use case: Data analysis, reports.

## 10. `itertools` – Iterators for Combinations/Permutations

```python
import itertools

nums = [1, 2, 3]

print(list(itertools.permutations(nums, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print(list(itertools.combinations(nums, 2)))
# [(1, 2), (1, 3), (2, 3)]
```

✅ Use case: Combinatorial problems, generating sequences.

## Quick Summary Table

| Module        | Purpose         | Example                          |
| ------------- | --------------- | -------------------------------- |
| `math`        | Math functions  | `math.sqrt(16)`                  |
| `random`      | Random values   | `random.randint(1, 10)`          |
| `datetime`    | Dates/times     | `datetime.now()`                 |
| `os`          | OS interaction  | `os.listdir()`                   |
| `sys`         | System info     | `sys.version`                    |
| `json`        | JSON parsing    | `json.loads()`                   |
| `re`          | Regex           | `re.search()`                    |
| `collections` | Data structures | `Counter(), defaultdict()`       |
| `statistics`  | Statistics      | `mean(), stdev()`                |
| `itertools`   | Iterators       | `combinations(), permutations()` |

## Conclusion

Python’s built-in modules are like a **Swiss Army knife** – they save time and reduce effort by providing ready-to-use tools.
