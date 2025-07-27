tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")