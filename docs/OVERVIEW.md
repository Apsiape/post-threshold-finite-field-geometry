## Overview

This repository freezes the current theorem package for the odd-prime / post-threshold finite-field program, with emphasis on the exact solved structural families around the `F_3^5` frontier.

## Research question

The central question is how local structure, threshold behavior, and post-threshold optimization geometry interact in finite-field additive settings. The current package isolates the first exact regimes, the first corrected failures of an earlier hull picture, and the first exact post-threshold structural closures.

## What this repository is

This is a publication-facing mathematical artifact. It is intended to be readable as a theorem ledger, a correction log, and a reproducibility bundle.

It is **not** a claim that the whole `F_3^5` ambient problem is solved, and it is **not** a claim that all current computational evidence has already been converted into symbolic proof certificates.

## Scientific positioning

The correct positioning is narrow and serious.

- The work is mathematics first.
- The broadest philosophical metathesis is **not** claimed as proved.
- The current theorem package does support a sharpened operational lesson: locally natural or locally stable structure need not be globally privileged, and leaving a stable local rendering may require qualitatively different geometry rather than a small perturbation.

## Frozen proved package

The repository records the following as **PROVED**:

1. the odd-prime threshold theorem;
2. falsification of the naive old hull in the odd-prime anisotropic branch;
3. exact solved subclass optima on `F_3^5`;
4. exact closure of the full star ansatz;
5. exact closure of the enlarged one-distinguished-coordinate extension;
6. exact closure of the currently solved star / near-star subbranches.

The package now also records the load-bearing exact source data for the frozen solved families: the defining degree-seven polynomial for `E_*` and the explicit one-distinguished-coordinate parameterization of `mu_dagger`.

## Computation-supported and open frontier

The first-order local optimality story for `mu_dagger` in the full support-`<=2` simplex remains **COMPUTATION-SUPPORTED** in this package, because the explicit symbolic certificate is not yet transcribed here.

The true full ambient optimum on `F_3^5` remains **OPEN**.

## Repository guide

- `docs/MAIN_RESULTS.md` presents the theorem package in theorem-style prose.
- `docs/THEOREM_LEDGER.md` gives the frozen status ledger.
- `docs/WITHDRAWN_AND_CORRECTED_CLAIMS.md` records withdrawn or superseded statements.
- `docs/PROOF_GUIDE.md` explains the proof architecture.
- `notes/` and `proofs/` retain shorter research-note summaries.
- `scripts/` and `tests/` provide reproducibility support with Python and SymPy.
