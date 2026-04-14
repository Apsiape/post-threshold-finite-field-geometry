from decimal import Decimal
from pathlib import Path
import sys

from sympy import Float, Poly, Rational, simplify, sqrt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from post_threshold_geometry import (
    EPSILON_DAGGER,
    E_STAR_DECIMAL,
    E_STAR_INTERVAL,
    E_STAR_POLY,
    E_STAR_SYMBOL,
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
)


def test_core_exact_constants():
    assert THRESHOLD_VALUE == Rational(1, 3)
    assert UNIFORM_SIGN_F35_VALUE == Rational(31, 90)
    assert simplify(STAR_VALUE_EXACT - (Rational(1478, 4095) - sqrt(205) / 819)) == 0
    assert simplify(EPSILON_DAGGER - STAR_VALUE_EXACT) == 0


def test_exchangeable_polynomial_data():
    assert E_STAR_INTERVAL == (Decimal("0.3442"), Decimal("0.3443"))
    assert E_STAR_DECIMAL == Decimal("0.34421042513543912767")
    assert Poly(E_STAR_POLY, E_STAR_SYMBOL).all_coeffs() == [
        6720000,
        -1096600000,
        5937209600,
        -7442465200,
        3638500832,
        -667345588,
        -3623728,
        9535419,
    ]
    assert abs(e_star_polynomial_value(Float(str(E_STAR_DECIMAL), 50)).evalf(50)) < Float("1e-12")


def test_mu_dagger_parameter_formulas():
    assert simplify(Q_DAGGER - (Rational(1, 18) - RHO_DAGGER / 6)) == 0
    assert simplify(X_DAGGER - (Rational(5, 18) - 5 * RHO_DAGGER / 6)) == 0
    assert simplify(Y_DAGGER - (Rational(5, 18) - 35 * RHO_DAGGER / 6)) == 0


def test_decimal_constants_match_exact_values():
    assert abs(Decimal(str(RHO_DAGGER.evalf(24))) - RHO_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(Q_DAGGER.evalf(24))) - Q_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(X_DAGGER.evalf(24))) - X_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(Y_DAGGER.evalf(24))) - Y_DAGGER_DECIMAL) < Decimal("1e-20")
    assert abs(Decimal(str(STAR_VALUE_EXACT.evalf(24))) - STAR_VALUE_DECIMAL) < Decimal("1e-20")
