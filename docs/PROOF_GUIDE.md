## Proof guide

This guide explains the architecture of the current theorem package. It is explanatory rather than fully formal.

## 1. Threshold phase

The first phase identifies the exact odd-prime threshold for when the full ambient additive value remains `1/3`. The statement is clean and global: for odd prime `p`, the threshold is exactly `k <= 3p/(p-1)`.

## 2. Falsification of the old hull picture

The next phase records that the earlier naive odd-prime anisotropic hull is false. This matters structurally: the post-threshold regime cannot be organized by that older hull model.

## 3. Exact solved subclasses on `F_3^5`

The program then isolates exact structural families that can be closed completely.

- the uniform-sign class closes exactly at `31/90`;
- the exchangeable support-`<=2` class closes exactly at `E_*`;
- the star family closes exactly at the `mu_dagger` value.

These solved subclasses are evidence of genuine post-threshold structure, not a substitute for the unsolved ambient problem.

## 4. Emergence of phase steering

The solved star and near-star analyses show that the post-threshold geometry is not exhausted by naively symmetric continuation from threshold behavior. Structural steering inside constrained families becomes decisive.

## 5. Star optimizer and exact closure

The star phase isolates an explicit optimizer `mu_dagger` and shows that the full star ansatz closes exactly at

`1478/4095 - sqrt(205)/819`.

The repository records the theorem, value, and explicit one-distinguished-coordinate orbit weights for `mu_dagger`.

## 6. Enlarged one-distinguished-coordinate closure

Adding the missing star-pair orbit types produces a stricter test of the star picture. The exact optimum nevertheless stays at the same star value. This is one of the central frozen theorems of the package.

## 7. Solved branch closures

The currently solved subbranches — including `tau = 0`, `s = 1/3`, `s >= 1/3`, `y = 0`, `x = y`, and the two tail-tail deformation branches — all close in favor of `mu_dagger`.

These closures are exact, but they are branch closures, not a theorem for the full ambient frontier.

## 8. Remaining frontier

What remains live is the part of the support-`<=2` and higher-support landscape not captured by the one-distinguished-coordinate closure. The present package therefore ends with a genuine open frontier rather than an overstated closure claim.
