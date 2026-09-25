# Scientific Report

## Requirements Classification Evidence Triage on a Gold Standard Benchmark

### Executive summary

This study examines two linked questions in requirements engineering. First, how reliable is automatic fine grained classification across several requirement labels? Second, if human review capacity is limited, can automatically available signals help concentrate review on items that are more likely to contain classification errors?

The analysis uses 571 eTour requirement elements from a public requirements classification benchmark together with corresponding automatic predictions from the NoRBERT and FTLR replication package. Five labels are evaluated: Function, Behavior, Data, F, and UserRelated.

Classification quality is uneven. F1 ranges from 0.653 to 0.945. The most important failure pattern is UserRelated: precision is high at 0.933, but recall is only 0.502, meaning many gold positive UserRelated labels are missed by the automatic classifier.

Across the five evaluated fields there are 534 label level errors. A gold aware oracle ranking can place 277 of those errors in the first 100 reviewed requirement elements, or 51.9% of all observed label errors. That result is diagnostically useful but cannot be deployed because it ranks items using the answer key.

The deployable experiment therefore uses only automatic predictions. It prioritizes rare five bit prediction patterns, then uses prediction only hierarchy inconsistency and predicted label density as deterministic tie breakers. At a review budget of 100 items, this queue captures 115 of 534 label errors, or 21.5%. Uniform random review has an expected capture share of 17.5%, so the heuristic yields 1.23 times the expected random error capture on this benchmark.

The central result is the gap between **error concentration** and **recoverable error concentration**. Errors are strongly concentrated when gold labels are known, but a simple prediction only signal recovers only part of that opportunity. This makes the repository a human in the loop review allocation study rather than merely a classifier evaluation.

### Research questions

1. How does classification performance vary across Function, Behavior, Data, F, and UserRelated?
2. How concentrated are observed label errors under a gold aware oracle review queue?
3. Can a review queue constructed without gold labels capture more errors than uniform random review on the same benchmark?

### Data source and provenance

The release is pinned to commit `02682a0d3cb2fb991942c2d88d11e03221f30f87` of the public FTLR replication repository.

Gold labels trace to the Zenodo dataset *Dataset for Requirements Classification in Traceability Link Recovery Datasets*, version DOI 10.5281/zenodo.7867846. Automatic labels are taken from the corresponding eTour NoRBERT and FTLR replication output.

The repository does not redistribute raw requirement text. It packages derived evaluation outcomes, prediction patterns, aggregate metrics, and review routing results.

### Unit of analysis

One eTour requirement element.

Each element can contribute more than one classification error because five labels are evaluated independently. Therefore, the reported total of 534 refers to **label level errors**, not 534 unique requirement elements.

### Evaluated labels

| Label | Gold positives | Predicted positives | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|
| Function | 299 | 334 | 0.790 | 0.883 | 0.834 |
| Behavior | 342 | 442 | 0.744 | 0.962 | 0.839 |
| Data | 186 | 211 | 0.701 | 0.796 | 0.746 |
| F | 457 | 506 | 0.899 | 0.996 | 0.945 |
| UserRelated | 279 | 150 | 0.933 | 0.502 | 0.653 |

The UserRelated pattern is especially important. The classifier rarely predicts UserRelated incorrectly when it does predict the label, but it misses many gold positive cases.

### Classification estimand

For each evaluated label, gold and automatic rows are joined by requirement ID and classified as true positive, false positive, false negative, or true negative.

Precision, recall, and F1 are then calculated independently for each label.

The source fields `functional`, `OnlyF`, `OnlyQ`, and `Q` are excluded from this release because the corresponding automatic eTour outputs are degenerate for those fields and would not support a meaningful comparative evaluation.

### Review triage problem

The engineering decision problem is not simply whether classification is accurate. It is how to allocate a limited review budget when every requirement cannot be inspected manually.

The repository therefore evaluates three review references.

#### Oracle upper bound

Each requirement element is assigned the number of gold versus prediction disagreements across the five evaluated labels. Items with the most observed errors are ranked first.

