# post-threshold-finite-field-geometry

A frozen public research repository for the odd-prime, post-threshold finite-field program. The aim is to package the current theorem ledger cleanly for GitHub publication and Zenodo archiving, with strict separation between **PROVED**, **COMPUTATION-SUPPORTED**, **OPEN**, and **WITHDRAWN** statements.

## Scope

This repository records a milestone in a theorem program on local-vs-global non-gluing, threshold rigidity, and post-threshold optimization geometry over finite fields. It is a mathematics-first artifact. Any broader significance is stated cautiously: the results support an operational lesson that locally natural or locally stable structure need not be globally privileged, and escaping a stable local rendering may require qualitatively different geometry rather than a small perturbation.

## Status at a glance

- **PROVED:** the odd-prime threshold theorem: the full ambient additive value equals `1/3` iff `k <= 3p/(p-1)` for every odd prime `p` and every `k >= 2`.
- **PROVED:** the naive old hull is false in the odd-prime anisotropic branch.
- **PROVED:** on `F_3^5`, the exact optimum in the full uniform-sign ambient class is `31/90`.
- **PROVED:** on `F_3^5`, the exact optimum in the exchangeable support-`<=2` class is `E_* ≈ 0.34421042513543912767`.
- **PROVED:** on `F_3^5`, the full star ansatz has exact optimum `1478/4095 - sqrt(205)/819 ≈ 0.34344588392762350042`, attained at the explicit star law `mu_dagger`.
- **PROVED:** the enlarged one-distinguished-coordinate extension, including the previously missing star-pair orbits, has the same exact optimum as the star ansatz.
- **PROVED:** the currently closed exact subbranches in the star / near-star analysis all close in favor of `mu_dagger`; see `docs/THEOREM_LEDGER.md`.
- **COMPUTATION-SUPPORTED:** first-order local optimality of `mu_dagger` in the full support-`<=2` simplex.
- **OPEN:** the true full ambient optimum on `F_3^5`.

## What is proved

The current frozen theorem package consists of:

1. the threshold theorem for all odd primes;
2. falsification of the earlier naive odd-prime anisotropic hull picture;
3. exact solved subclass optima on `F_3^5`;
4. exact closure of the full star ansatz on `F_3^5`;
5. exact closure of the enlarged one-distinguished-coordinate extension;
6. exact solved branch closures inside the current star / near-star analysis.

See `docs/MAIN_RESULTS.md` for theorem-style statements and `docs/THEOREM_LEDGER.md` for status labels.

## Exact frozen definitions

- **Exchangeable support-`<=2` constant.** `E_*` is the unique root in `(0.3442, 0.3443)` of
  `6720000 E^7 - 1096600000 E^6 + 5937209600 E^5 - 7442465200 E^4 + 3638500832 E^3 - 667345588 E^2 - 3623728 E + 9535419 = 0`.
- **Star optimizer.**
  `mu_dagger = x_dagger δ_{e_1} + y_dagger δ_{2e_1} + q_dagger Σ_{j=2}^5 (δ_{e_j} + δ_{2e_j}) + rho_dagger Σ_{j=2}^5 (δ_{2e_1+e_j} + δ_{2e_1+2e_j})`,
  where
  `rho_dagger = (32 + sqrt(205))/2457 ≈ 0.01885137202412549986`,
  `q_dagger = (787 - sqrt(205))/14742 ≈ 0.05241366021820130558`,
  `x_dagger = (3935 - 5*sqrt(205))/14742 ≈ 0.26206830109100652789`,
  `y_dagger = (2975 - 35*sqrt(205))/14742 ≈ 0.16781144097037902860`,
  and `epsilon_dagger = 1478/4095 - sqrt(205)/819 ≈ 0.34344588392762350042`.

## What remains open

- the full ambient optimum on `F_3^5`;
- whether support-`<=2` laws outside the closed one-distinguished-coordinate extension can beat `mu_dagger`;
- whether support `>=3` is genuinely needed for further improvement;
- broader post-threshold structure beyond the first solved regimes.

See `docs/OPEN_PROBLEMS.md`.

## Terminology

- **Threshold:** the exact odd-prime boundary for when the full ambient additive value is still `1/3`.
- **Uniform-sign class:** the `F_3^5` ambient class where the active anisotropic mass lies in a single sign pattern.
- **Exchangeable support-`<=2` class:** the support-`<=2` subclass invariant under coordinate permutations.
- **Star ansatz:** the explicit one-center star family on `F_3^5` whose exact optimum is attained at `mu_dagger`.
- **One-distinguished-coordinate extension:** the enlargement of the star ansatz obtained by allowing the missing star-pair orbit types while keeping one coordinate distinguished.

## Reproducibility

The repository includes checked-in Python and SymPy scripts under `scripts/` plus lightweight tests under `tests/`.

Suggested workflow:

1. create a virtual environment;
2. install the package and development extras;
3. run the verification scripts;
4. run `pytest`.

Detailed instructions are in `docs/REPRODUCIBILITY.md`.

## How to archive with Zenodo

This repository includes `CITATION.cff` and `.zenodo.json`. The GitHub-to-Zenodo connection and release creation are manual steps. See `docs/ZENODO_RELEASE_INSTRUCTIONS.md` for the exact sequence.

## Repository map

- `docs/` — public-facing overview, theorem ledger, main results, proof guide, open problems, correction log, reproducibility, and Zenodo instructions.
- `notes/` — concise research-note style summaries of the frozen solved components.
- `proofs/` — proof architecture notes for the proved pieces.
- `scripts/` — SymPy-based checks for the `E_*` polynomial, the `mu_dagger` mass identities, stored exact constants, and ledger consistency.
- `src/post_threshold_geometry/` — reusable constants, formulas, and theorem ledger data.
- `tests/` — sanity checks for constants and symbolic relations.

## Integrity note

This repository is deliberately conservative. It does **not** claim that the full ambient optimum on `F_3^5` is solved, and it does **not** upgrade computation-supported local optimality evidence to a theorem. Withdrawn and corrected claims are documented explicitly in `docs/WITHDRAWN_AND_CORRECTED_CLAIMS.md`.
