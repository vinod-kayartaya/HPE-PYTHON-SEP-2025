# Working with Language-Independent Formats in Python: XML and JSON

Modern applications rarely live in isolation. Data often needs to be exchanged across different systems, programming languages, or even organizations. To make this possible, we rely on **language-independent formats** like **XML (eXtensible Markup Language)** and **JSON (JavaScript Object Notation)**.

Both formats are widely supported across platforms, making them essential for tasks like configuration, data exchange, and APIs. In this tutorial, we’ll explore how to **build and parse XML and JSON in Python** with practical examples.

## Why XML and JSON?

- **XML**

  - Text-based, hierarchical format.
  - Good for representing complex, nested data with attributes.
  - Heavily used in legacy systems, document standards (SOAP, RSS, SVG).

- **JSON**

  - Lightweight, text-based format.
  - Easy to read and write.
  - The de facto standard for modern APIs (REST, GraphQL responses).

## Working with JSON in Python

Python’s standard library has the built-in `json` module, making it straightforward to handle JSON.

### Example: Creating JSON data

```python
import json

# Python dictionary
employee = {
    "id": 101,
    "name": "Vinod",
    "role": "Developer",
    "skills": ["Python", "Django", "REST"],
    "active": True
}

# Convert dictionary to JSON string
employee_json = json.dumps(employee, indent=4)
print(employee_json)
```

**Output:**

```json
{
  "id": 101,
  "name": "Vinod",
  "role": "Developer",
  "skills": ["Python", "Django", "REST"],
  "active": true
}
```

Here, `json.dumps()` converts Python objects to a JSON string. The `indent=4` makes it pretty-printed.

### Example: Parsing JSON data

```python
import json

# JSON string (imagine this came from an API)
data = '{"id": 202, "name": "Kumar", "role": "Data Scientist", "skills": ["Pandas", "NumPy"]}'

# Parse JSON to Python dictionary
employee = json.loads(data)
print(employee["name"])     # Kumar
print(employee["skills"])   # ['Pandas', 'NumPy']
```

- `json.loads()` converts JSON string → Python dictionary.
- You can now work with it like any normal Python object.

### Example: Reading/Writing JSON files

```python
import json

# Writing JSON to file
with open("employee.json", "w") as f:
    json.dump(employee, f, indent=4)

# Reading JSON from file
with open("employee.json", "r") as f:
    loaded_employee = json.load(f)
    print(loaded_employee["role"])
```

- `json.dump()` and `json.load()` work directly with files.

## Working with XML in Python

For XML, Python provides the `xml.etree.ElementTree` module, which is efficient and easy to use.

### Example: Building XML

```python
import xml.etree.ElementTree as ET

# Root element
employee = ET.Element("employee")

# Child elements
id_elem = ET.SubElement(employee, "id")
id_elem.text = "301"

name_elem = ET.SubElement(employee, "name")
name_elem.text = "Shyam"

role_elem = ET.SubElement(employee, "role")
role_elem.text = "System Analyst"

skills_elem = ET.SubElement(employee, "skills")
for skill in ["Linux", "Networking", "Shell Scripting"]:
    skill_elem = ET.SubElement(skills_elem, "skill")
    skill_elem.text = skill

# Convert to string
xml_str = ET.tostring(employee, encoding="unicode")
print(xml_str)
```

**Output:**

```xml
<employee>
  <id>301</id>
  <name>Shyam</name>
  <role>System Analyst</role>
  <skills>
    <skill>Linux</skill>
    <skill>Networking</skill>
    <skill>Shell Scripting</skill>
  </skills>
</employee>
```

### Example: Parsing XML

```python
import xml.etree.ElementTree as ET

# XML string (imagine this came from a config file)
xml_data = """
<employee>
  <id>401</id>
  <name>Sundar</name>
  <role>QA Engineer</role>
  <skills>
    <skill>Selenium</skill>
    <skill>Python</skill>
  </skills>
</employee>
"""

# Parse XML
root = ET.fromstring(xml_data)

print(root.find("name").text)       # Sundar
print(root.find("role").text)       # QA Engineer

# Iterate over skills
for skill in root.find("skills"):
    print("Skill:", skill.text)
```

### Example: Reading/Writing XML files

```python
tree = ET.ElementTree(employee)

# Write XML to file
tree.write("employee.xml", encoding="utf-8", xml_declaration=True)

# Read XML from file
tree = ET.parse("employee.xml")
root = tree.getroot()
print(root.find("name").text)
```

## JSON vs XML in Python

| Feature        | JSON                         | XML                                   |
| -------------- | ---------------------------- | ------------------------------------- |
| Format         | Lightweight, key–value pairs | Hierarchical with tags and attributes |
| Readability    | Easy for humans              | Verbose, harder to read               |
| Usage          | APIs, configs, logs          | Legacy systems, document standards    |
| Python support | `json` module                | `xml.etree.ElementTree`, `lxml`, etc. |

## Conclusion

Both **XML and JSON** play a critical role in data exchange.

- **JSON** is the go-to for modern applications, especially web APIs.
- **XML** is still widely used in enterprise and legacy systems.

Python makes it easy to **build, parse, read, and write** both formats with just its standard library.

Mastering these tools ensures your applications can communicate effectively with the outside world, regardless of language or platform.
