from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TheoremRecord:
    key: str
    title: str
    status: str
    statement: str
    notes: str = ""


LEDGER = [
    TheoremRecord(
        key="threshold_odd_primes",
        title="Odd-prime threshold theorem",
        status="PROVED",
        statement=(
            "For every odd prime p and every k >= 2, the full ambient additive "
            "value equals 1/3 if and only if k <= 3p/(p-1)."
        ),
        notes="In particular, the threshold cutoff is k <= 4 for p = 3 and k <= 3 for every odd prime p >= 5.",
    ),
    TheoremRecord(
        key="naive_old_hull_false",
        title="Failure of the naive old hull in the odd-prime anisotropic branch",
        status="PROVED",
        statement="The earlier naive old hull is false in the odd-prime anisotropic branch.",
    ),
    TheoremRecord(
        key="uniform_sign_f35",
        title="Uniform-sign ambient class on F_3^5",
        status="PROVED",
        statement="The exact optimum in the full uniform-sign class on F_3^5 is 31/90.",
    ),
    TheoremRecord(
        key="exchangeable_support_le2_f35",
        title="Exchangeable support-<=2 class on F_3^5",
        status="PROVED",
        statement="The exact optimum in the exchangeable support-<=2 class on F_3^5 is E_* ≈ 0.34421042513543912767.",
        notes=(
            "E_* is the unique root in (0.3442, 0.3443) of "
            "6720000 E^7 - 1096600000 E^6 + 5937209600 E^5 - 7442465200 E^4 + "
            "3638500832 E^3 - 667345588 E^2 - 3623728 E + 9535419 = 0."
        ),
    ),
    TheoremRecord(
        key="star_ansatz_f35",
        title="Full star ansatz on F_3^5",
        status="PROVED",
        statement="The exact optimum is 1478/4095 - sqrt(205)/819, attained at the explicit star law mu_dagger.",
        notes=(
            "mu_dagger = x_dagger δ_{e_1} + y_dagger δ_{2e_1} + q_dagger Σ_{j=2}^5 "
            "(δ_{e_j} + δ_{2e_j}) + rho_dagger Σ_{j=2}^5 (δ_{2e_1+e_j} + δ_{2e_1+2e_j}), "
            "with rho_dagger = (32 + sqrt(205))/2457, q_dagger = (787 - sqrt(205))/14742, "
            "x_dagger = (3935 - 5*sqrt(205))/14742, y_dagger = (2975 - 35*sqrt(205))/14742."
        ),
    ),
    TheoremRecord(
        key="distinguished_coordinate_extension_f35",
        title="One-distinguished-coordinate extension on F_3^5",
        status="PROVED",
        statement="After adding the missing star-pair orbits, the exact optimum remains 1478/4095 - sqrt(205)/819.",
    ),
    TheoremRecord(
        key="branch_closures_f35",
        title="Exact solved branch closures inside the current star / near-star analysis",
        status="PROVED",
        statement="The tau = 0, s = 1/3, region s >= 1/3, y = 0, x = y, tail-tail same-sign, and tail-tail mixed branches all close in favor of mu_dagger.",
        notes="These are frozen solved subbranches, not a proof of the full ambient optimum.",
    ),
    TheoremRecord(
        key="local_optimality_mu_dagger_support_le2",
        title="First-order local optimality of mu_dagger in the full support-<=2 simplex",
        status="COMPUTATION-SUPPORTED",
        statement="The theorem framework and formulas are exact, but the explicit subgradient witness / strict orbit gaps are not yet packaged here as a fully symbolic certificate.",
    ),
    TheoremRecord(
        key="full_ambient_optimum_f35",
        title="Full ambient optimum on F_3^5",
        status="OPEN",
        statement="The true full ambient optimum on F_3^5 remains open.",
    ),
    TheoremRecord(
        key="earlier_full_ambient_31_over_90",
        title="Earlier 31/90 full-ambient claim",
        status="WITHDRAWN",
        statement="The earlier claim that 31/90 was the full ambient value at (p, k) = (3, 5) is withdrawn.",
    ),
]


def records_by_status(status: str):
    return [record for record in LEDGER if record.status == status]
