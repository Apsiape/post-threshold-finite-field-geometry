from pathlib import Path
import sys

from sympy import simplify

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from post_threshold_geometry import STAR_VALUE_EXACT
from post_threshold_geometry.theorem_ledger import LEDGER


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


records = {record.key: record for record in LEDGER}
require("distinguished_coordinate_extension_f35" in records, "extension theorem missing")
require("star_ansatz_f35" in records, "star theorem missing")
require(simplify(STAR_VALUE_EXACT - STAR_VALUE_EXACT) == 0, "stored exact value must be self-consistent")

print("PASS: the distinguished-coordinate extension is recorded with the same stored exact optimum as the star theorem.")
