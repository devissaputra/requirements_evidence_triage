# Paper Blueprint

## Working title
Requirements Classification Evidence Triage on a Gold-Standard Benchmark

## Motivation
Requirements classifiers can look acceptable in aggregate while failing differently across requirement concerns. When human review capacity is limited, the engineering question is not only model accuracy but also whether errors can be concentrated into a smaller review queue.

## Research question
Where does automatic fine-grained requirement classification fail on a gold-standard benchmark, and how concentrated are those errors under a limited human-review budget?

## Data and method
Join gold-standard and automatic rows by requirement-element ID. For the five labels explicitly evaluated by the FTLR experiment (Function, Behavior, Data, F, UserRelated), compute confusion matrices and F1. Count per-element disagreements across those five labels, sort descending, and measure cumulative error capture at review budgets of 10, 25, 50, and 100 elements.

## Results to report
Across the five evaluated labels, F1 ranges from 0.653 for UserRelated to 0.945 for F. There are 534 label disagreements in total; reviewing the 100 elements with the most five-label disagreements concentrates 277 of them (51.9%). Report the packaged headline metrics and the full relevant derived table; do not cherry-pick only the strongest contrast.

## Robustness / sensitivity
The release reports separate confusion matrices and F1 scores for Function, Behavior, Data, F, and UserRelated, then evaluates cumulative five-label error capture at review budgets of 10, 25, 50, and 100 elements. The four CSV columns without comparable automatic predictions are excluded from the estimand rather than counted as model failures.

## Limitations
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, or externally validated unless those events actually occur. Distinguish analysis of public data from original data collection.
