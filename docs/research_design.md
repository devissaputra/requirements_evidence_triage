# Research Design

## Research question
Where does automatic fine-grained requirement classification fail on a gold-standard benchmark, and how concentrated are those errors under a limited human-review budget?

## Design
Secondary benchmark evaluation with disagreement-priority human review.

## Source and unit of analysis
Source: eTour fine-grained requirements-classification benchmark in the FTLR replication package. The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: classification quality differs substantially across the five evaluated labels (Function, Behavior, Data, F, UserRelated).
2. H2: UserRelated evidence has materially lower recall than the broad F label.
3. H3: disagreement-priority review captures a disproportionate share of five-label errors within a fixed review budget.

## Method
Join gold-standard and automatic rows by requirement-element ID. For the five labels explicitly evaluated by the FTLR experiment (Function, Behavior, Data, F, UserRelated), compute confusion matrices and F1. Count per-element disagreements across those five labels, sort descending, and measure cumulative error capture at review budgets of 10, 25, 50, and 100 elements.

## Validity boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.
