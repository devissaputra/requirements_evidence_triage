# Final QA Report

**Release status: PASS after correction.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- derived CSV structure checked against the stated sample and estimand;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods moved into `research/model.py`;
- tests exercise scientific logic and invariants;
- internet rebuild script has no synthetic fallback;
- four SVG assets regenerated as study-specific figures and XML-validated;
- local Markdown links checked;
- citation metadata points to the final repository slug;
- no preregistration claim is made.

## Final empirical finding
Across the five evaluated labels, F1 ranges from 0.653 for UserRelated to 0.945 for F. There are 534 label disagreements in total; reviewing the 100 elements with the most five-label disagreements concentrates 277 of them (51.9%).

## Required interpretation boundary
The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.
