# Data Provenance and Derived Evidence

## Public source

The release is pinned to FTLR replication commit:

`02682a0d3cb2fb991942c2d88d11e03221f30f87`

Gold labels trace to:

- *Dataset for Requirements Classification in Traceability Link Recovery Datasets*
- Zenodo version DOI: 10.5281/zenodo.7867846
- concept DOI: 10.5281/zenodo.7867845

Automatic eTour labels come from the corresponding pinned NoRBERT and FTLR replication artifact.

## Raw text policy

Raw requirement text is not redistributed in this repository.

## Packaged derived evidence

### `derived/evaluation_observations.csv`

Complete 571 row evidence table containing label outcomes and prediction derived routing features.

### `derived/primary_results.csv`

Five label classification evaluation table.

### `derived/triage_results.csv`

Oracle, prediction only, and random expected review results for budgets 10, 25, 50, and 100.

## Integrity policy

The public source rebuild fetches the exact commit pinned gold and automatic CSV files, reports SHA 256 digests for both, reconstructs the complete derived evidence, and fails if packaged evidence or released results differ.

## Information leakage policy

Gold labels are permitted for evaluation and for the explicitly named oracle upper bound.

The deployable ranking is constructed only from automatic prediction derived features.

## Claim boundary

The package demonstrates reproducible benchmark evaluation and exploratory review allocation. It does not establish optimal routing or transfer to other datasets, taxonomies, or classifiers.
