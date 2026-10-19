#!/usr/bin/env python3
"""R32: R31's layers.py with the modules R32 folded counted as gone (their notes dropped).

usage: python3 -B layers32.py [--list] [--write]   (as layers.py)"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import fold  # noqa: E402

spec = importlib.util.spec_from_file_location('layers', HERE.parent / 'r31-support' / 'layers.py')
layers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers)
layers.GONE += ['Becoming.' + x for x, _ in fold.FOLDS]

if __name__ == '__main__':
    layers.main()
