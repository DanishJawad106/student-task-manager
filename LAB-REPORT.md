# Lab Report

Muhammad Danish Jawad, FA23-BSE-106
CSC418 DevOps for Cloud Computing, Lab Assignment 4

## 1. Difference between Git and GitHub; purpose of add, commit and push

Git is the version control tool installed on my computer. It keeps the history of the project locally. GitHub is a website that hosts the repository online and adds things like issues, pull requests and Actions.

- `git add` stages the changes I want in the next commit.
- `git commit` saves the staged changes in the history with a message.
- `git push` uploads my commits to GitHub.

## 2. Why branches and pull requests are used; what causes merge conflicts

Branches let me work on a feature without touching main, so main always stays working. A pull request is used to review the changes, link the issue and run the tests before the branch is merged into main.

A merge conflict happens when two branches change the same line of a file in different ways. Git cannot decide which version to keep, so it asks you to fix it. In this assignment both status branches changed the "Project status" line in README.md.

## 3. Difference between fetch and pull, and between merge and rebase

`git fetch` downloads new commits from GitHub but does not change my branch. `git pull` downloads them and merges them into my branch.

`merge` joins two branches with a merge commit and keeps the history as it happened. `rebase` moves my commits on top of the other branch so the history is in one straight line, but it changes the commit ids.

## 4. How GitHub Issues and Actions help a development team

Issues keep a list of what needs to be done, with labels, and they close automatically when a pull request with "Closes #N" is merged. Actions run the tests automatically on every push and pull request, so a broken change shows up before it is merged.

## 5. One difficulty I faced and how I solved it

My laptop has two GitHub accounts logged in, and my global Git email belonged to the other account. I set the username and email only for this repository with `git config` (without `--global`) and switched the GitHub CLI to the correct account with `gh auth switch`.

GitHub also does not allow approving your own pull request, so I added comment reviews on the pull requests before merging them.
