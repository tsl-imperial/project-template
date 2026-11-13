# Imperial College London: Data Science Project Template

> **Create your repository from this template with Private visibility.** Coursework repositories must not be public.

A standard structure for data science coursework at Imperial College London, adapted from the [World Bank Project Template](https://github.com/worldbank/template). It keeps code, data, analysis and documentation in one reproducible repository, and the commit history shows who contributed what.

This file explains how to set up the repository. Before you submit, replace it with your own README, written from [README-EXAMPLE.md](README-EXAMPLE.md).

## Contents

| Path | Purpose |
|------|---------|
| `README-EXAMPLE.md` | Template for your project README |
| `requirements.txt` | Python packages, installed with `pip install -r requirements.txt` |
| `data/` | Datasets (see [Data](#data) below) |
| `notebooks/` | Jupyter notebooks for your analysis and report |
| `models/` | Saved trained models (e.g. `.joblib` files) |
| `src/` | Reusable Python code, and `app.py`, a starter Streamlit app |
| `docs/` | Guides listed below |

Guides in `docs/`:

- [Getting started with GitHub](docs/getting-started-github.md): GitHub Desktop, teamwork, conflicts and backups
- [Anaconda setup](docs/anaconda-setup.md): installing Python and managing the project environment
- [Notebooks](docs/notebooks-workflows.md): organising and documenting notebooks
- [Submission guidelines](docs/submission-guidelines.md): checklist and how to submit
- [Academic integrity](docs/academic-integrity.md): citations and AI tool disclosure
- [Getting help](docs/getting-help.md): common errors and where to ask

## Setting up

### 1. Create your repository

Sign in to [GitHub](https://github.com), click **Use this template** on this page, then **Create a new repository**. Give it a name, choose **Private**, and click **Create repository**.

Group projects use a single repository per group. Agree who will create it, then add the others as collaborators.

### 2. Add collaborators

In your repository, go to **Settings → Collaborators → Add people**.

- **Team members**: add each one with **Write** permission.
- **Instructor**: add **`p-ang`** (Prof Panagiotis Angeloudis) with **Read** permission. This is the official form of submission. You can add him early if you would like feedback while you work.

Invitations arrive by email and must be accepted.

Every team member must contribute code, notebooks and documentation, committing under their own GitHub account. Individual contributions are assessed from the commit history; writing documentation alone is not enough.

### 3. Set up your environment

If you do not have Anaconda, see the [Anaconda setup guide](docs/anaconda-setup.md). Then, from the repository folder:

```bash
conda create -n coursework python=3.11
conda activate coursework
pip install -r requirements.txt
jupyter notebook
```

## Working on your project

### Data

Put your datasets in `data/` and read them with relative paths (`../data/file.csv` from a notebook). Files of a few MB can be committed, so that your notebooks run for anyone who clones the repository. For any file larger than 50 MB, do not commit it: add it to `.gitignore` and write a `data/README.md` explaining where to download it.

### Streamlit demo app

`src/app.py` is a placeholder [Streamlit](https://streamlit.io) app to start your demo from. Run it from the repository root:

```bash
streamlit run src/app.py
```

It opens in your browser and works straight away with a stand-in model trained on made-up data. To use your own model, save it from your notebook with `joblib.dump(model, "models/power_model_plant1.joblib")` (and the same for `plant2`); the instructions at the top of `src/app.py` give the details. Change the app as much as you like. For ideas, see the [Streamlit gallery](https://streamlit.io/gallery).

Hosting the app online is optional. You can do it for free on [Streamlit Community Cloud](https://streamlit.io/cloud): sign in at [share.streamlit.io](https://share.streamlit.io) with GitHub, click **Create app**, pick your repository and set the main file path to `src/app.py`. Because your repository is private the app is private too, until you invite viewers with **Share**. The hosted app can only read files committed to the repository. The app's "How to host this app online" section has more detail.

## Learning resources

- [Jupyter Notebook tutorial](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook) and [cheat sheet](https://www.datacamp.com/cheat-sheet/jupyter-notebook-cheat-sheet) (DataCamp)
- [Introduction to Git](https://www.datacamp.com/courses/introduction-to-git) and [GitHub concepts](https://www.datacamp.com/courses/introduction-to-github-concepts) (DataCamp)
- [VS Code for data science](https://code.visualstudio.com/docs/datascience/data-science-tutorial)
- [GitHub Student Developer Pack](https://education.github.com/pack), which includes free GitHub Copilot

## Licence

The template is released under the MIT Licence; see [LICENSE](LICENSE). Your repository inherits it, which is fine for private coursework. Replace the file if you later publish your project under different terms.
