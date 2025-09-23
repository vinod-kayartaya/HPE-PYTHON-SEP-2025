# Functions in Python

Functions are one of the most important building blocks in Python. They allow you to group reusable blocks of code, give them a name, and call them whenever needed. This not only avoids code duplication but also makes your programs cleaner and easier to maintain.

In this article, we’ll cover:

- How to write your own functions in Python
- Understanding **positional arguments** vs **keyword arguments** with clear examples

## 1. What is a Function?

A **function** is a block of code that performs a specific task. You can think of it as a “machine”: you give it some input (arguments), it does something, and then gives back output (return value).

In Python, functions are defined using the `def` keyword.

**Basic structure:**

```python
def function_name(parameters):
    # code block
    return value
```

## 2. Writing Our Own Functions

Let’s start with a simple function that greets the user.

```python
def greet():
    print("Hello! Welcome to Python.")
```

Calling the function:

```python
greet()
# Output: Hello! Welcome to Python.
```

### Function with Parameters

Parameters let you pass information into functions.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Calling the function with an argument:

```python
greet("Vinod")
# Output: Hello, Vinod!
```

### Function with Return Value

Functions can return values using `return`.

```python
def square(number):
    return number * number

result = square(5)
print(result)  # 25
```

## 3. Positional Arguments

A **positional argument** is assigned to parameters **based on its position** in the function call.

Example:

```python
def add(a, b):
    return a + b

print(add(3, 4))   # 7
print(add(10, 20)) # 30
```

Here:

- `3` is assigned to `a`,
- `4` is assigned to `b`.

If you swap them:

```python
print(add(20, 10))  # 30 (but a=20, b=10 this time)
```

The meaning changes because arguments depend on their position.

## 4. Keyword Arguments

With **keyword arguments**, you explicitly specify which parameter gets which value by using the parameter name.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
```

Calling with keyword arguments:

```python
introduce(name="Vinod", age=52)
# Output: My name is Vinod and I am 52 years old.
```

Now, the order doesn’t matter:

```python
introduce(age=52, name="Vinod")
# Output: My name is Vinod and I am 52 years old.
```

## 5. Mixing Positional and Keyword Arguments

You can mix both, but positional arguments must **always come first**.

Example:

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 3))               # Positional: 2^3 = 8
print(power(base=2, exponent=3)) # Keyword: same result
print(power(2, exponent=5))      # Mixed: 2^5 = 32
```

⚠️ Wrong usage (keyword before positional) will cause an error:

```python
print(power(base=2, 3))  # ❌ Error
```

## 6. Default Arguments

Functions can have default values for parameters. If you don’t provide a value, the default is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Vinod")   # Hello, Vinod!
```

## 7. Practical Example

Imagine a function to calculate the price of an item after discount and tax:

```python
def final_price(price, discount=0.1, tax=0.05):
    return price - (price * discount) + (price * tax)
```

Usage:

```python
# Using default discount and tax
print(final_price(1000))
# Output: 950.0

# Overriding defaults with keyword arguments
print(final_price(1000, discount=0.2, tax=0.08))
# Output: 880.0
```

This shows how keyword arguments make your code more flexible and self-explanatory.

## 8. Key Takeaways

- Use `def` to define your own functions.
- Positional arguments are assigned based on their order.
- Keyword arguments explicitly match values with parameter names (order doesn’t matter).
- Default arguments let you create flexible functions.
- Always put positional arguments before keyword arguments.

✅ With this knowledge, you can now start writing clean, reusable, and more expressive Python functions.

## Variable-Length Arguments (`*args` and `**kwargs`)

So far, we’ve learned how to write functions and the difference between **positional** and **keyword arguments**. But sometimes, we don’t know in advance how many arguments a function will receive.

That’s where **variable-length arguments** (`*args` and `**kwargs`) come in. They give your functions flexibility to accept an arbitrary number of arguments.

## 1. `*args` – Variable-Length Positional Arguments

`*args` allows a function to accept **any number of positional arguments**. Inside the function, these arguments are collected into a **tuple**.

**Example:**

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3))             # 5
print(add_numbers(10, 20, 30, 40))   # 100
print(add_numbers())                 # 0
```

Here:

- `args` behaves like a tuple: `(2, 3)` or `(10, 20, 30, 40)`
- You don’t need to know in advance how many numbers will be passed.

## 2. `**kwargs` – Variable-Length Keyword Arguments

`**kwargs` lets a function accept **any number of keyword arguments**. Inside the function, these arguments are collected into a **dictionary**.

**Example:**

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Vinod", age=52, city="Bengaluru")
```

**Output:**

```
name: Vinod
age: 52
city: Bengaluru
```

Here:

- `kwargs` is a dictionary: `{'name': 'Vinod', 'age': 52, 'city': 'Bengaluru'}`

## 3. Combining `*args` and `**kwargs`

You can use both in the same function. `*args` collects extra **positional arguments**, while `**kwargs` collects extra **keyword arguments**.

**Example:**

```python
def mixed_example(a, b, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("Additional positional args:", args)
    print("Additional keyword args:", kwargs)

mixed_example(1, 2, 3, 4, x=10, y=20)
```

**Output:**

```
a = 1, b = 2
Additional positional args: (3, 4)
Additional keyword args: {'x': 10, 'y': 20}
```

## 4. Practical Example: Flexible Billing Function

Let’s say you’re writing a billing function where:

- `*args` → list of item prices
- `**kwargs` → optional charges (like tax, delivery, discount)

```python
def calculate_bill(*args, **kwargs):
    total = sum(args)

    for key, value in kwargs.items():
        if key == "tax":
            total += total * value
        elif key == "discount":
            total -= total * value
        elif key == "delivery":
            total += value

    return total

print(calculate_bill(100, 200, 300))
# 600 (no extra charges)

print(calculate_bill(100, 200, tax=0.05, delivery=50))
# 100 + 200 = 300 → +5% tax = 315 → +50 delivery = 365
```

This function works flexibly regardless of how many items or charges are passed.

## 5. Rules of Ordering Arguments

When combining different types of arguments, the correct order is:

1. **Positional arguments**
2. **`*args`**
3. **Keyword arguments with default values**
4. **`**kwargs`\*\*

Example:

```python
def order_example(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

order_example(1, 2, 3, 4, c=5, x=100, y=200)
# Output: 1 2 (3, 4) 5 {'x': 100, 'y': 200}
```

## 6. Key Takeaways

- Use `*args` when you want a function to accept variable numbers of **positional arguments**.
- Use `**kwargs` when you want a function to accept variable numbers of **keyword arguments**.
- You can combine them for maximum flexibility.
- Always follow the correct argument order to avoid errors.

✅ With `*args` and `**kwargs`, you can now write **flexible and reusable functions** that adapt to different scenarios.
