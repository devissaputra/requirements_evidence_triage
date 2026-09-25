# Final QA Report

**Release status: PENDING GITHUB-HOSTED VERIFICATION AFTER REPAIR.**

## Repairs completed
- corrected gold-label leakage in the interpretation of review prioritization;
- retained the 51.9% result only as an oracle upper bound;
- added prediction-only pattern-rarity triage and exact random expectation;
- packaged complete 571-row derived evaluation evidence;
- expanded tests across all confusion matrices and triage curves;
- pinned the FTLR source to commit `02682a0d3cb2fb991942c2d88d11e03221f30f87`;
- added SHA-256 reporting during source rebuild;
- added CI and empirical-source rebuild workflows;
- added reproducible figure generation and corrected misleading figures;
- restored the complete standard MIT license;
- removed stale portfolio references;
- expanded scholarly positioning and synchronized all research documentation.

## Release numbers
571 elements; 534 five-label errors; F1 range 0.653–0.945; oracle top-100 51.9%; prediction-only top-100 21.5%; random expected 17.5%; prediction-only enrichment 1.23×.

## Release condition
Mark PASS after CI and empirical-source rebuild both succeed on this repaired commit.
