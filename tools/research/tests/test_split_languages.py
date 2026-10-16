"""The language splitter: deterministic, anchor-keeping, and honest about Chinese-only content."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.research import split_languages as sl
from tools.research.reading_catalogue import anchors_from_text

SOURCE = '''---
title: x
---
# 生成之论 / The Theory

前言只有中文，没有英文对应的一段相当长的说明文字。

## 1. 生成：同一展开 / Becoming: one unfolding

生成是同一展开中的关系怎样形成。

Becoming is how relations form within one unfolding.

- 生生是方向。
- The object of G0 is 生生, the generation of life.

```lean
theorem x : True := trivial  -- 中文注释
```

[来源 / Source](a.md) · [Lean](b.lean)

| 层 / Layer | 内容 / Content |
|---|---|
| 逻辑 / Logic | 有限归纳 / Finite induction |

| 目标 | 现状 |
|---|---|
| 整体 | 开放 |

## 只有中文

中文小节。
'''


class SplitTests(unittest.TestCase):
    def setUp(self):
        self.s = sl.split(SOURCE, 'DOC.md')
        self.en, self.zh = '\n'.join(self.s.en), '\n'.join(self.s.zh)

    def test_headings_split_and_keep_the_original_anchor(self):
        self.assertIn('<a id="生成之论--the-theory"></a>\n# The Theory', self.en)
        self.assertIn('<a id="生成之论--the-theory"></a>\n# 生成之论', self.zh)
        self.assertIn('## 1. Becoming: one unfolding', self.en)  # the section number stays on both halves
        self.assertIn('## 1. 生成：同一展开', self.zh)
        original = anchors_from_text(SOURCE)
        self.assertLessEqual(original, anchors_from_text(self.en))
        self.assertLessEqual(original, anchors_from_text(self.zh))
        self.assertIn('<a id="只有中文"></a>', self.en)  # a Chinese-only heading keeps its anchor in English

    def test_paragraphs_and_items_go_by_script(self):
        self.assertIn('Becoming is how relations form', self.en)
        self.assertNotIn('生成是同一展开中的关系怎样形成', self.en)
        self.assertIn('生成是同一展开中的关系怎样形成', self.zh)
        self.assertNotIn('Becoming is how relations form', self.zh)
        self.assertIn('- The object of G0 is 生生, the generation of life.', self.en)  # quoting a Chinese term stays English
        self.assertNotIn('- 生生是方向。', self.en)

    def test_shared_blocks_go_to_both_and_labels_split(self):
        for out in (self.en, self.zh):
            self.assertIn('theorem x : True := trivial  -- 中文注释', out)
            self.assertTrue(out.startswith('---\ntitle: x\n---'))
        self.assertIn('[Source](a.md) · [Lean](b.lean)', self.en)
        self.assertIn('[来源](a.md) · [Lean](b.lean)', self.zh)

    def test_tables_split_by_cell_or_go_to_chinese(self):
        self.assertIn('| Logic | Finite induction |', self.en)
        self.assertIn('| 逻辑 | 有限归纳 |', self.zh)
        self.assertIn('<!-- zh-only table: see DOC.zh.md -->', self.en)
        self.assertIn('| 整体 | 开放 |', self.zh)
        self.assertNotIn('整体', self.en)

    def test_report_lists_chinese_without_english_counterpart(self):
        spans = self.s.zh_only_spans()
        firsts = [s['first_line'] for s in spans]
        self.assertTrue(any(f.startswith('前言只有中文') for f in firsts))
        self.assertTrue(any(f.startswith('| 目标') for f in firsts))
        self.assertTrue(any(f.startswith('中文小节') for f in firsts))
        self.assertFalse(any(f.startswith('生成是同一展开') for f in firsts))  # its English follows in the section

    def test_cli_is_deterministic_and_refuses_to_overwrite_its_input(self):
        with tempfile.TemporaryDirectory() as directory:
            d = Path(directory)
            (d / 'DOC.md').write_text(SOURCE)
            args = [str(d / 'DOC.md'), '--en', str(d / 'en.md'), '--zh', str(d / 'DOC.zh.md'), '--report', str(d / 'r.json')]
            sl.main(args)
            first = [(d / n).read_bytes() for n in ('en.md', 'DOC.zh.md', 'r.json')]
            sl.main(args)
            self.assertEqual(first, [(d / n).read_bytes() for n in ('en.md', 'DOC.zh.md', 'r.json')])
            self.assertEqual(json.loads(first[2])['tables']['zh_only'], 1)
            with self.assertRaises(SystemExit):
                sl.main([str(d / 'DOC.md'), '--en', str(d / 'DOC.md'), '--zh', str(d / 'z.md')])
            self.assertEqual((d / 'DOC.md').read_text(), SOURCE)


if __name__ == '__main__':
    unittest.main()
