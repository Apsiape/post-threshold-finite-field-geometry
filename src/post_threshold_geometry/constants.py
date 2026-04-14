from __future__ import annotations

from decimal import Decimal

from sympy import N, Rational, sqrt, symbols

THRESHOLD_VALUE = Rational(1, 3)
UNIFORM_SIGN_F35_VALUE = Rational(31, 90)

E_STAR_SYMBOL = symbols("E", real=True)
E_STAR_POLY = (
    6720000 * E_STAR_SYMBOL**7
    - 1096600000 * E_STAR_SYMBOL**6
    + 5937209600 * E_STAR_SYMBOL**5
    - 7442465200 * E_STAR_SYMBOL**4
    + 3638500832 * E_STAR_SYMBOL**3
    - 667345588 * E_STAR_SYMBOL**2
    - 3623728 * E_STAR_SYMBOL
    + 9535419
)
E_STAR_INTERVAL = (Decimal("0.3442"), Decimal("0.3443"))
E_STAR_DECIMAL = Decimal("0.34421042513543912767")

RHO_DAGGER = (Rational(32, 1) + sqrt(205)) / 2457
Q_DAGGER = Rational(1, 18) - RHO_DAGGER / 6
X_DAGGER = Rational(5, 18) - 5 * RHO_DAGGER / 6
Y_DAGGER = Rational(5, 18) - 35 * RHO_DAGGER / 6
EPSILON_DAGGER = Rational(1478, 4095) - sqrt(205) / 819
RHO_DAGGER_DECIMAL = Decimal("0.01885137202412549986")
Q_DAGGER_DECIMAL = Decimal("0.05241366021820130558")
X_DAGGER_DECIMAL = Decimal("0.26206830109100652789")
Y_DAGGER_DECIMAL = Decimal("0.16781144097037902860")

STAR_VALUE_EXACT = EPSILON_DAGGER
STAR_VALUE_DECIMAL = Decimal("0.34344588392762350042")
EXCHANGEABLE_SUPPORT_LE2_VALUE_APPROX = E_STAR_DECIMAL

EXCHANGEABLE_SUPPORT_LE2_NOTE = (
    "The theorem status of the exchangeable support-<=2 optimum is PROVED, "
    "with exact defining polynomial and interval now recorded in the package."
)

MU_DAGGER_NOTE = (
    "The star and distinguished-coordinate theorems are recorded as PROVED. "
    "The exact one-distinguished-coordinate parameterization of mu_dagger is "
    "recorded in the package."
)

BRANCH_CLOSURE_KEYS = (
    "tau_zero",
    "s_one_third",
    "region_s_ge_one_third",
    "y_zero",
    "x_eq_y",
    "tail_tail_same_sign",
    "tail_tail_mixed",
)


def star_value_numeric(precision: int = 50):
    return N(STAR_VALUE_EXACT, precision)
