## Simple To-Do List App
## Author: Esentila
## Description: A command-line task manager built with Python v1.0

tasks = []

def show_menu():
    print("\n============================")
    print("       TO-DO LIST APP       ")
    print("============================")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")
    print("============================")

def view_tasks():
    print("\n--- Your Tasks ---")
    if len(tasks) == 0:
        print("No tasks yet. Add one!")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "○"
            print(f"{i + 1}. [{status}] {task['name']}")

def add_task():
    name = input("\nEnter task name: ").strip()
    if name:
        tasks.append({"name": name, "done": False})
        print(f"Task '{name}' added!")
    else:
        print("Task name cannot be empty.")

def mark_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print(f"Task '{tasks[num - 1]['name']}' marked as done!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed['name']}' deleted.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the To-Do List App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nGoodbye! Stay productive 👋")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
    ## End of file
