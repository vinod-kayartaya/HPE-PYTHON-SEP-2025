# Object-Oriented Programming (OOP) in Python — classes, objects, methods, and more

Object-oriented programming (OOP) is a cornerstone of modern software design. In Python, OOP is expressive and flexible — you can create classes that model real-world things, encapsulate behavior, reuse code through inheritance, and write polymorphic code that’s easy to extend.

This article is a hands-on, tutorial-style deep dive covering:

- Classes, objects, methods (basics)
- The `__init__` method (constructors)
- Overriding special (dunder) methods like `__str__`, `__repr__`, `__eq__`, `__gt__` (and ordering)
- Polymorphism in Python (including duck typing and abstract base classes)
- Inheritance (single, multiple, MRO, `super()` and best practices)

I’ll include clear examples, warnings (mutable defaults, hashing, etc.), and a few practical patterns you’ll use daily.

## 1. Classes, objects, methods — the basics

A **class** is a blueprint. An **object** (instance) is a concrete realization of that blueprint. A **method** is a function defined inside a class.

```python
class Person:
    # class variable (shared)
    species = "Homo sapiens"

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

# create instances (objects)
alice = Person("Alice", 30)
print(alice.greet())            # Hello, I'm Alice and I'm 30 years old.
print(Person.species)           # Homo sapiens
```

Key points:

- `self` refers to the instance. Methods defined normally receive the instance (`self`) automatically.
- Class variables (like `species`) are shared among all instances; instance variables (`self.name`) are per-object.

## 2. The `__init__` method (constructor) — what to know

`__init__` is the initializer (commonly called constructor). It runs when a new instance is created.

### Example with defaults and varargs

```python
class Book:
    def __init__(self, title, author, pages=0, *tags, **meta):
        self.title = title
        self.author = author
        self.pages = pages
        self.tags = list(tags)
        self.meta = dict(meta)

b = Book("Python OOP", "Vinod", 250, "programming", "python", isbn="978-xyz", year=2025)
print(b.title, b.tags, b.meta)
```

### Avoid mutable defaults trap

Bad:

```python
class Collector:
    def __init__(self, items=[]):   # DO NOT do this
        self.items = items
```

Why it’s bad: the same list object is shared across instances. Use `None` and create a new list inside:

Good:

```python
class Collector:
    def __init__(self, items=None):
        self.items = [] if items is None else list(items)
```

## 3. Instance, class & static methods

- **Instance methods** — take `self`, operate on instance state.
- **Class methods** — take `cls`, operate on the class (use `@classmethod`).
- **Static methods** — no implicit first argument (use `@staticmethod`).

```python
class MyClass:
    counter = 0

    def __init__(self, value):
        self.value = value
        MyClass.counter += 1

    @classmethod
    def how_many(cls):
        return cls.counter

    @staticmethod
    def helper(x):
        return x * 2

obj = MyClass(5)
print(MyClass.how_many())  # 1
print(MyClass.helper(3))   # 6
```

Use `classmethod` for alternate constructors (e.g., `from_json`, `from_string`).

## 4. Special methods (dunder methods) — `__str__`, `__repr__`, `__eq__`, `__gt__`, etc.

Python objects support _special_ methods (also called dunder methods) that control built-in behavior.

### `__repr__` vs `__str__`

- `__repr__`: unambiguous, aimed at developers. `repr(obj)` or interactive interpreter uses this.
- `__str__`: readable, aimed at end users. `print(obj)` uses this; falls back to `__repr__` if `__str__` is absent.

Example:

```python
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(emp_id={self.emp_id!r}, name={self.name!r}, salary={self.salary!r})"

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}) — ₹{self.salary}"

e = Employee(101, "Vinod", 85000)
print(e)          # uses __str__: Vinod (ID: 101) — ₹85000
e                 # interpreter shows __repr__
```

### Equality: `__eq__` and hashing

If you override `__eq__`, Python makes instances unhashable by default (i.e., `__hash__ = None`) unless you explicitly define `__hash__`. If you want objects usable as dict keys or set members, implement `__hash__` consistent with equality.

