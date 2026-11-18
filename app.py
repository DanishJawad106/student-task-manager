"""Console front end for the Student Task Manager.

Run with:  python app.py
"""
from task_manager import TaskManager

STORAGE_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
0. Exit
"""


def handle_add(manager: TaskManager) -> None:
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added task #{task.id}: {task.title}")


def handle_list(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "x" if task.completed else " "
        print(f"[{mark}] #{task.id} {task.title}")


def read_task_id(prompt: str) -> int | None:
    """Ask for a task id. Returns None if the input is not a positive number."""
    raw = input(prompt).strip()
    if not raw.isdigit() or int(raw) == 0:
        print("Please enter a valid task number, for example 1.")
        return None
    return int(raw)


def handle_complete(manager: TaskManager) -> None:
    pending = manager.pending_tasks()
    if not pending:
        print("No pending tasks to complete.")
        return
    print("Pending tasks:")
    for task in pending:
        print(f"  #{task.id} {task.title}")
    task_id = read_task_id("Task number to complete: ")
    if task_id is None:
        return
    try:
        found = manager.complete_task(task_id)
    except ValueError as error:
        print(error)
        return
    if found:
        print(f"Task #{task_id} marked as completed.")
    else:
        print(f"Task #{task_id} not found.")


def handle_delete(manager: TaskManager) -> None:
    task_id = read_task_id("Task number to delete: ")
    if task_id is None:
        return
    if manager.delete_task(task_id):
        print(f"Task #{task_id} deleted.")
    else:
        print(f"Task #{task_id} not found.")


def main() -> None:
    manager = TaskManager(STORAGE_FILE)
    actions = {
        "1": handle_add,
        "2": handle_list,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if action is None:
            print("Unknown option, try again.")
            continue
        action(manager)


if __name__ == "__main__":
    main()
