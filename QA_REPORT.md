# Final QA Report

**Research bundle status: PASS.**  
**Current CI status: PASS.**  
**Current empirical source rebuild status: PASS.**

## Scientific repairs completed
- corrected gold-label leakage in the interpretation of review prioritization;
- retained the 51.9% result only as an oracle upper bound;
- added prediction-only pattern-rarity triage and exact random expectation;
- packaged complete 571-row derived evaluation evidence;
- expanded tests across all five confusion matrices and all triage curves;
- pinned the FTLR source to commit `02682a0d3cb2fb991942c2d88d11e03221f30f87`;
- added SHA-256 reporting for both pinned source CSVs during rebuild;
- added CI and empirical-source rebuild workflows;
- added reproducible five-figure generation and corrected misleading figures;
- restored the complete standard MIT license;
- removed stale portfolio references;
- expanded scholarly positioning and synchronized research documentation.

## Verified release numbers
- requirement elements: **571**
- five-label errors: **534**
- F1 range: **0.653–0.945**
- oracle top-100 capture: **277 errors / 51.9%**
- prediction-only top-100 capture: **115 errors / 21.5%**
- uniform-random expected top-100 share: **17.5%**
- prediction-only enrichment at 100: **1.23×**

## GitHub-hosted verification
- **CI:** PASS
- **Empirical source rebuild:** PASS

The source rebuild verified the complete packaged evidence against the exact pinned upstream commit and reported SHA-256 digests for both source CSV files.

## Interpretation boundary
The oracle queue uses gold labels and is not deployable. The prediction-pattern-rarity queue uses automatic predictions only, is exploratory and post hoc, and is not claimed to be optimal or externally validated.

No open research, code, data, test, CI, provenance, reproducibility, figure, or documentation defect remains in this QA report.
