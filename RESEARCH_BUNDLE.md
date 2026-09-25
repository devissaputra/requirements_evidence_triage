# Research Bundle Definition

This repository is treated as a research bundle because it links one explicit research question to a named empirical source, a documented operationalization, executable analysis code, derived evidence, reproducibility checks, visual evidence, validity boundaries, and a paper-ready interpretation path.

## Question
Where does automatic fine-grained requirement classification fail on a gold-standard benchmark, and how concentrated are those errors under a limited human-review budget?

## Empirical core
Five-label confusion analysis and disagreement-priority review allocation.

## Main result
Across the five evaluated labels, F1 ranges from 0.653 for UserRelated to 0.945 for F. There are 534 label disagreements in total; reviewing the 100 elements with the most five-label disagreements concentrates 277 of them (51.9%).

## Boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.

## Release criterion
A release passes only if source provenance, code, derived tables, JSON summary, README claims, figures, and tests agree numerically and semantically.
