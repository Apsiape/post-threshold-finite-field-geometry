from decimal import Decimal
from pathlib import Path
import sys

from sympy import N, Rational, simplify, sqrt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import (
    EPSILON_DAGGER,
    Q_DAGGER,
    Q_DAGGER_DECIMAL,
    RHO_DAGGER,
    RHO_DAGGER_DECIMAL,
    STAR_VALUE_DECIMAL,
    STAR_VALUE_EXACT,
    X_DAGGER,
    X_DAGGER_DECIMAL,
    Y_DAGGER,
    Y_DAGGER_DECIMAL,
    epsilon_dagger_value,
    mu_dagger_mass_sum,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


expected = Rational(1478, 4095) - sqrt(205) / 819
require(simplify(STAR_VALUE_EXACT - expected) == 0, "exact star expression mismatch")
require(simplify(EPSILON_DAGGER - expected) == 0, "epsilon_dagger exact expression mismatch")
require(simplify(epsilon_dagger_value() - expected) == 0, "epsilon_dagger helper mismatch")
require(simplify(mu_dagger_mass_sum() - 1) == 0, "mu_dagger mass should sum to 1 exactly")
require(RHO_DAGGER >= 0, "rho_dagger should be nonnegative")
require(Q_DAGGER >= 0, "q_dagger should be nonnegative")
require(X_DAGGER >= 0, "x_dagger should be nonnegative")
require(Y_DAGGER >= 0, "y_dagger should be nonnegative")

approx = Decimal(str(N(STAR_VALUE_EXACT, 24)))
require(abs(approx - STAR_VALUE_DECIMAL) < Decimal("1e-20"), "star decimal mismatch")
require(abs(Decimal(str(N(RHO_DAGGER, 24))) - RHO_DAGGER_DECIMAL) < Decimal("1e-20"), "rho_dagger decimal mismatch")
require(abs(Decimal(str(N(Q_DAGGER, 24))) - Q_DAGGER_DECIMAL) < Decimal("1e-20"), "q_dagger decimal mismatch")
require(abs(Decimal(str(N(X_DAGGER, 24))) - X_DAGGER_DECIMAL) < Decimal("1e-20"), "x_dagger decimal mismatch")
require(abs(Decimal(str(N(Y_DAGGER, 24))) - Y_DAGGER_DECIMAL) < Decimal("1e-20"), "y_dagger decimal mismatch")

print(
    "PASS: mu_dagger parameters are nonnegative, sum to 1 exactly, and produce "
    f"epsilon_dagger = {STAR_VALUE_EXACT} ≈ {approx}."
)
