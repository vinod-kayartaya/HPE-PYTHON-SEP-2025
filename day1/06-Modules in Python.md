# Modules in Python

When building Python programs, your code can quickly become large and complex. To keep things **organized, reusable, and maintainable**, Python provides a powerful feature: **Modules**.

In this article, I (Vinod Kayartaya) will walk you through everything you need to know about modules in Python.

## What is a Module?

A **module** is simply a Python file (`.py`) that contains code such as functions, variables, and classes.
Modules allow us to **split big programs into smaller pieces** and reuse code across projects.

👉 Think of a module like a **toolbox**: instead of writing the same tools every time, you can pick the tools you need from the box.

## Types of Modules

Python has three main categories of modules:

1. **Built-in modules** – Come pre-installed with Python (e.g., `math`, `os`, `random`).
2. **User-defined modules** – Modules that you (like Vinod) create.
3. **Third-party modules** – Developed by others and installed using `pip` (e.g., `requests`, `numpy`, `pandas`).

## Importing Modules

You can use the `import` keyword to bring a module into your program.

```python
import math

print(math.sqrt(25))   # 5.0
print(math.pi)         # 3.141592653589793
```

## Different Ways to Import

1. **Basic Import**

```python
import math
print(math.factorial(5))  # 120
```

2. **Import Specific Functions**

```python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.14159...
```

3. **Import with Alias**

```python
import random as rnd
print(rnd.randint(1, 10))   # Random number between 1 and 10
```

4. **Import All Functions (not recommended)**

```python
from math import *
print(cos(0))  # 1.0
```

## Creating a User-Defined Module

Let’s say Vinod wants to create a module for math utilities.

👉 **my_utils.py**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

author = "Vinod Kayartaya"
```

👉 **main.py**

```python
import my_utils

print(my_utils.add(10, 5))       # 15
print(my_utils.subtract(10, 5))  # 5
print(my_utils.author)           # Vinod Kayartaya
```

## Using the `dir()` Function

To see all functions/variables inside a module:

```python
import math
print(dir(math))
```

## The `__name__ == "__main__"` Trick

Every Python file has a built-in variable `__name__`.

- If the file is run directly → `__name__ == "__main__"`
- If imported as a module → `__name__` is the module’s name

👉 Example:

**my_module.py**

```python
def greet():
    print("Hello from Vinod's module!")

if __name__ == "__main__":
    print("Running directly")
    greet()
else:
    print("Imported as a module")
```

**main.py**

```python
import my_module
my_module.greet()
```

## Built-in Modules You Should Know

Some commonly used built-in modules in Python are:

- **math** → mathematical functions
- **random** → random number generation
- **os** → interact with the operating system
- **sys** → system-specific parameters
- **datetime** → date and time handling
- **json** → working with JSON data

👉 Example using `datetime`:

```python
from datetime import datetime

now = datetime.now()
print("Current time:", now)
```

## Third-Party Modules

You can install third-party modules using `pip`.

```bash
pip install requests
```

👉 Example using `requests`:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
```

## Why Use Modules?

- Code reusability
- Better organization of projects
- Easier debugging and collaboration
- Access to thousands of pre-built libraries

## Conclusion

Modules are one of the reasons Python is so powerful.
They make programs more **organized, reusable, and extensible**.
