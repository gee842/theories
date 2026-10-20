#!/usr/bin/env python3
"""R35 step 2(c), E7: law families. theories/becoming/results/data/law-families.json groups records that state one
law and its readings; registry.py checks it and renders a family line on each member's page, navigation.py a
table in RESULTS.md. Run once from the checkout root: python3 -B tools_e7.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]


def patch(path, pairs):
    p = ROOT / path
    s = p.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:80])
        s = s.replace(a, b)
    p.write_text(s)


patch('tools/research/registry.py', [
    ("GROWN = []  # sources changed only outside what the record cites, from the last validate()\n",
     "GROWN = []  # sources changed only outside what the record cites, from the last validate()\n"
     "LAW_FAMILIES = 'theories/becoming/results/data/law-families.json'\n\n\n"
     "def law_families():\n"
     "    \"\"\"The law families (twentieth review, E7): records stating one law and its readings, with a lead.\"\"\"\n"
     "    path = ROOT / LAW_FAMILIES\n"
     "    return json.loads(path.read_text()).get('families', []) if path.is_file() else []\n\n\n"
     "def law_family_errors(records):\n"
     "    ids, seen, errors = {r.get('id') for r in records}, {}, []\n"
     "    for f in law_families():\n"
     "        name = f.get('id', '<missing>')\n"
     "        if not pair(f.get('title')) or not pair(f.get('statement')):\n"
     "            errors.append(f'law family {name}: title and statement need English or Chinese')\n"
     "        if f.get('lead') not in f.get('members', []):\n"
     "            errors.append(f'law family {name}: the lead must be a member')\n"
     "        for m in f.get('members', []):\n"
     "            if m not in ids:\n"
     "                errors.append(f'law family {name}: unknown record {m}')\n"
     "            if m in seen:\n"
     "                errors.append(f'law family {name}: {m} is already in law family {seen[m]}')\n"
     "            seen[m] = name\n"
     "    return errors\n"),
    ("    settings = config()\n    errors += validate_standard_boundaries(settings)\n",
     "    settings = config()\n    errors += validate_standard_boundaries(settings)\n    errors += law_family_errors(records)\n"),
    ("def used_by_lines(r, result_link):\n",
     "def law_family_lines(r, result_link):\n"
     "    \"\"\"The law family the record belongs to (data/law-families.json), with its lead and members.\"\"\"\n"
     "    f = r.get('_law_family')\n"
     "    if not f:\n"
     "        return []\n"
     "    others = ' · '.join(result_link(m) for m in f['members'] if m != r['id'])\n"
     "    lead = 'this record' if f['lead'] == r['id'] else result_link(f['lead'])\n"
     "    return ['', f'**Law family:** {en(f[\"title\"])} (lead: {lead}). {en(f[\"statement\"])} Members: {others}.']\n\n\n"
     "def used_by_lines(r, result_link):\n"),
    ("    lines += used_by_lines(r, result_link)\n    lines += ['', heading('###', 'Sources', 'Sources / 来源')",
     "    lines += used_by_lines(r, result_link)\n    lines += law_family_lines(r, result_link)\n    lines += ['', heading('###', 'Sources', 'Sources / 来源')"),
    ("    lines += used_by_lines(r, result_link)\n    lines += ['', heading('##', 'Sources and existing receipts'",
     "    lines += used_by_lines(r, result_link)\n    lines += law_family_lines(r, result_link)\n    lines += ['', heading('##', 'Sources and existing receipts'"),
    ("        r['_used_by'] = sorted(used_by.get(r['id'], []))  # reverse edges, shown as \"Used by\" on the page\n",
     "        r['_used_by'] = sorted(used_by.get(r['id'], []))  # reverse edges, shown as \"Used by\" on the page\n"
     "    family = {m: f for f in law_families() for m in f.get('members', [])}\n"
     "    for r in records:\n"
     "        if r['id'] in family:\n"
     "            r['_law_family'] = family[r['id']]\n"),
    ("    shared = standard_boundaries_path() in changed  # its text renders on every citing page\n",
     "    shared = standard_boundaries_path() in changed  # its text renders on every citing page\n"
     "    families = LAW_FAMILIES in changed  # its text renders on every member's page\n"),
    ("                or (shared and r.get('standard_boundaries'))}\n",
     "                or (shared and r.get('standard_boundaries')) or (families and r.get('_law_family'))}\n"),
])

patch('tools/research/navigation.py', [
    ("                      H('##', 'Registered results', '已登记成果 / Registered results'), ''] + register_table(records, path) + ['',\n"
     "                      H('##', 'Where to look first', 'Where to look first'), ''] + WHERE_TO_LOOK + ['']\n",
     "                      H('##', 'Registered results', '已登记成果 / Registered results'), ''] + register_table(records, path) + ['',\n"
     "                      H('##', 'Law families', 'Law families / 规律族'), ''] + law_family_table(records, path) + ['',\n"
     "                      H('##', 'Where to look first', 'Where to look first'), ''] + WHERE_TO_LOOK + ['']\n"),
    ("def counts(records):\n",
     "def law_family_table(records, base):\n"
     "    \"\"\"Records that state one law and its readings, with a lead (theories/becoming/results/data/law-families.json).\"\"\"\n"
     "    by_id = {r['id']: r for r in records}\n"
     "    lines = ['Records that state one law and its readings, conditions or calibrations, grouped with a lead record; '\n"
     "             'each member page states the family. Source: ' + link(registry.LAW_FAMILIES, base, 'law-families.json') + '.', '',\n"
     "             '| Family | Lead | Members |', '|---|---|---|']\n"
     "    for f in registry.law_families():\n"
     "        lead = by_id.get(f['lead'])\n"
     "        members = ' · '.join(link(page_of(by_id[m]), base, f'`{m}`') for m in f['members'] if m in by_id and m != f['lead'])\n"
     "        lines += [f'| {registry.en(f[\"title\"])} | ' + (link(page_of(lead), base, registry.en(lead['title'])) if lead else f['lead'])\n"
     "                  + f' | {members} |']\n"
     "    return lines\n\n\n"
     "def counts(records):\n"),
])
print('patched')
