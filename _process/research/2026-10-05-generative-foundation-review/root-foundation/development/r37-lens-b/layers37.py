#!/usr/bin/env python3
"""R37: R34's layers34.py with the ring read too. Since R35b the checker lists the instances and the
applications apart from CORE (`INSTANCES`, `APPLICATIONS`); the module table and the notes keep a row
for each, so the modules whose layers are computed are those three lists. R37 adds Becoming.Witnesses
(its row and note from its doc) and removes no module.

usage: python3 -B layers37.py [--list] [--write]   (as layers.py)"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('layers34', HERE.parent / 'r34-evaluative-chain' / 'layers34.py')
layers34 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers34)
layers = layers34.layers
graph = layers.graph


def core_list():
    src = (graph.PKG / 'check_becoming.py').read_text()
    out = []
    for name in ('CORE', 'INSTANCES', 'APPLICATIONS'):
        m = re.search(r'^' + name + r' = \[(.*?)\]\n', src, re.S | re.M)
        out += re.findall(r'"([^"]+)"', m.group(1))
    return out


graph.core_list = core_list

if __name__ == '__main__':
    layers.main()
