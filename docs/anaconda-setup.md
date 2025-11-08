# Anaconda Setup Guide

This guide will help you set up Anaconda for your coursework and manage your project environment.

## What is Anaconda?

**Anaconda** is a distribution of Python that includes:
- Python itself
- Conda (package and environment manager)
- 250+ pre-installed data science packages
- Jupyter Notebook and JupyterLab
- Spyder IDE and other tools

It's the easiest way to get started with data science in Python!

## Installing Anaconda

### Download and Install

1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download the installer for your operating system:
   - **Windows**: Download the .exe installer
   - **macOS**: Download the .pkg installer
   - **Linux**: Download the .sh installer
3. Run the installer and follow the prompts
4. **Important**: Check "Add Anaconda to my PATH" (Windows only)

### Verify Installation

Open a terminal (Mac/Linux) or Anaconda Prompt (Windows) and run:

```bash
conda --version
```

You should see something like `conda 23.x.x`

## Using Conda Environments

### Why Use Environments?

Environments keep your projects separate:
- Each project can have different package versions
- Avoid conflicts between projects
- Easy to share your setup with teammates
- Keep your base installation clean

### Creating an Environment

For this coursework project:

```bash
# Create environment
conda create -n coursework python=3.11

# Activate it
conda activate coursework

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### Activating Your Environment

**Always activate your environment before working:**

```bash
conda activate coursework
```

Your terminal prompt will change to show `(coursework)` at the beginning.

### Installing Packages

With your environment activated, use pip to install packages:

```bash
# Install a single package
pip install pandas

# Install multiple packages
pip install numpy matplotlib seaborn

# Install from requirements.txt
pip install -r requirements.txt
```

### Listing Installed Packages

```bash
# See all packages in current environment
conda list

# Search for a specific package
conda list pandas
```

### Deactivating Environment

When you're done working:

```bash
conda deactivate
```

## Managing Your requirements.txt

### Export Your Environment

After installing packages, export for your teammates:

```bash
# Full export (includes all dependencies)
pip freeze > requirements.txt

# Or manually edit requirements.txt
# (recommended - only include main packages you need)
```

We recommend manually maintaining requirements.txt with only the packages you explicitly need.

### Example requirements.txt

```
# Core packages
jupyter
pandas
numpy
matplotlib
scikit-learn
seaborn
python-dotenv
httpx

# Add your additional packages below
```

### Update Environment from File

When a teammate adds new packages:

```bash
# Update existing environment
pip install -r requirements.txt

# Or remove and recreate (clean slate)
conda env remove -n coursework
pip install -r requirements.txt
```

## Working with Jupyter

### Starting Jupyter Notebook

```bash
# Activate environment
conda activate coursework

# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (more features)
jupyter lab
```

Your browser will open with Jupyter.

### Installing Jupyter (if needed)

```bash
conda activate coursework
conda install jupyter jupyterlab
```

### Jupyter Kernels

Make sure Jupyter uses your conda environment:

```bash
# Install ipykernel in your environment
conda install ipykernel

# Add your environment as a Jupyter kernel
python -m ipykernel install --user --name=coursework
```

Now in Jupyter, select "coursework" as your kernel.

## Useful Conda Commands

### Environment Management

```bash
# List all environments
conda env list

# Create environment with specific Python version
conda create -n myenv python=3.11

# Clone an environment
conda create --name newenv --clone coursework

# Remove an environment
conda env remove -n environment-name
```

### Package Management

```bash
# Update a package
conda update package-name

# Update all packages (careful!)
conda update --all

# Remove a package
conda remove package-name

# Search for packages
conda search pandas
```

### Conda Itself

```bash
# Update conda
conda update conda

# Update Anaconda distribution
conda update anaconda

# Check conda info
conda info
```

## Common Issues

### "conda: command not found"

**On Windows:**
- Use "Anaconda Prompt" instead of regular Command Prompt
- Or add Anaconda to PATH during installation

**On Mac/Linux:**
```bash
# Add conda to PATH
export PATH="$HOME/anaconda3/bin:$PATH"

# Or run conda init
~/anaconda3/bin/conda init
```

### "Package not found"

Try different channels:
```bash
# Try conda-forge
conda install -c conda-forge package-name

# Or use pip as fallback (in conda environment)
pip install package-name
```

### Environment activation not working

```bash
# Initialize conda for your shell
conda init

# Close and reopen terminal
# Then try activating again
conda activate coursework
```

### Jupyter kernel not found

```bash
# Reinstall ipykernel
conda install ipykernel
python -m ipykernel install --user --name=coursework --display-name "Python (coursework)"
```

### Slow package installation

```bash
# Use mamba (faster conda alternative)
conda install mamba -c conda-forge

# Then use mamba instead of conda
mamba install pandas numpy matplotlib
```

## Best Practices

### Do This ✅

- **Use requirements.txt**: Track all dependencies
- **Activate before working**: Always `conda activate coursework`
- **Export regularly**: Update requirements.txt when adding packages
- **Use --from-history**: Cleaner environment files
- **Specify channels**: Use conda-forge for better package availability

### Don't Do This ❌

- **Don't modify base**: Never install packages in base environment
- **Don't mix pip and conda**: Use conda when possible, pip only if needed
- **Don't commit environments**: Add to .gitignore, share requirements.txt instead
- **Don't forget to activate**: Check prompt shows `(coursework)`

## Alternative: Miniconda

If you want a lighter installation:

1. Download from [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
2. Miniconda = conda without the pre-installed packages
3. Smaller download, faster installation
4. Perfect if you only need what's in your requirements.txt

## Resources

### Official Documentation
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Conda User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)

### Video Tutorials
- [Anaconda for Beginners](https://www.youtube.com/results?search_query=anaconda+python+tutorial)
- [Conda Environments Explained](https://www.youtube.com/results?search_query=conda+environments)

### For Your Coursework
- [Getting Help](getting-help.md) - General troubleshooting

## Quick Reference

| Task | Command |
|------|---------|
| Create environment | `pip install -r requirements.txt` |
| Activate environment | `conda activate coursework` |
| Install package | `conda install package-name` |
| List packages | `conda list` |
| Export environment | `pip freeze --from-history > requirements.txt` |
| Update environment | `pip install -r requirements.txt` |
| Deactivate | `conda deactivate` |
| List environments | `conda env list` |
| Remove environment | `conda env remove -n name` |
| Start Jupyter | `jupyter notebook` |

---

> **Remember:** Always activate your environment before working on your project!
