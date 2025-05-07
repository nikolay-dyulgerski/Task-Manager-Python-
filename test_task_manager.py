import unittest
from task_classes import TaskManager
import os


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.test_filename = "C:\\Users\\user\\Desktop\\Project\\Project\\tasks.txt"
        self.task_manager.save_completed_tasks(self.test_filename)

    def test_load_tasks_from_file(self):

        test_filename = "C:\\Users\\user\\Desktop\\Project\\Project\\tasks.txt"
        with open(test_filename, "w") as file:
            file.write("Task 1,Description 1,2023-08-12,Done\n")
            file.write("Task 2,Description 2,2023-08-13,Pending\n")


        task_manager = TaskManager()
        task_manager.load_tasks_from_file(test_filename)


        self.assertEqual(len(task_manager.task_list.tasks), 2)
        self.assertEqual(task_manager.task_list.tasks[0].name, "Task 1")
        self.assertEqual(task_manager.task_list.tasks[1].name, "Task 2")

    def test_add_task(self):
        initial_task_count = len(self.task_manager.task_list.tasks)
        self.task_manager.add_task("Task 1", "Description 1", "2023-08-12")
        self.assertEqual(len(self.task_manager.task_list.tasks), initial_task_count + 1)
        added_task = self.task_manager.task_list.tasks[-1]
        self.assertEqual(added_task.name, "Task 1")
        self.assertEqual(added_task.description, "Description 1")
        self.assertEqual(added_task.deadline, "2023-08-12")
        self.assertEqual(added_task.status, "Pending")

    def test_mark_as_done(self):
        self.assertEqual(len(self.task_manager.task_list.tasks), 0)


        self.task_manager.add_task("Task 1", "Description", "2023-08-12")
        self.task_manager.mark_as_done(1)


        self.assertEqual(len(self.task_manager.task_list.tasks), 1)
        marked_task = self.task_manager.task_list.tasks[0]
        self.assertEqual(marked_task.status, "Done")

    def test_view_pending_tasks(self):
        self.task_manager.add_task("Task 1", "Description 1", "2023-08-12")
        self.task_manager.add_task("Task 2", "Description 2", "2023-08-13")

    def test_save_completed_tasks(self):

        self.task_manager.add_task("Task 1", "Description 1", "2023-08-12")
        self.task_manager.add_task("Task 2", "Description 2", "2023-08-13")
        self.task_manager.add_task("Task 3", "Description 3", "2023-08-14")
        self.task_manager.mark_as_done(1)
        self.task_manager.mark_as_done(3)
        test_filename = "tasks.txt"
        self.task_manager.save_completed_tasks(test_filename)
        self.assertTrue(os.path.exists(test_filename))
        with open(test_filename, "r") as file:
            file_contents = file.readlines()
        self.assertIn("Task 1,Description 1,2023-08-12,Done\n", file_contents)
        self.assertIn("Task 3,Description 3,2023-08-14,Done\n", file_contents)

    def delete_task(self, task_index):
        try:
            index = int(task_index)
            if index < 1 or index > len(self.task_list.tasks):
                raise IndexError("Task index out of range")
            del self.task_list.tasks[index - 1]
        except (ValueError, IndexError) as e:
            print(f"Error deleting task: {e}")


if __name__ == '__main__':
    unittest.main()
