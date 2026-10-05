"""Write the provenance and preservation record without rerunning calculations."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work/endogenous-renewal'
OUT = ROOT / 'outputs'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

baseline = json.loads((WORK/'preservation-manifest.json').read_text())
changed = [p for p, value in baseline.items() if (ROOT/p).exists() and sha(ROOT/p) != value]
missing = [p for p in baseline if not (ROOT/p).exists()]
artifacts = [OUT/'endogenous-renewal-and-consequential-feedback.md',
             OUT/'endogenous-renewal-mathematics.md', OUT/'endogenous-renewal.png',
             OUT/'endogenous-renewal.svg', WORK/'verify.py', WORK/'checks.json']
prior = OUT/'relational-regeneration-and-direction.md'
plural = Path('/Users/ren/theories/sources/15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md')
evidence = {
    'title':'Endogenous renewal and consequential feedback',
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'research_date_local':'2026-10-05',
    'timezone':'Asia/Bangkok',
    'user_request':'please, advance our theory',
    'retained_target':'Physical direction of reality itself toward proposed shared generativity and 善; relational situations containing distinct centers, not isolated individual fitness or a substituted ethical prescription.',
    'artifacts':{str(p.relative_to(ROOT)):sha(p) for p in artifacts},
    'results':{
        'formation':'C(0)=0<R(0) implies C_dot(0)=aR(0)>0 in the supplied reaction repertoire.',
        'global_threshold':'For positive a,b,k and maintained driving: M<=b/k implies R,C->0; M>b/k and R(0)+C(0)>0 imply convergence to the explicit positive equilibrium. All-degraded remains inactive.',
        'regulation':'D_dot=-kC(D-b/k); this is a restoring rate-balance relation where machinery persists, not assigned purpose, perception or allostasis.',
        'general_necessity':'Uniform componentwise production/loss bound with rho(L^-1 B)<1 implies exponential decay. Independent production and nondecaying capacities alter assumptions.',
        'hidden_mode':'Fixed aggregate observation leaves an unstable difference unobservable in the stated linear plant; no well-posed deterministic causal controller using only that observation stabilizes all nearby initial states.',
        'kindness':'No universal physical tendency to kindness, widening repair toward all affected centers, or open-ended novelty was proved.'
    },
    'checks':json.loads((WORK/'checks.json').read_text()),
    'visual_review':{'method':'Rendered PNG viewed after creation','outcome':'Readable titles, axes, legend, threshold annotation and deterministic-model caption; no clipping observed.'},
    'review':{
        'type':'Three collaborating AI agents; reasoning review, not external scientific peer review.',
        'reviewers':['/root/endogenous_regeneration','/root/generativity_critic','/root/generativity_formal'],
        'outcome':'No substantive mathematical errors found in saved drafts.',
        'refinements_applied':['Explicit accessible-state exception for global attraction in opening.',
                               'Well-posed closed-loop qualification in controller impossibility theorem.']
    },
    'sources':[
        {'kind':'prior work in current workspace','path':str(prior),'sha256_at_finalization':sha(prior),
         'scope':'Full report read; starting mechanism, physical-direction target and preservation context.'},
        {'kind':'other session research report','path':str(plural),'sha256_at_finalization':sha(plural),
         'scope':'Lines 1–170 returned and read, including joint feasibility, hidden burden in averages, and conditional scope. Used as conceptual connection, not empirical support.',
         'session_title':'Compare society to backpropagation (2)',
         'thread_id':'01a107a5-fd37-7b30-b1b8-f1c9587766bf'},
        {'kind':'primary conceptual paper','title':'Biological organisation as closure of constraints',
         'authors':'Maël Montévil and Matteo Mossio','year':2015,
         'url':'https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/',
         'doi':'10.1016/j.jtbi.2015.02.029',
         'scope':'Search-indexed author abstract and introduction inspected; direct author-page and PDF fetches failed. Only conceptual mutual-maintenance and thermodynamic-openness claims used.'},
        {'kind':'primary experimental paper','title':'Spontaneous formation of autocatalytic sets with self-replicating inorganic metal oxide clusters',
         'authors':'Haralampos N. Miras and colleagues','year':2020,
         'url':'https://www.chem.gla.ac.uk/cronin/images/pubs/Mathis-PNASMay2020.pdf',
         'doi':'10.1073/pnas.1921536117',
         'scope':'Author-hosted seven-page PDF text read through approximately line 342, including abstract, experimental kinetic/perturbation findings, and phenomenological model development. Not a full supporting-information review.',
         'use':'Physical example of formation of autocatalytic organization under particular chemical conditions; not evidence for the exact constructed model, indefinite persistence, or 善.'},
        {'kind':'primary theoretical abstract, background only','title':'Detecting autocatalytic, self-sustaining sets in chemical reaction systems',
         'authors':'Wim Hordijk and Mike Steel','year':2004,
         'url':'https://pubmed.ncbi.nlm.nih.gov/15038982/',
         'scope':'Full indexed primary abstract read by reviewer; contextual relationship only, not source of present proofs.'},
        {'kind':'primary theoretical abstract, background only','title':'Emergence of autocatalysis in prebiotic reaction networks',
         'authors':'Varun Varanasi and Jun Korenaga','year':2026,
         'url':'https://journals.aps.org/pre/abstract/10.1103/nmt5-qsym',
         'scope':'Publisher abstract and metadata inspected; nonoverlapping-core assumption noted. Full text not available and no quantitative result imported.'}
    ],
    'preservation':{'baseline_count':len(baseline),'changed_prior_outputs':changed,
                    'missing_prior_outputs':missing,'all_prior_outputs_unchanged':not changed and not missing,
                    'baseline_path':str(WORK/'preservation-manifest.json'),
                    'other_research_directories':'Read only during this turn. No messages sent to other user chats.'},
    'limitations':[
        'Constructed ideal kinetics with supplied reaction repertoire and maintained energetic driving; no actual chemical implementation established.',
        'Global convergence is a deterministic concentration-model result, not an eternal-survival guarantee.',
        'Exact finite-particle model eventually absorbs; no stochastic lifetime scaling calculated.',
        'Feedback model is local and separate; its machinery formation and energetic costs are not integrated into the chemical model.',
        'No new empirical experiment, cosmological test, universal kindness proof or priority claim.'
    ]
}
path = OUT/'endogenous-renewal-evidence.json'
path.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
links = []
for report in artifacts[:2]:
    content=report.read_text()
    for left,right in [(r'\(',r'\)'),(r'\[',r'\]')]:
        assert content.count(left)==content.count(right),(report,left)
    for target in re.findall(r'\]\(([^)]+)\)',content):
        if target.startswith(('http://','https://','#')): continue
        resolved=Path(unquote(target.split('#')[0]))
        if not resolved.is_absolute(): resolved=report.parent/resolved
        assert resolved.exists(),str(resolved)
        links.append(str(resolved))
print(json.dumps({'evidence':str(path),'local_links_checked':len(links),
                  'prior_files':len(baseline),'changed_prior_outputs':changed,
                  'missing_prior_outputs':missing,
                  'report_words':{p.name:len(p.read_text().split()) for p in artifacts[:2]}},indent=2))
