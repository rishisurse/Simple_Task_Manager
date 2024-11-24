def add_task(tasks):
    description = input("Enter task description: ")
    status = "Pending"
    tasks.append({"description": description, "status": status})
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']} - {task['status']}")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_status = input("Enter new status (Pending/Completed): ")
        tasks[task_number]['status'] = new_status
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if _name_ == "_main_":
    main()
