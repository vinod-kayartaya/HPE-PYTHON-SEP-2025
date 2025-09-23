# Using Regular Expressions in Python: Matching, Finding, and Replacing Patterns

Regular Expressions (often called **regex** or **regexp**) are a powerful tool for working with text. They let you search for, match, and manipulate strings based on **patterns** rather than fixed characters.

Python provides the built-in **`re` module** to work with regular expressions.

In this article, we’ll cover:

- What regex is and why it’s useful
- The basics of regex syntax
- Matching patterns (`match`, `search`)
- Finding patterns (`findall`, `finditer`)
- Replacing patterns (`sub`)
- Practical examples

## 1. Getting Started with the `re` Module

```python
import re
```

Common functions in `re` are:

- `re.match()` → matches pattern at the **start** of the string
- `re.search()` → searches for the **first occurrence** of the pattern
- `re.findall()` → returns **all matches** as a list
- `re.finditer()` → returns an iterator of match objects
- `re.sub()` → replaces matches with another string

## 2. Regex Syntax Basics

Some important symbols in regex:

- `.` → any character except newline
- `^` → start of string
- `$` → end of string
- `*` → 0 or more repetitions
- `+` → 1 or more repetitions
- `?` → 0 or 1 occurrence
- `{m,n}` → between m and n repetitions
- `[]` → character set
- `|` → OR
- `\d` → digit
- `\w` → word character (letters, digits, underscore)
- `\s` → whitespace

## 3. Matching Patterns

### Example 1: Match at the start of a string

```python
import re

pattern = r"Python"
text = "Python is fun"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
```

**Output:**

```
Match found: Python
```

### Example 2: Search anywhere in the string

```python
pattern = r"fun"
text = "Python is fun"

search = re.search(pattern, text)

if search:
    print("Found:", search.group())
```

**Output:**

```
Found: fun
```

## 4. Finding All Matches

### Example 1: `findall()` returns all matches as a list

```python
pattern = r"\d+"  # one or more digits
text = "There are 12 apples and 34 oranges."

numbers = re.findall(pattern, text)
print(numbers)  # ['12', '34']
```

### Example 2: `finditer()` returns match objects (with positions)

```python
pattern = r"\d+"
text = "There are 12 apples and 34 oranges."

for match in re.finditer(pattern, text):
    print(match.group(), "at position", match.start())
```

**Output:**

```
12 at position 10
34 at position 24
```

## 5. Replacing Patterns

Use `re.sub()` to replace matched text.

### Example 1: Replace digits with `#`

```python
pattern = r"\d"
text = "Call me at 123-456-7890"

new_text = re.sub(pattern, "#", text)
print(new_text)  # Call me at ###-###-####
```

### Example 2: Mask email addresses

```python
pattern = r"\w+@\w+\.\w+"
text = "Contact us at support@example.com"

masked = re.sub(pattern, "[hidden email]", text)
print(masked)  # Contact us at [hidden email]
```

## 6. Grouping and Extracting Substrings

Use **parentheses `()`** to capture groups.

### Example: Extract username and domain from email

```python
pattern = r"(\w+)@(\w+\.\w+)"
text = "My email is user@example.com"

match = re.search(pattern, text)
if match:
    print("Username:", match.group(1))
    print("Domain:", match.group(2))
```

**Output:**

```
Username: user
Domain: example.com
```

## 7. Practical Example: Validating Patterns

### Example 1: Check if a string is a valid phone number

```python
pattern = r"^\d{3}-\d{3}-\d{4}$"
phone = "123-456-7890"

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
```

### Example 2: Validate an email address

