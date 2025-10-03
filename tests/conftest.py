import sys
from pathlib import Path

# Ensure repo `src/` is on sys.path for test imports
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
