"""Record id renames (R35, E4): rewriting, refusals, former ids and redirect pages."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.research import registry, rename_ids


class Rewrite(unittest.TestCase):
    def test_mentions_are_whole_ids_outside_link_targets(self):
        text = ('See `old-id` and [old-id](../records/old-id.md#old-id); old-id-two and wisdom-old-id stay.')
        new, n = rename_ids.mention_rewrite(text, [('old-id', 'new-id')], rename_ids.moves.link_spans(text))
        self.assertEqual(new, 'See `new-id` and [new-id](../records/old-id.md#old-id); old-id-two and wisdom-old-id stay.')
        self.assertEqual(n, 2)

    def test_json_tokens_only(self):
        text = json.dumps({'id': 'x', 'dependencies': [{'id': 'old-id'}], 'note': 'old-id in prose'}, indent=2)
        new, n = rename_ids.json_rewrite(text, [('old-id', 'new-id')])
        self.assertEqual(n, 1)
        self.assertEqual(json.loads(new)['dependencies'][0]['id'], 'new-id')
        self.assertEqual(json.loads(new)['note'], 'old-id in prose')


class Refusals(unittest.TestCase):
    def plan(self, rows):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / 'plan.tsv'
        path.write_text('old_id\tnew_id\treason\n' + ''.join('\t'.join(r) + '\n' for r in rows))
        return str(path)

    def test_collision_unknown_and_chain(self):
        result = rename_ids.run(self.plan([('census-balance', 'laws-of-one-step', 'collision'),
                                           ('no-such-record', 'something-new', 'unknown'),
                                           ('market-partial-correction-boundary', 'market-partial-rejoining-boundary', 'chain')]))
        errors = '\n'.join(result['errors'])
        self.assertIn('laws-of-one-step is a record or a former id', errors)
        self.assertIn('unknown record no-such-record', errors)
        self.assertIn("market-partial-correction-boundary is named in the generativity chain's data", errors)

    def test_former_id_is_taken(self):
        records, _ = registry.load_records()
        former = next((f for r in records for f in r.get('former_ids', [])), None)
        if former is None:
            self.skipTest('no former id in the registry')
        result = rename_ids.run(self.plan([('census-balance', former, 'taken')]))
        self.assertIn(f'{former} is a record or a former id', '\n'.join(result['errors']))


class FormerIds(unittest.TestCase):
    def test_redirect_page_and_orphan_acceptance(self):
        records, _ = registry.load_records()
        renamed = [r for r in records if r.get('former_ids')]
        if not renamed:
            self.skipTest('no renamed record')
        pages = registry.redirect_pages(records)
        r = renamed[0]
        page = registry.record_path(r).with_name(r['former_ids'][0] + '.md')
        self.assertIn(f'({r["id"]}.md)', pages[page])
        self.assertEqual(registry.orphan_pages(records), [])

    def test_former_id_may_not_be_live(self):
        records, _ = registry.load_records()
        a, b = (dict(r) for r in records[:2])
        a['former_ids'] = [b['id']]
        errors, _ = registry.validate([a, b])
        self.assertTrue(any(f'former id {b["id"]} is a live record id' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
