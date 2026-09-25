# Empirical Study Protocol

## Study
Requirements Classification Evidence Triage on a Gold-Standard Benchmark

## Research questions
1. How heterogeneous is five-label classification performance?
2. How concentrated are observed errors under an oracle queue that knows the gold labels?
3. Does a prediction-only pattern-rarity queue capture more errors than uniform random review on this benchmark?

## Design
Secondary benchmark analysis of 571 eTour requirement elements.

## Source
The release is pinned to FTLR replication commit `02682a0d3cb2fb991942c2d88d11e03221f30f87`. Gold labels trace to the requirements-classification dataset (Zenodo concept DOI 10.5281/zenodo.7867845; versioned record 10.5281/zenodo.7867846). Automatic labels are the NoRBERT/FTLR eTour predictions.

## Primary classification estimand
For Function, Behavior, Data, F, and UserRelated, compute TP, FP, FN, TN, precision, recall, and F1 after joining gold and automatic rows by ID.

## Oracle review analysis
For each requirement element, count gold-vs-prediction disagreements across the five labels and sort descending. This uses gold labels and is therefore interpreted only as an oracle upper bound on error concentration.

## Deployable exploratory triage
Rank items using only automatic predictions: rarer five-label prediction patterns first, then prediction-only hierarchy inconsistency, predicted positive-label count, and ID as deterministic tie-breakers. Gold labels are used only after ranking to measure captured errors.

## Random-review comparator
For uniform random review of k out of N=571 items, expected captured error share is k/N.

## Result
F1 spans 0.653–0.945. There are 534 label errors. At budget 100, the oracle captures 277 errors (51.9%); the prediction-only heuristic captures 115 (21.5%); uniform random review has expected share 17.5%.

## Validity boundary
The prediction-only heuristic is post hoc, batch-dependent, and not externally validated. This is a requirement-element benchmark study, not end-to-end physical-system verification.
