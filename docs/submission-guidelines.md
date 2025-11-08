# Submission Guidelines

This guide will help you prepare your coursework repository for submission.

> **⚠️ Note:** These guidelines may change. Please check your coursework guidance for the most current requirements. Newer versions of this document can be found at https://github.com/tsl-imperial/project-template

## Before You Submit

### Pre-Submission Checklist

Use this checklist to ensure your submission is complete:

#### Code Quality
- [ ] All code runs without errors
- [ ] Code is well-commented and readable
- [ ] Variable and function names are descriptive

#### Documentation
- [ ] README.md is complete and describes your project
- [ ] Requirements/dependencies are documented
- [ ] Data sources are cited
- [ ] Methods and analysis are explained

#### Reproducibility
- [ ] All notebooks run from top to bottom without errors
- [ ] Dependencies are listed (requirements.txt)
- [ ] Results can be reproduced by following your instructions

#### Data Management
- [ ] No large data files committed to repository
- [ ] Sample data included (if appropriate)
- [ ] Data sources documented

#### Academic Integrity
- [ ] All sources properly cited
- [ ] Code attribution is clear
- [ ] AI assistance disclosed (if used and permitted)
- [ ] Collaboration documented (for group projects)

### What Your Repository Should Include

#### Required Files

1. **README.md**
   - Use [README-EXAMPLE.md](../README-EXAMPLE.md) as your template
   - Project title and student/group information (names, CIDs, GitHub usernames)
   - Executive summary (150-300 words)
   - How to run your code
   - Data sources with citations
   - Methodology overview and results
   - Individual contributions (for group projects)
   - AI tool usage statement
   - References

2. **requirements.txt**
   - List all pip package dependencies
   - Include version numbers (optional but recommended)
   - Generate with: `pip freeze > requirements.txt`

3. **LICENSE**
   - Keep MIT or update as appropriate

4. **.gitignore**
   - Ensure data files are ignored
   - Exclude conda environments
   - Exclude .env files

#### Recommended Structure

```
your-project/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── data/
│   ├── .gitkeep
│   └── README.md (describe data sources)
├── notebooks/
│   ├── example-world-bank-api.ipynb (delete or keep as reference)
│   ├── 01-data-exploration.ipynb
│   ├── 02-data-cleaning.ipynb
│   └── 03-analysis.ipynb
├── src/
│   ├── template/
│   │   ├── example-*.py (delete or keep as reference)
│   └── your_code.py
└── docs/
    └── methodology.md
```

## How to Submit

1. Ensure your repository is **Private**
2. Add your instructor as a collaborator (this is the official form of submission):
   - Go to Settings → Collaborators
   - Add username: **`p-ang`** (Prof Panagiotis Angeloudis)
   - Select **Read** permission (or as specified by instructor)
   - **Note:** You can add them at any time during the project if you want guidance, not just at submission
3. Submit the repository URL if required by your course platform
4. Be prepared to submit a copy of the repository as a ZIP file (see instructions in [Git Workflows](git-workflows.md#creating-a-repository-backup-zip))

## Common Mistakes to Avoid

**❌ Don't:**
- Use absolute file paths (`C:/Users/YourName/data.csv`) - use relative paths (`../data/data.csv`)
- Commit large datasets (>10MB) - use `.gitignore`
- Hardcode API keys or passwords - use `.env` files
- Leave incomplete README - provide clear step-by-step instructions
- Make one giant commit at the end - commit frequently with clear messages

**✅ Do:**
- Test in a fresh conda environment before submitting
- Run all notebooks from top to bottom (Restart Kernel → Run All)
- Write clear commit messages: "Add data cleaning" not "updates"
- Document dependencies: `pip freeze > requirements.txt`
- Verify instructor (`p-ang`) has access to your repository
- Keep a backup of your repository (clone or download ZIP)

## Group Project Considerations

> **⚠️ Critical:** Individual contributions will be assessed through Git commit history. Every team member must make substantial contributions to **code, notebooks, and documentation** throughout the project. All team members should write code - documentation alone is not sufficient.

### Individual Contributions Requirement

**What instructors will check:**
- Number and frequency of commits per team member
- **Types of contributions - code, notebooks, AND documentation all expected**

**What you need to do:**
- **Write actual code (Python files, Jupyter notebooks with analysis)**
- **Write clear documentation (README, methodology, code comments)**
- Commit regularly under your own GitHub account
- Ensure your Git config has the correct name and email



### Document Contributions

In your README, include:

```markdown
## Team Contributions

- **Student A**: Data collection and cleaning (notebooks/01-data-loading.ipynb)
- **Student B**: Exploratory analysis (notebooks/02-eda.ipynb)
- **Student C**: Machine learning models (notebooks/03-modeling.ipynb, src/models.py)
- **Student D**: Visualization and documentation (notebooks/04-results.ipynb, docs/)

All team members contributed to code review, testing, and integration.
```

### Git Commit Best Practices

- ✅ Commit code, notebooks, and documentation regularly (daily or more often)
- ✅ Use your own GitHub account (check `git config user.email`)
- ✅ Write clear commit messages describing your changes
- ✅ Contribute different types of work (code, analysis, visualization, documentation)
- ✅ Mix technical and documentation contributions
- ✅ Push frequently so work is visible
- ❌ Don't make one giant commit at the end
- ❌ Don't commit only documentation without any code/notebooks
- ❌ Don't commit only code without any documentation
- ❌ Don't have uneven contribution (one person writing all the code)
- ❌ Don't divide into "coders" and "writers" - everyone does both

## What Markers Look For

- **Code quality**: Readable, well-organized, follows best practices
- **Documentation**: Clear explanations of methods and results
- **Reproducibility**: Can they run your code and get the same results?
- **Analysis quality**: Sound methodology and interpretation
- **Presentation**: Professional formatting and structure

## After Submission

- **Don't delete your repository** until after grading
- **Don't make changes** after the deadline unless permitted
- Keep a backup of your repository

---

**Questions?** Contact your course instructor or teaching assistant before the deadline if you're unsure about submission requirements.
