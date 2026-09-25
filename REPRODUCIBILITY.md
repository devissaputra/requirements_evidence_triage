# Reproducibility

## Offline
```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Tests recompute all five confusion matrices and the oracle/deployable/random review curves from the complete 571-row derived evidence.

## Pinned-source rebuild
```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild retrieves exact commit-pinned source files, prints SHA-256 hashes for both, reconstructs the full derived evidence, and fails on any released-result mismatch.

## Figures
```bash
python scripts/generate_figures.py --out-dir /tmp/requirements_figures
```

CI smoke-tests generation and XML validity for all five SVGs.
