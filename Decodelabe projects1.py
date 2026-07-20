# ==============================
#      TO-DO LIST PROJECT
# ==============================

# List to store tasks
tasks = []


# Function to add task
def add_task():
    task = input("\nEnter a new task: ").strip()

    if task == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print("✅ Task added successfully!")


# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n========== YOUR TASKS ==========")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("================================")


# Function to delete task
def delete_task():
    if len(tasks) == 0:
        print("\nNo task to delete.")
        return

    view_tasks()

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"{removed}' deleted successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main Menu
while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")