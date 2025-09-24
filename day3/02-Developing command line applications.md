# Developing Command-Line Applications in Python

Python isn’t just for web apps, data science, or scripting—it’s also a fantastic language for building **command-line applications (CLI tools)**.

In this article, we’ll learn how to:

- Access command-line arguments with the **`sys` module**.
- Create user-friendly CLI apps with the **`argparse` module**.
- Chain CLI tools together using the **`subprocess` module**.

We’ll build practical examples that you can run on your terminal.

## Why Command-Line Applications?

Command-line tools are:

- Lightweight and fast.
- Easy to automate (via scripts, cron jobs).
- Flexible—users can chain commands together.

Examples include `git`, `pip`, or even simple utilities like `ls` or `grep`. Let’s build some of our own!

## Using the `sys` Module

The **`sys.argv`** list lets you access raw command-line arguments.

### Example 1: Greeting Script

```python
# greet_sys.py
import sys

if len(sys.argv) < 2:
    print("Usage: python greet_sys.py <name>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}!")
```

**Run it:**

```bash
python greet_sys.py Vinod
```

**Output:**

```
Hello, Vinod!
```

- `sys.argv[0]` is the script name.
- `sys.argv[1:]` are the arguments.

This works, but for complex apps, `argparse` is a better choice.

## Using the `argparse` Module

The `argparse` module makes your CLI tools **self-documenting** and user-friendly.

### Example 2: A Calculator CLI

```python
# calc.py
import argparse

parser = argparse.ArgumentParser(description="Simple calculator")

parser.add_argument("operation", choices=["add", "sub", "mul", "div"],
                    help="Operation to perform")
parser.add_argument("x", type=float, help="First number")
parser.add_argument("y", type=float, help="Second number")

args = parser.parse_args()

if args.operation == "add":
    print(args.x + args.y)
elif args.operation == "sub":
    print(args.x - args.y)
elif args.operation == "mul":
    print(args.x * args.y)
elif args.operation == "div":
    if args.y == 0:
        print("Error: Division by zero")
    else:
        print(args.x / args.y)
```

**Run it:**

```bash
python calc.py add 10 5
python calc.py sub 20 8
```

**Output:**

```
15.0
12.0
```

Notice how `argparse` automatically generates help text:

```bash
python calc.py --help
```

Output:

```
usage: calc.py [-h] {add,sub,mul,div} x y
```

### Example 3: CLI Tool with Optional Arguments

Let’s extend our calculator so users can display results with labels.

```python
# calc_verbose.py
import argparse

parser = argparse.ArgumentParser(description="Calculator with verbose mode")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"])
parser.add_argument("x", type=float)
parser.add_argument("y", type=float)
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show detailed output")

args = parser.parse_args()

if args.operation == "add":
    result = args.x + args.y
    op = "+"
elif args.operation == "sub":
    result = args.x - args.y
    op = "-"
elif args.operation == "mul":
    result = args.x * args.y
    op = "*"
else:  # div
    result = args.x / args.y
    op = "/"

if args.verbose:
    print(f"{args.x} {op} {args.y} = {result}")
else:
    print(result)
```

**Run it:**

```bash
python calc_verbose.py add 10 5 -v
```

**Output:**

```
10.0 + 5.0 = 15.0
```

## Chaining CLI Applications with `subprocess`

Sometimes, your CLI needs to **call other CLI tools**. That’s where the **`subprocess`** module comes in.

### Example 4: Running Shell Commands

```python
import subprocess

# Run 'ls' command
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
```

This runs the system’s `ls -l` command and captures the output.

### Example 5: Chaining Our Own CLI Apps

Imagine we have two scripts:

1. `greet_sys.py` (greets a user).
2. `calc.py` (performs math).

We can chain them:

```python
# chain.py
import subprocess

# Step 1: Greet user
subprocess.run(["python", "greet_sys.py", "Kumar"])

# Step 2: Perform calculation
subprocess.run(["python", "calc.py", "mul", "7", "6"])
```

**Run it:**

```bash
python chain.py
```

**Output:**

```
Hello, Kumar!
42.0
```

### Example 6: Capturing Output from Another Script

