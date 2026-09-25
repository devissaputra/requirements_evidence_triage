# Empirical Study Protocol

## Study
Requirements Classification Evidence Triage on a Gold-Standard Benchmark

## Research question
Where does automatic fine-grained requirement classification fail on a gold-standard benchmark, and how concentrated are those errors under a limited human-review budget?

## Design and source
Secondary benchmark evaluation with disagreement-priority human review. Source: eTour fine-grained requirements-classification benchmark in the FTLR replication package. Analysis/retrieval date: 2026-09-25.

## Hypotheses
1. H1: classification quality differs substantially across the five evaluated labels (Function, Behavior, Data, F, UserRelated).
2. H2: UserRelated evidence has materially lower recall than the broad F label.
3. H3: disagreement-priority review captures a disproportionate share of five-label errors within a fixed review budget.

## Operationalization and method
Join gold-standard and automatic rows by requirement-element ID. For the five labels explicitly evaluated by the FTLR experiment (Function, Behavior, Data, F, UserRelated), compute confusion matrices and F1. Count per-element disagreements across those five labels, sort descending, and measure cumulative error capture at review budgets of 10, 25, 50, and 100 elements.

## Primary empirical result
Across the five evaluated labels, F1 ranges from 0.653 for UserRelated to 0.945 for F. There are 534 label disagreements in total; reviewing the 100 elements with the most five-label disagreements concentrates 277 of them (51.9%).

## Validity and claim boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.

## Reproducibility status
The repository packages derived results, study-specific analysis functions, deterministic or seeded procedures where relevant, an internet-enabled source rebuild script, and tests for both computations and critical scientific invariants. The released analysis was documented after dataset selection and should not be represented as preregistered.
