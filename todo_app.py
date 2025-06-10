# todo_app.py

# Declaring an empty list to save tasks
tasks = []

# Add task
def add_task(task):
    tasks.append(task)
    print(f' Task "{task}" added.')

# List tasks
def list_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    print("\nYour Tasks")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

# Remove tasks
def remove_tasks(task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task numbers")
        return
    removed = tasks.pop(task_number - 1)
    print(f'Task "{removed}" removed.')

# menu
def main():
     while True:
         print("\nOptions:")
         print("1. Add Task")
         print("2. List Tasks")
         print("3. Remove Task")
         print("4. Exit")

         choice = input("Choose an option: ")

         if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
         elif choice == "2":
            list_tasks()
         elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_tasks(task_number)
            except ValueError:
                print("Please enter valid number.")
         elif choice == "4":
             print("Good Bye!")
             break
         else:
             print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


