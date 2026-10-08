#!/usr/bin/env python3
"""Compatibility entry point; implementation lives in tools/research/generative_chain.py."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.research.generative_chain import *
if __name__ == '__main__':
    raise SystemExit(main())
