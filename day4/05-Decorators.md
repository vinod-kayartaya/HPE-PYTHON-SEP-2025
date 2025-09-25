# Understanding Decorators in Python

Decorators are a powerful and elegant feature in Python that allow you to **modify or enhance the behavior of functions or methods** without changing their code. They are widely used in logging, authentication, caching, and more.

In this article, we’ll cover:

- What decorators are
- Function decorators
- Decorating functions with parameters
- Chaining decorators
- Practical examples

## What is a Decorator?

A **decorator** is a function that takes another function as input, adds some functionality, and returns a new function.

Think of it as a **wrapper** around a function.

## Basic Decorator Example

```python
def simple_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

def greet():
    print("Hello, Vinod!")

# Applying decorator
greet = simple_decorator(greet)
greet()
```

**Output:**

```
Before calling the function
Hello, Vinod!
After calling the function
```

## Using the `@` Syntax

Python provides a shorthand `@decorator_name` to apply decorators:

```python
@simple_decorator
def greet():
    print("Hello, Kumar!")

greet()
```

Output is the same as the previous example. The `@` syntax makes code cleaner and more readable.

## Decorators with Parameters

If the function you want to decorate takes arguments, the wrapper must accept them using `*args` and `**kwargs`:

```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Function is about to be called")
        result = func(*args, **kwargs)
        print("Function has been called")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

print(add(5, 7))
```

**Output:**

```
Function is about to be called
Function has been called
12
```

## Chaining Decorators

You can apply multiple decorators to a function. They are applied from **bottom to top**:

```python
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def greet():
    print("Hello, Shyam!")

greet()
```

**Output:**

```
Decorator 1
Decorator 2
Hello, Shyam!
```

## Practical Examples

### 1. Logging Decorator

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

Output:

```
Calling function 'multiply' with args=(3, 4), kwargs={}
12
```

### 2. Timer Decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()
```

### 3. Authorization Decorator

```python
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            print(f"User {user['name']} is not authorized!")
            return
        return func(user, *args, **kwargs)
    return wrapper

@require_admin
def delete_user(user, user_to_delete):
    print(f"{user['name']} deleted {user_to_delete}")

admin_user = {"name": "Vinod", "is_admin": True}
normal_user = {"name": "Kumar", "is_admin": False}

delete_user(admin_user, "Shyam")
delete_user(normal_user, "Shyam")
```

Output:

```
Vinod deleted Shyam
User Kumar is not authorized!
```

## Conclusion

Decorators are a **clean and Pythonic way to extend functionality**:

- They allow you to **wrap functions** without modifying the original code.
- Useful for logging, authentication, caching, timing, and more.
- You can **chain multiple decorators** for modular enhancements.

By mastering decorators, you can write **more reusable, readable, and elegant Python code**.

---

# Advanced Python Decorators: With Arguments and Classes

Decorators are a powerful feature in Python, and their real potential shines when you use **arguments** or apply them to **classes**. In this article, we’ll cover:

- Function decorators with arguments
- Class decorators
- Practical examples

## 1. Function Decorators with Arguments

Sometimes you want your decorator to **accept parameters** to modify its behavior dynamically.

### Example: Greeting Decorator with a Custom Message

```python
def greet_decorator(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@greet_decorator("Hello from Vinod's decorator!")
def say_hello(name):
    print(f"Hi, {name}!")

say_hello("Kumar")
```

**Output:**

```
Hello from Vinod's decorator!
Hi, Kumar!
```

**Explanation:**

- `greet_decorator("...")` returns a decorator function.
- That decorator wraps the original function.
- You can now pass **custom arguments** to control the decorator.

### Another Example: Multiplying Result

```python
def multiply_result(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator

@multiply_result(3)
def add(a, b):
    return a + b

print(add(5, 7))  # (5+7) * 3 = 36
```

## 2. Class Decorators

Decorators aren’t limited to functions—they can also modify **classes**.

### Example: Adding a Method to a Class

```python
def add_greet_method(cls):
    cls.greet = lambda self: f"Hello, I am {self.name}"
    return cls

@add_greet_method
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Shyam")
print(p.greet())
```

**Output:**

```
Hello, I am Shyam
```

### Example: Logging Class Instantiations

```python
def log_instantiation(cls):
    original_init = cls.__init__
    def new_init(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__} with args={args}, kwargs={kwargs}")
        original_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls

@log_instantiation
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

u = User("Vinod", "Admin")
```

**Output:**

```
Creating instance of User with args=('Vinod', 'Admin'), kwargs={}
```

## 3. Decorators on Methods

You can also decorate **methods** inside classes:

```python
def uppercase(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        return result.upper()
    return wrapper

class Message:
    @uppercase
    def greet(self, name):
        return f"Hello, {name}"

m = Message()
print(m.greet("Kumar"))  # HELLO, KUMAR
```

## Key Takeaways

- **Decorators with arguments** allow dynamic customization.
- **Class decorators** can add or modify class behavior.
- You can decorate **methods**, **functions**, and even **built-in classes**.
- Combined with function decorators, they allow highly reusable and modular code.

### Practical Uses

- Logging or auditing function calls
- Adding default methods or attributes to classes
- Controlling access to functions or methods (authentication)
- Timing functions or class operations