```python
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "test.user@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

## 8. Key Takeaways

- Use the **`re` module** for regex in Python.
- **`match`** → start of string, **`search`** → anywhere in string.
- **`findall`** and **`finditer`** → get multiple matches.
- **`sub`** → replace matched patterns.
- Regex patterns allow **powerful text manipulation and validation**.

✅ With regular expressions, you can handle everything from **simple text matching** to **complex string validation and transformations** in Python.

# Python Regex Cheat Sheet — Quick Reference

| Pattern                         | Meaning                       | Example                                           |       |                              |
| ------------------------------- | ----------------------------- | ------------------------------------------------- | ----- | ---------------------------- |
| `.`                             | Any character except newline  | `re.match("a.c", "abc")` → matches                |       |                              |
| `^`                             | Start of string               | `re.match("^Hello", "Hello World")` → matches     |       |                              |
| `$`                             | End of string                 | `re.search("World$", "Hello World")` → matches    |       |                              |
| `*`                             | 0 or more repetitions         | `re.findall("a*", "aaab")` → \['aaa', '', '']     |       |                              |
| `+`                             | 1 or more repetitions         | `re.findall("a+", "aaab")` → \['aaa']             |       |                              |
| `?`                             | 0 or 1 occurrence             | `re.findall("a?", "aaab")` → \['a','a','a','']    |       |                              |
| `{m,n}`                         | Between m and n repetitions   | `re.findall("a{2,3}", "aaab")` → \['aaa']         |       |                              |
| `[]`                            | Character set                 | `[abc]` matches 'a', 'b', or 'c'                  |       |                              |
| \`                              | \`                            | OR operator                                       | \`cat | dog\` matches 'cat' or 'dog' |
| `\d`                            | Digit `[0-9]`                 | `re.findall("\d", "Phone: 123")` → \['1','2','3'] |       |                              |
| `\D`                            | Non-digit                     | `\D` matches letters or symbols                   |       |                              |
| `\w`                            | Word character `[a-zA-Z0-9_]` | `\w+` matches words                               |       |                              |
| `\W`                            | Non-word character            | Matches punctuation, spaces                       |       |                              |
| `\s`                            | Whitespace                    | Matches spaces, tabs, newlines                    |       |                              |
| `\S`                            | Non-whitespace                | Matches letters, digits, symbols                  |       |                              |
| `()`                            | Grouping / capturing          | `(\w+)@(\w+\.\w+)` captures username and domain   |       |                              |
| `(?P<name>...)`                 | Named group                   | `(?P<user>\w+)@(\w+\.\w+)`                        |       |                              |
| `re.sub(pattern, repl, string)` | Replace pattern with `repl`   | `re.sub("\d", "#", "123")` → "###"                |       |                              |
| `re.findall(pattern, string)`   | List all matches              | `re.findall("\d+", "a1b22")` → \['1','22']        |       |                              |
| `re.match(pattern, string)`     | Match at start                | `re.match("\d+", "123abc")` → matches '123'       |       |                              |
| `re.search(pattern, string)`    | Search anywhere               | `re.search("\d+", "abc123")` → matches '123'      |       |                              |
| `re.finditer(pattern, string)`  | Iterator of matches           | Useful for positions (`match.start()`)            |       |                              |

### Common Patterns

| Pattern                    | Description        | Example            |                       |
| -------------------------- | ------------------ | ------------------ | --------------------- |
| `^\d{3}-\d{3}-\d{4}$`      | US phone number    | `123-456-7890`     |                       |
| `^[\w\.-]+@[\w\.-]+\.\w+$` | Email address      | `user@example.com` |                       |
| `\d{4}-\d{2}-\d{2}`        | Date (YYYY-MM-DD)  | `2025-09-23`       |                       |
| `[A-Z][a-z]+`              | Capitalized word   | `Python`           |                       |
| `\b\w{4}\b`                | 4-letter words     | `test, code`       |                       |
| \`(http                    | https)://\[^\s]+\` | URLs               | `https://example.com` |

### Tips

- Use **raw strings** for patterns: `r"\d+"` instead of `"\\d+"`.
- Test your regex on tools like [regex101.com](https://regex101.com/) for instant feedback.
- Start simple, then add complexity using groups and quantifiers.
- Combine with `map`, `filter`, or list comprehensions for text processing pipelines.
