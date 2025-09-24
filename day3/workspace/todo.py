#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

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
        tasks[index-1] = tasks[index-1].replace("[ ]", "[✅]", 1)
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