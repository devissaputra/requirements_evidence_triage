# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary estimand / descriptive target
Where does automatic fine-grained requirement classification fail on a gold-standard benchmark, and how concentrated are those errors under a limited human-review budget?

## Analysis
Join gold-standard and automatic rows by requirement-element ID. For the five labels explicitly evaluated by the FTLR experiment (Function, Behavior, Data, F, UserRelated), compute confusion matrices and F1. Count per-element disagreements across those five labels, sort descending, and measure cumulative error capture at review budgets of 10, 25, 50, and 100 elements.

## Specified outputs for this release
1. source/sample size and provenance;
2. primary derived metric(s);
3. comparator, cross-group, cross-time, or frontier contrast where applicable;
4. uncertainty, sensitivity, or error information supported by the source;
5. explicit construct and external-validity limitations.

## Missingness / exclusions

Gold and automatic files are joined by the 571 shared requirement-element IDs. Evaluation is restricted to Function, Behavior, Data, F, and UserRelated because those five labels have meaningful automatic predictions in this benchmark. No missing labels are imputed.

## Interpretation boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.
