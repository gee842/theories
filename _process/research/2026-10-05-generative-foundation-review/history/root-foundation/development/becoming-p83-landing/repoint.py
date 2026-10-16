#!/usr/bin/env python3
"""Re-point P83 records with the shared guarded landing helper.

Usage: python3 -B repoint.py ROOT [BASE]
Keeps unmatched drift untouched, updates periphery closure counts, and records the receipt transition
in history without changing documentary review times for unchanged claims.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, '-B', str(HERE.parent / 'becoming-landing-kit/repoint.py'),
                str(HERE), sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'HEAD'], check=True)
