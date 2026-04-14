## Main results

## Theorem 1 — odd-prime threshold theorem

**Status: PROVED.** For every odd prime `p` and every integer `k >= 2`, the full ambient additive value equals `1/3` if and only if

`k <= 3p/(p - 1)`.

### Corollary 1.1

For `p = 3`, the threshold region is `k <= 4`. For every odd prime `p >= 5`, the threshold region is `k <= 3`.

## Proposition 2 — failure of the naive odd-prime anisotropic hull

**Status: PROVED.** The earlier naive old hull is false in the odd-prime anisotropic branch. The threshold theorem therefore does not extend by the older hull picture in the form previously suggested.

## Proposition 3 — exact solved subclass optima on `F_3^5`

**Status: PROVED.** The following exact subclass optima are part of the frozen package.

1. In the full uniform-sign ambient class, the optimum is `31/90`.
2. In the exchangeable support-`<=2` class, the optimum is `E_* ≈ 0.34421042513543912767`.
   Here `E_*` is the unique root in `(0.3442, 0.3443)` of `6720000 E^7 - 1096600000 E^6 + 5937209600 E^5 - 7442465200 E^4 + 3638500832 E^3 - 667345588 E^2 - 3623728 E + 9535419 = 0`.
3. In the full star ansatz, the optimum is `1478/4095 - sqrt(205)/819`.

## Theorem 4 — exact closure of the full star ansatz

**Status: PROVED.** On `F_3^5`, the full star ansatz has exact optimum

`1478/4095 - sqrt(205)/819 ≈ 0.34344588392762350042`,

attained at the explicit star law `mu_dagger`.

The law is

`mu_dagger = x_dagger δ_{e_1} + y_dagger δ_{2e_1} + q_dagger Σ_{j=2}^5 (δ_{e_j} + δ_{2e_j}) + rho_dagger Σ_{j=2}^5 (δ_{2e_1+e_j} + δ_{2e_1+2e_j})`,

with exact parameters

`rho_dagger = (32 + sqrt(205))/2457 ≈ 0.01885137202412549986`,
`q_dagger = (787 - sqrt(205))/14742 ≈ 0.05241366021820130558`,
`x_dagger = (3935 - 5*sqrt(205))/14742 ≈ 0.26206830109100652789`,
`y_dagger = (2975 - 35*sqrt(205))/14742 ≈ 0.16781144097037902860`.

## Theorem 5 — exact closure of the enlarged one-distinguished-coordinate extension

**Status: PROVED.** After adding the previously missing star-pair orbit types, the exact optimum remains the same star value

`1478/4095 - sqrt(205)/819`.

This theorem closes the enlarged one-distinguished-coordinate family, but it does not close the full ambient problem.

## Proposition 6 — exact solved branch closures

**Status: PROVED.** The following solved subbranches close in favor of `mu_dagger`:

- `tau = 0`;
- `s = 1/3`;
- the region `s >= 1/3`;
- `y = 0`;
- the `x = y` line;
- tail-tail same-sign deformations;
- tail-tail mixed deformations.

These are exact subfamily closures only.

## Frontier statement

**Status: OPEN.** The true full ambient optimum on `F_3^5` remains open. The currently live frontier lies outside the closed one-distinguished-coordinate extension, and it remains open whether non-one-distinguished-coordinate support-`<=2` laws or support `3+` are needed for further improvement.
