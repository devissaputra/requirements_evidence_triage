# Paper Blueprint

## Working title
From Oracle Error Concentration to Deployable Review Triage in Fine-Grained Requirements Classification

## Motivation
Aggregate classifier scores do not answer where scarce human review capacity should be spent. Review-routing studies must also avoid using the answer key to decide what gets reviewed.

## Contribution
This study separates classification performance, an oracle upper bound on known-error concentration, and an exploratory queue computed from automatic predictions alone.

## Main result
The benchmark contains 534 five-label errors. The gold-aware oracle puts 51.9% in 100 items. Prediction-pattern rarity captures 21.5% in 100 items versus 17.5% expected under uniform random review.

## Interpretation
The large oracle-to-deployable gap shows that error concentration exists but is not automatically recoverable from a simple prediction-only signal. That motivates calibrated uncertainty, confidence-aware abstention, learned routing, and external validation.

## Limitations
Single benchmark, post-hoc heuristic, no probability/confidence outputs, descriptive analysis, and no claim of optimality or causal effect.
