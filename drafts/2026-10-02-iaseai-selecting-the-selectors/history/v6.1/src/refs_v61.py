"""Build the reference lists of THEORY, SUPPLEMENT and DISCUSSION from the v6.0 bibliography plus works added in V6.1,
with the corrections and verification marks of the v6.0 evidence review. Writes src/{core,supp,disc}/z9_refs.md.
Run from v6.1/src after an assembly (it reads the assembled documents to find citations), then assemble again."""
import re, pathlib
V61=pathlib.Path('/Users/ren/theories/drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1')
OLD=(V61.parent/'v6'/'THEORY.md').read_text().split('## References',1)[1]
lines=[l for l in OLD.splitlines() if l.startswith('- ')]
def key_of(line):
    first=line[2:].split(',')[0].split(' ')[0].strip('.*')
    if line.startswith('- Dal Bó'): first='Dal'
    if line.startswith('- Bueno de Mesquita'): first='Bueno'
    if line.startswith('- Van Evera'): first='Van'
    if line.startswith('- Van Reenen'): first='VanR'
    if line.startswith('- Maynard Smith'): first='Maynard'
    if line.startswith('- Pérez'): first='Pérez-Castrillo'
    y=re.search(r"\b(1[5-9]\d\d|20\d\d)([ab])?(?:/\d+)?\.",line)
    return (first, y.group(1)+(y.group(2) or '')) if y else None
E={}
for l in lines:
    k=key_of(l)
    if k: E.setdefault(k,[]).append(l)
# corrections and upgrades from the evidence review of v6.0
def sub(k, old, new):
    E[k]=[x.replace(old,new) for x in E[k]]
def mark(k):
    E[k]=[re.sub(r' (†|‡[^\n]*)$','',x)+' ‡' for x in E[k]]
fix_vol={('Anderson','2015'):('*Psychological Bulletin*.','*Psychological Bulletin* 141(3):574–601.'),
 ('Maynard','1995'):('Oxford University Press.','W. H. Freeman (first edition; Oxford University Press reprint).'),
 ('Hofstadter','1944'):('*Social Darwinism in American Thought*.','*Social Darwinism in American Thought*. University of Pennsylvania Press.'),
 ('Alger','2020'):('*Journal of Economic Theory*.','*Journal of Economic Theory* 185:104951.'),
 ('Engels','2025'):('arXiv:2504.18530.','arXiv:2504.18530; NeurIPS 2025 (spotlight).'),
 ('Skalse','2022'):('Defining and characterizing reward hacking. *NeurIPS 2022*.','Defining and characterizing reward gaming. *NeurIPS 2022* (arXiv:2209.13085, "…reward hacking").'),
 ('Caulin','2011'):('26(4).','26(4):175–182.'),
}
for k,(o,n) in fix_vol.items():
    if k in E: sub(k,o,n)
for k in [('Anderson','2015'),('Maynard','1995'),('Hofstadter','1944'),('Engels','2025'),('Skalse','2022'),('Caulin','2011'),('Duersch','2012'),('Turner','2021'),('Gao','2023'),('Schoen','2025'),('Hammond','2025'),('Critch','2020'),('West','2015'),('Choi','2007'),('Rees','1994'),('Barrett','2003'),('Hart','2017'),('Cheng','2013'),('Liberman','2004'),('Bowles','2012'),('Stern','2011'),('Bannister','1979'),('Hirschman','1977'),('Soulé','2003'),('Richardson','1960'),('Farrell','1996'),('Abreu','1988'),('Stafford','2022'),('Leonard','2009'),('Trachtenberg','1988'),('Bueno','2026'),('Fudenberg','2026')]:
    if k in E: mark(k)
# Copeland split
if ('Copeland','2000') in E:
    E[('Copeland','2000a')]=[x.replace('2000.','2000a.') for x in E[('Copeland','2000')] if 'Origins' in x]
    E[('Copeland','2000b')]=[x.replace('2000.','2000b.') for x in E[('Copeland','2000')] if 'constructivist' in x]
