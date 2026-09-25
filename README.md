# Requirements Classification Evidence Triage on a Gold Standard Benchmark

[![CI](https://github.com/devissaputra/requirements_evidence_triage/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/requirements_evidence_triage/actions/workflows/ci.yml)
[![Empirical source rebuild](https://github.com/devissaputra/requirements_evidence_triage/actions/workflows/empirical-rebuild.yml/badge.svg)](https://github.com/devissaputra/requirements_evidence_triage/actions/workflows/empirical-rebuild.yml)

> **System Engineering Research Package** · Engineering Management Research · Requirements Engineering · Human Review Allocation

A reproducible secondary study of 571 eTour requirement elements that separates classifier performance, a gold aware oracle review ceiling, and an exploratory prediction only triage rule.

![Classification evidence](assets/research_design.svg)

## Start here

- [Scientific report](REPORT.md)
- [Empirical study protocol](EMPIRICAL_STUDY.md)
- [Paper blueprint](docs/paper_blueprint.md)
- [Research design](docs/research_design.md)
- [Analysis plan](docs/analysis_plan.md)
- [Reproducibility guide](REPRODUCIBILITY.md)
- [Data provenance](data/README.md)
- [Final QA evidence](QA_REPORT.md)

## Research questions

1. How does classification performance vary across Function, Behavior, Data, F, and UserRelated?
2. How concentrated are observed label errors under a gold aware oracle queue?
3. Can a prediction only review queue capture more errors than uniform random review on this benchmark?

## Source

| Item | Value |
|---|---|
| Benchmark | eTour requirements classification subset |
| Requirement elements | 571 |
| Gold dataset | Zenodo 10.5281/zenodo.7867846 |
| Automatic predictions | NoRBERT and FTLR replication output |
| Pinned source commit | `02682a0d3cb2fb991942c2d88d11e03221f30f87` |
| Analysis date | 25 September 2026 |
| Raw requirement text republished | No |

## Classification evidence

| Label | Precision | Recall | F1 |
|---|---:|---:|---:|
| Function | 0.790 | 0.883 | 0.834 |
| Behavior | 0.744 | 0.962 | 0.839 |
| Data | 0.701 | 0.796 | 0.746 |
| F | 0.899 | 0.996 | 0.945 |
| UserRelated | 0.933 | 0.502 | 0.653 |

The lowest F1 is UserRelated. Its precision is high while recall is only 0.502, so the dominant issue is missed positive UserRelated labels rather than excessive positive predictions.

## Leakage safe review analysis

The gold aware ranking is retained only as an oracle ceiling. It answers how concentrated the observed errors could be if their locations were already known.

The operational experiment uses only automatic prediction outputs. The queue prioritizes rare five label prediction patterns and uses prediction only hierarchy inconsistency plus predicted label density as tie breakers.

![Review pipeline](assets/method.svg)

## Review results

| Budget | Oracle capture | Prediction only capture | Random expected | Prediction only enrichment |
|---:|---:|---:|---:|---:|
| 10 | 7.1% | 3.4% | 1.8% | 1.93× |
| 25 | 15.5% | 6.4% | 4.4% | 1.45× |
| 50 | 29.6% | 12.2% | 8.8% | 1.39× |
| 100 | 51.9% | 21.5% | 17.5% | 1.23× |

![Triage comparison](assets/triage.svg)

The core finding is the distance between the oracle and the deployable queue. Errors are highly concentrated in hindsight, but a simple prediction only signal recovers only part of that concentration.

## What this study contributes

The contribution is not a new requirements classifier. It is a transparent review allocation analysis with four explicit layers:

1. label level classification performance;
2. a gold aware upper bound on error concentration;
3. a deployable prediction only ranking;
4. a uniform random review comparator.

This separation prevents answer key leakage from being presented as an operational triage result.

## Claim boundary

**Supported by this release:** five label confusion matrices, 534 total label level errors, exact review curves at four budgets, and prediction only enrichment over uniform random expectation on the pinned eTour benchmark.

**Not supported:** optimal triage, external validation, calibrated uncertainty, reviewer cost savings, end to end system verification, or transfer to other datasets and classifiers.

## Reproduce

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/fetch_and_analyze.py --check
python scripts/generate_figures.py
```

The source rebuild uses exact commit pinned URLs, reports SHA 256 values for the two source CSV files, reconstructs the full 571 row derived evidence, and checks all released primary and triage results.

## Repository map

- `REPORT.md`: scientific report
- `EMPIRICAL_STUDY.md`: released protocol and validity boundaries
- `docs/paper_blueprint.md`: manuscript plan and draft abstract
- `docs/analysis_plan.md`: estimands and comparison logic
- `docs/research_design.md`: evidence and routing design
- `docs/data_dictionary.md`: derived variables and output definitions
- `data/source_manifest.json`: source pinning and provenance
- `data/derived/evaluation_observations.csv`: complete 571 row evaluation evidence
- `data/derived/primary_results.csv`: label level classification results
- `data/derived/triage_results.csv`: oracle, prediction only, and random review curves
- `research/model.py`: evaluation and routing logic
- `scripts/`: source rebuild and figure generation
- `tests/`: scientific invariant and leakage tests
- `QA_REPORT.md`: release consistency evidence

## Research integrity

The analysis is not preregistered. The prediction only heuristic is exploratory and post hoc. Gold labels are used to evaluate the queue after ranking, never to construct the deployable ranking.
