# Unit Testing in Python with the `unittest` Module

When building software, writing code is only half the job—the other half is **making sure it works correctly**. That’s where **unit testing** comes in.

Python’s built-in **`unittest`** module allows you to write automated tests that verify your code behaves as expected.

In this tutorial, we’ll cover:

- What unit testing is.
- Writing test cases with `unittest`.
- Running and organizing tests.
- Using assertions.
- Building a **test suite**.

## What is Unit Testing?

- **Unit testing** = testing individual pieces of code (functions, classes, modules).
- Benefits:

  - Catches bugs early.
  - Makes refactoring safer.
  - Improves code quality.

The `unittest` module provides:

- `TestCase` classes for test grouping.
- Assertion methods for validation.
- A test runner for execution.

## A Simple Example

Let’s test a couple of utility functions:

```python
# math_utils.py
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y
```

## Writing a Test Case

```python
# test_math_utils.py
import unittest
import math_utils

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_utils.add(2, 3), 5)
        self.assertEqual(math_utils.add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(math_utils.divide(10, 2), 5)
        self.assertAlmostEqual(math_utils.divide(7, 3), 2.3333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            math_utils.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
```

## Running Tests

Run from terminal:

```bash
python -m unittest test_math_utils.py
```

**Output:**

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Common Assertion Methods

- `assertEqual(a, b)` → equality.
- `assertNotEqual(a, b)` → inequality.
- `assertTrue(x)` / `assertFalse(x)`.
- `assertIsNone(x)` / `assertIsNotNone(x)`.
- `assertIn(a, b)` / `assertNotIn(a, b)`.
- `assertRaises(Error)` → checks exceptions.

Example:

```python
self.assertTrue(5 > 3)
self.assertIn("Vinod", ["Vinod", "Kumar", "Shyam"])
```

## Example: Testing a Class

```python
# bank_account.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
```

**Test Case:**

```python
# test_bank_account.py
import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Kumar", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(40), 60)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == "__main__":
    unittest.main()
```

- **`setUp()`** runs before each test, ensuring a fresh account every time.
- This avoids duplication and makes tests more reliable.

## Organizing Tests

For larger projects, keep tests in a dedicated folder:

```
project/
    math_utils.py
    bank_account.py
    tests/
        test_math_utils.py
        test_bank_account.py
```

Run all tests at once:

```bash
python -m unittest discover -s tests
```

## Building a Test Suite

A **test suite** is a collection of tests that you can run together.

```python
# test_suite.py
import unittest
from test_math_utils import TestMathUtils
from test_bank_account import TestBankAccount

# Create suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMathUtils))
    suite.addTest(unittest.makeSuite(TestBankAccount))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

**Run it:**

```bash
python test_suite.py
```

This way, you can **combine multiple test cases** into one suite and run them in a controlled order.

## Conclusion

In this tutorial, we learned how to:

- Write unit tests with `unittest.TestCase`.
- Use common assertion methods.
- Organize tests into files and directories.
- Build and run a **test suite** for grouped execution.

Unit testing makes your code more **reliable, maintainable, and future-proof**. The more you test, the fewer surprises you’ll encounter when your application grows.
