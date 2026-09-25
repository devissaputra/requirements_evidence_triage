# Research Design

## Unit of analysis
One eTour requirement element.

## Data pairing
Gold and automatic rows are joined by the 571 shared IDs.

## Evaluated labels
Function, Behavior, Data, F, UserRelated.

## Three analysis layers
1. **Classification:** confusion matrices and F1.
2. **Oracle diagnostic:** rank by actual disagreement count to quantify a gold-aware upper bound.
3. **Deployable exploratory routing:** rank using only prediction-pattern rarity and prediction-derived tie-breakers.

## Leakage correction
A gold-error ranking cannot be used before review. This release therefore reports it only as an oracle ceiling and evaluates a separate prediction-only rule against uniform-random expectation.

## External validity
The prediction-only rule is batch-dependent because rarity is estimated from the current prediction set. Performance may differ with another classifier, dataset, taxonomy, or prevalence pattern.
