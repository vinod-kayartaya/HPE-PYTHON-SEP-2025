# Working with the `datetime` Module in Python

Working with dates and times is a common requirement in Python projects—from logging events to scheduling tasks. Python’s built-in **`datetime` module** provides classes for manipulating dates and times in both simple and complex ways.

In this article, we’ll cover:

- Getting the current date and time
- Creating and formatting dates
- Performing arithmetic with dates
- Parsing strings into dates

## Importing the Module

```python
import datetime
```

The `datetime` module has several classes, but the most commonly used are:

- `datetime.date` → Represents a date (year, month, day)
- `datetime.time` → Represents a time (hour, minute, second, microsecond)
- `datetime.datetime` → Combines date and time
- `datetime.timedelta` → Represents a duration (difference between dates)

## Getting Current Date and Time

```python
from datetime import datetime, date

# Current date and time
now = datetime.now()
print("Now:", now)

# Current date only
today = date.today()
print("Today:", today)
```

**Sample Output:**

```
Now: 2025-09-23 20:15:30.123456
Today: 2025-09-23
```

## Creating Specific Dates

```python
from datetime import date, datetime

# A specific date
birthday = date(2005, 4, 15)
print("Birthday:", birthday)

# A specific date and time
meeting = datetime(2025, 9, 30, 14, 30, 0)
print("Meeting:", meeting)
```

## Formatting Dates

Use `strftime` to convert a date/datetime object into a string:

```python
now = datetime.now()

print(now.strftime("%Y-%m-%d"))          # 2025-09-23
print(now.strftime("%d/%m/%Y"))          # 23/09/2025
print(now.strftime("%B %d, %Y"))         # September 23, 2025
print(now.strftime("%I:%M %p"))          # 08:15 PM
```

- `%Y` → Year with century
- `%m` → Month as zero-padded decimal
- `%d` → Day of the month
- `%B` → Full month name
- `%I` → Hour (12-hour clock)
- `%M` → Minutes
- `%p` → AM/PM

## Parsing Strings into Dates

Use `strptime` to convert strings into datetime objects:

```python
from datetime import datetime

date_str = "23-09-2025 20:15"
dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(dt)  # 2025-09-23 20:15:00
```

## Date Arithmetic with `timedelta`

```python
from datetime import datetime, timedelta

today = datetime.now()
print("Today:", today)

# Add 10 days
future = today + timedelta(days=10)
print("10 days later:", future)

# Subtract 5 days
past = today - timedelta(days=5)
print("5 days ago:", past)

# Add hours and minutes
meeting = today + timedelta(hours=2, minutes=30)
print("Meeting in 2.5 hours:", meeting)
```

## Comparing Dates

```python
from datetime import date

d1 = date(2025, 9, 23)
d2 = date(2025, 12, 25)

print(d2 > d1)  # True
print(d2 - d1)  # 93 days, 0:00:00
```

You can subtract dates to get a `timedelta` object and access `.days`, `.seconds`, etc.

## Practical Example: Birthday Reminder

```python
from datetime import date

birthdays = {
    "Vinod": date(2005, 4, 15),
    "Kumar": date(2004, 9, 25),
    "Shyam": date(2005, 12, 5)
}

today = date.today()

for name, bday in birthdays.items():
    if bday.month == today.month and bday.day == today.day:
        print(f"Wish {name} a Happy Birthday!")
    else:
        days_left = (date(today.year, bday.month, bday.day) - today).days
        print(f"{days_left} days left for {name}'s birthday")
```

## Conclusion

The `datetime` module is versatile and essential for any Python developer working with dates and times. With `datetime`, `date`, `time`, and `timedelta`, you can:

- Get the current date/time
- Format dates for display
- Parse date strings
- Perform arithmetic and comparisons

Mastering `datetime` makes scheduling, logging, and reporting in Python much easier and more reliable.
