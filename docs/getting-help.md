# Getting Help

Having trouble with your coursework? Here's where to get help.

## Quick Troubleshooting

### Common Issues

#### "Module not found" error
```bash
# Solution: Activate your conda environment and install packages
conda activate coursework
conda install package-name

# Or reinstall all dependencies
pip install -r requirements.txt
```

#### "File not found" error
- Check you're using **relative paths**, not absolute paths
- Make sure you're running code from the correct directory
```python
# Bad
data = pd.read_csv('C:/Users/yourname/data.csv')

# Good
data = pd.read_csv('../data/data.csv')
```

#### Git push rejected
```bash
# Pull changes first
git pull origin main

# Then push
git push origin main
```

#### Jupyter notebook won't start
```bash
# Ensure conda environment is activated
conda activate coursework

# Ensure jupyter is installed
conda install jupyter

# Start from project root
jupyter notebook
```

#### Import errors with your own modules
```python
# Add your src folder to Python path in notebooks
import sys
sys.path.append('../src')

# Then you can import your modules
from your_module import your_function
```

## Where to Get Help

### 1. Course Resources

**First, check:**
- Course materials, lecture notes, Datalab workspace
- Assignment specifications
- Piazza/Ed Discussion (if available)
- Course Moodle/Blackboard page

### 2. Documentation

**Read the docs:**
- [Anaconda Setup Guide](anaconda-setup.md) - Setting up your Python environment
- [Getting Started with GitHub](getting-started-github.md) - GitHub Desktop and basics
- [Git Workflows](git-workflows.md) - Git and GitHub practices
- [Submission Guidelines](submission-guidelines.md) - How to prepare for submission
- [Academic Integrity](academic-integrity.md) - Citation and plagiarism

### 3. Office Hours

**Talk to course staff:**
- Attend instructor office hours
- Visit teaching assistant drop-in sessions
- Book one-on-one consultation if available

**Come prepared:**
- Describe what you've tried
- Share error messages
- Show relevant code snippets

**💡 Tip for GitHub projects:** If you've added Prof Angeloudis (`p-ang`) as a collaborator to your repository, you can reference specific commits, files, or issues when asking for help. This makes it easier for instructors to see exactly what you're working on.

### 4. Peer Support

**Collaborate (appropriately):**
- Discuss concepts with classmates
- Form study groups
- Do NOT share code for individual assignments
- See [Academic Integrity](academic-integrity.md) for guidelines

### 5. Online Resources

#### Learning Git & GitHub
- [GitHub Skills](https://skills.github.com/) - Interactive tutorials
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing Git mistakes

#### Python Help
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/) - Tutorials and guides
- [Python for Data Analysis](https://wesmckinney.com/book/) - Pandas book

#### Data Science
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

#### Stack Overflow
- Search before asking - your question may already be answered
- Follow [How to Ask](https://stackoverflow.com/help/how-to-ask) guidelines
- Always cite if you use code from Stack Overflow!

## Asking Good Questions

When asking for help, include:

1. **What you're trying to do**
   - "I'm trying to load a CSV file..."

2. **What you expected**
   - "I expected it to create a DataFrame with 100 rows..."

3. **What actually happened**
   - "I got a FileNotFoundError..."

4. **Error messages** (full error, not just the last line)
   ```
   Traceback (most recent call last):
     File "script.py", line 10, in <module>
       data = pd.read_csv('data.csv')
   FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
   ```

5. **What you've tried**
   - "I checked the file exists, and I'm in the right directory..."

6. **Minimal reproducible example**
   - Simplify to the smallest code that shows the problem

## Debugging Tips

### Use Print Statements
```python
print("Before loading data")
data = pd.read_csv('data.csv')
print(f"Loaded {len(data)} rows")
```

### Check Types and Values
```python
print(type(variable))
print(variable.shape)  # For DataFrames/arrays
print(variable.head())  # For DataFrames
```

### Read Error Messages Carefully
- Start from the **bottom** of the traceback
- Look for the **file and line number**
- Google the error type: "FileNotFoundError python"

### Use a Debugger
```python
# Add breakpoint
import pdb; pdb.set_trace()

# Or in Jupyter
%debug
```

### Isolate the Problem
- Comment out code until error goes away
- Then gradually add back to find the issue

## Imperial College Resources

### Computing Support
- [Imperial College ICT Service Desk](https://www.imperial.ac.uk/admin-services/ict/self-service/)
- Email: service.desk@imperial.ac.uk

### Library Resources
- [Imperial Library Research Support](https://www.imperial.ac.uk/admin-services/library/learning-support/)
- Citation and referencing help
- Literature search assistance

### Student Support
- [Student Hub](https://www.imperial.ac.uk/students/hubs/)
- [Academic English Support](https://www.imperial.ac.uk/students/academic-support/academic-english/)
- [Disability Advisory Service](https://www.imperial.ac.uk/disability-advisory-service/)

## Still Stuck?

If you've:
- ✅ Checked the documentation
- ✅ Searched for your error online
- ✅ Asked classmates (without sharing code)
- ✅ Tried the troubleshooting steps

**Then contact your course instructor or teaching assistant.**

When contacting them, include:
- Your GitHub repository (if applicable)
- Full error messages
- What you've already tried
- Specific questions

---

> **Remember:** Everyone gets stuck sometimes. Asking for help is a sign of good problem-solving, not weakness!
