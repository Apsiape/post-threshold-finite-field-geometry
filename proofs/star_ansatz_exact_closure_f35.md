## Proof note: exact closure of the star ansatz on F_3^5

The star theorem closes the full star ansatz exactly at

`1478/4095 - sqrt(205)/819 ≈ 0.34344588392762350042`.

The optimizer is the explicit star law

`mu_dagger = x_dagger δ_{e_1} + y_dagger δ_{2e_1} + q_dagger Σ_{j=2}^5 (δ_{e_j} + δ_{2e_j}) + rho_dagger Σ_{j=2}^5 (δ_{2e_1+e_j} + δ_{2e_1+2e_j})`,

with `rho_dagger = (32 + sqrt(205))/2457 ≈ 0.01885137202412549986`, `q_dagger = (787 - sqrt(205))/14742 ≈ 0.05241366021820130558`, `x_dagger = (3935 - 5*sqrt(205))/14742 ≈ 0.26206830109100652789`, and `y_dagger = (2975 - 35*sqrt(205))/14742 ≈ 0.16781144097037902860`.

This theorem is distinct from, and weaker than, a closure of the full ambient problem.
