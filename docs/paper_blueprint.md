# Paper Blueprint

## Working title

**From Error Concentration to Deployable Review Triage in Fine Grained Requirements Classification**

Alternative title:

**Separating Oracle and Prediction Only Review Prioritization in Requirements Classification**

## Paper identity

This should be written as an empirical requirements engineering and human in the loop decision support paper.

The strongest contribution is the explicit separation of three questions that are often conflated:

1. how well a classifier performs;
2. how concentrated known errors are;
3. how much of that concentration can be recovered without access to gold labels.

The paper should not be framed as a new classifier paper.

## One sentence contribution

Using 571 eTour requirement elements, the study quantifies the gap between a gold aware upper bound on error concentration and an exploratory prediction only review queue.

## Draft abstract

Automatic requirements classification can support traceability and other downstream engineering tasks, but aggregate classification scores do not indicate where scarce human review effort should be allocated. This study analyzes 571 eTour requirement elements using released gold labels and automatic classifications from a pinned NoRBERT and FTLR replication artifact. Five labels are evaluated: Function, Behavior, Data, F, and UserRelated. F1 ranges from 0.653 to 0.945, with UserRelated showing high precision of 0.933 but recall of only 0.502. Across the five labels, 534 label level errors are observed. A gold aware oracle ranking concentrates 51.9% of these errors in the first 100 reviewed items, demonstrating substantial error concentration but using information unavailable before review. A prediction only heuristic based on rare label patterns, hierarchy inconsistency, and predicted label density captures 21.5% of errors in the first 100 items, compared with 17.5% expected under uniform random review. The result shows both the potential and the limitation of targeted review: errors are highly concentrated in hindsight, while a simple deployable signal recovers only part of that concentration. The study argues that classifier evaluation and review policy evaluation should be reported separately to avoid information leakage and overstated operational claims.

## Introduction logic

### Paragraph 1: engineering problem

Requirements classification can help identify relevant parts of requirements for downstream activities such as traceability recovery. Human review remains necessary when classification is imperfect.

### Paragraph 2: decision problem

A team with limited review capacity needs more than F1. It needs evidence about which items should be inspected first.

### Paragraph 3: methodological risk

A review policy can appear extremely effective if it is ranked using the same gold labels later used for evaluation. That is useful as an oracle diagnostic but invalid as a deployable policy.

### Paragraph 4: contribution

This study keeps the oracle and deployable questions separate and measures the gap between them on a pinned public benchmark.

## Research questions

**RQ1.** How does classification performance vary across five fine grained requirement labels?

**RQ2.** How concentrated are observed label errors under a gold aware oracle queue?

**RQ3.** Does an exploratory prediction only queue outperform uniform random review expectation at fixed review budgets?

## Data section

Report:

- 571 eTour requirement elements;
- gold labels from Zenodo record 10.5281/zenodo.7867846;
- automatic predictions from the pinned NoRBERT and FTLR replication package;
- exact source commit;
- raw text not redistributed;
- five included labels;
- four excluded degenerate source fields.

Explain that 534 is a count of label level errors, not unique erroneous requirements.

## Classification method

For every included label, compute TP, FP, FN, TN, precision, recall, and F1.

Report the full table rather than only macro or aggregate values.

Highlight the UserRelated pattern because recall, not precision, is the dominant weakness.

## Review routing method

### Oracle upper bound

Rank by observed gold versus prediction disagreement count.

State prominently that this is non deployable and is included only to quantify maximum observed concentration under perfect hindsight.

### Prediction only queue

Rank by prediction pattern rarity, hierarchy inconsistency, predicted positive count, and deterministic ID tie breaking.

Define each term explicitly.

### Random expectation

At budget k, expected uniform random error capture share is k / 571.

Do not describe this as a Monte Carlo result.

## Results structure

### 1. Label level classification

Use a grouped precision, recall, and F1 figure.

### 2. Error concentration

Report 534 total label errors.

### 3. Review curves

| Budget | Oracle | Prediction only | Random expected | Enrichment |
|---:|---:|---:|---:|---:|
| 10 | 7.1% | 3.4% | 1.8% | 1.93× |
| 25 | 15.5% | 6.4% | 4.4% | 1.45× |
| 50 | 29.6% | 12.2% | 8.8% | 1.39× |
| 100 | 51.9% | 21.5% | 17.5% | 1.23× |

### 4. Oracle to deployable gap

At budget 100, the oracle captures 277 errors while the prediction only queue captures 115. The difference is 162 label errors.

Interpret this as evidence that substantial error concentration exists but is not fully exposed by simple prediction pattern rarity.

## Discussion

### Classification implication

UserRelated performance shows why a single F1 summary can obscure the type of failure. High precision with low recall implies many missed positives.

### Review allocation implication

A classifier and a review policy are separate systems. Improvement in one does not guarantee improvement in the other.

### Leakage implication

Gold aware prioritization should be clearly labeled as oracle analysis. Otherwise an apparently strong review result can be operationally impossible.

### Future model direction

The oracle gap motivates stronger deployable signals such as calibrated probabilities, entropy, margin, ensemble disagreement, conformal uncertainty, learned routing, or reviewer cost aware prioritization.

These are future research directions, not claims demonstrated in this release.

## Limitations

Include at least:

1. one benchmark domain;
2. one automatic prediction artifact;
3. five selected labels;
4. gold labels treated as reference truth;
5. exploratory post hoc heuristic;
6. no probability or confidence output;
7. batch dependent rarity score;
8. no reviewer cost or error severity weighting;
9. random comparator reported as expectation without uncertainty interval;
10. no external validation.

## Figures

**Figure 1. Classification evidence.** Grouped precision, recall, and F1 by label, with UserRelated recall explicitly highlighted.

**Figure 2. Leakage safe review pipeline.** Gold and automatic labels enter evaluation, but only prediction derived features enter the deployable ranking.

**Figure 3. Review error capture by budget.** Oracle, prediction only, and random expected curves using distinct colors and clear labeling.

## Tables

**Table 1.** Dataset, source, labels, and exclusions.

**Table 2.** Confusion matrix and precision, recall, F1 for five labels.

**Table 3.** Review budget results.

**Appendix.** Full heuristic definition and exact source commit.

## Literature positioning

Use the Hey, Keim, and Corallo work to establish the role of requirements classification in traceability link recovery.

Use human in the loop literature only to motivate review allocation and human oversight.

Do not claim that prediction pattern rarity is a state of the art uncertainty estimator. It is intentionally a transparent baseline heuristic.

## Writing rules

- Say “label level errors,” not “534 incorrect requirements.”
- Say “oracle upper bound,” not “best triage model.”
- Say “prediction only heuristic,” not “AI confidence.”
- Say “expected under uniform random review,” not “random experiment.”
- Keep classifier quality and routing quality in separate subsections.
- Do not describe the work as preregistered or externally validated.

## Completion checklist

A manuscript draft is ready for external feedback when:

- every result maps to a released CSV or JSON file;
- the oracle information boundary is visible in both text and figures;
- the abstract contains the deployable result, not only the oracle result;
- UserRelated recall is reported explicitly;
- limitations are complete;
- references and DOIs are verified;
- a tagged repository release is cited.
