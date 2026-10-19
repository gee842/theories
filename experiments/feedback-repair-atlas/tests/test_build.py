"""Check that the atlas refuses stale evidence instead of silently rebinding it."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('atlas_build', Path(__file__).parents[1] / 'build.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class EvidenceBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.here = self.root / 'experiments/atlas'
        (self.here / 'model').mkdir(parents=True)
        (self.here / 'src').mkdir()
        self.source = self.root / 'Example.lean'
        self.source.write_text('-- literal </script> must not end the containing script\n')
        h = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.here.joinpath('components.json').write_text(json.dumps({'components': [
            {'id': 'example', 'path': 'Example.lean', 'line': 1, 'end': 1, 'sha256': h}
        ]}))
        for receipt, verifier in [('verification.json', 'verify.py'),
                                  ('interaction-verification.json', 'verify_interaction.py'),
                                  ('gradual-verification.json', 'verify_gradual.py')]:
            script = self.here / 'model' / verifier
            script.write_text('# test fixture verifier\n')
            self.here.joinpath('model', receipt).write_text(json.dumps({
                'status': 'passed', 'axiom_dependencies': {}, 'checked_at_utc': 'fixture',
                'theorems': 1, 'declarations': 1,
                'verification_script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
                'source_sha256': {'Example.lean': h},
            }))
        (self.here / 'src/atlas.fragment.html').write_text('<script>const data=__RETRY_DATA__;</script>')
        (self.here / 'src/dynamics.js').write_text('// fixture dynamics\n')
        (self.here / 'src/shell.html').write_text('<main><!--__ATLAS_FRAGMENT__--></main>')
        old = builder.ROOT, builder.HERE
        self.addCleanup(lambda: self.restore(old))
        builder.ROOT, builder.HERE = self.root, self.here

    @staticmethod
    def restore(old):
        builder.ROOT, builder.HERE = old

    def test_build_is_deterministic_and_raw_code_cannot_close_the_script(self):
        first = builder.build()
        self.assertEqual(first, builder.build())
        self.assertIn(r'<\/script>', first)
        self.assertNotIn('literal </script>', first)

    def test_changed_component_source_is_rejected(self):
        self.source.write_text('-- changed after the recorded check\n')
        with self.assertRaisesRegex(ValueError, 'Component source changed'):
            builder.build()

    def test_changed_verifier_is_rejected(self):
        (self.here / 'model/verify_gradual.py').write_text('# modified verifier\n')
        with self.assertRaisesRegex(ValueError, 'Verifier changed'):
            builder.build()

    def test_transitive_source_drift_is_rejected(self):
        receipt = self.here / 'model/gradual-verification.json'
        content = json.loads(receipt.read_text())
        content['source_sha256']['Example.lean'] = '0' * 64
        receipt.write_text(json.dumps(content))
        with self.assertRaisesRegex(ValueError, 'Receipt source changed'):
            builder.build()

    def test_unexpected_axiom_report_is_rejected(self):
        receipt = self.here / 'model/gradual-verification.json'
        content = json.loads(receipt.read_text())
        content['axiom_dependencies'] = {'Example.claim': ['sorryAx']}
        receipt.write_text(json.dumps(content))
        with self.assertRaisesRegex(ValueError, 'Unverified application'):
            builder.build()


if __name__ == '__main__':
    unittest.main()
