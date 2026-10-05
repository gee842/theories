from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work/conditions-of-generativity'
OUT=ROOT/'outputs'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((WORK/'preservation-manifest.json').read_text())
missing=[p for p in baseline if not (ROOT/p).exists()]
changed=[p for p,h in baseline.items() if (ROOT/p).exists() and sha(ROOT/p)!=h]
artifacts=[OUT/'conditions-of-generativity.md',OUT/'conditions-of-generativity-mathematics.md',
           OUT/'conditions-of-generativity.png',OUT/'conditions-of-generativity.svg',
           WORK/'verify.py',WORK/'checks.json']
prior=OUT/'endogenous-renewal-mathematics.md'
record={
 'title':'Generativity through supporting conditions',
 'created_utc':datetime.now(timezone.utc).isoformat(),
 'local_date':'2026-10-05','timezone':'Asia/Bangkok',
 'user_steering':'being generative needs conditions, if there is no sun there is no us on the planet, please explore into this direction.',
 'interpretation':'Supporting conditions are part of the relational foundation. Investigate usable energy, retention, conversion, renewal and timing without requiring local self-sufficiency or substituting a normative thesis.',
 'artifacts':{str(p.relative_to(ROOT)):sha(p) for p in artifacts},
 'claim_status':{
   'constant_power_threshold':'Proved global active-material decay at and below Pc=loss*b/(k*M); existence, uniqueness and local asymptotic stability of positive equilibrium above Pc.',
   'positive_global_attraction':'Not proved for the extended energy model.',
   'same_mean_timing_counterexample':'Proved in the same supplied-power model: constant1.2 has stable positive equilibrium; 2.4 for30 then0 for30 globally extinguishes active material from every finite initial energy reserve.',
   'contraction_certificate':'Analytic positive matrix bound with an explicit eventual reserve envelope2.41; strict upper bound verified independently and via rational/Taylor inequalities.',
   'energy_balance':'Exact reduced work-equivalent balance, not a complete molecular thermodynamic realization.',
   'entropy_scope':'Net entropy export conclusion restricted to bounded/sublinear entropy storage and existing long-run averages.',
   'current_state':'Supply phase can be included as a physical state coordinate; mean input alone discards causal information.',
   'universal_root':'Working conceptual formulation; not a proof of all generativity, open-ended novelty, the physical reaction repertoire, or universal direction toward kindness.'
 },
 'checks':json.loads((WORK/'checks.json').read_text()),
 'visual_review':{'method':'Viewed rendered PNG twice; moved upper legend to eliminate interference with supply curve.',
                  'outcome':'Axes, captions, threshold, logarithmic activity scale and legends readable; no clipping observed.'},
 'reviews':{
   'type':'Independent reasoning reviews by three collaborating AI agents, not external scientific peer review.',
   'agents':['/root/endogenous_regeneration','/root/generativity_formal','/root/generativity_critic'],
   'outcome':'Mathematical results and physical scope passed. One entropy-scope refinement applied.',
   'applied_refinement':'Changed unqualified sustained-activity entropy export claim to bounded steady dissipative operation.'
 },
 'sources':[
   {'kind':'prior internal report','path':str(prior),'sha256':sha(prior),
    'scope':'Full read; base material-renewal model, energy reserve limitation, and sufficient-present discussion.'},
   {'kind':'primary author analysis','author':'Axel Kleidon',
    'title':'How does the Earth system generate and maintain thermodynamic disequilibrium and what does it imply for the future of the planet?',
    'url':'https://arxiv.org/html/1103.2014',
    'version_read':'2011 author manuscript, arXiv1103.2014v2; reviewer identifies later2012 publication.',
    'scope':'Parent read returned text through section3.2, including boundaries, balances, photon conversion and free-energy transfer. Reviewer inspected sections2–4.5. Main report uses only disequilibrium, conversion and entropy-balance claims.',
    'excluded':'No adoption of maximum entropy production as a universal law, no present-day numerical planetary estimates imported, no claim that the paper proves our model.'},
   {'kind':'primary institutional Earth-observation explanation','organization':'NASA',
    'title':'Climate and Earth’s Energy Budget',
    'url':'https://science.nasa.gov/earth/earth-observatory/climate-and-earths-energy-budget/',
    'scope':'Retrieved passages about incoming solar and outgoing thermal radiation, energy balance and cooling; no dated numerical flux estimates used.'},
   {'kind':'background only','authors':'Axel Kleidon and Maik Renner',
    'title':'A simple explanation for the sensitivity of the hydrologic cycle to surface temperature and solar radiation and its implications for global climate change',
    'url':'https://doi.org/10.5194/hess-17-2873-2013',
    'scope':'Reviewer inspected primary abstract only; detailed PDF fetch failed. Its extraction-feedback example informed discussion but no quantitative result was imported into artifacts.'},
   {'kind':'failed retrieval, unused','title':'Ilya Prigogine Nobel lecture',
    'url':'https://www.nobelprize.org/uploads/2018/06/prigogine-lecture.pdf',
    'scope':'Direct fetch failed; no claim based on unseen lecture text.'}
 ],
 'preservation':{'baseline_count':len(baseline),'changed_prior_outputs':changed,
                 'missing_prior_outputs':missing,'all_prior_outputs_unchanged':not changed and not missing,
                 'baseline_path':str(WORK/'preservation-manifest.json'),
                 'other_research_directories':'No writes in this turn.'},
 'limitations':['All rates and timings in the comparison are dimensionless; no planetary or organism fit.',
                'Continuous deterministic concentrations do not imply indefinite finite-particle survival.',
                'Asymptotic depletion does not establish finite-time disappearance.',
                'Capture, storage construction and feedback on the source are not endogenous in this extension.',
                'Numerical trajectories are illustrations; no new empirical experiment was performed.']
}
evidence=OUT/'conditions-of-generativity-evidence.json'
evidence.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
links=0
for p in artifacts[:2]:
    content=p.read_text()
    for a,b in [(r'\(',r'\)'),(r'\[',r'\]')]:
        assert content.count(a)==content.count(b),(p,a)
    for link in re.findall(r'\]\(([^)]+)\)',content):
        if link.startswith(('https://','http://','#')): continue
        target=Path(unquote(link.split('#')[0]))
        if not target.is_absolute():target=p.parent/target
        assert target.exists(),target
        links+=1
print(json.dumps({'prior_output_count':len(baseline),'changed':changed,'missing':missing,
 'local_links_checked':links,'word_counts':{p.name:len(p.read_text().split()) for p in artifacts[:2]},
 'evidence_path':str(evidence)},indent=2))
