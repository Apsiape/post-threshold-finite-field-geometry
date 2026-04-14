## Reproducibility

This repository uses checked-in Python scripts and SymPy-based verification rather than notebook-only workflows.

## Environment

A minimal environment is enough:

1. Python 3.11+
2. SymPy
3. pytest for the test suite

## Suggested setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Verification scripts

Run these from the repository root:

- `python scripts/verify_threshold_theorem.py`
- `python scripts/verify_exchangeable_value.py`
- `python scripts/verify_star_value.py`
- `python scripts/verify_star_branch_closures.py`
- `python scripts/verify_distinguished_coordinate_extension.py`
- `python scripts/verify_constants.py`

These scripts check stored exact expressions, the `E_*` defining polynomial, the `mu_dagger` mass identities, decimal agreement, threshold cutoffs, and ledger consistency.

## Tests

Run:

```bash
pytest
```

The tests cover:

- exact constants and decimal approximations;
- threshold helper formulas;
- symbolic simplifications that should vanish;
- internal theorem-ledger consistency.

## Exact checks now included

The package now includes exact symbolic data for:

1. the defining degree-seven polynomial of `E_*` and its isolating interval;
2. the explicit `mu_dagger` parameterization and the exact mass-sum identity;
3. the exact expression `epsilon_dagger = 1478/4095 - sqrt(205)/819`.
