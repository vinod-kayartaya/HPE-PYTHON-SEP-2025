# List Comprehensions in Python

Python is famous for its simplicity and readability, and one of the features that makes Python so elegant is **list comprehensions**. They provide a concise way to create and manipulate lists, often replacing longer loops with a single expressive line of code.

In this article, we’ll explore what list comprehensions are, how they work, and see plenty of practical examples.

## 1. What is a List Comprehension?

A **list comprehension** is a compact syntax for generating lists. Instead of writing multiple lines with a `for` loop, you can use a single line to express the same logic.

**General syntax:**

```python
[expression for item in iterable if condition]
```

- **expression** → what to do with each item
- **item** → variable representing each element from the iterable
- **iterable** → the data structure you’re looping through (list, tuple, range, etc.)
- **condition** _(optional)_ → filter which items are included

## 2. Basic Example

Let’s start simple. Suppose you want a list of squares of numbers from 1 to 5.

### Traditional approach:

```python
squares = []
for i in range(1, 6):
    squares.append(i * i)

print(squares)  # [1, 4, 9, 16, 25]
```

### With list comprehension:

```python
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

Much shorter, right?

## 3. Adding a Condition

You can add an `if` statement to filter elements.

Example: Get only even numbers from 1 to 10.

```python
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```

## 4. Using Functions Inside List Comprehensions

You can call functions inside the expression.

Example: Convert all strings in a list to uppercase.

```python
words = ["python", "java", "c++"]
uppercase = [word.upper() for word in words]
print(uppercase)  # ['PYTHON', 'JAVA', 'C++']
```

## 5. Nested Loops in List Comprehensions

List comprehensions can also replace nested loops.

Example: Create all pairs `(x, y)` where `x` is from `[1, 2]` and `y` is from `[3, 4]`.

### Traditional approach:

```python
pairs = []
for x in [1, 2]:
    for y in [3, 4]:
        pairs.append((x, y))

print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

### With list comprehension:

```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

## 6. List Comprehensions with If-Else Expressions

You can add an inline `if-else` inside the expression part.

Example: Label numbers from 1 to 5 as `"even"` or `"odd"`.

```python
labels = ["even" if i % 2 == 0 else "odd" for i in range(1, 6)]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

## 7. Flattening a List of Lists

List comprehensions are great for flattening nested lists.

Example: Convert `[[1, 2], [3, 4], [5, 6]]` into `[1, 2, 3, 4, 5, 6]`.

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

## 8. Real-World Examples

### a) Extracting digits from a string

```python
text = "Order number: 12345"
digits = [int(ch) for ch in text if ch.isdigit()]
print(digits)  # [1, 2, 3, 4, 5]
```

### b) Filtering files by extension

```python
files = ["data.csv", "report.pdf", "image.png", "notes.txt"]
csv_files = [f for f in files if f.endswith(".csv")]
print(csv_files)  # ['data.csv']
```

### c) Reversing strings in a list

```python
words = ["apple", "banana", "cherry"]
reversed_words = [w[::-1] for w in words]
print(reversed_words)  # ['elppa', 'ananab', 'yrrehc']
```

## 9. When **Not** to Use List Comprehensions

While list comprehensions are powerful, don’t overuse them.
If your comprehension becomes too long or involves **complex nested conditions**, a regular `for` loop may be more readable.

Bad practice (hard to read):

```python
result = [x * y for x in range(10) for y in range(10) if x * y % 2 == 0 and x > 5]
```

Better:

```python
result = []
for x in range(10):
    for y in range(10):
        if x * y % 2 == 0 and x > 5:
            result.append(x * y)
```

## 10. Conclusion

List comprehensions are a **Pythonic way** of creating lists quickly, elegantly, and readably.

- They reduce boilerplate code.
- They make your intent clearer.
- They’re powerful enough for filtering, transformation, and even nested loops.

But remember — readability is more important than clever one-liners. Use them wisely!

Try experimenting with list comprehensions in your own projects. They’ll quickly become one of your favorite Python tools.
