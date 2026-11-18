# Lab Report: Student Task Manager with Git and GitHub

**Name:** Muhammad Danish Jawad
**Registration No:** FA23-BSE-106
**Course:** CSC418 DevOps for Cloud Computing, Lab Assignment 4
**Repository:** https://github.com/DanishJawad106/student-task-manager
**Release:** https://github.com/DanishJawad106/student-task-manager/releases/tag/v1.0.0

## 1. Git vs GitHub, and add / commit / push

Git is the version control tool that runs on my machine. It records snapshots of the project and keeps the full history locally, with no network needed.
GitHub is a hosting service built around Git. It stores a copy of the repository online and adds the team features Git does not have: issues, pull requests, code review, Actions and releases.

- `git add` moves changes into the staging area, so I choose exactly what goes into the next commit.
- `git commit` saves the staged changes as a snapshot in the local history, with a message saying why.
- `git push` uploads my local commits to the remote (GitHub) so others can see and pull them.

## 2. Branches, pull requests, and merge conflicts

A branch is a separate line of work. I built each feature (add-task validation, complete-task, delete-task) on its own branch, so half-finished work never sat on `main` and each feature could be reviewed on its own.
A pull request asks to merge a branch into `main`. It shows the diff, links the issue it closes, runs CI, and gives a place for review comments before anything lands.

A merge conflict happens when two branches change the same lines of the same file differently, and Git cannot decide which version is correct. In Part D, `status/development` and `status/testing` both edited the `Project status:` line in README.md. After the first merge, the second one conflicted on that line. I resolved it by writing one line that keeps the meaning of both changes and removing the conflict markers.

## 3. fetch vs pull, merge vs rebase

- `git fetch` downloads new commits from the remote and updates `origin/main`, but does not touch my working branch. I can inspect what changed first.
- `git pull` is `fetch` followed by a merge (or rebase) into my current branch, in one step.

- `merge` joins two branches with a merge commit. History stays exactly as it happened, including the fork and join. I used merge commits for every PR, which is why `git log --graph` shows the feature branches.
- `rebase` replays my commits on top of another branch so history looks linear. It is cleaner to read, but it rewrites commit ids, so it should not be used on branches other people already pulled.

## 4. How Issues and Actions help a team

Issues turn work into a visible list: what needs doing, who is on it, and labels such as `enhancement`, `validation`, `testing` and `documentation`. Writing `Closes #1` in a PR closed the issue automatically on merge, so the issue history links straight to the code that fixed it.

GitHub Actions runs the tests on every push and pull request to `main`. Nobody has to remember to run them, and a broken change is visible on the PR before it is merged. In this project the first CI run failed on a deliberately wrong assertion, and the red check appeared on PR #9 until the fix commit made it green.

## 5. A difficulty and how I solved it

My laptop is logged in to two GitHub accounts, and my global Git config used the email of my other account. If I had committed with it, every commit would have shown up under the wrong user, and pushes could have used the wrong saved credentials.
I fixed it per repository instead of changing my global setup: `git config user.name` / `git config user.email` inside this repo only, switched the GitHub CLI to the FA23-BSE-106 account with `gh auth switch`, and set the repo's credential helper to `gh auth git-credential` so pushes use that account.

A second, smaller one: GitHub does not allow approving your own pull request (`Can not approve your own pull request`). Since I am the only contributor, I reviewed each PR with a Comment review plus an inline comment on a changed line, then merged.

## Evidence summary

| Requirement | In this repo |
|---|---|
| 12+ meaningful commits | yes, see `git log` |
| 3 feature branches | `feature/add-task`, `feature/complete-task`, `feature/delete-task` |
| 4+ issues | #1 to #5 |
| 5 merged pull requests | #6, #7, #8, #9, #10 |
| 1 resolved conflict | merge of `status/testing` into `main` |
| 3+ automated tests | 7 tests in `tests/test_task_manager.py` |
| 1 workflow | `.github/workflows/tests.yml` |
| 1 release | v1.0.0 |

Screenshots for every step are in `lab-evidence/`.
