# Student Task Manager: User Guide

## Starting the app

From the project folder run:

```bash
python app.py
```

You will see the menu:

```
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
0. Exit
```

Type the number of an option and press Enter.

## 1. Add a task

Type a title such as `Finish DevOps lab report`. Leading and trailing spaces are removed.
An empty title, or one longer than 100 characters, is rejected with a message and nothing is added.
Each task gets a number (its id). Ids are never reused, even after a delete.

## 2. Show tasks

Lists every task with its id. `[x]` means completed, `[ ]` means still pending.

```
[x] #1 Finish DevOps lab report
[ ] #2 Revise OS chapter 4
```

## 3. Complete a task

The app lists the pending tasks, then asks for the task number.
If there are no pending tasks it tells you so. If you pick a task that is already completed, you get a warning.

## 4. Delete a task

Enter the task number. If that id does not exist, the app says so and nothing changes.
Otherwise it shows the task title and asks `(y/n)`. Only `y` deletes; anything else cancels.

## 0. Exit

Closes the app. Your tasks are already saved in `tasks.json` in the project folder after every change.

## Troubleshooting

- **"Please enter a valid task number"**: type the number only, for example `2`, not `#2`.
- **Start with an empty list**: close the app and delete `tasks.json`.
- **`TypeError` about `|` when starting**: your Python is older than 3.10. Install a newer Python.
