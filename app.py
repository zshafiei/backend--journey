import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return file.read().splitlines()

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task saved!\n")

    elif choice == "2":
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        print()

    elif choice == "3":
        break

    else:
        print("Invalid choice\n")
