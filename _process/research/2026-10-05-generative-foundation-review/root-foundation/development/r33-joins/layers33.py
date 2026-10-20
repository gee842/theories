#!/usr/bin/env python3
"""R33: R32's layers32.py with the two modules R33 joined into Becoming.LawAlongRun counted as gone.

usage: python3 -B layers33.py [--list] [--write]   (as layers.py)"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R32 = HERE.parent / 'r32-folds'
sys.path.insert(0, str(R32))
sys.path.insert(0, str(HERE.parent / 'r31-support'))

spec = importlib.util.spec_from_file_location('layers32', R32 / 'layers32.py')
layers32 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers32)
layers = layers32.layers
layers.GONE += ['Becoming.LawThroughCoupling', 'Becoming.LawThroughChangingCoupling']

if __name__ == '__main__':
    layers.main()
