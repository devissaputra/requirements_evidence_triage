# Originality and Positioning Map

## What this repository is

A reproducible requirements engineering study that separates classifier evaluation from human review routing and explicitly measures the gap between an oracle diagnostic and a deployable prediction only heuristic.

## What it is not

It is not:

- a new requirements classifier;
- a new uncertainty calibration method;
- an end to end reproduction of the FTLR paper;
- a claim of optimal human review routing;
- a production verification system.

## Distinctive combination

The repository combines:

1. a pinned public gold benchmark;
2. paired automatic predictions;
3. five label confusion analysis;
4. a gold aware error concentration ceiling;
5. a prediction only triage heuristic;
6. exact random expectation;
7. a leakage test proving that gold outcomes do not alter deployable ranking;
8. reproducible source reconstruction.

## Research contribution

The defensible contribution is methodological transparency around review allocation.

The study shows that:

- classifier quality varies substantially by label;
- errors can be highly concentrated in hindsight;
- a simple deployable signal captures more errors than random expectation but far less than the oracle;
- oracle and operational review results should be reported separately.

## Portfolio position

**Engineering Management Research**

Public portfolio presentation:

**Research in System Engineering**

Focus:

**Requirements Engineering / Human Review Allocation / Evidence Triage**
