from pathlib import Path
import sys

import pytest
from sympy import Float, Rational, simplify

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from post_threshold_geometry import (
    E_STAR_DECIMAL,
    Q_DAGGER,
    RHO_DAGGER,
    X_DAGGER,
    Y_DAGGER,
    e_star_polynomial_value,
    epsilon_dagger_value,
    mu_dagger_mass_sum,
    threshold_bound,
    threshold_condition,
    threshold_max_integer,
)


@pytest.mark.parametrize("p, bound, cutoff", [(3, Rational(9, 2), 4), (5, Rational(15, 4), 3), (7, Rational(7, 2), 3)])
def test_threshold_bound_and_cutoff(p, bound, cutoff):
    assert threshold_bound(p) == bound
    assert threshold_max_integer(p) == cutoff
    assert threshold_condition(p, cutoff)
    assert not threshold_condition(p, cutoff + 1)


def test_exchangeable_polynomial_helper():
    assert abs(e_star_polynomial_value(Float(str(E_STAR_DECIMAL), 50)).evalf(50)) < Float("1e-12")


def test_mu_dagger_helpers():
    assert simplify(mu_dagger_mass_sum() - 1) == 0
    assert simplify(epsilon_dagger_value() - (Rational(1478, 4095) - Rational(1, 819) * (205 ** Rational(1, 2)))) == 0
    assert all(parameter >= 0 for parameter in (RHO_DAGGER, Q_DAGGER, X_DAGGER, Y_DAGGER))
