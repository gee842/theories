"""Record-history compaction (R35, E3): the classifier keeps every note that says what the record says or
why it changed, and compaction stores the record's exact bytes before replacing the bookkeeping notes."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from tools.research import history_notes as h


def note(en):
    return {'en': en, 'zh': en}


class Classify(unittest.TestCase):
    def test_first_note_is_kept(self):
        self.assertEqual(h.classify(0, note('Rebound to the new receipt.')), 'first')

    def test_bookkeeping(self):
        for text in ('2026-10-11 P46: validation scope re-pointed to consolidated receipt 20261011T001147.906623Z. The claim is unchanged.',
                     '15 October 2026, landing P109: rebound to the new receipts and rehashed: BECOMING-RENEWAL-READING.md.',
                     '19 October 2026, Y3: BECOMING-RENEWAL-READING.md re-pointed after reading the change. The claim is unchanged.'):
            self.assertEqual(h.classify(3, note(text)), 'bookkeeping', text)

    def test_substantive_cue_keeps_a_rebinding_note(self):
        for text in ('Rebound to the new receipt; the statement becomes the law over every exchange.',
                     'Re-pointed; retitled "Ceasing needs arising".',
                     'Receipt updated and a counterexample added for infinitely many outcomes.',
                     'Rebound; status becomes superseded.'):
            self.assertEqual(h.classify(2, note(text)), 'substantive', text)

    def test_cue_inside_parentheses_of_another_file_is_not_substantive(self):
        text = ('Re-pointed after reading the change (THE-THEORY-OF-BECOMING.md: the statement becomes shorter). '
                'The claim is unchanged.')
        self.assertEqual(h.classify(2, note(text)), 'bookkeeping')

    def test_other_is_kept(self):
        self.assertEqual(h.classify(1, note('Joined to the spine as an instance of the census law.')), 'other')

    def test_condensing_note_is_never_condensed_again(self):
        made = h.condensing_note(4, '9 October 2026', '19 October 2026', 'x.json')
        self.assertEqual(h.classify(5, made), 'other')


class Compact(unittest.TestCase):
    def test_round_trip_keeps_every_byte_in_the_snapshot(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'demo.json'
            record = {'id': 'demo', 'schema_version': 2, 'history': [note('Created.'),
                                                note('9 October 2026: rebound to the new receipt. The claim is unchanged.'),
                                                note('The statement becomes the general law.'),
                                                note('19 October 2026: re-pointed after reading the change. The claim is unchanged.')]}
            raw = (json.dumps(record, ensure_ascii=False, indent=2) + '\n').encode()
            path.write_bytes(raw)
            stored = {}

            def snapshot(ident):
                data = path.read_bytes()
                target = root / 'snap' / (ident + '.json')
                target.parent.mkdir()
                target.write_bytes(data)
                stored['bytes'] = data
                return {'path': 'snap/demo.json', 'sha256': hashlib.sha256(data).hexdigest(), 'note': note('x')}

            dry = h.compact(root, [path], snapshot)
            self.assertEqual(path.read_bytes(), raw)
            self.assertEqual((dry['records_compacted'], dry['notes_condensed'], dry['notes_after']), (1, 2, 3))
            receipt = root / 'receipt.json'
            done = h.compact(root, [path], snapshot, apply=True, receipt=receipt)
            self.assertEqual(stored['bytes'], raw)
            after = json.loads(path.read_text())
            self.assertEqual([n['en'] for n in after['history'][:2]], ['Created.', 'The statement becomes the general law.'])
            self.assertIn('2 bookkeeping notes condensed from 9 October 2026 to 19 October 2026', after['history'][2]['en'])
            self.assertEqual(after['text_versions'][0]['path'], 'snap/demo.json')
            self.assertEqual(done['records'][0]['sha256_before'], hashlib.sha256(raw).hexdigest())
            self.assertTrue(receipt.is_file())
            again = h.compact(root, [path], snapshot)
            self.assertEqual(again['records_compacted'], 0)
            with self.assertRaises(ValueError):
                h.compact(root, [path], snapshot, apply=True, receipt=receipt)

    def test_schema_one_record_names_the_snapshot_without_text_versions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'old.json'
            path.write_text(json.dumps({'id': 'old', 'history': [note('Created.'), note('Rebound to the new receipt.')]}))
            h.compact(root, [path], lambda ident: {'path': 'snap/old.json', 'sha256': '0' * 64, 'note': note('x')}, apply=True)
            after = json.loads(path.read_text())
            self.assertNotIn('text_versions', after)
            self.assertIn('snap/old.json', after['history'][-1]['en'])


if __name__ == '__main__':
    unittest.main()
