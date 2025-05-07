# This file contains three classes: Task, TaskList, and TaskManager.
# The Task class represents individual tasks with attributes such as name, description, deadline, and status.
# TaskList manages a list of tasks, allowing addition and viewing of tasks based on status.
# TaskManager coordinates user interactions, providing functionalities like adding, viewing, filtering, deleting,
# marking tasks as done, postponing tasks, and saving/loading tasks from a file named 'tasks.txt'.
class Task:
    """
   Presents a single task
   """
    def __init__(self, name, description=None, deadline=None, status="Pending"):
        """
        Initialize a Task object.
        Args:
        name(str): The name of the task.
        description(str): Description of the task.
        deadline(str, optional): Task deadline.
        status(str, optional): Task status. Defaults to "Pendin "
         """

        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        """ Mark the task as Done. """
        self.status = "Done"

        """ Postpone the task  """
    def postpone(self):
        self.status = "Postponed"


class TaskList:
    """Represents a list of tasks"""

    def __init__(self):
        """Initialize a TaskList object."""
        self.tasks = []

    def add_task(self, task):
        """
        Add task to the list.
        Args:
            task (Task): Task object to add to the list.
        """
        self.tasks.append(task)

    def view_tasks(self):
        """View the list of the tasks"""
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(
                    f"{idx}. [{task.status}]{task.name} - Deadline: {task.deadline}"
                )


