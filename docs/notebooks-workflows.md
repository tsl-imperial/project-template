# Notebooks

## Organising notebooks

Number notebooks in the order they should be run, and name them after what they do:

```
notebooks/
├── 00-report.ipynb
├── 01-data-exploration.ipynb
├── 02-regression.ipynb
└── 03-classification.ipynb
```

Keep each notebook to one topic. A notebook that loads, cleans, models and plots everything is hard to review and is where team conflicts happen. Code you reuse across notebooks belongs in a module in `src/`.

## Inside a notebook

- Start with a title and a short paragraph saying what the notebook does and which data it uses.
- Use `##` headings for sections, and explain in markdown what each section does and what its results show. Code without explanation is hard to mark.
- Give every plot a title, axis labels with units, and a legend where there is more than one series.
- State assumptions and limitations where they arise.

## Before you commit

Run **Kernel → Restart & Run All** and check the notebook runs from top to bottom without errors. Notebooks that only work when cells are run in a particular order are not reproducible.
