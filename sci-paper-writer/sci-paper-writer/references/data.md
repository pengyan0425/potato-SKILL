# Data / Study Design — Guided Drafting Module

## Purpose
Describe what was studied, how data was collected or generated, and justify
the study design. This section may appear as part of Methods or as its own section
depending on the journal.

## Guiding Questions

### Study Design
1. What type of study is this? (experimental, observational, computational, survey, etc.)
2. What is the unit of analysis? (individuals, cells, samples, datasets, simulations)
3. What is the study population or scope?

### Data Collection
4. What data did you collect? What variables?
5. How was data collected? (instruments, surveys, databases, APIs, sensors)
6. What time period does the data cover?
7. What is the sample size? How was it determined?

### Data Sources
8. Is data from your own experiments, or an existing dataset?
   - If existing: name, version, source, license
   - If original: describe the collection protocol
9. Are there any preprocessing steps? (cleaning, filtering, normalization)

### Variables & Measures
10. What are the independent variables (predictors)?
11. What are the dependent variables (outcomes)?
12. How were key variables measured or operationalized?
13. Were there control variables? Why were they chosen?

### Ethical & Practical Considerations
14. Was ethics approval obtained? (IRB, ethics committee)
15. Was informed consent obtained?
16. Any data privacy considerations?

## Structure Template

```
[Study design type] + [population/scope]
[Data source description] + [collection method]
[Sample size] + [time period] + [selection criteria]
[Variables] + [measurement approach]
[Preprocessing / quality control]
[Ethics / approvals if applicable]
```

## Writing Patterns

### Describing Data Sources
- "Data were collected from [source] between [date] and [date]."
- "We obtained [N] samples from [source/institution]."
- "The dataset comprises [N] observations of [description]."
- "We used the [Dataset Name] [Version], publicly available at [URL/DOI]."

### Justifying Sample Size
- "A power analysis indicated that [N] samples were required to detect [effect size]..."
- "This sample size is consistent with previous studies [refs]."
- "Data were collected until [stopping criterion] was reached."

### Describing Variables
- "The primary outcome was [variable], measured using [instrument/method]."
- "We controlled for [variables] to account for [potential confound]."
- "[Variable] was operationalized as [definition]."

## Common Pitfalls
- Insufficient detail for reproducibility
- Missing justification for sample size
- Unclear variable definitions
- Not addressing data limitations
- Forgetting to mention ethics/consent

## Quality Checklist
- [ ] Another researcher could replicate the study from this description
- [ ] Sample size is stated and justified
- [ ] Variables are clearly defined
- [ ] Data source is identified (with DOI/URL if public)
- [ ] Preprocessing steps are described
- [ ] Ethical considerations are addressed
