
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            def display_menu():
    

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
