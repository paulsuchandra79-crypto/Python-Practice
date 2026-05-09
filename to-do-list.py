# Mini Project: To-Do List App in Python

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # View Tasks
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # Add Task
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_num = int(input("Enter task number to remove: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List App...")
        break

    else:
        print("Invalid choice. Please try again.")
