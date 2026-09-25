# Reproducibility Guide

## Goal

The release supports two verification routes:

1. offline recomputation from the packaged 571 row derived evidence;
2. online reconstruction from exact commit pinned public source files.

## Environment

```bash
python -m pip install -r requirements.txt
```

## Offline verification

```bash
pytest -q
python run_demo.py
```

The test suite verifies:

- the 571 row scope;
- the total of 534 label errors;
- all five confusion matrices;
- exact F1 values;
- oracle and prediction only review curves;
- random expected shares;
- separation of oracle and deployable rankings;
- invariance of the deployable ranking to altered gold outcomes;
- full bundle validation.

## Pinned source rebuild

```bash
python scripts/fetch_and_analyze.py --check
```

The script fetches `eTour_gold.csv` and `eTour_best.csv` from the exact pinned commit, prints SHA 256 digests for both files, reconstructs the 571 row evaluation evidence, recomputes label metrics, recomputes review curves, and fails if any packaged release result differs.

## Figures

```bash
python scripts/generate_figures.py
```

The figure generator reads the packaged primary and triage tables so the visible values remain synchronized with the release.

## Evidence map

| Claim | Primary evidence |
|---|---|
| 571 requirement elements | `data/derived/evaluation_observations.csv` |
| Five confusion matrices | `data/derived/primary_results.csv` |
| 534 label errors | evaluation evidence and tests |
| Oracle review curve | `data/derived/triage_results.csv` |
| Prediction only review curve | `data/derived/triage_results.csv` |
| Leakage safe ranking inputs | `research/model.py` and tests |
| Public source consistency | `scripts/fetch_and_analyze.py --check` |

## Boundary

Computational reproducibility does not establish external validity. Another classifier, domain, taxonomy, or prevalence pattern may produce a different ranking result.
