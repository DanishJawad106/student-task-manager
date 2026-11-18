"""Core logic for the Student Task Manager.

This module has no input() or print() calls so it can be unit tested
without a console. The console front end lives in app.py.
"""
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Keeps the list of tasks and hands out increasing task ids."""

    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return list(self.tasks)