```python
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id == other.emp_id

    def __hash__(self):
        return hash(self.emp_id)
```

Now `Employee` instances with the same `emp_id` are considered equal and can be used in sets/dicts.

### Comparisons & ordering: `__lt__`, `__gt__`, `__le__`, etc.

Python sorting (e.g., `sorted(...)`) typically relies on `__lt__`. Implementing all comparison methods is tedious; use `functools.total_ordering` to generate the others from `__eq__` and one ordering method (`__lt__`, say).

```python
from functools import total_ordering

@total_ordering
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.emp_id}, {self.name!r}, {self.salary})"

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id == other.emp_id

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary < other.salary

e1 = Employee(1, "A", 50000)
e2 = Employee(2, "B", 60000)
e3 = Employee(1, "A2", 70000)

print(e1 == e3)                    # True (same emp_id)
print(sorted([e2, e1]))            # sorts by salary (uses __lt__)
```

Important: If `__eq__` returns `NotImplemented` for differing types, Python will try reflected operations or treat them as non-equal.

## 5. Polymorphism in Python

**Polymorphism** = same interface, many implementations. In Python this is natural and flexible.

### Duck typing (Pythonic polymorphism)

“If it quacks like a duck…” — Python cares about behavior (methods), not explicit types.

```python
class Bird:
    def fly(self):
        print("flying")

class Airplane:
    def fly(self):
        print("taking off")

def let_it_fly(obj):
    obj.fly()   # we don't care what obj is, as long as it has fly()

let_it_fly(Bird())       # flying
let_it_fly(Airplane())   # taking off
```

### Polymorphism via inheritance (runtime polymorphism)

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r * self.r

shapes = [Rectangle(2, 3), Circle(1)]
for s in shapes:
    print(s.area())    # calls Rectangle.area or Circle.area as appropriate
```

### Abstract Base Classes (ABCs) to enforce interface

Use `abc.ABC` and `@abstractmethod` for explicit interface enforcement.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} by UPI")

# Payment() would be illegal (abstract). UpiPayment must implement pay().
```

ABCs are helpful for larger systems and unit tests.

## 6. Inheritance in Python — single, multiple, MRO, `super()`

### Single inheritance & overriding

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def speak(self):
        return "Woof!"

d = Dog("Rex", "Labrador")
print(d.species)   # Dog
print(d.speak())   # Woof!
```

`super()` makes it easy to call parent implementations (including constructors).

### Multiple inheritance and MRO (method resolution order)

Python uses C3 linearization to compute MRO.

Example (diamond problem pattern):

```python
class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")
        super().do()

class C(A):
    def do(self):
        print("C")
        super().do()

class D(B, C):
    def do(self):
        print("D")
        super().do()

d = D()
d.do()
# Output order: D, B, C, A (due to MRO)
print(D.__mro__)   # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

Use `super()` in cooperative methods (that call `super().method()`), so multiple inheritance composes predictably.

### When to prefer composition over inheritance

- Inheritance is an “is-a” relationship. Composition is a “has-a” relationship.
- Overuse of inheritance (deep hierarchies) makes code brittle. Prefer composition (embedding objects) when behavior is better modeled that way.

Example (composition):

```python
class Engine:
    def start(self): print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car driving")
```

## 7. Encapsulation, private attrs, and `@property`

Python follows a convention for privacy: `_single_leading_underscore` = “internal use”, `__double_leading` triggers _name mangling_.

```python
class Secret:
    def __init__(self):
        self._internal = "keep private by convention"
        self.__very_private = "name mangled"

s = Secret()
print(s._internal)          # accessible (convention only)
# print(s.__very_private)   # AttributeError
print(s._Secret__very_private)  # works (name mangling)
```

Use `@property` to create computed attributes with getter/setter semantics:

```python
class Celsius:
    def __init__(self, c=0.0):
        self._c = float(c)

    @property
    def celsius(self):
        return self._c

    @celsius.setter
    def celsius(self, value):
        self._c = float(value)

    @property
    def fahrenheit(self):
        return self._c * 9/5 + 32

t = Celsius(25)
print(t.fahrenheit)   # 77.0
t.celsius = 30
```

