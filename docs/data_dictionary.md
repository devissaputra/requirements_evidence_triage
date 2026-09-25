# Data Dictionary

## Evaluation evidence

### `data/derived/evaluation_observations.csv`

Complete 571 row derived evaluation table. Raw requirement text is not included.

Each row contains:

- `ID`: requirement identifier;
- one outcome field per evaluated label, coded TP, FP, FN, or TN;
- `predicted_pattern`: five bit automatic prediction pattern in label order;
- `pattern_frequency`: frequency of that prediction pattern in the 571 item batch;
- `predicted_positive_count`: number of predicted positive labels;
- `hierarchy_violation`: prediction only inconsistency flag;
- `label_errors`: number of FP plus FN outcomes across the five labels.

## Label order

The prediction pattern uses:

1. Function
2. Behavior
3. Data
4. F
5. UserRelated

## Hierarchy flag

`hierarchy_violation = 1` when Function, Behavior, or Data is predicted positive while F is predicted negative.

The flag is constructed only from automatic predictions.

## Primary classification results

### `data/derived/primary_results.csv`

One row per evaluated label with:

- precision;
- recall;
- F1;
- TP;
- FP;
- FN;
- TN.

## Review results

### `data/derived/triage_results.csv`

One row per method and review budget with:

- `method`;
- `budget`;
- `errors_captured`;
- `error_capture_share`;
- `enrichment_vs_random`;
- `uses_gold_for_ranking`.

Methods:

- `oracle_upper_bound`;
- `prediction_pattern_rarity`;
- `random_expected`.

## Error unit

`label_errors` counts label level disagreements. It is not a binary indicator that the entire requirement is wrong.

## Excluded source fields

`functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded because the automatic eTour artifact is degenerate for these fields.
