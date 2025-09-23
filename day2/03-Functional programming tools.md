# Functional Programming Tools in Python

Python is a **multi-paradigm language**, meaning it supports more than one programming style. Apart from **Object-Oriented Programming (OOP)** and **Procedural Programming**, Python also supports **Functional Programming**.

Functional programming treats computation as the evaluation of mathematical functions and avoids changing state or mutable data.

In this article, we’ll explore three important functional programming tools in Python:

- **map()**
- **filter()**
- **reduce()**

## 1. The `map()` Function

The `map()` function applies a given function to **all items** in an iterable (like a list) and returns a map object (which can be converted to a list, tuple, etc.).

### Syntax

```python
map(function, iterable)
```

- **function** → the function to apply.
- **iterable** → list, tuple, or any sequence.

### Example 1: Squaring numbers

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

print(list(squared))  # [1, 4, 9, 16, 25]
```

Here, the `lambda` function squares each element of the list.

### Example 2: Converting strings to uppercase

```python
words = ["python", "java", "c++"]
uppercased = map(str.upper, words)

print(list(uppercased))  # ['PYTHON', 'JAVA', 'C++']
```

## 2. The `filter()` Function

The `filter()` function filters items from an iterable based on whether they satisfy a given condition (function returning `True` or `False`).

### Syntax

```python
filter(function, iterable)
```

- **function** → returns `True` (keep the item) or `False` (exclude the item).
- **iterable** → list, tuple, etc.

### Example 1: Filtering even numbers

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # [2, 4, 6]
```

### Example 2: Filtering words longer than 3 characters

```python
words = ["a", "an", "the", "python", "java"]
long_words = filter(lambda w: len(w) > 3, words)

print(list(long_words))  # ['python', 'java']
```

## 3. The `reduce()` Function

Unlike `map()` and `filter()`, the `reduce()` function is not built-in. It comes from the `functools` module.

The `reduce()` function applies a function **cumulatively** to the items of an iterable, reducing it to a single value.

### Syntax

```python
from functools import reduce
reduce(function, iterable[, initializer])
```

- **function** → takes two arguments, combines them, and returns one result.
- **iterable** → list, tuple, etc.
- **initializer** (optional) → starting value.

### Example 1: Summing a list

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)

print(total)  # 15
```

### Example 2: Finding the maximum

```python
from functools import reduce

numbers = [10, 45, 32, 67, 2]
maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)  # 67
```

## 4. Combining map(), filter(), and reduce()

These functions can be combined to build powerful data-processing pipelines.

### Example: Sum of squares of even numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Square them
squares = map(lambda x: x**2, evens)

# Step 3: Reduce to sum
result = reduce(lambda x, y: x + y, squares)

print(result)  # 56 (2^2 + 4^2 + 6^2 = 4 + 16 + 36)
```

## 5. When to Use These Functions?

- Use **map()** when you need to transform data.
- Use **filter()** when you need to select a subset of data.
- Use **reduce()** when you need to combine values into a single result.

## 6. Alternative: List Comprehensions

Python developers often prefer **list comprehensions** because they are more readable.

**Example: Same as above (sum of squares of even numbers)**

```python
numbers = [1, 2, 3, 4, 5, 6]
result = sum([x**2 for x in numbers if x % 2 == 0])

print(result)  # 56
```

Both approaches are valid — `map`, `filter`, and `reduce` are powerful, while comprehensions are usually more Pythonic.

## 7. Key Takeaways

- **map()** → applies a function to every element.
- **filter()** → selects elements that meet a condition.
- **reduce()** → combines elements into a single result.
- They can be chained for powerful functional programming workflows.
- List comprehensions often serve as a cleaner alternative.

✅ With these tools, you can write **cleaner, more functional-style Python code**, making transformations and aggregations simple and expressive.