NEW={
('Barnes','2020'):'- Barnes, B. and Christiano, P. 2020. Debate update: obfuscated arguments problem. AI Alignment Forum. †',
('Cardaliaguet','1999'):'- Cardaliaguet, P., Quincampoix, M. and Saint-Pierre, P. 1999. Set-valued numerical analysis for optimal control and differential games. In Bardi, M., Raghavan, T. and Parthasarathy, T. (eds), *Stochastic and Differential Games*. Birkhäuser. †',
('Denison','2024'):'- Denison, C. et al. 2024. Sycophancy to subterfuge: investigating reward-tampering in large language models. arXiv:2406.10162. †',
('Everitt','2021'):'- Everitt, T., Hutter, M., Kumar, R. and Krakovna, V. 2021. Reward tampering problems and solutions in reinforcement learning: a causal influence diagram perspective. *Synthese* 198. †',
('Frank','1995'):"- Frank, S. A. 1995. George Price's contributions to evolutionary genetics. *Journal of Theoretical Biology* 175(3). †",
('Hanahan','2011'):'- Hanahan, D. and Weinberg, R. A. 2011. Hallmarks of cancer: the next generation. *Cell* 144(5). †',
('Knight','1986'):'- Knight, J. C. and Leveson, N. G. 1986. An experimental evaluation of the assumption of independence in multiversion programming. *IEEE Transactions on Software Engineering* SE-12(1). †',
('Korbak','2025'):'- Korbak, T. et al. 2025. Chain of thought monitorability: a new and fragile opportunity for AI safety. arXiv:2507.11473. †',
('Langosco','2022'):'- Langosco, L., Koch, J., Sharkey, L., Pfau, J. and Krueger, D. 2022. Goal misgeneralization in deep reinforcement learning. *ICML 2022*. †',
('Powell','1991'):'- Powell, R. 1991. Absolute and relative gains in international relations theory. *American Political Science Review* 85(4). †',
('Price','1972'):'- Price, G. R. 1972. Extension of covariance selection mathematics. *Annals of Human Genetics* 35(4):485–490. †',
('Hamilton','1975'):'- Hamilton, W. D. 1975. Innate social aptitudes of man: an approach from evolutionary genetics. In Fox, R. (ed.), *Biosocial Anthropology*. †',
('Qi','2024'):'- Qi, X. et al. 2024. Fine-tuning aligned language models compromises safety, even when users do not intend to! *ICLR 2024*. †',
('Tennenholtz','2004'):'- Tennenholtz, M. 2004. Program equilibrium. *Games and Economic Behavior* 49(2). †',
('Tessler','2024'):'- Tessler, M. H. et al. 2024. AI can help humans find common ground in democratic deliberation. *Science* 386(6719). †',
('Aumann','1990'):'- Aumann, R. 1990. Nash equilibria are not self-enforcing. In Gabszewicz, J., Richard, J.-F. and Wolsey, L. (eds), *Economic Decision-Making*. †',
('Schelling','1966'):'- Schelling, T. 1966. *Arms and Influence*. Yale University Press. †',
('Fuhrmann','2010'):'- Fuhrmann, M. and Kreps, S. E. 2010. Targeting nuclear programs in war and peace. *Journal of Conflict Resolution* 54(6). † (not retrieved)',
('Rosenberg','1983'):'- Rosenberg, D. A. 1983. The origins of overkill. *International Security* 7(4). † (not retrieved)',
('Schwartz','1964'):'- Schwartz, B. 1964. *In Search of Wealth and Power: Yen Fu and the West*. Harvard University Press. †',
('Walt','1987'):'- Walt, S. 1987. *The Origins of Alliances*. Cornell University Press. †',
('Yan','1898'):'- Yan Fu 1898. 《天演论》, a rendering of Huxley 1893. †',
('Huxley','1893'):'- Huxley, T. H. 1893. *Evolution and Ethics* (Romanes Lecture). †',
('Acemoglu','2012b'):'- Acemoglu, D. and Robinson, J. 2012. *Why Nations Fail*. Crown. †',
}
for k,v in NEW.items(): E[k]=[v]
ALIAS={'Mesquita':'Bueno','Bó':'Dal','Evera':'Van'}
CIT=re.compile(r"\b([A-Z][A-Za-zÀ-ÿ'’\-]+)(?:(?:,| and) (?:[A-Z][A-Za-zÀ-ÿ'’\-]+|de|van|von)(?: [A-Z][A-Za-zÀ-ÿ'’\-]+)?)*(?: et al\.)? \(?((?:1[5-9]|20)\d\d[ab]?)(?:/\d+)?")
def build(doc, extra=()):
    t=(V61/f'{doc}.md').read_text().split('\n## References')[0]
    keys=set()
    for m in CIT.finditer(t):
        a,y=re.sub(r"['’]s$","",m.group(1)),m.group(2)
        a=ALIAS.get(a,a)
        if (a,y) in E: keys.add((a,y))
    if 'Why Nations Fail' in t or 'Acemoglu and Robinson 2012' in t: keys.add(('Acemoglu','2012b'))
    for k in extra: keys.add(k)
    items=sorted({x for k in keys for x in E[k]}, key=lambda s: re.sub(r'[*《]','',s).lower())
    return items
head="""## References

Marks: ‡ works whose existence and identifier were checked on 3 October 2026; † works not yet independently verified; unmarked works carried from the verified bibliography of v3.1. Sources of observations are listed with dates and links in EVIDENCE.md.

"""
for doc,folder in [('THEORY','core'),('SUPPLEMENT','supp'),('DISCUSSION','disc')]:
    items=build(doc)
    (V61/'src'/folder/'z9_refs.md').write_text(head+'\n'.join(items)+'\n')
    print(doc,len(items))
