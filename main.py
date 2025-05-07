# This file contains a Task Manager program that utilizes the 'Task', 'TaskList', and 'TaskManager'
# classes from the 'task_classes' module to manage tasks. It loads tasks from 'tasks.txt' file,
# presents a menu for users to perform various actions like adding, viewing, filtering, deleting,
# marking as done, or postponing tasks until the user chooses to exit.
from task_classes import Task, TaskList, TaskManager

task_manager = TaskManager()
task_manager.load_tasks_from_file('tasks.txt')

while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Filter tasks")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Postpone Task")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    should_exit = task_manager.handle_user_choice(choice)
    if should_exit:
        break