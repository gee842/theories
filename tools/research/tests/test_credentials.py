import hashlib
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.research import research


class CredentialTests(unittest.TestCase):
    def test_reports_hashes_only_and_respects_the_allowlist(self):
        # Built at run time so this file never contains a matching credential itself.
        revoked = 'sk-or-v1-' + 'ab' * 32
        live = 'gh' + 'p_' + 'A1' * 18
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'notes.md').write_text(f'old key {revoked}\nanother {live}\nplain sk-ant- prefix only\n')
            (root / 'untracked.md').write_text(live + '\n')
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            subprocess.run(['git', 'add', 'notes.md'], cwd=root, check=True)
            digest = hashlib.sha256(revoked.encode()).hexdigest()
            result = research.secrets(root, allowlist=[{'sha256': digest, 'note': 'revoked'}])
            self.assertEqual(result['allowlisted'], 1)
            self.assertEqual([(f['kind'], f['path'], f['line']) for f in result['findings']], [('github', 'notes.md', 2)])
            self.assertEqual(result['findings'][0]['sha256'], hashlib.sha256(live.encode()).hexdigest())
            self.assertNotIn(live, repr(result))
            self.assertNotIn(revoked, repr(result))

    def test_every_kind_is_recognised(self):
        samples = {
            'openrouter': 'sk-or-v1-' + '0f' * 32, 'anthropic': 'sk-ant-' + 'api03-' + 'x' * 30,
            'openai': 'sk-proj-' + 'Y' * 30, 'github': 'github_' + 'pat_' + 'Z' * 30,
            'aws': 'AKIA' + 'ABCDEFGHIJKLMNOP', 'google': 'AIza' + 'b' * 35, 'slack': 'xo' + 'xb-' + '1234567890ab',
            'huggingface': 'hf_' + 'Q' * 34, 'private-key': '-----BEGIN ' + 'RSA PRIVATE KEY-----',
        }
        import re
        for kind, sample in samples.items():
            self.assertTrue(re.search(research.SECRET_PATTERNS[kind], sample), kind)
            self.assertTrue(any(p in sample for p in research.SECRET_PREFIXES), kind)


if __name__ == '__main__':
    unittest.main()
