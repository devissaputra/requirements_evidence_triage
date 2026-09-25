# Released Results

## `empirical_summary.json`

Contains the released headline metrics:

- 571 requirement elements;
- five F1 values;
- 534 label level errors;
- oracle top 100 capture;
- prediction only top 100 capture;
- random expected top 100 share;
- prediction only enrichment.

## Primary classification table

`data/derived/primary_results.csv` contains complete confusion matrix counts and precision, recall, F1 for all five evaluated labels.

## Review table

`data/derived/triage_results.csv` contains the full review curves for:

- oracle upper bound;
- prediction pattern rarity;
- random expected review.

## Interpretation

The 51.9% top 100 value is a gold aware oracle ceiling.

The deployable top 100 value is 21.5%, compared with 17.5% expected from uniform random review.

These results are deterministic for the pinned evidence and declared ranking rules.
