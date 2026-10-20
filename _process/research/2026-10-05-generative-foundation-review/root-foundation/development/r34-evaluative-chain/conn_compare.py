#!/usr/bin/env python3
"""R34: compare two outputs of THEOREM-CONNECTIVITY.py (JSON, possibly after log lines): the counts the study
and the chapter cite, before and after.

usage: python3 -B conn_compare.py BEFORE.json AFTER(.json|.log)"""
import json
import sys

MODS = ('Becoming.Ranking', 'Becoming.ActiveReading', 'Becoming.Relevance', 'Becoming.Retaining',
        'Becoming.Boundaries', 'Becoming.Direction', 'Becoming.ScoreRepresentation', 'Becoming.Extension')


def load(p):
    t = open(p).read()
    return json.JSONDecoder().raw_decode(t[t.find('{'):])[0]


def size(v):
    return len(v) if isinstance(v, (list, dict)) else v


def summary(d):
    comps = d['components']
    return {
        'commit': d['commit'][:9], 'spine_theorems': d['spine_theorems'], 'apart': d['apart'],
        'general_structure': d['apart_general_structure_by_design'], 'apart_roots': d['apart_roots'],
        'roots_by_category': d['apart_roots_by_category'], 'classes': d['classes'],
        'families': d['families_reach_each_other'],
        'pure_forwarders': size(d['pure_forwarders']),
        'own_law': sum(d['statement_through_own_law_by_module'].values()),
        'both': sum(d['statements_on_both_by_module'].values()),
        'components': size(comps) if not isinstance(comps, dict) else {k: size(v) for k, v in comps.items()},
        'apart_in': {m: d['apart_by_module'].get(m) for m in MODS},
        'register_not_roots': d['register_entries_not_apart_roots'],
    }


a, b = summary(load(sys.argv[1])), summary(load(sys.argv[2]))
for k in a:
    print(k, ':', a[k], '->', b[k])
