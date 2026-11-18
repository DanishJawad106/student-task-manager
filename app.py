"""Console front end for the Student Task Manager.

Run with:  python app.py
"""
from task_manager import TaskManager

MENU = """
===== Student Task Manager =====
1. Add task
2. Show tasks
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


def main() -> None:
    manager = TaskManager()
    actions = {"1": handle_add, "2": handle_list}
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
