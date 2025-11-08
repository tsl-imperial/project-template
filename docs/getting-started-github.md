# Getting Started with GitHub

This guide will help you get started with GitHub for your coursework. We recommend using **GitHub Desktop** - it's the easiest way to work with Git and GitHub.

## What is Git and GitHub?

- **Git**: Version control system that tracks changes to your files
- **GitHub**: Website that hosts your Git repositories online
- **GitHub Desktop**: Desktop app that makes Git easy to use (no command line needed!)

## Setup

### 1. Create a GitHub Account

If you don't have one already:
1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Use your Imperial College email for education benefits

### 2. Install GitHub Desktop

1. Download from [desktop.github.com](https://desktop.github.com)
2. Install and open the app
3. Sign in with your GitHub account

## Working with Your Repository

### Clone Your Repository

After creating your repository from the template:

1. Open GitHub Desktop
2. Click **File** → **Clone repository**
3. Find your repository in the list
4. Choose where to save it on your computer
5. Click **Clone**

Your repository is now on your computer!

### Basic Workflow with GitHub Desktop

#### 1. Make Changes

Work on your project normally:
- Edit code in your favorite editor (VS Code, PyCharm, etc.)
- Run Jupyter notebooks
- Add data files (remember: keep them in `data/` folder)

#### 2. Review Changes

In GitHub Desktop:
- You'll see all changed files in the left sidebar
- Click on files to see what changed (green = added, red = removed)
- Review your changes before committing

#### 3. Commit Changes

A commit is like a "save point" for your project:

1. Check the boxes next to files you want to commit (usually all)
2. Write a **commit message** in the bottom-left:
   - Summary: Brief description (e.g., "Add data cleaning code")
   - Description (optional): More details if needed
3. Click **Commit to main**

**Good commit messages:**
- ✅ "Add exploratory data analysis notebook"
- ✅ "Fix bug in data loading function"
- ✅ "Update README with installation instructions"

**Bad commit messages:**
- ❌ "Update"
- ❌ "Changes"
- ❌ "asdfasdf"

#### 4. Push to GitHub

After committing, your changes are saved locally but not yet on GitHub:

1. Click **Push origin** (top-right)
2. Your changes are now on GitHub!

**Tip:** Push regularly so your work is backed up online.

### Viewing Your Repository Online

1. In GitHub Desktop, click **Repository** → **View on GitHub**
2. Or go to `https://github.com/YOUR-USERNAME/YOUR-REPO-NAME`

## Working in a Team (Group Projects)

### Getting Team Updates

Before you start working, get the latest changes:

1. Click **Fetch origin** (top-right)
2. If there are changes, click **Pull origin**

**Always pull before you start working!** This avoids conflicts.

### Handling Merge Conflicts

If two people edited the same file:

1. GitHub Desktop will warn you about conflicts
2. Click **Open in [Your Editor]**
3. Look for conflict markers:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Teammate's changes
   >>>>>>> main
   ```
4. Decide which version to keep (or combine them)
5. Remove the conflict markers
6. Save the file
7. In GitHub Desktop, commit the resolved conflict

**Tips to avoid conflicts:**
- Communicate with your team about who's working on what
- Pull frequently
- Work on different files when possible

## Using Branches (Optional but Recommended)

Branches let you work on features without affecting the main code.

### Create a Branch

1. Click **Current branch** (top-center)
2. Click **New branch**
3. Name it (e.g., "data-analysis" or "fix-bug")
4. Click **Create branch**

### Work on Your Branch

- Make changes and commit as normal
- Your main branch stays unchanged
- Perfect for trying new things!

### Merge Back to Main

When your work is ready:

1. Push your branch to GitHub
2. On GitHub.com, create a **Pull Request**
3. Team reviews your changes
4. Click **Merge pull request**

GitHub Issues can help you track tasks and bugs in your project.

## Common Tasks

### Undo Last Commit (Before Pushing)

1. Click **History** tab
2. Right-click the last commit
3. Click **Undo commit**

Your changes return to "uncommitted" state.

### Discard All Changes to a File

1. Right-click the file in Changes tab
2. Click **Discard changes**

**Warning:** This permanently deletes your changes!

### See Full History

1. Click **History** tab
2. See all commits, who made them, and when
3. Click any commit to see what changed

## Command Line Basics (Optional)

Most students use GitHub Desktop, but here are basic Git commands if needed:

### Basic Commands

```bash
# Check status
git status

# See what changed
git diff

# Pull latest changes
git pull

# Stage all changes
git add .

# Commit
git commit -m "Your message"

# Push to GitHub
git push

# Create and switch to new branch
git checkout -b branch-name

# Switch branches
git checkout main
```

### View History
```bash
# See commit history
git log

# See simplified history
git log --oneline
```

## Best Practices

### Do This ✅

- **Commit often**: Small, frequent commits are better than large ones
- **Write clear messages**: Explain what and why
- **Pull before you work**: Always get latest changes first
- **Push regularly**: Back up your work online
- **Review before committing**: Check what you're committing

### Don't Do This ❌

- **Don't commit secrets**: Never commit API keys or passwords
- **Don't commit large files**: Keep datasets in `.gitignore`
- **Don't use vague messages**: "Update" tells you nothing later
- **Don't force push**: Can delete teammates' work
- **Don't work without pulling**: Leads to conflicts

## Troubleshooting

### "Can't push - need to pull first"

Someone else pushed changes:
1. Click **Pull origin**
2. Resolve any conflicts
3. Push again

### "Authentication failed"

1. Open GitHub Desktop
2. Go to **File** → **Options** (Windows) or **Preferences** (Mac)
3. Click **Sign out** and sign back in

### "Repository not found"

- Check you have access to the repository
- For private repos, ensure you're added as a collaborator
- Try signing out and back in

### Changes Not Showing in GitHub Desktop

- Make sure you saved the files!
- Check you're in the right repository (top-left dropdown)
- Try **Repository** → **Refresh**

## Learning More

### GitHub Desktop
- [GitHub Desktop Documentation](https://docs.github.com/en/desktop)
- [GitHub Desktop Tutorial](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop)

### Git Basics
- [Git Workflows](git-workflows.md) - More advanced Git topics
- [GitHub Skills](https://skills.github.com/) - Interactive tutorials
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### For Your Coursework
- [Submission Guidelines](submission-guidelines.md) - Preparing for submission
- [Getting Help](getting-help.md) - Troubleshooting guide

## Quick Reference

| Task | GitHub Desktop | Command Line |
|------|----------------|--------------|
| Get latest changes | Fetch/Pull origin | `git pull` |
| Save changes | Commit to main | `git commit -m "message"` |
| Upload changes | Push origin | `git push` |
| Undo last commit | Right-click → Undo | `git reset HEAD~1` |
| Create branch | New branch button | `git checkout -b name` |
| See history | History tab | `git log` |

---

> **Remember:** GitHub Desktop handles most Git tasks for you. Focus on writing good commit messages and pushing regularly!
