import sys
from pathlib import Path

# Add domain root to sys.path so `from src.xxx import yyy` works in all tests.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
