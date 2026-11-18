"""Core logic for the Student Task Manager.

This module has no input() or print() calls so it can be unit tested
without a console. The console front end lives in app.py.
"""
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Keeps the list of tasks and hands out increasing task ids.

    If storage_path is given, tasks are loaded from and saved to that JSON
    file after every change. Tests pass None to keep everything in memory.
    """

    def __init__(self, storage_path: str | Path | None = None) -> None:
        self.storage_path = Path(storage_path) if storage_path else None
        self.tasks: list[Task] = []
        self._next_id = 1
        self._load()

    def add_task(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self.tasks.append(task)
        self._next_id += 1
        self._save()
        return task

    def list_tasks(self) -> list[Task]:
        return list(self.tasks)

    def _load(self) -> None:
        if self.storage_path is None or not self.storage_path.exists():
            return
        data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        self.tasks = [Task(**item) for item in data]
        # Ids are never reused, even after a delete, so a deleted id cannot
        # silently point at a different task later.
        self._next_id = max((t.id for t in self.tasks), default=0) + 1

    def _save(self) -> None:
        if self.storage_path is None:
            return
        data = [asdict(t) for t in self.tasks]
        self.storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
