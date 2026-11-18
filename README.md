# student-task-manager

Project status: In development (core features done), testing in progress

[![Tests](https://github.com/DanishJawad106/student-task-manager/actions/workflows/tests.yml/badge.svg)](https://github.com/DanishJawad106/student-task-manager/actions/workflows/tests.yml)

A small Python console app for students to keep track of coursework tasks: add, list, complete and delete.
It was built for CSC418 (DevOps for Cloud Computing), Lab Assignment 4, where the point is the workflow around the code:
feature branches, issues, reviewed pull requests, a resolved merge conflict, CI with GitHub Actions and a tagged release.
The app logic is kept free of `input()`/`print()` so it can be unit tested, and 7 unittest tests run on every push and pull request to `main`.

## Features

- Add a task. Empty, whitespace-only and over-100-character titles are rejected.
- Show all tasks with a `[x]` / `[ ]` completion mark.
- Complete a task: pending tasks are listed first, and completing an already completed task gives a warning.
- Delete a task by id: unknown ids are rejected and a y/n confirmation is asked first.
- Tasks are saved to `tasks.json`, so they are still there next time you run the app.

## Project layout

```
task_manager.py              Task model and TaskManager (all logic, no console I/O)
app.py                       Console menu that calls TaskManager
tests/test_task_manager.py   unittest tests
.github/workflows/tests.yml  GitHub Actions workflow
docs/user-guide.md           Short user guide
LAB-REPORT.md                Answers to the assignment questions
lab-evidence/                Screenshots of each assignment step
```

## Setup

Requires Python 3.10 or newer (the code uses `X | None` type hints). There are no third-party dependencies.

```bash
git clone https://github.com/DanishJawad106/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python app.py
```

Pick an option by number: 1 add, 2 show, 3 complete, 4 delete, 0 exit. See [docs/user-guide.md](docs/user-guide.md) for an example session.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs in GitHub Actions on every push to `main` and every pull request targeting `main`.

## What I would do next

- Due dates and sorting by due date, since that is what a student actually needs from a task list.
- A `--file` option so different courses can keep separate task files.
- Tests for `app.py` itself by patching `input()`, which are not covered yet.
