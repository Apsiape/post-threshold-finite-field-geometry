## Theorem ledger

This ledger is the authoritative status table for the frozen public repository.

## PROVED

1. **Odd-prime threshold theorem.** For every odd prime `p` and every `k >= 2`, the full ambient additive value equals `1/3` if and only if `k <= 3p/(p-1)`.
2. **Failure of the naive old hull.** The earlier naive old hull is false in the odd-prime anisotropic branch.
3. **Uniform-sign full ambient class on `F_3^5`.** Exact optimum: `31/90`.
4. **Exchangeable support-`<=2` class on `F_3^5`.** Exact optimum: `E_* ≈ 0.34421042513543912767`.
   - Exact definition: `E_*` is the unique root in `(0.3442, 0.3443)` of `6720000 E^7 - 1096600000 E^6 + 5937209600 E^5 - 7442465200 E^4 + 3638500832 E^3 - 667345588 E^2 - 3623728 E + 9535419 = 0`.
5. **Full star ansatz on `F_3^5`.** Exact optimum: `1478/4095 - sqrt(205)/819 ≈ 0.34344588392762350042`, attained at the explicit star law `mu_dagger`.
   - Exact law: `mu_dagger = x_dagger δ_{e_1} + y_dagger δ_{2e_1} + q_dagger Σ_{j=2}^5 (δ_{e_j} + δ_{2e_j}) + rho_dagger Σ_{j=2}^5 (δ_{2e_1+e_j} + δ_{2e_1+2e_j})`.
   - Parameters: `rho_dagger = (32 + sqrt(205))/2457 ≈ 0.01885137202412549986`, `q_dagger = (787 - sqrt(205))/14742 ≈ 0.05241366021820130558`, `x_dagger = (3935 - 5*sqrt(205))/14742 ≈ 0.26206830109100652789`, `y_dagger = (2975 - 35*sqrt(205))/14742 ≈ 0.16781144097037902860`.
6. **Enlarged one-distinguished-coordinate extension.** After adding the missing star-pair orbits, the exact optimum remains `1478/4095 - sqrt(205)/819`.
7. **Exact solved branch closures inside the current star / near-star analysis.**
   - `tau = 0` closes at `mu_dagger`.
   - `s = 1/3` closes at `mu_dagger`.
   - the region `s >= 1/3` closes at `mu_dagger`.
   - the `y = 0` branch does not beat `mu_dagger`.
   - the `x = y` line does not threaten `mu_dagger`.
   - the tail-tail same-sign deformation branch closes in favor of `mu_dagger`.
   - the tail-tail mixed deformation branch closes in favor of `mu_dagger`.

These branch closures are solved subfamilies only. They are **not** a proof of the full ambient optimum.

## COMPUTATION-SUPPORTED

1. **First-order local optimality of `mu_dagger` in the full support-`<=2` simplex.**
   - The theorem framework and formulas are exact.
   - The explicit subgradient witness / strict orbit gaps are presently computation-supported in this package.
2. **Any numerical optimization evidence over reduced live families** that has not yet been converted into a symbolic certificate remains computation-supported only.

## WITHDRAWN / CORRECTED

1. The earlier claim that `31/90` was the full ambient value at `(p, k) = (3, 5)` is **WITHDRAWN**.
2. The earlier claim that the exchangeable support-`<=2` value `E_*` might be the full support-`<=2` optimum is superseded.
3. Earlier closure attempts later corrected because of bookkeeping or derivation errors are preserved in `docs/WITHDRAWN_AND_CORRECTED_CLAIMS.md`.

## OPEN

1. The true full ambient optimum on `F_3^5`.
2. The remaining live frontier outside the closed one-distinguished-coordinate extension.
3. Whether support-`<=2` non-one-distinguished-coordinate laws can beat `mu_dagger`.
4. Whether support `3+` is needed for further improvement.
5. Broader post-threshold theory beyond the first solved regimes.