class TaskManager:
    """Manage tasks and interactions"""

    def __init__(self):
        """Initialize a TaskManager object."""
        self.task_list = TaskList()
        self.home_selected = False

    def add_task(self, name, description=None, deadline=None):
        """ Add a new task to the task list
        Args:
        name(str): name of the task
        description(str, optional): description of the task
        deadline(str, optional): deadline of the task
        """
        task = Task(name, description, deadline)
        self.task_list.add_task(task)
        print(f'Task "{name}" added successfully!')

    def view_tasks(self):
        """ Show all the tasks in the task list. """
        self.task_list.view_tasks()

    def view_tasks_by_status(self, status):
        filtered_tasks = [task for task in self.task_list.tasks if task.status == status]
        if filtered_tasks:
            print(f"Tasks with status '{status}':")
            for idx, task in enumerate(filtered_tasks, start=1):
                print(f"{idx}. [{task.status}] {task.name} - Deadline: {task.deadline}")

    def delete_task(self, task_index):
        """Delete a specific task or all of them
        Args:
            task_index (str): the index or action to delete tasks
        """
        if task_index == "DELETE ALL":
            confirmation = input("Are you sure you want to delete all of the tasks ? (Yes/No): ")
            if confirmation.lower() == "yes":
                self.task_list.tasks = []
                print("All tasks deleted! ")
            elif confirmation.lower() == "no":
                print("No tasks deleted! ")
            else:
                print("Invalid input. Enter Yes or No. ")
        elif task_index.isdigit():
            task_index = int(task_index)
            if 1 <= task_index <= len(self.task_list.tasks):
                deleted_task = self.task_list.tasks.pop(task_index - 1)
                print(f'Task "{deleted_task.name}" deleted successfully!')
            else:
                print("Invalid input enter the number of the task! ")
        elif task_index == "Home":
            print("Returning to main menu!")
        else:
            print("Invalid input. Enter a valid task number or 'DELETE ALL' or write 'Home' to get back to main menu. ")
            task_index = input("Enter the task number to delete or 'DELETE ALL' to remove all. ")

    def mark_as_done(self, task_index):
        """
        Marks a task as done based on the provided task index.
        Args:
            task_index(int or str): The index of the task is mark as Done.
            if task_index is an integer the task will be marked as Done
            if task_index is Home, the method will print a message and get back to the main menu
            """
        if 1 <= task_index <= len(self.task_list.tasks):
            self.task_list.tasks[task_index - 1].mark_as_done()
            print("Task marked as Done!")
        elif task_index == "Home":
            print("Returning to main menu!")
        else:
            print("Invalid task index.")

    def view_pending_tasks(self):
        """ View only pending tasks, when opening the mark as done funcion """
        pending_tasks = [task for task in self.task_list.tasks if task.status == "Pending"]
        if pending_tasks:
            print("Pending Tasks:")
            for idx, task in enumerate(pending_tasks, start=1):
                print(f"{idx}. [{task.status}] {task.name} - Deadline: {task.deadline}")
        else:
            print("No tasks to show!")

    def postpone_task(self, task_index):
        """ To postpone a task
        Args:
        task_index(int): The index of the task to postpone.
        """
        if 1 <= task_index <= len(self.task_list.tasks):
            self.task_list.tasks[task_index - 1].postpone()
            print("Task postponed!")
        elif task_index == "Home":
            print("Returning to main menu!")
        else:
            print("Invalid task index.")

    def save_completed_tasks(self, filename):
        completed_tasks = [task for task in self.task_list.tasks if task.status == "Done"]
        with open("tasks.txt", "w") as file:
            for task in completed_tasks:
                file.write(f"{task.name},{task.description},{task.deadline},{task.status}\n")
            print("Completed tasks save to file.")

    def filtering_tasks(self, status):
        """ Filter tasks based on status and print them.
        Args:
        status(str): the status with which the tasks will be marked
        """
        filtered_tasks = [task for task in self.task_list.tasks if task.status.lower() == status.lower()]
        if filtered_tasks:
            print(f"Filtered tasks with status '{status}':")
            for idx, task in enumerate(filtered_tasks, start=1):
                print(f"{idx}. [{task.status}] {task.name} - Deadline: {task.deadline}")
            else:
                print("No tasks found.")

    def save_tasks_to_file(self, filename):
        """Saves tasks to the file tasks.txt
        Args:
        the name of the file(str): Saves it to the path
        """

        with open("C:\\Users\\user\\Desktop\\Project\\Project\\tasks.txt", 'w') as file:
            for task in self.task_list.tasks:
                file.write(f"{task.name},{task.description},{task.deadline},{task.status}\n")
        print("Tasks saved to file.")

    def load_tasks_from_file(self, filename):
        """ Loads tasks from the file and adds them to the list
        Args:
        name of the file(str): The path which it opens to load them
        """

        with open("C:\\Users\\User\\Downloads\\Project\\tasks.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_info = line.strip().split(',')
                if len(task_info) == 4:
                    task_name, task_desc, task_deadline, task_status = task_info
                    task = Task(task_name, task_desc, task_deadline, task_status)
                    self.task_list.add_task(task)
                else:
                    print(f"Issue parsing line: {line}. Insufficient information for task creation.")

    print("Tasks loaded from file.")

    def home(self):
        """
        Set the home_selected attribute to True.
        """

        self.home_selected = True

    def handle_user_choice(self, choice):
        """ Handle user choices for task management.
        Args:
            choice(str): The option chosen from the user by the menu.
        Returns:
            bool: True if the user decides to exit, if not then False
        """

        if self.home_selected:
            self.home_selected = False
            return False
        if choice == "1":
            new_task = input("Enter the task: ")
            description = input("Enter task description (optional): ")
            deadline = input("Enter task deadline (optional): ")
            self.add_task(new_task, description, deadline)
        elif choice == "2":
            self.view_tasks()
        elif choice == "3":
            status = input("Enter the status to filter tasks(Done/Pending): ")
            self.view_tasks_by_status(status)
        elif choice == "4":
            self.view_tasks()
            task_index = input("Enter the task number to delete or write 'DELETE ALL' to remove them: ")
            self.delete_task(task_index)
        elif choice == "5":
            self.view_pending_tasks()
            task_index = input("Enter the task number as Done or write 'Home' to get back to main menu: ")
            if task_index.isdigit():
                self.mark_as_done(int(task_index))
            elif task_index == "Home":
                print("Returning to main menu!")
            else:
                print("Invalid input!")
        elif choice == "6":
            self.view_pending_tasks()
            task_index = input("Enter the task number to Postpone or write 'Home' to get back to main menu: ")
            if task_index.isdigit():
                self.postpone_task(int(task_index))
            elif task_index == "Home":
                print("Returning to main menu!")
            else:
                print("Invalid Input!")
        elif choice == "7":
            self.save_tasks_to_file("C:\\Users\\user\\Desktop\\Project\\Project\\tasks.txt")
            print("Exiting Task Manager. Goodbye!")
            return True
        elif choice == "Home":
            self.home()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        return False
