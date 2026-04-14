from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import threshold_condition, threshold_max_integer


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


cases = {3: 4, 5: 3, 7: 3, 11: 3, 101: 3}
for p, cutoff in cases.items():
    require(threshold_max_integer(p) == cutoff, f"unexpected cutoff for p={p}")
    require(threshold_condition(p, cutoff), f"threshold should hold at cutoff for p={p}")
    require(not threshold_condition(p, cutoff + 1), f"threshold should fail above cutoff for p={p}")

print("PASS: odd-prime threshold helper reproduces the expected integer cutoffs.")
