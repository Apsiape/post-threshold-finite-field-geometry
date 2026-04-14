from decimal import Decimal
from pathlib import Path
import sys

from sympy import Float, N, Rational, simplify, sqrt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import (
    EPSILON_DAGGER,
    E_STAR_DECIMAL,
    E_STAR_INTERVAL,
    E_STAR_POLY,
    Q_DAGGER,
    Q_DAGGER_DECIMAL,
    RHO_DAGGER,
    RHO_DAGGER_DECIMAL,
    STAR_VALUE_EXACT,
    STAR_VALUE_DECIMAL,
    THRESHOLD_VALUE,
    UNIFORM_SIGN_F35_VALUE,
    X_DAGGER,
    X_DAGGER_DECIMAL,
    Y_DAGGER,
    Y_DAGGER_DECIMAL,
    e_star_polynomial_value,
    epsilon_dagger_value,
    mu_dagger_mass_sum,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


require(THRESHOLD_VALUE == Rational(1, 3), "threshold value mismatch")
require(UNIFORM_SIGN_F35_VALUE == Rational(31, 90), "uniform-sign value mismatch")
require(simplify(STAR_VALUE_EXACT - (Rational(1478, 4095) - sqrt(205) / 819)) == 0, "star value mismatch")
require(simplify(EPSILON_DAGGER - epsilon_dagger_value()) == 0, "epsilon helper mismatch")
require(simplify(mu_dagger_mass_sum() - 1) == 0, "mu_dagger mass-sum mismatch")
require(E_STAR_DECIMAL == Decimal("0.34421042513543912767"), "exchangeable decimal mismatch")
require(E_STAR_INTERVAL == (Decimal("0.3442"), Decimal("0.3443")), "exchangeable interval mismatch")
require(E_STAR_POLY.as_poly() is not None, "exchangeable polynomial should be polynomial data")
require(abs(N(e_star_polynomial_value(Float(str(E_STAR_DECIMAL), 50)), 50)) < Float("1e-12"), "exchangeable polynomial residual too large")
require(E_STAR_DECIMAL > Decimal("0.34"), "exchangeable value unexpectedly small")
require(E_STAR_DECIMAL > Decimal(str(N(STAR_VALUE_EXACT, 20))), "exchangeable value should exceed star value")
require(all(parameter >= 0 for parameter in (RHO_DAGGER, Q_DAGGER, X_DAGGER, Y_DAGGER)), "mu_dagger parameters should be nonnegative")
require(abs(Decimal(str(N(RHO_DAGGER, 24))) - RHO_DAGGER_DECIMAL) < Decimal("1e-20"), "rho decimal mismatch")
require(abs(Decimal(str(N(Q_DAGGER, 24))) - Q_DAGGER_DECIMAL) < Decimal("1e-20"), "q decimal mismatch")
require(abs(Decimal(str(N(X_DAGGER, 24))) - X_DAGGER_DECIMAL) < Decimal("1e-20"), "x decimal mismatch")
require(abs(Decimal(str(N(Y_DAGGER, 24))) - Y_DAGGER_DECIMAL) < Decimal("1e-20"), "y decimal mismatch")
require(abs(Decimal(str(N(STAR_VALUE_EXACT, 24))) - STAR_VALUE_DECIMAL) < Decimal("1e-20"), "star decimal mismatch")

print("PASS: core constants are internally consistent.")
