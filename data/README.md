# Data

**Primary source:** eTour fine-grained requirements-classification benchmark in the FTLR replication package

**Source page:** https://github.com/tobhey/finegrained-traceability

**Reuse note:** Gold-standard requirements-classification dataset: CC BY 4.0 (Zenodo DOI 10.5281/zenodo.7867846). Automatic predictions are taken from the cited FTLR replication repository.

Raw source observations are not bundled here by default. Derived tables are packaged under `data/derived/`; their completeness or subset status is stated in `docs/data_dictionary.md`.

**Construct boundary:** The benchmark evaluates requirement-element classification, not end-to-end physical-system verification. The four additional fields in the CSVs (functional, OnlyF, OnlyQ, Q) are excluded from the triage estimand because the supplied eTour automatic file is degenerate for those fields (all-zero outputs), so treating them as ordinary predictions would inflate disagreement counts and misstate the classifier output.
