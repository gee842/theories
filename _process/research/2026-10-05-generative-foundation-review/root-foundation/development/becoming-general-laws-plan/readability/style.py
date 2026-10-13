"""Readability lint for canonical records (prototype).

Reports, never rewrites. For schema_version 1 records every finding is a warning;
for schema_version 2 records the rules marked ERROR fail the check. The lint
judges form only (length, process narration, repeated boilerplate); it never
judges whether a boundary is substantive -- that stays an author's reading.
"""
from __future__ import annotations
import re

# Per-language caps: (en chars, zh chars). zh/en length ratio in current records:
# median 0.36, p95 0.50, so zh caps are about half the English cap.
CAPS_V1 = {'title': (120, 60), 'claim': (1500, 700), 'limitations': (800, 350),
           'validation_scope': (800, 350), 'correspondence': (1200, 500), 'next_delta': (400, 180)}
CAPS_V2 = {'title': (100, 40), 'statement': (300, 150), 'claim': (1500, 700),
           'validation_scope': (600, 260), 'correspondence': (1200, 500), 'next_delta': (400, 180)}
# Hard caps only on the reading surface; elsewhere a cap warns, so it never forces a substantive boundary out.
HARD_CAPS = {'title', 'statement', 'validation_scope', 'next_delta'}
ITEM_CAPS_V2 = {'does_not_show': (240, 110, 8), 'not_required': (200, 90, 6), 'progress': (240, 110, 16),
                'laws': (420, 190, 40), 'hypotheses': (420, 190, 9)}

PROCESS = [
    ('receipt-timestamp', re.compile(r'\b\d{8}T\d{6}(?:\.\d+)?Z\b')),
    ('round-number', re.compile(r'(?<![A-Za-z0-9_.])P\d{2,3}[a-z]?(?![A-Za-z0-9_])')),
    ('section-reference', re.compile(r'\bSections? \d+|§+\s?\d+|第\s?\d+\s?节')),
    ('date', re.compile(r'\b20\d\d-\d\d-\d\d\b')),
    ('round-narration', re.compile(r'\b(?:this|the present|each) (?:round|session)\b|\bthis record (?:adds|registers|receives|records)\b|\bhas landed\b|\bCodex\b|本轮|本次|已落地', re.I)),
    ('session-id', re.compile(r'\[[0-9a-f]{6}\]')),
]
EVIDENCE = re.compile(r'\bno new (?:theorem|Lean|empirical|experiment|independent|mathemat)|\bnot recounted\b|'
                      r'\bno (?:new )?independent (?:acceptance|review)\b|无新|新增[^。；]{0,12}为零|不重计|无新增', re.I)
STATUS = re.compile(r'\bremains? (?:open|unproved|unestablished)|\b(?:is|are) (?:unproved|unestablished)\b|'
                    r'\bnot (?:yet )?(?:established|derived)\b|仍(?:开放|未)|尚未|未完成', re.I)
NEGATIVE_EN = re.compile(r"\b(?:not|no|nor|neither|without|cannot|does not|do not|never)\b|n't\b|\bremains? open\b", re.I)
NEGATIVE_ZH = re.compile(r'不|未|无|非|没有')

# Boilerplate that recurs across records and should be a standard-boundary key.
STOCK = {
    'discrete-steps': re.compile(r'[Ss]tated for discrete steps|discrete steps'),
    'decidability': re.compile(r'needs? (?:the determination )?decid\w+ \(a logical commitment\)|decidability \(a logical commitment\)'),
    'pointwise-properties': re.compile(r'in place of function extensionality'),
    'no-evaluation': re.compile(r'[Ee]valuates neither|[Cc]ontains no ethical predicate'),
    'names-provisional': re.compile(r"names? (?:are|is) (?:the AI['’]s choice|Ren['’]s to choose)|readings? (?:remain|are) Ren['’]s"),
    'no-ethical-premise': re.compile(r'[Nn]o ethical premise and no Lean axiom'),
    'zero-axiom-target-open': re.compile(r'zero-substantive-axiom (?:grounding|normative warrant|foundation)'),
    'omission-not-refutation': re.compile(r'omission in a weaker description does not|is no counterexample to fuller'),
    'conditional-not-universal': re.compile(r'[Cc]onditional laws do not make their antecedents universal'),
}
# A cross-reference repeated as prose; better as a typed link (related: restated-in).
RESTATEMENT = re.compile(r'exact restatement for every world is')


def sentences(text, lang):
    if lang == 'zh':
        parts = re.split(r'(?<=[。；！？])', text)
    else:
        parts = re.split(r'(?<=[.;!?])\s+(?=[A-Z(“"`\[])', text)
    return [p.strip() for p in parts if p.strip()]


def text_fields(r):
    """(field label, language, text) for every public text in a record."""
    v2 = r.get('schema_version') == 2
    singles = ['title', 'claim', 'correspondence', 'validation_scope', 'next_delta'] + (['statement'] if v2 else ['limitations'])
    for key in singles:
        value = r.get(key)
        if isinstance(value, dict):
            for lang in ('en', 'zh'):
                yield key, lang, value.get(lang, '')
    for key in ('does_not_show', 'not_required', 'progress', 'laws', 'hypotheses'):
        for i, item in enumerate(r.get(key, []) or []):
            if isinstance(item, dict):
                for lang in ('en', 'zh'):
                    yield f'{key}[{i}]', lang, item.get(lang, '')
    for i, c in enumerate(r.get('counterexamples', []) or []):
        if isinstance(c, dict) and isinstance(c.get('detail'), dict):
            for lang in ('en', 'zh'):
                yield f'counterexamples[{i}]', lang, c['detail'].get(lang, '')
    for key in ('title', 'summary', 'evidence'):
        value = (r.get('overview') or {}).get(key)
        if isinstance(value, dict):
            for lang in ('en', 'zh'):
                yield f'overview.{key}', lang, value.get(lang, '')


