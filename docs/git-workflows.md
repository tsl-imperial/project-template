# Git and GitHub Best Practices

This guide covers essential practices for managing your coursework with GitHub Desktop.

> **New to GitHub?** Start with [Getting Started with GitHub](getting-started-github.md) first - it covers the basics using GitHub Desktop.


## Daily Workflow

**Using GitHub Desktop:**

1. **Fetch and Pull** - Click "Fetch origin" then "Pull origin" to get latest changes
2. **Work** - Edit your notebooks and code
3. **Review** - Check what changed in GitHub Desktop
4. **Commit** - Write a clear message and commit
5. **Push** - Click "Push origin" to upload your changes

## Writing Good Commit Messages

**Good commit messages:**
- ✅ "Add exploratory data analysis notebook"
- ✅ "Fix missing value handling in clean_data()"
- ✅ "Create correlation heatmap visualization"
- ✅ "Update README with installation instructions"

**Bad commit messages:**
- ❌ "Update"
- ❌ "Fixed stuff"
- ❌ "Changes"
- ❌ "Final version"

**Why it matters:** Good messages help you (and your instructor) understand what changed and when.

## What NOT to Commit

Your `.gitignore` file already excludes these, but be aware:

- ❌ **Data files** - Keep data local (especially large files)
- ❌ **`.env` files** - Never commit API keys or passwords
- ❌ **Personal information** - No names, emails, addresses in data
- ❌ **Conda environments** - These are huge and unnecessary
- ❌ **Temporary files** - `.ipynb_checkpoints/`, `__pycache__/`, etc.

**If you accidentally commit something sensitive:**
1. Don't panic
2. Remove it from the repository
3. Change the password/API key immediately
4. Ask your instructor for help if needed

## Branches (Optional - Advanced)

**For most coursework, you can work directly on the main branch.** Branches are useful for trying experimental approaches without affecting your main work.

**In GitHub Desktop:**
1. Click "Current Branch" at the top
2. Click "New Branch"
3. Give it a descriptive name (e.g., "try-different-model")
4. Work on your experiment
5. If it works: merge back to main
6. If it doesn't: just switch back to main and delete the branch

**When to use branches:**
- Trying a risky change
- Experimenting with different approaches
- Working on a big feature that takes multiple days

## Checking Your History

**In GitHub Desktop:**
- Click the "History" tab to see all your commits
- Click any commit to see what changed
- Useful for finding when you introduced a bug

**On GitHub.com:**
- Go to your repository
- Click "Insights" → "Contributors" to see who contributed what
- Your instructor uses this to verify individual contributions

## Common Issues

### "I can't push my changes"

**Likely cause:** Someone else pushed changes

**Solution in GitHub Desktop:**
1. Click "Fetch origin"
2. Click "Pull origin"
3. Resolve any conflicts
4. Click "Push origin" again

### "I want to undo my last commit"

**In GitHub Desktop:**
1. Go to History tab
2. Right-click the commit
3. Click "Revert this commit"

**Note:** Only do this if you haven't pushed yet!

### "I committed the wrong files"

**Before pushing:**
1. History tab → Right-click commit → "Undo commit"
2. Uncheck the files you don't want
3. Commit again with only the right files

**After pushing:**
- Best to leave it or ask instructor for help

### "My commit shows the wrong name"

**Fix in GitHub Desktop:**
1. Go to Preferences/Settings
2. Click "Git" tab
3. Update your name and email to match your GitHub account
4. Tell your instructor about past commits with wrong name

## Best Practices Summary

**Do this:**
- ✅ Pull before you start working
- ✅ Commit small changes frequently
- ✅ Write clear commit messages
- ✅ Push regularly (at least daily)
- ✅ Check what you're committing before you commit
- ✅ Keep your `.gitignore` up to date

**Don't do this:**
- ❌ Make one giant commit at the end
- ❌ Commit sensitive data or large files
- ❌ Use vague commit messages
- ❌ Forget to push (your work isn't backed up!)
- ❌ Work for days without pulling

## Creating a Repository Backup (ZIP)

You may need to submit a ZIP file of your repository as a backup.

**On GitHub.com:**
1. Go to your repository on GitHub
2. Click the green **Code** button
3. Click **Download ZIP**
4. Save the file with a clear name (e.g., `coursework-backup-2025-03-15.zip`)

**In GitHub Desktop:**
1. Right-click your repository in the left sidebar
2. Select **Show in Finder** (Mac) or **Show in Explorer** (Windows)
3. Go up one folder level to see your repository folder
4. Right-click the repository folder → **Compress** (Mac) or **Send to → Compressed folder** (Windows)

> **Tip:** Create your backup AFTER you've pushed all final changes to GitHub.

## Resources

- [Getting Started with GitHub](getting-started-github.md) - GitHub Desktop basics
- [GitHub Desktop Documentation](https://docs.github.com/en/desktop)
- [Getting Help](getting-help.md) - Troubleshooting

---

> **Remember:** Commit frequently, push regularly, and write clear messages!
