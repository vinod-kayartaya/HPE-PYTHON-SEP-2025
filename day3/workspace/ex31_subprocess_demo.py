import subprocess


def menu():
    print("=== Main Menu ===")
    print("0. Exit")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as DONE")
    print("4. Remove all tasks")
    print()
    return int(input('Enter your choice: '))


def main():
    while True:
        subprocess.run(['clear'])
        choice = menu()

        if choice == 0:
            exit(0)

        if choice not in range(5):
            print('Invalid choice. Try again')
            continue

        if choice == 1:
            task = input('Enter task details: ')
            result = subprocess.run(['python3', 'todo.py', 'add', task], capture_output=True, text=True)
        elif choice == 2:
            result = subprocess.run(['python3', 'todo.py', 'list'], capture_output=True, text=True)
        elif choice == 3:
            task_id = input('Enter task id: ')
            result = subprocess.run(['python3', 'todo.py', 'done', task_id], capture_output=True, text=True)
        
        print(result.stdout)
        input('Press RETURN to continue')

if __name__ == '__main__':
    main()
