# Exploring Nested Dictionaries in Python

Python dictionaries are powerful for storing key-value pairs. But often, we deal with **complex, structured data** like JSON from APIs, configuration files, or database results. In such cases, **nested dictionaries** become very useful.

Let’s explore how to work with them step by step.

## What is a Nested Dictionary?

A **nested dictionary** means having dictionaries **inside another dictionary**.
This allows hierarchical storage of information.

```python
# Example by Vinod Kayartaya
students = {
    "101": {"name": "Alice", "age": 20, "grade": "A"},
    "102": {"name": "Bob", "age": 22, "grade": "B"},
    "103": {"name": "Charlie", "age": 21, "grade": "A"},
}
```

Here:

- Outer dictionary → student IDs (`101`, `102`, `103`)
- Inner dictionaries → student details (`name`, `age`, `grade`)

## Accessing Nested Dictionary Values

You can access values by chaining keys.

```python
print(students["101"]["name"])   # Alice
print(students["102"]["grade"])  # B
```

## Adding and Updating Values

You can update existing values or add new keys.

```python
# Update grade
students["101"]["grade"] = "A+"

# Add a new attribute
students["103"]["city"] = "Bengaluru"

print(students["103"])
# {'name': 'Charlie', 'age': 21, 'grade': 'A', 'city': 'Bengaluru'}
```

## Deleting Keys

```python
del students["102"]["age"]   # delete age of Bob
print(students["102"])
# {'name': 'Bob', 'grade': 'B'}
```

## Iterating Through Nested Dictionaries

We can loop through both outer and inner dictionaries.

```python
for student_id, details in students.items():
    print(f"ID: {student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")
```

**Output:**

```
ID: 101
  name: Alice
  age: 20
  grade: A+
ID: 102
  name: Bob
  grade: B
ID: 103
  name: Charlie
  age: 21
  grade: A
  city: Bengaluru
```

## Using `get()` Safely

Sometimes a key may not exist. Use `.get()` to avoid errors.

```python
print(students.get("104", {}).get("name", "Not Found"))
# Output: Not Found
```

## Practical Example – Employee Records

As a trainer and developer, I (Vinod Kayartaya) often use nested dictionaries to represent structured data like employee records.

```python
employees = {
    "E001": {"name": "Ravi", "dept": "IT", "skills": ["Python", "Django"]},
    "E002": {"name": "Sneha", "dept": "Finance", "skills": ["Excel", "SAP"]},
    "E003": {"name": "Arjun", "dept": "HR", "skills": ["Recruitment", "Onboarding"]}
}

# Access Ravi's department
print(employees["E001"]["dept"])  # IT

# Add new skill to Sneha
employees["E002"]["skills"].append("Power BI")

# Loop through employees
for emp, details in employees.items():
    print(f"{details['name']} works in {details['dept']}")
```

## Nested Dictionary with Comprehensions

We can also build nested dictionaries dynamically.

```python
# Example by Vinod Kayartaya
nested = {x: {y: y**2 for y in range(1, 4)} for x in range(1, 4)}
print(nested)

# Output:
# {
#   1: {1: 1, 2: 4, 3: 9},
#   2: {1: 1, 2: 4, 3: 9},
#   3: {1: 1, 2: 4, 3: 9}
# }
```

## Real-Life Use Case: JSON Data

APIs often return JSON, which in Python is simply nested dictionaries.

```python
api_response = {
    "user": {
        "id": 1001,
        "name": "Vinod Kayartaya",
        "location": {"city": "Bengaluru", "country": "India"}
    }
}

print(api_response["user"]["location"]["city"])  # Bengaluru
```

## Conclusion

Nested dictionaries allow Python developers to represent **complex hierarchical data** in a clean and structured way. They are widely used when handling **JSON, config files, or structured datasets**.
