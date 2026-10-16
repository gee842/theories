#!/usr/bin/env python3
"""Apply P58c's exact identifier map to the current inventory classifier.

Usage: python3 -B inventory_names.py ROOT
Keeps every classification and newly added category; never copies an older tool.
This is normally a no-op. The inventory itself is regenerated afterward.
"""
from pathlib import Path
import sys

import p58c_names as names

root = Path(sys.argv[1]).resolve()
path = root / '_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.py'
before = path.read_text()
after = names.rename(before)
assert not names.old_left(after)
if after != before:
    path.write_text(after)
print('inventory classifier: exact identifiers updated' if after != before else 'inventory classifier: already current')
