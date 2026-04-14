from __future__ import annotations

from sympy import Rational, floor, isprime, sympify

from .constants import E_STAR_POLY, EPSILON_DAGGER, Q_DAGGER, RHO_DAGGER, X_DAGGER, Y_DAGGER


def validate_odd_prime(p: int) -> None:
    if not isinstance(p, int):
        raise TypeError("p must be an integer")
    if p <= 2 or p % 2 == 0 or not isprime(p):
        raise ValueError("p must be an odd prime")


def validate_k(k: int) -> None:
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 2:
        raise ValueError("k must satisfy k >= 2")


def threshold_bound(p: int):
    validate_odd_prime(p)
    return Rational(3 * p, p - 1)


def threshold_condition(p: int, k: int) -> bool:
    validate_odd_prime(p)
    validate_k(k)
    return Rational(k, 1) <= threshold_bound(p)


def threshold_max_integer(p: int) -> int:
    validate_odd_prime(p)
    return int(floor(threshold_bound(p)))


def e_star_polynomial_value(value):
    return E_STAR_POLY.subs(next(iter(E_STAR_POLY.free_symbols)), sympify(value))


def mu_dagger_mass_sum():
    return X_DAGGER + Y_DAGGER + 8 * Q_DAGGER + 8 * RHO_DAGGER


def epsilon_dagger_value():
    return EPSILON_DAGGER
