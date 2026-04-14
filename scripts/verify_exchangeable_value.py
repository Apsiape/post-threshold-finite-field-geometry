from decimal import Decimal
from pathlib import Path
import sys

from sympy import Abs, Float, N, Poly, im, re

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import (
    E_STAR_DECIMAL,
    E_STAR_INTERVAL,
    E_STAR_POLY,
    STAR_VALUE_EXACT,
    UNIFORM_SIGN_F35_VALUE,
    e_star_polynomial_value,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


star_decimal = Decimal(str(N(STAR_VALUE_EXACT, 20)))
uniform_decimal = Decimal(str(N(UNIFORM_SIGN_F35_VALUE, 20)))
interval_low = Float(str(E_STAR_INTERVAL[0]), 60)
interval_high = Float(str(E_STAR_INTERVAL[1]), 60)
poly = Poly(E_STAR_POLY)
roots = poly.nroots(n=80, maxsteps=200)
real_roots_in_interval = [
    root
    for root in roots
    if Abs(im(root)) < Float("1e-40") and interval_low < re(root) < interval_high
]
e_star_numeric = Float(str(E_STAR_DECIMAL), 60)
residual = Abs(N(e_star_polynomial_value(e_star_numeric), 60))
endpoint_product = N(e_star_polynomial_value(interval_low) * e_star_polynomial_value(interval_high), 60)

require(len(real_roots_in_interval) == 1, "expected a unique real root in the stated interval")
require(endpoint_product < 0, "polynomial should change sign across the stated interval")
require(residual < Float("1e-12"), "polynomial evaluated at E_* decimal should be near zero")
require(E_STAR_DECIMAL > star_decimal, "exchangeable value should exceed the star value")
require(E_STAR_DECIMAL < uniform_decimal, "exchangeable value should be below 31/90")

print(
    "PASS: exchangeable support-<=2 class constant E_* lies in the stated interval, "
    "is the unique real root there, and satisfies its defining polynomial numerically."
)
