import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.research import completion  # noqa: E402

LEAN = """namespace Becoming

variable {F : Type} (W : Web F)

/-- doc -/
theorem Web.base (h : W.Balances) : True := trivial

theorem Web.next (d : Decidable True) : True :=
  W.base trivial

namespace Inner
theorem deeper : True := Web.next (W := W) (isTrue trivial)
end Inner

end Becoming
"""


class ParserTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        path = Path(self.dir.name) / 'M.lean'
        path.write_text(LEAN)
        self.decls = {d['full']: d for d in completion.parse_module(path)}

    def tearDown(self):
        self.dir.cleanup()

    def test_full_names_statements_and_proofs(self):
        self.assertEqual(set(self.decls), {'Becoming.Web.base', 'Becoming.Web.next', 'Becoming.Inner.deeper'})
        self.assertIn('W.Balances', self.decls['Becoming.Web.base']['statement'])
        self.assertIn('W.base', self.decls['Becoming.Web.next']['proof'])

    def test_reading_takes_namespace_and_used_variables(self):
        text = completion.reading(self.decls['Becoming.Web.base'])
        self.assertIn('Web', text)
        self.assertIn('W : Web F', text)

    def test_references_resolve_by_namespace_and_field_notation(self):
        refs = completion._references(self.decls)
        self.assertEqual(refs('Becoming.Web.next'), frozenset({'Becoming.Web.base'}))
        self.assertEqual(refs('Becoming.Inner.deeper'), frozenset({'Becoming.Web.next'}))
        self.assertTrue(completion.reaches(self.decls, 'Becoming.Inner.deeper', 'Becoming.Web.base'))
        self.assertFalse(completion.reaches(self.decls, 'Becoming.Web.base', 'Becoming.Web.next'))


class RegisterTests(unittest.TestCase):
    def cov(self):
        return {'rows': [{'id': 'r', 'open_items': [1]}], 'open_register': {'classes': ['further proof', 'philosophical warrant']}}

    def test_open_register_classes_and_open_parts(self):
        chapter = ('### 8.1 Open items, ranked\n\n1. **A** (further proof; a remark). *Open:* x.\n'
                   '2. **B** (philosophical warrant, §8.5). No formal work.\n3. **A** (guess). x\n\n### 8.2 Next\n')
        findings, items = completion.k7(self.cov(), chapter)
        self.assertEqual([i['class'] for i in items], ['further proof', 'philosophical warrant', 'guess'])
        self.assertTrue(any('class "guess"' in f for f in findings))
        self.assertTrue(any('item 3 (A): no open part' in f for f in findings))
        self.assertTrue(any('"A" listed 2 times' in f for f in findings))

    def test_validation_reports_unknown_names_and_records(self):
        cov = json.loads((ROOT / completion.COVERAGE).read_text())
        cov['rows'][0]['declarations'] = cov['rows'][0]['declarations'] + ['Becoming.no_such_law']
        cov['rows'][0]['records'] = cov['rows'][0]['records'] + ['no-such-record']
        decls = {n: {} for r in cov['rows'] for n in r['declarations'] if n != 'Becoming.no_such_law'}
        decls.update({w: {} for p in cov['premises']['items'] for w in p['witnesses']})
        decls.update({n: {} for n in cov['ethics_chain']['steps']})
        decls.update({x[k]: {} for x in cov['representation']['natural_number_laws'] for k in ('law', 'dense') if x.get(k)})
        records = {r for row in cov['rows'] for r in row['records']} - {'no-such-record'}
        errors = completion.validate(cov, decls, records)
        self.assertEqual(len(errors), 2, errors)


class RepositoryTests(unittest.TestCase):
    def test_the_coverage_file_validates_against_the_core(self):
        result = completion.evaluate()
        self.assertEqual(result['errors'], [])
        self.assertEqual(set(result['met']), {'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7'})


if __name__ == '__main__':
    unittest.main()
