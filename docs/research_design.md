# Research Design

## Design summary

Secondary benchmark study of requirements classification and review allocation using 571 paired eTour gold and automatic prediction records.

## Unit of analysis

One requirement element.

## Evidence layers

The study separates four layers:

1. **gold reference labels** used for evaluation;
2. **automatic predictions** available before human review;
3. **classification outcomes** used to diagnose model performance;
4. **review routing signals** used to prioritize human inspection.

## Classification layer

For five labels, gold and predicted values are compared independently.

The released metrics are confusion matrix counts, precision, recall, and F1.

## Oracle diagnostic layer

Actual label disagreements are counted per requirement and used to construct a hindsight ranking.

This layer deliberately uses gold outcomes and therefore measures only the concentration of known errors.

## Deployable routing layer

The deployable queue uses prediction derived information only:

- pattern frequency;
- hierarchy inconsistency;
- predicted label density;
- deterministic ID tie breaking.

The queue is constructed without access to gold outcomes.

## Information boundary

Gold labels may enter:

- classification evaluation;
- oracle analysis;
- post ranking measurement of captured errors.

Gold labels may not enter:

- deployable queue construction.

This boundary is enforced by tests.

## Comparator

Uniform random review provides an expected capture reference at the same review budgets.

## Inference scope

The study supports descriptive claims about the pinned eTour benchmark and released automatic predictions.

It does not establish causal effects, optimal routing, calibrated confidence, cross dataset generalization, or production reviewer efficiency.

## Threats to validity

Gold labels are assumed to be the evaluation reference.

Prediction pattern rarity is estimated within the current batch.

All label errors are counted equally even though real engineering consequences may differ.

The analysis uses one dataset and one prediction artifact.
