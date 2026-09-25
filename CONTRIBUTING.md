# Contributing

Changes should preserve the information boundary between evaluation and deployable review routing.

## Scientific changes

If a contribution changes the evaluated labels, ranking rule, review budgets, source artifact, exclusion rule, or error definition, update the analysis documentation and add tests.

Do not silently change the released estimand.

## Leakage control

Gold outcomes may be used for evaluation and oracle diagnostics.

They must not enter the construction of a ranking described as deployable or prediction only.

Add tests whenever ranking features change.

## Data changes

Preserve provenance and source pinning. Do not redistribute raw requirement text unless its license and redistribution conditions are explicitly checked.

## Documentation changes

Keep numerical claims synchronized with the released CSV and JSON evidence.

Use “label level errors” when discussing the count of 534.

## Claim discipline

Do not describe the prediction pattern rarity heuristic as optimal, calibrated, externally validated, or production ready unless new evidence establishes that status.
