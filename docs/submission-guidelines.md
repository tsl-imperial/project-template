# Submission Guidelines

Your coursework brief takes precedence over this guide where they differ. The latest version of this guide is at [github.com/tsl-imperial/project-template](https://github.com/tsl-imperial/project-template).

## Checklist

**Runs**
- [ ] Every notebook runs from top to bottom after **Restart & Run All**.
- [ ] Paths are relative (`../data/file.csv`), not specific to your computer.
- [ ] `requirements.txt` lists every package you import.
- [ ] The Streamlit app starts with `streamlit run src/app.py`, if your coursework includes one.

**Documented**
- [ ] `README.md` is your own, written from [README-EXAMPLE.md](../README-EXAMPLE.md), not this template's.
- [ ] Data sources, references and AI tool use are stated.
- [ ] Individual contributions are summarised (group projects).

**Repository**
- [ ] The repository is **Private**.
- [ ] No passwords, API keys or personal data are committed.
- [ ] Data files over 50 MB are not committed, and `data/README.md` says where to get them.
- [ ] Everything is pushed: check on GitHub.com, not just on your computer.

## Recommended structure

```
your-project/
├── README.md
├── requirements.txt
├── LICENSE
├── data/
│   └── README.md          (if any data must be downloaded separately)
├── notebooks/
│   ├── 00-report.ipynb
│   ├── 01-data-exploration.ipynb
│   └── 02-analysis.ipynb
├── models/
│   └── power_model_plant1.joblib
└── src/
    ├── app.py             (Streamlit demo)
    └── your_module.py
```

## How to submit

1. Check the repository is **Private**.
2. Add **`p-ang`** (Prof Panagiotis Angeloudis) as a collaborator with **Read** permission: **Settings → Collaborators → Add people**. This is the official form of submission. You can do it at any point; adding him early lets him see your progress if you ask for feedback.
3. Submit the repository URL on Blackboard if the brief asks for it.
4. Keep a ZIP copy in case you are asked for one (see [Making a ZIP backup](getting-started-github.md#making-a-zip-backup)).

Do not push changes after the deadline unless you have been given permission, and do not delete the repository until marks are released.

## Group projects

Individual contributions are assessed from the Git commit history: how often each member committed, and what. Every member must:

- write code and notebooks as well as documentation; dividing the team into "coders" and "writers" is not acceptable;
- commit regularly under their own GitHub account, with the name and email set correctly (see [Getting started with GitHub](getting-started-github.md#setup));
- push throughout the project, not in one batch at the end.

Summarise who did what in the README's "Individual Contributions" section.

## What markers look for

- **Reproducibility**: can they clone the repository and get your results?
- **Correctness**: are the methods appropriate and correctly applied?
- **Explanation**: do the notebooks explain the approach and interpret the results?
- **Presentation**: clear plots, readable code and a well-organised repository.
