from decimal import Decimal
from pathlib import Path
import sys

from sympy import N, simplify

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from post_threshold_geometry import (
    BRANCH_CLOSURE_KEYS,
    E_STAR_DECIMAL,
    Q_DAGGER,
    Q_DAGGER_DECIMAL,
    RHO_DAGGER,
    RHO_DAGGER_DECIMAL,
    STAR_VALUE_EXACT,
    STAR_VALUE_DECIMAL,
    UNIFORM_SIGN_F35_VALUE,
    X_DAGGER,
    X_DAGGER_DECIMAL,
    Y_DAGGER,
    Y_DAGGER_DECIMAL,
    mu_dagger_mass_sum,
)
from post_threshold_geometry.theorem_ledger import records_by_status


def test_decimal_ordering():
    star_decimal = Decimal(str(N(STAR_VALUE_EXACT, 24)))
    uniform_decimal = Decimal(str(N(UNIFORM_SIGN_F35_VALUE, 18)))
    assert abs(star_decimal - STAR_VALUE_DECIMAL) < Decimal("1e-20")
    assert star_decimal < E_STAR_DECIMAL < uniform_decimal


def test_mu_dagger_symbolic_relations():
    assert simplify(mu_dagger_mass_sum() - 1) == 0
    assert all(parameter >= 0 for parameter in (RHO_DAGGER, Q_DAGGER, X_DAGGER, Y_DAGGER))
    assert abs(Decimal(str(N(RHO_DAGGER, 24))) - RHO_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(N(Q_DAGGER, 24))) - Q_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(N(X_DAGGER, 24))) - X_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(N(Y_DAGGER, 24))) - Y_DAGGER_DECIMAL) < Decimal("1e-20")


def test_ledger_shape():
    proved_keys = {record.key for record in records_by_status("PROVED")}
    assert "threshold_odd_primes" in proved_keys
    assert "branch_closures_f35" in proved_keys
    assert len(BRANCH_CLOSURE_KEYS) == 7
