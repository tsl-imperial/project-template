# Getting Help

## Common errors

**`ModuleNotFoundError: No module named ...`**
Activate the environment and install the project packages: `conda activate coursework`, then `pip install -r requirements.txt`. In Jupyter, check the kernel is `coursework` (see [Anaconda setup](anaconda-setup.md)).

**`FileNotFoundError`**
Use paths relative to the notebook, not to your computer. A notebook in `notebooks/` reads data with:
```python
data = pd.read_csv("../data/file.csv")       # works for everyone
data = pd.read_csv("C:/Users/me/file.csv")   # works only for you
```

**Importing your own code from `src/`**
```python
import sys
sys.path.append("../src")
from my_module import my_function
```

**Git push rejected**
Someone else pushed first. Pull, resolve any conflicts, and push again (see [Getting started with GitHub](getting-started-github.md#fixing-mistakes)).

## Debugging

- Read a traceback from the bottom: the last line names the error, the lines above show where it happened.
- Check what you actually have: `type(x)`, `x.shape`, `df.head()`, `df.dtypes`.
- After an error in Jupyter, run `%debug` in a new cell to inspect the variables at the point of failure.
- Cut the code down until the problem disappears, then add it back a piece at a time.

## Where to ask

1. **Course materials**: lecture notes, tutorials and the coursework brief.
2. **The Coursework Q&A forum on Blackboard.** Other students probably have the same question, and the answer helps everyone.
3. **AI assistants** (GitHub Copilot, ChatGPT, Claude). Paste the full error and the relevant code, and say what you expected to happen. Read and understand any code you use, and disclose it (see [Academic integrity](academic-integrity.md)).
4. **Your instructor or teaching assistants**, in person or by email.

When you ask, include what you were trying to do, the full error message, what you expected, and what you have already tried. A link to your repository helps if your instructor has access.
