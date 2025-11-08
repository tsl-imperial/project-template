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

### 2. Online Resources

- [Stack Overflow](https://stackoverflow.com) - Search for your specific error
- Follow [How to Ask](https://stackoverflow.com/help/how-to-ask) guidelines
- Always cite if you use code from Stack Overflow!

### 3. AI Assistants (Copilot/ChatGPT)

If you want quick, actionable help, ask an AI assistant. Include relevant files, error messages, your OS, and what you've tried.

**Using GitHub Copilot:** You can try different models in Copilot. Note that models without a "0x" next to them are subject to usage quotas, so use them wisely for complex problems.

Good prompts to use:

- "Debug this error: <paste full traceback>. I expected X but got Y. Relevant file: path/to/file.py"
- "Explain what this function does, line by line: ```python\n# paste function\n```"
- "Refactor this function to be more readable and add type hints: ```python\n# paste function\n```"
- "Write pytest unit tests for this function (show fixtures and edge cases): ```python\n# paste function\n```"
- "Suggest performance improvements for this code and explain trade-offs: ```python\n# paste code\n```"
- "Convert this Jupyter notebook cell into a standalone Python script (specify entrypoint and args)."
- "Generate a minimal reproducible example that demonstrates this bug based on the code below: ```python\n# paste code\n```"
- "Create a .gitignore and recommended dev environment setup for a Python data-science project on macOS."
- "Draft a clear git commit message and short PR description for these changes: <brief summary or diff>"

**Tips when prompting AI assistants:**
- Paste the full error or relevant code blocks
- State the expected behavior and the actual behavior
- Mention the project structure or file paths when relevant

## Asking Good Questions

When asking for help (from instructors, TAs, or online), include:

1. **What you're trying to do**
   - "I'm trying to load a CSV file and analyze the data..."

2. **What error you're getting**
   - Paste the full error message and traceback

3. **What you expected to happen**
   - "I expected the file to load into a DataFrame..."

4. **What you've tried**
   - "I checked the file exists, I'm in the right directory..."

5. **A minimal reproducible example**
   - Simplify to the smallest code that shows the problem

## Debugging Tips

### Add Print Statements
```python
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
