"""One shared path-role classifier for the repository, driven by _process/research-config.json.

Roles:
- source:    imported originals (sources/); never edited, never moved.
- scratch:   working areas and tool caches (tmp/, work/, .claude/, .lake/, __pycache__ ...).
- history:   retired material: any path component named exactly `history`, plus the
             hash-addressed `_process/architecture/history/` store.
- evidence:  frozen run material: timestamped run folders (`*-checks/<UTC>/`, nanosecond run
             ids), `verification-history/`, `legacy-replays/`, snapshots, "before" copies, the
             move receipts (`move_receipts`), and the paths the config key `evidence_paths` names,
             each with its reason (frozen copies and hash-pinned inputs that keep their place).
- generated: pages written by `make research-render` (the generated manifest and record pages).
- live:      everything else; the files readers and sessions edit.

The order above is the precedence: a generated page inside a history root is history.
The rules come from the config key `path_roles`; DEFAULTS apply to keys it leaves out.
"""
from __future__ import annotations
from functools import lru_cache
import json
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / '_process/research-config.json'
ROLES = ('live', 'generated', 'evidence', 'history', 'source', 'scratch')

DEFAULTS = {
    'source_prefixes': ['sources/'],
    'scratch_prefixes': ['tmp/', 'work/', '.claude/', '.git/'],
    'scratch_components': ['.lake', '__pycache__', 'node_modules', '.venv', '.pytest_cache'],
    'history_components': ['history'],
    'history_prefixes': ['_process/architecture/history/'],
    'evidence_components': ['verification-history', 'legacy-replays', 'snapshots', 'source-snapshots', 'before'],
    # A UTC run folder (20261016T121942.123456Z, with suffixes such as -before), a numeric run
    # id, or a saved "before" copy (2026-10-06-before-axiom-removal, zero-axiom-classification-before).
    'evidence_component_patterns': [r'^\d{8}T\d{6}(\.\d+)?Z', r'^\d{10,}$', r'(^|-)before(-|$)'],
    # Saved copies by file name: README-BEFORE-RESULTS-CATALOGUE.md, before-00-RESEARCH.md,
    # immediate-before-01-RESEARCH.md.
    'evidence_name_patterns': [r'-BEFORE[-.]', r'^before-', r'(^|-)before-\d'],
}


def load_config(root: Path = ROOT) -> dict:
    try:
        return json.loads((root / '_process/research-config.json').read_text())
    except (OSError, ValueError):
        return {}


def posix(path) -> str:
    """A repository-relative POSIX path string without a leading './'."""
    text = str(PurePosixPath(str(path).replace('\\', '/')))
    return text[2:] if text.startswith('./') else text


class Classifier:
    def __init__(self, settings: dict | None = None, root: Path = ROOT, generated: set[str] | None = None):
        self.root = root
        self.settings = load_config(root) if settings is None else settings
        rules = dict(DEFAULTS)
        rules.update(self.settings.get('path_roles') or {})
        self.rules = rules
        self.component_patterns = [re.compile(p) for p in rules['evidence_component_patterns']]
        self.name_patterns = [re.compile(p) for p in rules['evidence_name_patterns']]
        # Move receipts record former paths on purpose; they are evidence, never rewritten.
        receipts = self.settings.get('move_receipts')
        self.evidence_prefixes = [receipts.rstrip('/') + '/'] if isinstance(receipts, str) and receipts.strip('/') else []
        # Named frozen paths: a key ending in '/' covers a directory, any other key one file.
        named = rules.get('evidence_paths') or {}
        self.evidence_files = {k for k in named if not k.endswith('/')}
        self.evidence_prefixes += [k for k in named if k.endswith('/')]
        self._generated = generated

    @property
    def generated(self) -> set[str]:
        if self._generated is None:
            found = set()
            manifest = self.settings.get('generated_manifest')
            if isinstance(manifest, str):
                try:
                    found |= set(json.loads((self.root / manifest).read_text()).get('files', {}))
                except (OSError, ValueError, AttributeError):
                    pass
            for directory in self.settings.get('record_directories', []):
                found |= {posix(p.relative_to(self.root)) for p in (self.root / directory).glob('*.md')}
            self._generated = found
        return self._generated

    def role(self, path) -> str:
        path = posix(path)
        parts = path.split('/')
        directories = parts[:-1]
        r = self.rules
        if any(path.startswith(p) for p in r['source_prefixes']):
            return 'source'
        if any(path.startswith(p) for p in r['scratch_prefixes']) or any(c in r['scratch_components'] for c in parts):
            return 'scratch'
        if any(c in r['history_components'] for c in directories) or any(path.startswith(p) for p in r['history_prefixes']):
            return 'history'
        if any(c in r['evidence_components'] or any(p.search(c) for p in self.component_patterns) for c in directories) \
                or any(p.search(parts[-1]) for p in self.name_patterns) or any(path.startswith(p) for p in self.evidence_prefixes) \
                or path in self.evidence_files:
            return 'evidence'
        if path in self.generated:
            return 'generated'
        return 'live'

    def is_live(self, path) -> bool:
        return self.role(path) == 'live'


@lru_cache(maxsize=1)
def default() -> Classifier:
    return Classifier()


def role(path) -> str:
    return default().role(path)


@lru_cache(maxsize=4096)
def glob_regex(pattern: str, flags: int = 0) -> re.Pattern:
    """Compile a repository glob: `**` spans directories, `*` and `?` stay within one."""
    out, i = '', 0
    while i < len(pattern):
        if pattern.startswith('**/', i):
            out += '(?:.*/)?'
            i += 3
        elif pattern.startswith('**', i):
            out += '.*'
            i += 2
        elif pattern[i] == '*':
            out += '[^/]*'
            i += 1
        elif pattern[i] == '?':
            out += '[^/]'
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(out + r'\Z', flags)


def matches(path: str, patterns, flags: int = 0) -> bool:
    path = posix(path)
    return any(glob_regex(p, flags).match(path) for p in patterns)
