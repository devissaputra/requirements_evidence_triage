# Final QA Report

## Release verdict

**Status: PASS for a reproducible portfolio research package.**

This file verifies consistency. It is not the scientific report. The research narrative is in [REPORT.md](REPORT.md).

## Scope checked

The release was checked for agreement across:

- pinned benchmark provenance;
- 571 row derived evidence;
- five confusion matrices;
- oracle review curve;
- prediction only review curve;
- random expectation;
- source rebuild;
- analysis code;
- tests;
- figures;
- README;
- scientific report;
- paper blueprint;
- validity and leakage statements.

## Numerical consistency

| Check | Released value | Status |
|---|---:|---|
| Requirement elements | 571 | PASS |
| Label level errors | 534 | PASS |
| Function F1 | 0.834 | PASS |
| Behavior F1 | 0.839 | PASS |
| Data F1 | 0.746 | PASS |
| F F1 | 0.945 | PASS |
| UserRelated F1 | 0.653 | PASS |
| Oracle top 100 capture | 277 / 534 = 51.9% | PASS |
| Prediction only top 100 capture | 115 / 534 = 21.5% | PASS |
| Random expected top 100 share | 17.5% | PASS |
| Prediction only enrichment | 1.23× | PASS |

## Leakage check

The deployable ranking uses only:

- prediction pattern frequency;
- prediction derived hierarchy inconsistency;
- predicted positive count;
- ID tie breaking.

The test suite alters gold outcome fields and confirms that prediction only ranking order does not change.

The oracle ranking is intentionally gold aware and is labeled only as an upper bound.

## Scientific consistency

The documentation now distinguishes **label level errors** from unique requirement elements.

UserRelated is described correctly as a recall problem: precision is 0.933 and recall is 0.502.

The random comparator is described as an expected capture share under uniform random review rather than as a measured random run.

No file claims that prediction pattern rarity is optimal, calibrated, externally validated, or guaranteed to generalize.

## Presentation repairs completed

- added a real `REPORT.md` and changed the portfolio Report MD link to it;
- rewrote the portfolio summary around review allocation rather than classifier demonstration;
- rebuilt the classification figure to show precision, recall, and F1 with semantic color;
- rebuilt the method figure to expose the gold information boundary and separate oracle from deployable routing;
- recolored the triage, architecture, and evidence boundary graphics for consistent scientific communication;
- expanded the paper blueprint, protocol, analysis plan, research design, data documentation, and reproducibility guide;
- synchronized public presentation under Research in System Engineering.

## Remaining limitations

A PASS means the package is internally coherent and reproducible for its stated scope. It does not mean the heuristic is externally validated, publication accepted, or ready for production review routing.
