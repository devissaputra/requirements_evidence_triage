# Analysis Plan

## Status
This file documents the released analysis. It is **not a preregistration**.

## RQ1
Evaluate Function, Behavior, Data, F, and UserRelated using confusion matrices, precision, recall, and F1.

## RQ2
Compute per-item gold-vs-prediction disagreement counts and rank descending. Report capture at budgets 10, 25, 50, and 100. Because the ranking uses gold labels, interpret it only as an oracle upper bound.

## RQ3
Construct a deployable ranking without gold labels using prediction-pattern rarity. Rarer five-label outputs rank first; prediction-only hierarchy inconsistency, predicted label density, and ID are deterministic tie-breakers.

## Comparator
Uniform random review has expected error-capture share k/N at budget k.

## Outputs
Complete 571-row derived evaluation evidence, five-label confusion/F1 results, oracle/deployable/random curves, enrichment versus random expectation, and explicit validity boundaries.

## Exclusions
`functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded because the supplied automatic eTour output is degenerate for those fields.

## Interpretation
The prediction-only heuristic is exploratory and post hoc; no external-validation or optimality claim is made.