This queue uses gold labels. It cannot be used operationally before review. It is interpreted only as an upper bound on how concentrated the observed errors are.

#### Prediction only heuristic

The deployable queue uses no gold outcomes for ranking.

Items are sorted by:

1. lower frequency of the five bit prediction pattern;
2. prediction only hierarchy inconsistency;
3. larger number of predicted positive labels;
4. requirement ID as a deterministic final tie breaker.

The hierarchy flag is triggered when Function, Behavior, or Data is predicted positive while the broader F label is predicted negative.

The heuristic is exploratory and batch dependent because prediction pattern rarity is estimated from the current set of 571 predictions.

#### Uniform random comparator

For simple random review of k items from N = 571, the expected captured share of total label errors is k divided by N.

This is an exact expectation for the sample design, not an observed random run.

### Review results

| Review budget | Oracle errors | Oracle share | Prediction only errors | Prediction only share | Random expected share | Prediction only enrichment |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 38 | 7.1% | 18 | 3.4% | 1.8% | 1.93× |
| 25 | 83 | 15.5% | 34 | 6.4% | 4.4% | 1.45× |
| 50 | 158 | 29.6% | 65 | 12.2% | 8.8% | 1.39× |
| 100 | 277 | 51.9% | 115 | 21.5% | 17.5% | 1.23× |

The oracle result shows that errors are not uniformly distributed across requirement elements. The prediction only heuristic also exceeds random expectation at every released budget, but the advantage decreases as the review budget grows.

The large oracle to deployable gap is the most important engineering result. It shows that knowing errors are concentrated is not the same as having an operational signal that identifies them reliably.

### Systems engineering interpretation

Human review is a scarce verification resource. A review policy should therefore be evaluated independently from the classifier it supports.

This study separates three layers:

1. **classification evidence**, which asks how well labels are predicted;
2. **diagnostic concentration**, which asks how concentrated known errors are;
3. **deployable routing**, which asks what can be prioritized without using gold labels.

That separation prevents label leakage from being mistaken for a practical review strategy.

### Relation to the source research

The underlying 2024 IEEE Requirements Engineering study investigates requirements classification as a way to filter irrelevant requirement parts before traceability link recovery. This repository does not reproduce the entire end to end FTLR evaluation. Instead, it takes the released eTour gold and automatic classification artifacts and studies their review allocation implications.

The contribution is therefore narrower than the source paper: it focuses on classification heterogeneity, leakage safe triage evaluation, and the gap between oracle and deployable review prioritization.

### Threats to validity

**Gold standard validity.** The benchmark labels are treated as the reference truth for evaluation. Annotation errors or ambiguous requirement semantics are not independently re adjudicated here.

**Construct validity.** Classification errors across five labels are treated as units of review value. Different projects may assign different costs to false positives, false negatives, or labels.

**Internal validity.** The oracle and deployable queues are deterministic given the packaged evidence. No causal inference is made.

**Heuristic validity.** Prediction pattern rarity is post hoc and not calibrated from a separate development set. Its ranking quality may partly reflect this specific batch.

**Comparator validity.** Uniform random review provides a simple baseline expectation. The release does not estimate a full probability distribution or confidence interval for random capture.

**External validity.** Results are based on one eTour benchmark, one automatic prediction artifact, and one taxonomy. Performance may change with another domain, classifier, prevalence pattern, or labeling scheme.

**Operational validity.** No reviewer time, review cost, severity weighting, or downstream correction benefit is modeled.

### Reproducibility

Install dependencies and run the offline checks:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Rebuild the evidence from the exact pinned public source:

```bash
python scripts/fetch_and_analyze.py --check
```

Regenerate the scientific figures:

```bash
python scripts/generate_figures.py
```

### Research integrity statement

This is a secondary analysis of public benchmark artifacts. It is not preregistered, externally validated, or a claim of optimal review routing.

The oracle queue is explicitly non deployable because it uses gold labels. The prediction only heuristic is exploratory and is evaluated only after its ranking has been produced without access to gold outcomes.