# Fields where process narration is never acceptable (public statement of the result).
STATEMENT_FIELDS = ('title', 'statement', 'claim', 'overview.', 'does_not_show', 'not_required', 'laws', 'next_delta', 'limitations',
                    'counterexamples', 'progress')


def lint(r):
    """Return findings: dicts with id, field, rule, severity, detail."""
    out = []
    v2 = r.get('schema_version') == 2
    ident = r.get('id', '<missing>')

    def add(field, rule, detail, error_in_v2=True):
        out.append({'id': ident, 'field': field, 'rule': rule,
                     'severity': 'error' if (v2 and error_in_v2) else 'warning', 'detail': detail})

    caps = CAPS_V2 if v2 else CAPS_V1
    for key, (en_cap, zh_cap) in caps.items():
        value = r.get(key)
        if isinstance(value, dict):
            for lang, cap in (('en', en_cap), ('zh', zh_cap)):
                n = len(value.get(lang, ''))
                if n > cap:
                    add(key, 'length', f'{lang} {n} chars > {cap}', error_in_v2=key in HARD_CAPS)
    if v2:
        for key, (en_cap, zh_cap, max_items) in ITEM_CAPS_V2.items():
            items = r.get(key, []) or []
            if len(items) > max_items:
                add(key, 'item-count', f'{len(items)} items > {max_items}', error_in_v2=False)
            for i, item in enumerate(items):
                for lang, cap in (('en', en_cap), ('zh', zh_cap)):
                    n = len(item.get(lang, ''))
                    if n > cap:
                        add(f'{key}[{i}]', 'length', f'{lang} {n} chars > {cap}', error_in_v2=False)
                if key in ('does_not_show', 'not_required') and len(sentences(item.get('en', ''), 'en')) > 2:
                    add(f'{key}[{i}]', 'one-sentence', 'item has more than two sentences')

    markers_by_field = {}
    for field, lang, text in text_fields(r):
        public = field.startswith(STATEMENT_FIELDS)
        for rule, pattern in PROCESS:
            hits = sorted(set(pattern.findall(text)))
            if hits:
                markers_by_field.setdefault(field, set()).update(hits)
                if public:
                    add(field, 'process-marker:' + rule, f'{lang}: ' + ', '.join(map(str, hits[:5])))
        if field.split('[')[0] in ('claim', 'statement', 'limitations', 'does_not_show', 'next_delta') and EVIDENCE.search(text):
            add(field, 'evidence-in-claim', f'{lang}: evidence disclaimer belongs in validation_scope')
        if lang == 'en' and RESTATEMENT.search(text):
            add(field, 'prose-cross-reference', 'state the restatement as a typed related link', error_in_v2=False)
        if field.split('[')[0] in ('limitations', 'does_not_show') and lang == 'en':
            n = sum(bool(STATUS.search(s)) for s in sentences(text, 'en'))
            if n:
                add(field, 'status-restatement', f'{n} sentence(s) restate open/unproved status', error_in_v2=False)
            for key, pattern in STOCK.items():
                if pattern.search(text):
                    add(field, 'stock-boundary', f'use standard_boundaries key "{key}"')
        if field == 'statement' and lang == 'en' and text:
            text = re.sub(r'^(?:Target|Open target|Candidate):\s*', '', text)
            # Mathematical negation is often the content of a theorem ("never returns"), so
            # claims are not checked; only the one-sentence statement must lead positively.
            ss = sentences(text, 'en')
            neg = sum(bool(NEGATIVE_EN.search(s)) for s in ss)
            lead = re.split(r'[;:]| — ', ss[0])[0] if ss else ''
            if lead and NEGATIVE_EN.search(lead) and not re.search(r'\b(?:exactly|only|iff)\b', lead):
                add(field, 'negation-lead', f'{neg}/{len(ss)} sentences are negations; lead with what the result does', error_in_v2=False)
    for field, hits in markers_by_field.items():
        rounds = {h for h in hits if re.fullmatch(r'P\d{2,3}[a-z]?|Sections? \d+|§+\s?\d+|第\s?\d+\s?节', str(h))}
        if len(rounds) >= 3:
            add(field, 'round-accretion', f'{len(rounds)} rounds/sections cited: per-round notes belong in history/progress')
    title = (r.get('title') or {}).get('en', '')
    if not v2 and (len(title) > 120 or re.search(r':\s.{60,}', title)):
        add('title', 'title-is-statement', 'split into a short title and a statement')
    return out


def growth(old, new, fields=('limitations', 'validation_scope', 'correspondence')):
    """Ratchet for the migration window: a touched v1 record may not lengthen these fields."""
    if new.get('schema_version') == 2:
        return []
    found = []
    for key in fields:
        before = len((old.get(key) or {}).get('en', ''))
        after = len((new.get(key) or {}).get('en', ''))
        if after > before:
            found.append({'id': new.get('id'), 'field': key, 'rule': 'v1-growth', 'severity': 'error',
                          'detail': f'en grew {before} -> {after}; migrate the record to schema 2 before adding boundaries'})
    return found