```python
# capture.py
import subprocess

result = subprocess.run(["python", "calc.py", "add", "12", "8"],
                        capture_output=True, text=True)

print("Calculation result:", result.stdout.strip())
```

**Output:**

```
Calculation result: 20.0
```

Here, we captured the output of one CLI tool and used it inside another program.

## Conclusion

In this tutorial, we’ve learned how to:

- Use **`sys.argv`** for quick access to raw command-line arguments.
- Use **`argparse`** to build user-friendly, professional CLI apps.
- Use **`subprocess`** to chain commands and capture their output.

With these tools, you can build your own CLI utilities—whether for personal automation, DevOps, or full-scale developer tools.

---

# Project: Building a Todo Manager CLI App in Python

Managing daily tasks is something we all need. Instead of installing big apps, let’s build a simple **command-line todo manager**.

We’ll support commands like:

- **add** → Add a new task.
- **list** → Show all tasks.
- **done** → Mark a task as complete.
- **clear** → Remove all tasks.

Tasks will be stored in a simple **text file** (`todos.txt`).

## Step 1: Setting Up with argparse

```python
# todo.py
import argparse
import os

TODO_FILE = "todos.txt"

def read_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f]

def write_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = read_tasks()
    tasks.append("[ ] " + task)
    write_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_done(index):
    tasks = read_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1] = tasks[index-1].replace("[ ]", "[x]", 1)
        write_tasks(tasks)
        print(f"Task {index} marked as done.")
    else:
        print("Invalid task number.")

def clear_tasks():
    write_tasks([])
    print("All tasks cleared!")

# ---- Argument parsing ----
parser = argparse.ArgumentParser(description="Todo Manager CLI")
subparsers = parser.add_subparsers(dest="command")

# Add task
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task", type=str, help="Task description")

# List tasks
subparsers.add_parser("list", help="List all tasks")

# Mark done
done_parser = subparsers.add_parser("done", help="Mark task as done")
done_parser.add_argument("index", type=int, help="Task number to mark done")

# Clear tasks
subparsers.add_parser("clear", help="Clear all tasks")

args = parser.parse_args()

# Command execution
if args.command == "add":
    add_task(args.task)
elif args.command == "list":
    list_tasks()
elif args.command == "done":
    mark_done(args.index)
elif args.command == "clear":
    clear_tasks()
else:
    parser.print_help()
```

## Step 2: Trying It Out

**Add tasks:**

```bash
python todo.py add "Finish Python blog"
python todo.py add "Call Shyam"
```

**List tasks:**

```bash
python todo.py list
```

**Output:**

```
1. [ ] Finish Python blog
2. [ ] Call Shyam
```

**Mark task done:**

```bash
python todo.py done 1
```

**Output:**

```
Task 1 marked as done.
```

**List again:**

```
1. [x] Finish Python blog
2. [ ] Call Shyam
```

**Clear tasks:**

```bash
python todo.py clear
```

## Step 3: Chaining with subprocess

Let’s say we want a script that:

1. Adds a reminder.
2. Lists tasks immediately after.

```python
# todo_chain.py
import subprocess

# Add a new task
subprocess.run(["python", "todo.py", "add", "Buy groceries for Sundar"])

# Show all tasks
subprocess.run(["python", "todo.py", "list"])
```

**Run it:**

```bash
python todo_chain.py
```

**Output:**

```
Task added: Buy groceries for Sundar
1. [ ] Buy groceries for Sundar
```

## Step 4: Capturing Output

What if you want to **process the tasks inside another program**?

```python
# capture_list.py
import subprocess

result = subprocess.run(["python", "todo.py", "list"],
                        capture_output=True, text=True)

print("Captured task list:")
print(result.stdout)
```

**Output:**

```
Captured task list:
1. [ ] Call Shyam
2. [x] Finish Python blog
```

## Conclusion

We built a **Todo Manager CLI** with:

- `argparse` for handling commands and subcommands.
- File operations for persistence.
- `subprocess` for chaining multiple CLI commands together.

This project demonstrates how small utilities can grow into **powerful command-line tools**.

👉 Next challenge for readers:

- Add a **search command** to find tasks by keyword.
- Add a **deadline option** when adding tasks.
- Export tasks to JSON or XML using what you learned earlier!
