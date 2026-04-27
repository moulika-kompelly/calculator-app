tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!\n")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!\n")
        else:
        print("Invalid number!\n")

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")