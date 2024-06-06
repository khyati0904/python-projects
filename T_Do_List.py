import os

# Define the file name for storing tasks
FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

# Add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i + 1}. {task['task']} [{status}]")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()