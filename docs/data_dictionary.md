# Data Dictionary

## `evaluation_observations.csv`
Complete 571-row derived evaluation evidence. It does not republish requirement text. Each row stores TP/FP/FN/TN outcomes for the five evaluated labels, the five-bit prediction pattern, pattern frequency, predicted-positive count, a prediction-only hierarchy flag, and total label-error count.

## `primary_results.csv`
Complete five-label confusion-matrix and precision/recall/F1 summary.

## `triage_results.csv`
Review-budget results for:
- `oracle_upper_bound`: gold-aware ranking;
- `prediction_pattern_rarity`: prediction-only ranking;
- `random_expected`: exact expectation under uniform random review.

## `empirical_summary.json`
Headline metrics and bounded interpretation.

## Excluded columns
`functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded because the automatic eTour file is degenerate for those fields.
