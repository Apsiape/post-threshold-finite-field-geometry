## Proof note: threshold theorem

The threshold theorem is the global entry point of the package. The public proof note should emphasize the exact iff statement and the simple arithmetic consequence for the integer cutoff:

- `p = 3` gives cutoff `k <= 4`;
- every odd prime `p >= 5` gives cutoff `k <= 3`.

The scripts in this repository verify the cutoff formula and its integer consequences for sample odd primes, but the proof itself remains a mathematical argument rather than a computational derivation.
