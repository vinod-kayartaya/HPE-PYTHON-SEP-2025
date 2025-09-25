# Working with CSV Files in Python

CSV (Comma-Separated Values) is one of the most common formats for storing tabular data. Python’s built-in **`csv` module** makes it simple to read from and write to CSV files without relying on external libraries.

In this article, we’ll walk through practical examples of working with CSV files: reading, writing, handling delimiters, and some best practices.

## Why Use CSV?

- Easy to read and edit in any text editor.
- Supported by Excel, Google Sheets, and databases.
- Lightweight compared to formats like JSON or XML.

## Reading CSV Files

### Example 1: Reading a Simple CSV

Suppose you have a file `students.csv`:

```csv
name,age,grade
Vinod,15,A
Kumar,14,B
Shyam,16,A
Sundar,15,C
```

You can read it using `csv.reader`:

```python
import csv

with open("students.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Output:**

```text
['name', 'age', 'grade']
['Vinod', '15', 'A']
['Kumar', '14', 'B']
['Shyam', '16', 'A']
['Sundar', '15', 'C']
```

⚡ Note: Each row is returned as a list of strings.

### Example 2: Reading with `csv.DictReader`

If you prefer to work with dictionaries (column names as keys):

```python
import csv

with open("students.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "→", row["grade"])
```

**Output:**

```text
Vinod → A
Kumar → B
Shyam → A
Sundar → C
```

This makes your code more readable since you can access values by column name.

## Writing CSV Files

### Example 3: Writing with `csv.writer`

```python
import csv

students = [
    ["name", "age", "grade"],
    ["Vinod", 15, "A"],
    ["Kumar", 14, "B"],
    ["Shyam", 16, "A"],
    ["Sundar", 15, "C"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
```

This creates `output.csv` with the same data.

### Example 4: Writing with `csv.DictWriter`

If you prefer dictionaries:

```python
import csv

students = [
    {"name": "Vinod", "age": 15, "grade": "A"},
    {"name": "Kumar", "age": 14, "grade": "B"},
    {"name": "Shyam", "age": 16, "grade": "A"},
    {"name": "Sundar", "age": 15, "grade": "C"}
]

with open("output_dict.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()   # write column names
    writer.writerows(students)
```

## Handling Custom Delimiters

CSV files don’t always use commas. For example, `data.tsv` (Tab-Separated Values):

```text
name	age	grade
Vinod	15	A
Kumar	14	B
```

Read it using:

```python
import csv

with open("data.tsv", newline="") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)
```

## Skipping Headers

Sometimes you only want the data:

```python
import csv

with open("students.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        print(row)
```

## Practical Example: Filtering Students

Let’s say we want only students with grade **A**:

```python
import csv

with open("students.csv", newline="") as file:
    reader = csv.DictReader(file)
    top_students = [row for row in reader if row["grade"] == "A"]

print("Top Students:", top_students)
```

**Output:**

```text
Top Students: [{'name': 'Vinod', 'age': '15', 'grade': 'A'}, {'name': 'Shyam', 'age': '16', 'grade': 'A'}]
```

## ⚠️ Gotchas & Best Practices for CSV

1. **Always use `newline=""` when opening files**

   - On Windows, omitting `newline=""` may cause extra blank lines in output.

2. **Be mindful of encoding**

   - Many CSVs use UTF-8, but files from Excel may use `utf-16` or `cp1252`.

   ```python
   open("students.csv", encoding="utf-8")
   ```

3. **Quoting issues**

   - If your data contains commas inside values (`"Bangalore, India"`), use `quoting=csv.QUOTE_ALL` when writing.

   ```python
   writer = csv.writer(file, quoting=csv.QUOTE_ALL)
   ```

4. **Large files**

   - Instead of loading the entire CSV into memory, process line by line with a loop.
   - For heavy-duty tasks, consider `pandas` which is optimized for large datasets.

5. **Consistent field order**

   - When using `DictWriter`, always provide `fieldnames` to avoid mismatched column orders.

6. **Use context managers (`with open(...)`)**

   - Ensures files are closed properly, even if an error occurs.

## Conclusion

The `csv` module in Python is a simple yet powerful way to handle tabular data. Whether you’re importing data from Excel, exporting results, or filtering information, `csv.reader`, `csv.DictReader`, `csv.writer`, and `csv.DictWriter` provide everything you need.

By keeping in mind common gotchas like encoding, quoting, and large files, you can write robust code that works across different platforms and data sources.
