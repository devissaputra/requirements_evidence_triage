# Data Dictionary

## Provenance
See `data/source_manifest.json`. Raw source observations are not silently republished.

## `data/derived/primary_results.csv`
Complete confusion-matrix summary for the five evaluated labels; secondary table contains the full reported review-budget curve.

## `data/derived/secondary_results.csv`
When present and non-empty, this contains a second derived table needed to reproduce a reported comparison. If empty, no second packaged table is required.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, estimates, and the release finding. Values must agree with README text and the derived CSVs.

## Construct boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.
