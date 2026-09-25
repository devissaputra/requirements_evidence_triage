# Empirical Study Protocol

## Study title

**Requirements Classification Evidence Triage on a Gold Standard Benchmark**

## Study type

Secondary benchmark evaluation with human review routing analysis.

This document records the released analysis and is not a preregistration.

## Research questions

**RQ1.** How heterogeneous is classification performance across Function, Behavior, Data, F, and UserRelated?

**RQ2.** How concentrated are observed label errors under a gold aware oracle queue?

**RQ3.** Can a prediction only ranking capture more errors than uniform random review on the same benchmark?

## Data pairing

Gold and automatic rows are joined by the 571 shared requirement IDs from the pinned eTour artifacts.

The release does not redistribute raw requirement text.

## Evaluated labels

Function, Behavior, Data, F, and UserRelated.

The fields `functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded because the available automatic eTour output is degenerate for those fields.

## Classification estimand

For each included label, compute:

- true positives;
- false positives;
- false negatives;
- true negatives;
- precision;
- recall;
- F1.

## Error unit

A label error is one false positive or one false negative for one requirement and one evaluated label.

Because each requirement has five evaluated labels, one requirement can contribute multiple label errors.

## Oracle diagnostic

For each requirement element, count the number of disagreements between gold and automatic labels across the five evaluated fields.

Rank items by descending disagreement count.

This ranking uses gold labels and is therefore interpreted only as an oracle upper bound on possible error concentration.

## Prediction only review routing

Construct the operational ranking without gold outcomes.

Ordering is:

1. lower prediction pattern frequency;
2. hierarchy violation first;
3. higher predicted positive label count;
4. ID for deterministic tie breaking.

A hierarchy violation occurs when Function, Behavior, or Data is predicted positive while F is predicted negative.

Gold labels are used only after ranking to calculate captured errors.

## Random comparator

For simple uniform review of k out of 571 items, the expected share of total label errors captured is k / 571.

## Released budgets

10, 25, 50, and 100 requirement elements.

## Released findings

Classification F1 ranges from 0.653 to 0.945.

There are 534 label level errors across the five evaluated labels.

At budget 100:

- oracle captures 277 errors, or 51.9%;
- prediction only rarity captures 115 errors, or 21.5%;
- uniform random review has expected capture share 17.5%;
- prediction only enrichment versus random expectation is 1.23×.

## Interpretation rule

The oracle result quantifies error concentration but is not an operational policy.

The prediction only result is a benchmark specific exploratory routing result. It is not interpreted as optimal or externally validated.

## Validity boundaries

The benchmark gold labels are treated as reference truth.

No reviewer cost, error severity, downstream correction benefit, uncertainty calibration, or cross dataset validation is modeled.

The prediction rarity rule is batch dependent and post hoc.

## Reproducibility

The release contains complete derived evidence, exact source pinning, deterministic analysis functions, confusion matrices, review curves, tests, CI, source rebuild checks, and reproducible SVG generation.
