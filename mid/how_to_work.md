# Mid Homework Guide

## How To Do The Homework

For every task at this level:

1. Define the system boundary first.
2. Write down the source layer, transformation layer, and output layer.
3. State the data quality and freshness expectations.
4. Build with clear structure, not one large script.
5. Add tests or checks before calling the task complete.
6. Review performance, rerun behavior, and failure handling.

## What You Must Explain After Each Task

After each task, explain these points:

- why this design was chosen
- what alternative design you rejected
- what the grain is
- how the transformations are layered
- how tests protect the output
- how the job recovers from failure
- what happens during a backfill or rerun
- where the performance bottleneck could be

## Mid Quality Rules

- No hidden dependencies.
- No unexplained model layers.
- No orchestration without failure handling.
- No data model without grain definition.
- No transformation without test coverage or validation logic.

## Submission Standard

A task is complete only when you have:

- working implementation
- design explanation
- data quality checks or tests
- rerun and failure behavior explained
- at least one identified tradeoff
