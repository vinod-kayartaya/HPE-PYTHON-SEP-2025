# Working with Databases in Python

Most applications need to store and retrieve data. Python provides multiple ways to interact with databases, both **SQL** (relational) and **NoSQL**. In this tutorial, we’ll focus on **relational databases** like SQLite, MySQL, and PostgreSQL using Python’s libraries.

We’ll cover:

- Connecting to a database
- Creating tables
- Inserting, querying, updating, and deleting data
- Using parameterized queries to avoid SQL injection

## Choosing a Database

For beginners, **SQLite** is easiest because it’s lightweight and built into Python. For production, **MySQL** or **PostgreSQL** are popular choices.

## Using SQLite

### 1. Importing the Module

```python
import sqlite3
```

SQLite comes built-in with Python—no installation needed.

### 2. Connecting to a Database

```python
conn = sqlite3.connect("my_database.db")  # creates the database if it doesn't exist
cursor = conn.cursor()
```

### 3. Creating a Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()
```

### 4. Inserting Data

```python
# Single row
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
               ("Vinod", 15, "A"))
conn.commit()

# Multiple rows
students = [
    ("Kumar", 14, "B"),
    ("Shyam", 16, "A"),
    ("Sundar", 15, "C")
]
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students)
conn.commit()
```

### 5. Querying Data

```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

**Sample Output:**

```
(1, 'Vinod', 15, 'A')
(2, 'Kumar', 14, 'B')
(3, 'Shyam', 16, 'A')
(4, 'Sundar', 15, 'C')
```

### 6. Updating Data

```python
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Sundar"))
conn.commit()
```

### 7. Deleting Data

```python
cursor.execute("DELETE FROM students WHERE name = ?", ("Kumar",))
conn.commit()
```

### 8. Closing the Connection

```python
conn.close()
```

Always close the connection to ensure data is written and resources are released.

## Using MySQL or PostgreSQL

For production databases:

### 1. Install the library

```bash
# MySQL
pip install mysql-connector-python

# PostgreSQL
pip install psycopg2
```

### 2. Connect to Database

```python
# MySQL example
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="school"
)
cursor = conn.cursor()
```

After connecting, **CRUD operations** (Create, Read, Update, Delete) are similar to SQLite.

## Parameterized Queries: Avoid SQL Injection

Never do this:

```python
name = "Vinod"
cursor.execute(f"SELECT * FROM students WHERE name = '{name}'")
```

Instead, always use placeholders:

```python
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
```

For MySQL/PostgreSQL, use `%s` as placeholder:

```python
cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
```

## Practical Example: Fetching Top Students

```python
cursor.execute("SELECT name, grade FROM students WHERE grade = 'A' OR grade = 'A+'")
top_students = cursor.fetchall()

for student in top_students:
    print(f"{student[0]} → {student[1]}")
```

## Conclusion

Python makes working with databases easy. You can:

- Use **SQLite** for quick projects or testing.
- Use **MySQL/PostgreSQL** for production-level apps.
- Perform all CRUD operations using `cursor.execute()` and parameterized queries.
- Always commit your changes and close the connection.

Mastering these basics allows you to integrate Python applications with databases for storing, retrieving, and analyzing data efficiently.
