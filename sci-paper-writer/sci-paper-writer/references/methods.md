# Methods — Guided Drafting Module

## Purpose
Describe exactly what was done so that another researcher can reproduce the work.
Precision and completeness are paramount.

## Guiding Questions

### Overall Approach
1. What is the overall methodology? (experimental, computational, analytical, mixed)
2. Why was this approach chosen over alternatives?
3. What is the high-level workflow? (step 1 → step 2 → step 3)

### Detailed Procedures
4. What specific techniques, algorithms, or protocols were used?
5. What equipment, software, or tools were used? (include versions)
6. What parameters or settings were used? (learning rates, temperatures, concentrations)
7. Were any established protocols followed? (cite them)

### For Computational/ML Studies
8. What is the model architecture? (layers, dimensions, activation functions)
9. How was the model trained? (optimizer, loss function, epochs, batch size)
10. How was hyperparameter tuning done? (grid search, random, Bayesian)
11. What hardware was used? (GPU type, memory)
12. What software framework? (PyTorch, TensorFlow, R version, packages)

### For Experimental Studies
13. What materials/chemicals were used? (supplier, purity, catalog numbers)
14. What instruments were used? (model, manufacturer, settings)
15. What was the experimental procedure? (step by step)
16. How many replicates? How were controls set up?

### Validation & Robustness
17. How were results validated? (cross-validation, hold-out, independent dataset)
18. What metrics were used to evaluate performance?
19. Were sensitivity analyses or robustness checks performed?

## Structure Template

```
[Overall approach] + [justification]
[Step-by-step procedure] (subsections for each major step)
[Tools/software/hardware with versions]
[Parameters and settings]
[Validation approach]
[Statistical methods]
```

## Writing Patterns

### Describing Procedures
- "[Action] was performed using [tool/method] with [parameters]."
- "We followed the protocol described in [ref] with the following modifications..."
- "[Process] was carried out at [conditions] for [duration]."
- "The workflow consisted of three stages: (1)..., (2)..., (3)..."

### Citing Methods
- "Statistical analyses were performed using R v4.3.0 [ref]."
- "We adopted the framework proposed by [Author, Year] for..."
- "Model architecture follows [ref], with modifications to [component]."

### Describing Parameters
- "The learning rate was set to [value], with a batch size of [N]."
- "Reactions were incubated at [temp]°C for [time] with [rpm] shaking."
- "Significance was assessed at α = 0.05 using [test name]."

## Common Pitfalls
- Insufficient detail for reproducibility
- Missing software versions
- Not explaining why a method was chosen
- Burying important parameters in text (use tables for many parameters)
- Mixing methods and results (don't report outcomes here)

## Quality Checklist
- [ ] Another expert could reproduce the work from this section alone
- [ ] All software/tools with versions are listed
- [ ] Key parameters are stated (or referenced)
- [ ] Statistical methods are specified
- [ ] Validation approach is clear
- [ ] No results mixed into this section
