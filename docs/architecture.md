# Architecture

## Current MVP

```text
Synthetic eval cases CSV
        |
        v
Scoring script
        |
        v
Eval results CSV
        |
        v
Streamlit dashboard
```

## Design principles

- Simple enough for PMs to understand
- Transparent scoring over black-box scoring
- Synthetic data only
- Easy to extend with real evaluator workflows
- Product decisions visible in documentation

## Future architecture

```text
Prompt versions + model outputs + golden dataset
        |
        v
Automated scoring + human review
        |
        v
Failure taxonomy + trend analysis
        |
        v
Launch readiness dashboard + decision memo
```
