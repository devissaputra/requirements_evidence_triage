# Analysis Plan

## Status

This document records the released analysis. It is not a preregistration.

## Study objective

Evaluate classification quality and human review allocation as two related but distinct systems engineering problems.

## RQ1: classification performance

For Function, Behavior, Data, F, and UserRelated, compute TP, FP, FN, TN, precision, recall, and F1 after joining gold and automatic rows by requirement ID.

The primary comparison is label specific. No single aggregate score replaces the five label results.

## RQ2: oracle error concentration

For each requirement element, count disagreements across the five evaluated labels.

Rank by descending disagreement count.

Report error capture at review budgets 10, 25, 50, and 100.

Because this ranking uses gold outcomes, it is interpreted only as an oracle upper bound.

## RQ3: prediction only review routing

Construct a ranking that does not access gold outcomes.

Sort by:

1. ascending five bit prediction pattern frequency;
2. hierarchy violation first;
3. descending predicted positive label count;
4. ID as deterministic tie breaker.

Evaluate the ranking with gold labels only after the queue has been constructed.

## Error unit

One false positive or false negative for one label is one label level error.

A requirement can contribute multiple errors.

## Random comparator

For uniform random review of k from N = 571 items, expected error capture share is k / N.

## Released outputs

1. complete 571 row derived evidence;
2. five confusion matrices and precision, recall, F1 values;
3. oracle capture curve;
4. prediction only capture curve;
5. random expected curve;
6. enrichment versus random expectation;
7. explicit leakage and validity boundaries;
8. reproducibility and source pinning evidence.

## Exclusions

The fields `functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded because the supplied automatic eTour output is degenerate for those fields.

## Interpretation constraints

The oracle is diagnostic only.

The prediction pattern rarity rule is exploratory, post hoc, and batch dependent.

No optimality, calibrated uncertainty, reviewer cost saving, or external validation claim is made.
