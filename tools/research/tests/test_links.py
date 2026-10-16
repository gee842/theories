import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.research import moves, paths


class AnchorTests(unittest.TestCase):
    def test_github_anchor_rules(self):
        self.assertEqual(moves.github_slug('9. 形式脊柱 / The formal spine'), '9-形式脊柱--the-formal-spine')
        self.assertEqual(moves.github_slug('落地队列 / Landing queue'), '落地队列--landing-queue')
        self.assertEqual(moves.github_slug('What `change_readings` says: (a) *new*'), 'what-change_readings-says-a-new')
        self.assertEqual(moves.github_slug('“生生”与‘生成’——关系'), '生生与生成关系')
        self.assertEqual(moves.github_slug('[Link](x.md) and **bold**'), 'link-and-bold')

    def test_anchors_cover_duplicates_setext_and_explicit_ids(self):
        body = ('---\ntitle: x\n---\n# Same\n\n## Same\n\nSetext 标题\n---\n\n<a id="old-anchor"></a>\n'
                '<a name="named"></a>\n```\n# Not a heading\n<a id="in-code"></a>\n```\n')
        found = moves.anchors(body)
        self.assertTrue({'same', 'same-1', 'setext-标题', 'old-anchor', 'named'} <= found, found)
        self.assertNotIn('not-a-heading', found)
        self.assertNotIn('in-code', found)
        self.assertNotIn('title-x', found)

    def test_links_skip_code_footnotes_and_external(self):
        body = ('[a](a.md) `[b](b.md)` [c](<c d.md#x> "t") [e](https://example.org)\n'
                '[^note]: **Proved**\n[ref]: r.md\n<a href="h.md">h</a>\n```\n[f](f.md)\n```\n')
        targets = [raw for _s, _e, raw in moves.links(body)]
        self.assertEqual(targets, ['a.md', '<c d.md#x>', 'https://example.org', 'r.md', 'h.md'])
        self.assertIsNone(moves.split_target('https://example.org'))
        self.assertEqual(moves.split_target('<c d.md#x>'), ('c d.md', '', 'x'))
        self.assertEqual(moves.resolve('a/b/C.md', '../D.md'), 'a/D.md')
        self.assertIsNone(moves.resolve('a/C.md', '../../D.md'))


class LinkCheckTests(unittest.TestCase):
    def test_reports_broken_live_links_only(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            files = {
                'docs/A.md': '# A\n[ok](B.md#范围--scope) [bad](missing.md) [anchor](B.md#nope) [self](#a) [dir](../docs/)\n',
                'docs/B.md': '# 范围 / Scope\n',
                'docs/history/OLD.md': '[bad](gone.md)\n',
                'sources/S.md': '[bad](gone.md)\n',
                'runs/20261016T121942.123456Z/R.md': '[bad](gone.md)\n',
            }
            for name, body in files.items():
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text(body)
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            subprocess.run(['git', 'add', '-A'], cwd=root, check=True)
            result = moves.check_links(root, classifier=paths.Classifier(settings={}, root=root, generated=set()))
            self.assertEqual(result['broken'], 2, result['list'])
            self.assertEqual({b['target'] for b in result['list']}, {'missing.md', 'B.md#nope'})
            self.assertEqual(result['broken_by_kind'], {'missing-anchor': 1, 'missing-path': 1})
            self.assertEqual(result['by_directory'], {'docs': 2})
            limited = moves.check_links(root, only=['docs/B.md'], classifier=paths.Classifier(settings={}, root=root, generated=set()))
            self.assertEqual(limited['broken'], 0)


if __name__ == '__main__':
    unittest.main()
