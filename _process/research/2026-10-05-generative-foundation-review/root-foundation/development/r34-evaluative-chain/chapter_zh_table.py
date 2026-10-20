#!/usr/bin/env python3
"""R34: R33's chapter_zh_table.py (the Chinese chapter's §9 module table takes the receipt's theorem counts and
the computed layers), with a row for Becoming.Direction, which R34 added.
usage: python3 -B chapter_zh_table.py RECEIPT_ID"""
import importlib.util
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('layers34', HERE / 'layers34.py')
l34 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(l34)
sys.modules['layers'] = l34.layers
l34.layers.NOTES['Becoming.Direction'] = {
    'after': 'Becoming.FrontierFrames',
    'zh': '网之动作上的方向（除各定理所写者不加前提）：动作的结果上 C 读作扩大（`Direction.extension_iff_widens`）；在 J1/J2（`Priority`）之下被选的动作保持基本接纳（`Direction.chosen_keeps_basic`、`Direction.kept_required`），被扩大的动作在扩大是否增加基本接纳可判定之处不被选（`Direction.narrowed_not_chosen`）；区分两个动作的接纳在行动者耦合闭包之外，只经耦合入它的组被选择（`Direction.widening_selected_by_pool`）；`Clearing.direction` 是实例',
    'en': '',
    'note': [],
}
runpy.run_path(str(HERE.parent / 'r31-support' / 'chapter_zh_table.py'), run_name='__main__')
