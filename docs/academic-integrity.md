# Academic Integrity and Proper Attribution

## Academic Integrity

Academic integrity is fundamental to your work at Imperial College London. When using this template for coursework, you must ensure that all work submitted is your own (or your team's) and properly attributed.

## What You Must Do

### 1. Cite Your Sources

Always cite:
- **Data sources**: Where did your data come from?
- **Code you adapted**: If you used code from tutorials, Stack Overflow, or other sources
- **Ideas and methods**: If you used techniques from papers or other sources
- **Libraries and packages**: Acknowledge the tools you used

### 2. Proper Attribution

When you use code or ideas from others:

```python
# Source: https://stackoverflow.com/questions/12345
# Adapted from: John Doe's tutorial on data cleaning
# Original author: Jane Smith
def my_function():
    # Your implementation
    pass
```

### 3. Collaboration Guidelines

**For Individual Assignments:**
- Do NOT share code with other students
- Do NOT copy code from classmates
- You may discuss concepts, but write your own code

**For Group Projects:**
- All team members should contribute
- Use Git commits to track who did what
- Document each member's contributions in README

## What is Plagiarism?

Plagiarism includes:
- ❌ Copying code without attribution
- ❌ Submitting someone else's work as your own
- ❌ Using AI tools (ChatGPT, Copilot) without disclosure (if prohibited by your course)
- ❌ Paraphrasing without citation

## Using AI Tools

**Important:** Check your course guidelines on AI usage. Some courses allow it, others don't.

If AI tools are permitted:
- ✅ Disclose when you used AI assistance
- ✅ Review and understand all AI-generated code
- ✅ Document what the AI helped with

Example disclosure:
```markdown
## AI Assistance Disclosure
- Used ChatGPT to debug error in data loading function (lines 45-60)
- Used GitHub Copilot for code completion and documentation
- All code was reviewed, tested, and understood before inclusion
```

## Data Ethics and Privacy

### What NOT to Commit to Git

Never commit:
- ❌ Personal data (names, addresses, emails)
- ❌ Sensitive information (medical records, financial data)
- ❌ Data you don't have permission to share
- ❌ Large datasets (use `.gitignore`)

### Handling Sensitive Data

If working with sensitive data:
1. Anonymize data before analysis
2. Store sensitive data locally only (never commit)
3. Use sample/synthetic data in your repository
4. Document data sources and access restrictions

### GDPR and Data Protection

If using data about people:
- Ensure you have permission to use the data
- Anonymize personal information
- Don't share raw data publicly
- Follow Imperial College's data protection policies

## Citing Data Sources

Always document where your data came from:

```markdown
## Data Sources

1. **Dataset Name**: [Source Name]
   - URL: https://example.com/data
   - Access Date: 2025-01-15
   - License: CC-BY-4.0
   - Description: Brief description of the dataset

2. **API Data**: [API Name]
   - Endpoint: https://api.example.com
   - Access Date: 2025-01-15
   - Terms of Use: Link to terms
```

## Citation Formats

Use appropriate citation formats for your field:

**For Academic Papers:**
```
Smith, J., & Doe, J. (2024). Title of Paper. Journal Name, 12(3), 45-67.
```

**For Datasets:**
```
Organization Name. (2024). Dataset Title (Version 1.0) [Data set].
https://doi.org/10.1234/example
```

**For Software/Packages:**
```
Developer Name. (2024). Package Name (Version 2.1.0) [Software].
https://github.com/example/package
```

## Resources

- [Imperial College Academic Integrity](https://www.imperial.ac.uk/students/academic-support/graduate-school/students/masters/professional-development/academic-integrity/)
- [Imperial College Library - Referencing](https://www.imperial.ac.uk/admin-services/library/learning-support/reference-management/)
- [Understanding Plagiarism](https://www.imperial.ac.uk/students/academic-support/graduate-school/students/doctoral/professional-development/research-integrity/plagiarism/)

## Questions?

If you're unsure about:
- Whether something constitutes plagiarism
- How to properly cite a source
- Whether you can use a particular dataset

**Ask your course instructor or module coordinator before submission.**

---

> **Remember:** When in doubt, cite it! Over-attribution is always better than under-attribution.
