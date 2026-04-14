from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import BRANCH_CLOSURE_KEYS
from post_threshold_geometry.theorem_ledger import records_by_status


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


proved = {record.key for record in records_by_status("PROVED")}
require("branch_closures_f35" in proved, "branch-closure theorem missing from ledger")
require(len(BRANCH_CLOSURE_KEYS) == 7, "expected seven frozen branch closures")

print("PASS: branch-closure ledger is present and lists seven exact solved subbranches.")
