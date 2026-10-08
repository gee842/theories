#!/usr/bin/env python3
"""Compatibility test entry point for the shared research infrastructure."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from tools.research.tests.test_registry import RegistryTests
if __name__ == '__main__':
    unittest.main()
