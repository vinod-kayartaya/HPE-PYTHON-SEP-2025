# Using the `pdb` Module to Debug in Python

Debugging is a crucial part of development. While `print()` statements are often used to inspect values, Python provides a much more powerful and structured tool: the **Python Debugger (`pdb`)**. With `pdb`, you can pause program execution, inspect variables, step through code line by line, and identify the root cause of bugs.

In this article, we’ll explore how to use `pdb` effectively with practical examples.

## Why Use `pdb`?

- **Interactive debugging**: Pause execution at any point and check variable values.
- **Control execution flow**: Step into functions, move to the next line, or continue.
- **No need for repeated `print()` debugging**: Directly inspect and modify execution context.

## Starting the Debugger

You can start the debugger in multiple ways:

### 1. Using `pdb.set_trace()`

Insert this line in your code where you want to pause execution:

```python
import pdb

def divide(a, b):
    result = a / b
    return result

def main():
    x, y = 10, 0
    pdb.set_trace()   # Debugger starts here
    print(divide(x, y))

if __name__ == "__main__":
    main()
```

When you run this program, execution pauses at `pdb.set_trace()`. Now, you can type commands interactively.

## Common `pdb` Commands

Here are the most useful ones:

- **`n` (next)**: Execute the next line in the current function.
- **`s` (step)**: Step into a function call.
- **`c` (continue)**: Continue execution until the next breakpoint.
- **`q` (quit)**: Exit the debugger.
- **`p variable`**: Print the value of a variable.
- **`l` (list)**: Show source code around the current line.
- **`b lineno`**: Set a breakpoint at a specific line number.

## Example: Debugging a Function

Let’s say you are debugging a function that processes student scores:

```python
import pdb

def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    return average

def main():
    scores = [90, 85, 70, 0]
    pdb.set_trace()
    avg = calculate_average(scores)
    print("Average Score:", avg)

if __name__ == "__main__":
    main()
```

### Debugging session:

1. When paused, type `p scores` → shows `[90, 85, 70, 0]`.
2. Type `s` to step into `calculate_average`.
3. Inside, type `p total`, `p count`.
4. Step through until you find potential issues (like division by zero if scores were empty).

## Running Code with `-m pdb`

Another way is to run your script with:

```bash
python -m pdb myscript.py
```

This starts the debugger **before execution**. You can set breakpoints before the script runs.

## Breakpoints Without Changing Code (Python 3.7+)

From Python 3.7 onwards, you can use:

```python
breakpoint()
```

It behaves like `pdb.set_trace()` but respects the environment variable `PYTHONBREAKPOINT`, which allows customization.

## Debugging a Larger Program

Here’s a practical example with multiple functions:

```python
def greet(name):
    return f"Hello, {name}"

def farewell(name):
    return f"Goodbye, {name}"

def conversation(name):
    msg1 = greet(name)
    msg2 = farewell(name)
    return msg1 + " ... " + msg2

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    person = "Vinod"
    print(conversation(person))
```

During the session:

- Step into `conversation` using `s`.
- Step over each line using `n`.
- Print `msg1` or `msg2` using `p msg1`.

This way, you can confirm logic is correct.

## Creating a Test Suite with `pdb`

When writing unit tests, sometimes they fail and you want to debug interactively. You can run:

```bash
python -m pdb -m unittest discover
```

This launches failing tests inside the debugger, helping you quickly locate the issue.

## 📌 `pdb` Command Cheat Sheet

| Command        | Description                                      |
| -------------- | ------------------------------------------------ |
| `h`            | Show help for commands                           |
| `n` (next)     | Execute the next line (stay in current function) |
| `s` (step)     | Step into function calls                         |
| `c` (continue) | Continue execution until next breakpoint         |
| `q` (quit)     | Exit the debugger                                |
| `p expr`       | Print the value of an expression                 |
| `pp expr`      | Pretty-print the value of an expression          |
| `l` (list)     | Show source code around current line             |
| `b lineno`     | Set a breakpoint at line number                  |
| `b funcname`   | Set a breakpoint at function entry               |
| `cl lineno`    | Clear breakpoint at line                         |
| `where` or `w` | Show the current stack trace                     |
| `u` (up)       | Move up one stack frame                          |
| `d` (down)     | Move down one stack frame                        |
| `args`         | Show arguments of current function               |
| `! statement`  | Execute a Python statement in current context    |

## Conclusion

The `pdb` module is a powerful ally when debugging Python programs. Instead of scattering `print()` statements everywhere, use `pdb` to interactively step through code, inspect variables, and understand what’s really happening under the hood.

Next time you run into a tricky bug, just drop a `pdb.set_trace()` or `breakpoint()` and take control of your debugging process!
