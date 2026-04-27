# Junior Homework Guide

## How To Do The Homework

For every task at this level:

1. Start with the business problem, not the tool.
2. Define the source, target, and expected behavior.
3. Decide how you will validate the data before loading.
4. Build the simplest correct version first.
5. Rerun it to prove it is repeatable.
6. Refactor the code only after the data flow works.

## What You Must Explain After Each Task

After each task, explain these points:

- What business question or operational problem this task solves
- What the source system is
- What the target table or output is
- What rules were used to clean or transform data
- How duplicates, nulls, and bad rows were handled
- How the task behaves when rerun
- What data quality checks were added
- What part still feels weak or risky

## Junior Quality Rules

- Every script should be rerunnable.
- Every load should have a quality check.
- Every transformation should be explainable in business terms.
- Every failure should be visible in logs or output.
- Avoid using advanced frameworks to hide weak understanding.

## Submission Standard

A task is complete only when you have:

- working code
- reproducible output
- a short design explanation
- at least one quality check
- proof that rerunning does not create chaos