`@property` keeps callers using attribute access while letting you control validation or lazy computation inside.

## 8. Dataclasses — boilerplate reduction

Python’s `dataclasses` generate `__init__`, `__repr__`, `__eq__`, and optionally ordering methods for you.

```python
from dataclasses import dataclass

@dataclass(order=True)
class Point:
    x: float
    y: float

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)         # Point(x=1, y=2)
print(p1 < p2)    # True (uses tuple ordering)
```

Use `frozen=True` to make them immutable (then dataclass generates `__hash__` too).

## 9. Full example — putting pieces together

A small system: `Shape` (abstract), `Rectangle`, `Circle`, support printing, equality by ID, sorting by area.

```python
from abc import ABC, abstractmethod
from functools import total_ordering
import math

@total_ordering
class Shape(ABC):
    _id_counter = 0
    def __init__(self):
        Shape._id_counter += 1
        self._id = Shape._id_counter

    @abstractmethod
    def area(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._id})"

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self._id == other._id

    # For ordering, compare areas
    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area()

class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return f"Rectangle(id={self._id}, w={self.w}, h={self.h}, area={self.area()})"

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def __str__(self):
        return f"Circle(id={self._id}, r={self.r}, area={self.area():.2f})"

shapes = [Rectangle(2, 3), Circle(1.5), Rectangle(1, 10)]
print(sorted(shapes))   # sorts using area (via __lt__)
for s in shapes:
    print(s)
```

## 10. Best practices & pitfalls

- **Prefer composition over inheritance** when relationships are _has-a_.
- Use `@property` to control attribute access; avoid exposing internal state directly.
- When overriding `__eq__`, **also override `__hash__`** if you need hashable objects. Ensure equal objects have same hash.
- Avoid mutable default arguments — use `None`.
- Keep `__init__` lightweight — don’t do heavy I/O in constructors.
- Use `abc.ABC` to define interfaces for larger codebases.
- Use `functools.total_ordering` to simplify rich comparison implementations.
- Don’t rely on name mangling for security — it’s only to avoid accidental name clashes.

## 11. Quick dunder method cheat sheet

- `__init__(self, ...)` — initializer
- `__repr__(self)` — developer representation (unambiguous)
- `__str__(self)` — user-friendly string
- `__eq__(self, other)` — equality (`==`)
- `__hash__(self)` — hashing (for sets/dicts)
- `__lt__`, `__le__`, `__gt__`, `__ge__` — ordering comparisons
- `__add__`, `__sub__`, `__mul__` — arithmetic operator overloading
- `__len__`, `__iter__`, `__next__` — container/iterator protocol
- `__call__` — make instances callable like functions

## 12. Exercises (practice)

1. **Employee system**

   - Create `Employee` with `emp_id`, `name`, `salary`.
   - Implement `__repr__`, `__str__`, `__eq__` (by `emp_id`) and `__hash__`.
   - Allow sorting employees by `salary` (hint: `__lt__` or `sorted(..., key=lambda e: e.salary)`).

2. **Bank account**

   - Implement `BankAccount` with `deposit`, `withdraw`, `balance` (use `@property`).
   - Create `SavingsAccount` subclass with `apply_interest()`.

3. **Shape hierarchy (abstract)**

   - Implement abstract `Shape` with `area()` and `perimeter()` abstract methods.
   - Implement `Triangle`, `Rectangle`, `Circle`. Make them comparable by area.

4. **Multiple inheritance & `super()`**

   - Create mixins `Loggable` (adds logging) and `JsonSerializable` (adds `to_json()`), then create a class that uses both. Observe MRO with `Class.__mro__`.

5. **Dataclass vs manual**

   - Implement a `Point` as a regular class (with `__eq__`) and as a `@dataclass`. Compare the behavior.

## 13. Closing notes

This overview should give you a clear, practical understanding of Python OOP and the tools you’ll use day-to-day: constructors (`__init__`), special methods for rich behavior, polymorphism (duck typing and abstract interfaces), and inheritance (including multiple inheritance and MRO).
