"""Unit tests for TaskManager. Run with: python -m unittest discover -s tests -v"""
import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()  # no storage path, so nothing touches disk

    def test_add_task_stores_title_and_assigns_id(self):
        task = self.manager.add_task("  Finish lab report  ")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish lab report")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.list_tasks(), [])


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task = self.manager.add_task("Revise OS chapter 4")

    def test_complete_task_marks_it_completed(self):
        self.assertTrue(self.manager.complete_task(self.task.id))
        self.assertTrue(self.manager.get_task(self.task.id).completed)
        self.assertEqual(self.manager.pending_tasks(), [])

    def test_complete_task_twice_raises(self):
        self.manager.complete_task(self.task.id)
        with self.assertRaises(ValueError):
            self.manager.complete_task(self.task.id)


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.first = self.manager.add_task("Buy notebook")
        self.second = self.manager.add_task("Email professor")

    def test_delete_task_removes_only_that_task(self):
        self.assertTrue(self.manager.delete_task(self.first.id))
        remaining = self.manager.list_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0].id, self.second.id)
        self.assertIsNone(self.manager.get_task(self.first.id))

    def test_delete_unknown_id_returns_false(self):
        self.assertFalse(self.manager.delete_task(99))
        self.assertEqual(len(self.manager.list_tasks()), 2)


class TestStorage(unittest.TestCase):
    def test_tasks_persist_between_instances(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tasks.json"
            TaskManager(path).add_task("Persisted task")
            reloaded = TaskManager(path)
            self.assertEqual([t.title for t in reloaded.list_tasks()], ["Persisted task"])
            # New ids continue after the highest saved id.
            self.assertEqual(reloaded.add_task("Next").id, 2)


if __name__ == "__main__":
    unittest.main()
