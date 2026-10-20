"""Law families (R35, E7): the check of data/law-families.json and the family line on a member's page."""
import unittest
from unittest.mock import patch

from tools.research import registry

FAMILY = {'id': 'f', 'title': {'en': 'F', 'zh': 'F'}, 'statement': {'en': 'One law.', 'zh': '一条规律。'},
          'lead': 'a', 'members': ['a', 'b']}


class LawFamilies(unittest.TestCase):
    def test_the_repository_file_is_consistent(self):
        records, _ = registry.load_records()
        self.assertEqual(registry.law_family_errors(records), [])

    def test_errors(self):
        records = [{'id': 'a'}, {'id': 'b'}]
        bad = [dict(FAMILY, lead='c'), dict(FAMILY, id='g', members=['a', 'x'], lead='a')]
        with patch.object(registry, 'law_families', return_value=bad):
            errors = registry.law_family_errors(records)
        self.assertIn('law family f: the lead must be a member', errors)
        self.assertIn('law family g: unknown record x', errors)
        self.assertIn('law family g: a is already in law family f', errors)

    def test_line(self):
        link = lambda ident: f'[{ident}]({ident}.md)'
        lead = registry.law_family_lines({'id': 'a', '_law_family': FAMILY}, link)[1]
        member = registry.law_family_lines({'id': 'b', '_law_family': FAMILY}, link)[1]
        self.assertIn('(lead: this record)', lead)
        self.assertIn('Members: [b](b.md).', lead)
        self.assertIn('(lead: [a](a.md))', member)
        self.assertEqual(registry.law_family_lines({'id': 'c'}, link), [])


if __name__ == '__main__':
    unittest.main()
