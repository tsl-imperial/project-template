# Anaconda Setup

Anaconda installs Python, the conda environment manager and Jupyter. This guide covers installing it and managing the environment for your project.

## Installing

1. Download the installer for your system from [anaconda.com/download](https://www.anaconda.com/download) and run it.
2. Open a terminal (Mac/Linux) or **Anaconda Prompt** (Windows) and check it works:
   ```bash
   conda --version
   ```

[Miniconda](https://docs.anaconda.com/miniconda/) is a smaller alternative: conda and Python without the pre-installed packages. Everything below works the same with it.

## The project environment

An environment keeps this project's packages separate from everything else on your computer, so the whole team runs the same versions. Create it once, from the repository folder:

```bash
conda create -n coursework python=3.11
conda activate coursework
pip install -r requirements.txt
```

Then activate it every time you work on the project. Your prompt shows `(coursework)` when it is active.

```bash
conda activate coursework
jupyter notebook        # or: jupyter lab
```

If Jupyter does not list the environment as a kernel, register it:

```bash
python -m ipykernel install --user --name=coursework
```

## Adding packages

Install packages with pip, inside the activated environment, and add each one to `requirements.txt` by hand so your teammates get it too:

```bash
pip install seaborn
```

Keep `requirements.txt` to the packages you import yourself. `pip freeze > requirements.txt` writes out every dependency with exact versions, which often fails to install on another operating system.

When a teammate adds a package, run `pip install -r requirements.txt` again.

To start again from a clean environment:

```bash
conda deactivate
conda env remove -n coursework
conda create -n coursework python=3.11
conda activate coursework
pip install -r requirements.txt
```

## Common problems

**"conda: command not found".** On Windows, use Anaconda Prompt rather than Command Prompt. On Mac or Linux, run `~/anaconda3/bin/conda init` (or `~/miniconda3/bin/conda init`), then close and reopen the terminal.

**"ModuleNotFoundError" in a notebook.** The notebook is using a different kernel. Check the kernel name at the top right is `coursework`; if it is missing, register it as above.

**`conda activate` does nothing.** Run `conda init`, then close and reopen the terminal.

## Quick reference

| Task | Command |
|------|---------|
| Create the environment | `conda create -n coursework python=3.11` |
| Activate it | `conda activate coursework` |
| Install project packages | `pip install -r requirements.txt` |
| Install one package | `pip install package-name` |
| List installed packages | `pip list` |
| List environments | `conda env list` |
| Remove the environment | `conda env remove -n coursework` |

See the [conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/) for more.
