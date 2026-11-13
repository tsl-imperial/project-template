# Getting Started with GitHub

This guide covers what you need to manage coursework with Git and GitHub. It uses **GitHub Desktop**, which needs no command line; equivalent commands are listed at the end.

- **Git** tracks changes to your files.
- **GitHub** hosts your repository online and lets your team share it.
- **GitHub Desktop** is an app for using both.

## Setup

1. Create an account at [github.com](https://github.com). Using your Imperial email makes you eligible for the [Student Developer Pack](https://education.github.com/pack).
2. Install [GitHub Desktop](https://desktop.github.com) and sign in.
3. In GitHub Desktop, check **Preferences → Git** (Mac) or **Options → Git** (Windows): the name and email must match your GitHub account, or your commits will not be credited to you.
4. Clone your repository: **File → Clone repository**, pick it from the list, choose a folder and click **Clone**.

## Daily workflow

1. **Fetch origin**, then **Pull origin** if there are changes. Do this before you start, every time.
2. Work on your notebooks and code.
3. Review the changed files in GitHub Desktop. Untick anything you do not mean to commit.
4. Write a commit message and click **Commit to main**.
5. Click **Push origin**. Until you push, your work exists only on your computer.

Commit small pieces of work often, and push at least daily.

### Commit messages

Say what changed: "Add correlation heatmap to EDA notebook" or "Fix missing value handling in clean_data()". Messages such as "Update", "Fixed stuff" or "Final version" tell your team and your marker nothing.

### What not to commit

The `.gitignore` file already excludes conda environments, `.env` files and temporary files such as `.ipynb_checkpoints/` and `__pycache__/`. You are responsible for the rest:

- data files over 50 MB (see [Data](../README.md#data))
- passwords and API keys
- personal data

If you commit a password or key by mistake, change it straight away: deleting the file does not remove it from the history.

## Working in a team

Pull before you start, agree who is working on which file, and work on different notebooks where possible. Two people editing the same notebook at once is the most common source of conflicts, because notebook files are hard to merge.

### Merge conflicts

When two people change the same lines, GitHub Desktop reports a conflict:

1. Click **Open in [your editor]**.
2. Find the conflict markers:
   ```
   <<<<<<< HEAD
   your changes
   =======
   your teammate's changes
   >>>>>>> main
   ```
3. Keep the right version (or combine them) and delete the markers.
4. Save, then commit in GitHub Desktop.

### Branches (optional)

For most coursework you can work on `main`. A branch is useful for trying something risky: click **Current branch → New branch**, work and commit as usual, and when it works, push it and open a **Pull Request** on GitHub.com to merge it into `main`. If it does not work, switch back to `main` and delete the branch.

## Fixing mistakes

| Problem | What to do |
|---------|------------|
| Can't push: "need to pull first" | Someone else pushed. **Pull origin**, resolve any conflicts, push again. |
| Last commit not pushed yet and wrong | **History** tab, right-click the commit, **Undo commit**. Your changes return to uncommitted. |
| Commit already pushed and wrong | **History** tab, right-click the commit, **Revert changes in commit**. This adds a new commit that undoes it. |
| Discard uncommitted changes to a file | Right-click the file in the **Changes** tab, **Discard changes**. This cannot be undone. |
| Commits show the wrong name | Fix the name and email (Setup step 3) and tell your instructor which earlier commits were yours. |
| "Authentication failed" | Sign out of GitHub Desktop and sign back in. |
| "Repository not found" | Check you have accepted the collaborator invitation. |

Never force push: it can delete your teammates' work.

## Checking contributions

**History** in GitHub Desktop lists every commit, who made it and what changed. On GitHub.com, **Insights → Contributors** shows the same per person; your instructor uses this to assess individual contributions.

## Making a ZIP backup

You may be asked to submit a ZIP copy of your repository. Push all your changes first, then on GitHub.com click the green **Code** button and **Download ZIP**.

## Command line equivalents

| Task | GitHub Desktop | Command line |
|------|----------------|--------------|
| Get latest changes | Fetch / Pull origin | `git pull` |
| See what changed | Changes tab | `git status`, `git diff` |
| Commit | Commit to main | `git add .` then `git commit -m "message"` |
| Upload | Push origin | `git push` |
| Undo last (unpushed) commit | History → Undo commit | `git reset HEAD~1` |
| Undo a pushed commit | History → Revert changes in commit | `git revert <commit>` |
| New branch | Current branch → New branch | `git switch -c name` |
| History | History tab | `git log --oneline` |

## Further reading

- [GitHub Desktop documentation](https://docs.github.com/en/desktop)
- [GitHub Skills](https://skills.github.com/): short interactive courses
