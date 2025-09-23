# Exceptions and How to Handle Them in Python

Errors are a part of programming. No matter how carefully you write code, things can (and will) go wrong: missing files, invalid inputs, network issues, or bugs.

In Python, such errors are represented as **exceptions**. If not handled properly, exceptions will cause your program to crash. Fortunately, Python provides a powerful way to catch and handle exceptions gracefully.

This article covers:

- What exceptions are
- Common built-in exceptions
- How to handle exceptions (`try`, `except`)
- Using `else` and `finally`
- Raising exceptions
- Creating custom exceptions
- Best practices

## 1. What is an Exception?

An **exception** is an event that occurs during the execution of a program and disrupts its normal flow.

Example of an unhandled exception:

```python
print(10 / 0)
```

**Output:**

```
ZeroDivisionError: division by zero
```

Here, dividing by zero causes a `ZeroDivisionError`, and since it isn’t handled, the program crashes.

## 2. Common Built-in Exceptions

Python has many built-in exceptions. Some frequently encountered ones are:

- **`ZeroDivisionError`** – Division by zero
- **`ValueError`** – Invalid value (e.g., converting "abc" to integer)
- **`TypeError`** – Invalid type operation (e.g., adding string and int)
- **`IndexError`** – Invalid list index
- **`KeyError`** – Accessing missing dictionary key
- **`FileNotFoundError`** – Trying to open a file that doesn’t exist

Example:

```python
# IndexError
numbers = [1, 2, 3]
print(numbers[5])  # Invalid index
```

## 3. Handling Exceptions with `try` and `except`

To handle exceptions, wrap the risky code inside a **try block**, and handle errors in an **except block**.

### Example 1: Basic handling

```python
try:
    x = int("abc")   # This will raise ValueError
except ValueError:
    print("Invalid input! Cannot convert to integer.")
```

**Output:**

```
Invalid input! Cannot convert to integer.
```

## 4. Handling Multiple Exceptions

You can catch different exceptions separately.

```python
try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("Conversion error: not a number.")
except ZeroDivisionError:
    print("Math error: cannot divide by zero.")
```

**Output:**

```
Conversion error: not a number.
```

## 5. Catching All Exceptions

You can catch all exceptions with a generic `except Exception as e`.

```python
try:
    file = open("missing.txt", "r")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Output:**

```
An error occurred: [Errno 2] No such file or directory: 'missing.txt'
```

⚠️ Use this carefully — catching everything may hide real bugs.

## 6. Using `else` with `try`

The **`else` block** runs if no exception occurs.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")
```

**Output:**

```
Result: 5.0
```

## 7. Using `finally`

The **`finally` block** always runs, whether an exception occurred or not. Useful for cleanup (closing files, releasing resources).

```python
try:
    file = open("data.txt", "w")
    file.write("Hello")
except Exception as e:
    print(f"Error: {e}")
finally:
    file.close()
    print("File closed.")
```

## 8. Raising Exceptions

You can raise your own exceptions using `raise`.

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    print(f"Withdrew {amount}")

withdraw(-100)
```

**Output:**

```
ValueError: Amount cannot be negative
```

## 9. Custom Exceptions

You can define your own exception classes by inheriting from `Exception`.

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)
```

**Output:**

```
Not enough balance
```

## 10. Best Practices for Exception Handling

- Catch specific exceptions (e.g., `ValueError`) instead of a blanket `except`.
- Use `finally` for cleanup.
- Don’t ignore exceptions silently.
- Raise meaningful exceptions for invalid operations.
- Create custom exceptions for domain-specific errors.

## 11. Real-world Example

Let’s handle file reading safely:

```python
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except PermissionError:
        print("You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Operation finished.")

content = read_file("notes.txt")
```

## 12. Key Takeaways

- Exceptions represent runtime errors.
- Use **try/except** to handle them gracefully.
- Add **else** for success cases and **finally** for cleanup.
- You can raise exceptions manually with `raise`.
- Create custom exceptions for clearer error handling.

✅ With proper exception handling, your Python programs become **more robust, user-friendly, and fault-tolerant**.
