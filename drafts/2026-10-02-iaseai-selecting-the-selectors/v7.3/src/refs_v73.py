"""Build the reference lists of THEORY, SUPPLEMENT and DISCUSSION from the v6.0 bibliography plus works added in V6.2,
with the corrections and verification marks of the v6.0 evidence review. Writes src/{core,supp,disc}/z9_refs.md.
Run from v7.3/src after an assembly (it reads the assembled documents to find citations), then assemble again.

Citations and entries are matched by (first author's surname, second author's surname or 'et al.' or '', year),
so that "Maynard Smith and Szathmáry 1995" and "Smith 1995", or "Acemoglu, Egorov and Sonin 2012" and
"Acemoglu and Robinson 2012", are different works. Three or more authors key as 'et al.' whether the citation
names them all or not, except where one first author has two or more such works in one year (Greenblatt 2024):
there the key takes the second author, so "Greenblatt, Shlegeris, Sachan and Roger 2024" and "Greenblatt, Roger,
Krasheninnikov and Krueger 2024" are different works, and a bare "Greenblatt et al. 2024" is reported as ambiguous.
Surnames keep their particles (Maynard Smith, Bueno de Mesquita, Dal Bó, Van Evera, van Damme, de Vries, van der Weij). xref_v73.py imports entry_keys() and citations() from here, so both use one rule."""
import re, pathlib
V61=pathlib.Path(__file__).resolve().parent.parent      # the v6.2 folder (name kept from v6.1)
YEAR=r"(?:1[5-9]|20)\d\d[ab]?"
PART=r"(?:van|von|de|der|den|da|di|du|le|la)"
UP=r"[A-ZÀ-ÖØ-Þ](?:[^\W\d_]|[\-'’](?=[^\W\d_]))*"     # a capitalised word; inner hyphen or apostrophe allowed
NAME=rf"(?:Maynard Smith|Dal Bó|Van Evera|Van Reenen|(?:{PART} ){{0,2}}{UP}(?: {PART} {UP})?)"
POSS=r"(?:['’]s)?"
CIT=re.compile(rf"(?<![\w-])({NAME}{POSS}(?:(?:,? and |, ){NAME}{POSS})*)( et al\.{POSS})? \(?({YEAR})(?:/\d+)?((?:, {YEAR}(?![\d.]))*)")
SKIP={'Section','Sections','Proposition','Theorem','Lemma','Remark','Definition','Corollary','Assumption','Stage',
      'Convention','Treaty','Protocol','January','February','March','April','May','June','July','August','September',
      'October','November','December','In','Test','The','EV','Branch','Figure','Table','Part','Step','Case','Claim',
      'Its','Since','Checked','Report','Research','Summit','ICML','NeurIPS','ICLR','AI','Plan','Act','Order','Declaration',
      'Resolution','Statement','Version','Draft'}
BIB_ALIAS={'Yan Fu':'Yan'}          # a Chinese name, cited by surname
SHARED=set()      # (first author, year) with two or more works of three or more authors; filled from the data below
def _key(names, etal, year):
    names=[re.sub(r"['’]s$","",n) for n in names]
    if etal or len(names)>=3:
        second=names[1] if (names[0], year) in SHARED and len(names)>=2 else 'et al.'
    else:
        second=names[1] if len(names)==2 else ''
    return (names[0], second, year)
def _parse_entry(line):
    """(names, et al. flag, years) of one bibliography line; None if it has no author-year."""
    body=line[2:] if line.startswith('- ') else line
    y=re.search(rf"\b({YEAR})(?:/\d+)?\.", body)
    if not y: return None
    authors=re.sub(r'\((?:eds?\.?)\)','',body[:y.start()])
    etal='et al.' in authors; authors=authors.replace('et al.','')
    segs=[x.strip(' *') for x in re.split(r',\s*|\s+and\s+', authors)]
    names=[BIB_ALIAS.get(x,x) for x in segs if x and not re.fullmatch(r"(?:[A-Z][a-z]?\.[\s-]*)+", x)]  # initials carry dots; 'Qi', 'Ok' do not
    if not names: return None
    years=[y.group(1)]+re.findall(rf"; ({YEAR})\.", body)    # 'Schelling, T. 1960. *A*; 1966. *B*.'
    return names, etal, years
def entry_keys(line):
    """Keys of one bibliography line ('- Surname, I., Surname, I. and Surname, I. 2012. Title…'); [] if none."""
    p=_parse_entry(line)
    if not p: return []
    names, etal, years = p
    return [_key(names, etal, yr) for yr in years]
def loose_match(k, keys):
    """The one listed key with the same first author and year as k, when the citation's form differs from the
    entry's (e.g. 'Deutsch 1957' for 'Deutsch, K. W. et al. 1957'); None if there is none or more than one."""
    near=[x for x in keys if x[0]==k[0] and x[2]==k[2]]
    return near[0] if len(near)==1 else None
def citations(text):
    """Author-year citations in prose, as {key: first matched string}."""
    out={}
    for m in CIT.finditer(text):
        names=re.split(r",? and |, ", m.group(1))
        if re.sub(r"['’]s$","",names[0]) in SKIP: continue
        for yr in [m.group(3)]+re.findall(YEAR, m.group(4) or ''):
            out.setdefault(_key(names, bool(m.group(2)), yr), m.group(0))
    return out

# The corrections below were written against v6.0's (first word, year) handles; they are applied under those
# handles and the result is then re-keyed by entry_keys() (see B below).
def _legacy_key(line):
    first=line[2:].split(',')[0].split(' ')[0].strip('.*')
    for pre,k in (('Dal Bó','Dal'),('Bueno de Mesquita','Bueno'),('Van Evera','Van'),('Van Reenen','VanR'),
                  ('Maynard Smith','Maynard'),('Pérez','Pérez-Castrillo')):
        if line.startswith('- '+pre): first=k
    y=re.search(r"\b(1[5-9]\d\d|20\d\d)([ab])?(?:/\d+)?\.",line)
    return (first, y.group(1)+(y.group(2) or '')) if y else None
OLD=(V61.parent/'v6'/'THEORY.md').read_text().split('## References',1)[1]
E={}
for l in OLD.splitlines():
    if l.startswith('- ') and _legacy_key(l): E.setdefault(_legacy_key(l),[]).append(l)
# corrections and upgrades from the evidence review of v6.0
def sub(k, old, new):
    E[k]=[x.replace(old,new) for x in E[k]]
def mark(k):          # upgrade to ‡; a † mark loses its parenthetical too ('† (title seen; …)' -> '‡')
    E[k]=[re.sub(r' (?:†(?: \([^()]*\))?|‡[^\n]*)$','',x)+' ‡' for x in E[k]]
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
    del E[('Copeland','2000')]
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
# V6.2: corrections and additions of the evidence update (planning/D4-evidence-notes.md, section (b), as corrected by
# its Verification section), under the legacy handles (first word, year). A list holds every work sharing a handle.
D4={
('Jones','2024'):['- Jones, C. I. 2024. The AI dilemma: growth versus existential risk. *American Economic Review: Insights* 6(4):575–590. ‡ (full text)'],
('Copeland','2000b'):['- Copeland, D. C. 2000b. The constructivist challenge to structural realism: a review essay. *International Security* 25(2):187–212. † (record)'],
('Leonard','2009'):["- Leonard, T. C. 2009. Origins of the myth of social Darwinism: the ambiguous legacy of Richard Hofstadter's *Social Darwinism in American Thought*. *Journal of Economic Behavior and Organization* 71(1):37–51. † (record)"],
('Fuhrmann','2010'):['- Fuhrmann, M. and Kreps, S. E. 2010. Targeting nuclear programs in war and peace: a quantitative empirical analysis, 1941–2000. *Journal of Conflict Resolution* 54(6):831–859. † (record)'],
('Rosenberg','1983'):['- Rosenberg, D. A. 1983. The origins of overkill: nuclear weapons and American strategy, 1945–1960. *International Security* 7(4):3–71. † (record)'],
('Larsen','2026'):['- Larsen, T., Dean, R., Halstead, B., Lifland, E., Greenblatt, R. and Kokotajlo, D. 2026. *AI 2040: Plan A*. AI Futures Project, with its supplements (Deal Decline; Comparing Possible Plans; Capability Scaling Strategy; Verification Plan). ‡ (page; names from the site; figures as checked by the handoff review, see EVIDENCE.md, EV10)'],
('Kulveit','2025'):['- Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D. and Duvenaud, D. 2025. Position: humanity faces existential risk from gradual disempowerment. *ICML 2025* (position paper track), PMLR 267; arXiv:2501.16946. ‡ (abstract)'],
('Marks','2025'):['- Marks, S., Treutlein, J., Bricken, T., Lindsey, J., Marcus, J., Mishra-Sharma, S. et al. 2025. Auditing language models for hidden objectives. arXiv:2503.10965. ‡ (abstract)'],
('Hendrycks','2025'):['- Hendrycks, D., Schmidt, E. and Wang, A. 2025. Superintelligence strategy: expert version. arXiv:2503.05628. ‡ (abstract)'],
('Duersch','2012'):['- Duersch, P., Oechssler, J. and Schipper, B. C. 2012. Unbeatable imitation. *Games and Economic Behavior* 76(1):88–96. † (record; wording checked by the v6.1 evidence review against the source)'],
('Cardaliaguet','1999'):['- Cardaliaguet, P., Quincampoix, M. and Saint-Pierre, P. 1999. Set-valued numerical analysis for optimal control and differential games. In Bardi, M., Raghavan, T. E. S. and Parthasarathy, T. (eds), *Stochastic and Differential Games*, Annals of the International Society of Dynamic Games 4, 177–247. Birkhäuser. † (pages per the v6.1 evidence review)'],
('Güth','1992'):['- Güth, W. and Yaari, M. 1992. Explaining reciprocal behavior in simple strategic games: an evolutionary approach. In Witt, U. (ed.), *Explaining Process and Change: Approaches to Evolutionary Economics*. University of Michigan Press. † (record of the volume)'],
('Snyder','1965'):['- Snyder, G. H. 1965. The balance of power and the balance of terror. In Seabury, P. (ed.), *The Balance of Power*. Chandler. † (not retrieved)'],
('Crawford','1982'):['- Crawford, V. P. and Sobel, J. 1982. Strategic information transmission. *Econometrica* 50(6):1431–1451. † (record)'],
('Gabriel','2020'):['- Gabriel, I. 2020. Artificial intelligence, values, and alignment. *Minds and Machines* 30(3):411–437. † (record)'],
('Kydd','1997'):['- Kydd, A. 1997. Game theory and the spiral model. *World Politics* 49(3):371–400. † (record)'],
('Kydd','2000'):['- Kydd, A. 2000. Trust, reassurance, and cooperation. *International Organization* 54(2):325–357. † (record)'],
('Powell','1991'):['- Powell, R. 1991. Absolute and relative gains in international relations theory. *American Political Science Review* 85(4):1303–1320. † (record)'],
('Powell','1999'):['- Powell, R. 1999. *In the Shadow of Power: States and Strategies in International Politics*. Princeton University Press. † (record)'],
('Powell','2006'):['- Powell, R. 2006. War as a commitment problem. *International Organization* 60(1):169–203. † (record)'],
('Schaffer','1988'):['- Schaffer, M. E. 1988. Evolutionarily stable strategies for a finite population and a variable contest size. *Journal of Theoretical Biology* 132(4):469–478. † (record)'],
('Konrad','2009'):['- Konrad, K. A. and Kovenock, D. 2009. Multi-battle contests. *Games and Economic Behavior* 66(1):256–274. † (record)',
                   '- Konrad, K. A. 2009. *Strategy and Dynamics in Contests*. Oxford University Press. † (record)'],
('Harris','1987'):['- Harris, C. and Vickers, J. 1987. Racing with uncertainty. *Review of Economic Studies* 54(1):1–21. † (record)'],
('Caulin','2011'):["- Caulin, A. F. and Maley, C. C. 2011. Peto's paradox: evolution's prescription for cancer prevention. *Trends in Ecology and Evolution* 26(4):175–182. † (record)"],
('Abecassis','2025'):['- Abecassis, D. 2025. Refining MAIM: identifying changes required to meet conditions for deterrence. Machine Intelligence Research Institute, April. ‡ (page)'],
('Bueno','2026'):['- Bueno de Mesquita, E., Dziuda, W. and Polborn, M. 2026. The AGI race and existential risk. NBER Working Paper 35276. ‡ (full text)'],
('Turner','2021'):['- Turner, A. M., Smith, L., Shah, R., Critch, A. and Tadepalli, P. 2021. Optimal policies tend to seek power. *NeurIPS 2021*; arXiv:1912.01683. ‡ (abstract)'],
('Turner','2020'):['- Turner, A. M., Hadfield-Menell, D. and Tadepalli, P. 2020. Conservative agency via attainable utility preservation. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 385–391; arXiv:1902.09725. † (record)'],
('Turner','2022'):['- Turner, A. M. and Tadepalli, P. 2022. Parametrically retargetable decision-makers tend to seek power. *Advances in Neural Information Processing Systems* 35:31391–31401; arXiv:2206.13477. † (record)'],
('Ho','2024'):['- Ho, A., Besiroglu, T., Erdil, E., Owen, D., Rahman, R., Guo, Z. C., Atkinson, D., Thompson, N. and Sevilla, J. 2024. Algorithmic progress in language models. *Advances in Neural Information Processing Systems* 37:58245–58283; arXiv:2403.05812. ‡ (abstract)'],
('Smith','1995'):['- Smith, H. L. 1995. *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems*. American Mathematical Society. † (not retrieved)'],
('Schelling','1960'):['- Schelling, T. C. 1960. *The Strategy of Conflict*. Harvard University Press. †'],
('Schelling','1966'):['- Schelling, T. C. 1966. *Arms and Influence*. Yale University Press. †'],
('Schelling','1961'):['- Schelling, T. C. and Halperin, M. H. 1961. *Strategy and Arms Control*. Twentieth Century Fund. † (record)'],
('Grieco','1988'):['- Grieco, J. M. 1988. Anarchy and the limits of cooperation: a realist critique of the newest liberal institutionalism. *International Organization* 42(3):485–507. † (record)'],
('Snidal','1991'):['- Snidal, D. 1991. Relative gains and the pattern of international cooperation. *American Political Science Review* 85(3):701–726. † (record)'],
('Gilbert','1982'):['- Gilbert, R. J. and Newbery, D. M. G. 1982. Preemptive patenting and the persistence of monopoly. *American Economic Review* 72(3):514–526. † (record)'],
('Budd','1993'):['- Budd, C., Harris, C. and Vickers, J. 1993. A model of the evolution of duopoly: does the asymmetry between firms tend to increase or decrease? *Review of Economic Studies* 60(3):543–573. † (record)'],
('Athey','2001'):['- Athey, S. and Schmutzler, A. 2001. Investment and market dominance. *RAND Journal of Economics* 32(1):1–26. † (record)'],
('Aghion','2001'):['- Aghion, P., Harris, C., Howitt, P. and Vickers, J. 2001. Competition, imitation and growth with step-by-step innovation. *Review of Economic Studies* 68(3):467–492. † (record)'],
('Avenhaus','2002'):['- Avenhaus, R., von Stengel, B. and Zamir, S. 2002. Inspection games. In Aumann, R. J. and Hart, S. (eds), *Handbook of Game Theory with Economic Applications*, vol. 3, ch. 51, 1947–1987. Elsevier. † (record)'],
('Shavell','1986'):['- Shavell, S. 1986. The judgment proof problem. *International Review of Law and Economics* 6(1):45–58. † (record)'],
('Grossman','1994'):['- Grossman, G. M. and Helpman, E. 1994. Protection for sale. *American Economic Review* 84(4):833–850. ‡ (abstract)'],
('Hehenkamp','2004'):['- Hehenkamp, B., Leininger, W. and Possajennikov, A. 2004. Evolutionary equilibrium in Tullock contests: spite and overdissipation. *European Journal of Political Economy* 20(4):1045–1057. † (record)'],
('Cardaliaguet','1996'):['- Cardaliaguet, P. 1996. A differential game with two players and one target. *SIAM Journal on Control and Optimization* 34(4):1441–1460. † (record)'],
('Kuran','1995'):['- Kuran, T. 1995. *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Harvard University Press. † (record)'],
('MacKenzie','2006'):['- MacKenzie, D. 2006. *An Engine, Not a Camera: How Financial Models Shape Markets*. MIT Press. † (record)'],
('Butler','2025'):['- Butler, G., Baker, J., Amend, S. R., Pienta, K. J. and Venditti, C. 2025. No evidence for Peto\'s paradox in terrestrial vertebrates. *Proceedings of the National Academy of Sciences* 122(9):e2422861122. ‡ (abstract)'],
('Dietz','2003'):['- Dietz, T., Ostrom, E. and Stern, P. C. 2003. The struggle to govern the commons. *Science* 302(5652):1907–1912. † (record)'],
('Podvig','2002'):['- Podvig, P. 2002. History and the current status of the Russian early-warning system. *Science and Global Security* 10(1):21–60. † (record)'],
('Hoffman','2009'):['- Hoffman, D. E. 2009. *The Dead Hand: The Untold Story of the Cold War Arms Race and Its Dangerous Legacy*. Doubleday. † (record)'],
('Askell','2019'):['- Askell, A., Brundage, M. and Hadfield, G. 2019. The role of cooperation in responsible AI development. arXiv:1907.04534. ‡ (abstract)'],
('Hubinger','2024'):['- Hubinger, E., Denison, C., Mu, J., Lambert, M., Tong, M., MacDiarmid, M. et al. 2024. Sleeper agents: training deceptive LLMs that persist through safety training. arXiv:2401.05566. ‡ (abstract)'],
('Greenblatt','2024'):E[('Greenblatt','2024')]+[
    '- Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDiarmid, M., Marks, S. et al. 2024. Alignment faking in large language models. arXiv:2412.14093. ‡ (abstract)',
    '- Greenblatt, R., Roger, F., Krasheninnikov, D. and Krueger, D. 2024. Stress-testing capability elicitation with password-locked models. arXiv:2405.19550. ‡ (abstract record)'],
('Meinke','2024'):['- Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R. and Hobbhahn, M. 2024. Frontier models are capable of in-context scheming. arXiv:2412.04984. ‡ (abstract)'],
('MacDiarmid','2025'):['- MacDiarmid, M., Wright, B., Uesato, J., Benton, J., Kutasov, J., Price, S. et al. 2025. Natural emergent misalignment from reward hacking in production RL. arXiv:2511.18397. ‡ (abstract)'],
('Schlatter','2025'):['- Schlatter, J., Weinstein-Raun, B. and Ladish, J. 2025. Incomplete tasks induce shutdown resistance in some frontier LLMs. arXiv:2509.14260; *Transactions on Machine Learning Research* (2026). ‡ (abstract)'],
('van','2024'):['- van der Weij, T., Hofstätter, F., Jaffe, O., Brown, S. F. and Ward, F. R. 2024. AI sandbagging: language models can strategically underperform on evaluations. arXiv:2406.07358. ‡ (abstract)'],
('Li','2026'):["- Li, X., Ochwang'i, K., Bharadwaj, A. R., Souly, A. and Kirk, R. 2026. EvalDetectBench: a benchmark for measuring evaluation awareness in frontier language models. arXiv:2609.01611. ‡ (abstract)"],
('Stix','2025'):['- Stix, C., Pistillo, M., Sastry, G., Hobbhahn, M., Ortega, A., Balesni, M. et al. 2025. AI behind closed doors: a primer on the governance of internal deployment. arXiv:2504.12170. ‡ (abstract)'],
('Davidson','2025'):['- Davidson, T., Finnveden, L. and Hadshar, R. 2025. *AI-Enabled Coups: How a Small Group Could Use AI to Seize Power*. Forethought, April. ‡ (page)'],
('Taylor','2016'):['- Taylor, J. 2016. Quantilizers: a safer alternative to maximizers for limited optimization. *AAAI-16 Workshop on AI, Ethics, and Society*. ‡ (page)'],
('Soares','2015'):['- Soares, N., Fallenstein, B., Yudkowsky, E. and Armstrong, S. 2015. Corrigibility. *AAAI-15 Workshop on AI and Ethics*. ‡ (page)'],
('Thornley','2024'):['- Thornley, E. 2024. The shutdown problem: an AI engineering puzzle for decision theorists. *Philosophical Studies* 182(7):1653–1680 (online 2024). † (record)'],
('Baker','2025'):['- Baker, B., Huizinga, J., Gao, L., Dou, Z., Guan, M. Y., Madry, A. et al. 2025. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. arXiv:2503.11926. ‡ (abstract)'],
('Guan','2025'):['- Guan, M. Y., Wang, M., Carroll, M., Dou, Z., Wei, A. Y., Williams, M. et al. 2025. Monitoring monitorability. arXiv:2512.18311. ‡ (abstract)'],
('Bai','2022'):['- Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N. et al. 2022. Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv:2204.05862. † (record)'],
('Huang','2025'):['- Huang, T., Hu, S., Ilhan, F., Tekin, S. F., Yahn, Z., Xu, Y. et al. 2025. Safety tax: safety alignment makes your large reasoning models less reasonable. arXiv:2503.00555. † (record)'],
('Terekhov','2026'):['- Terekhov, M., Liu, Z. N. D., Gulcehre, C. and Albanie, S. 2026. Control tax: the price of keeping AI in check. *ICLR 2026*; arXiv:2506.05296 (2025). † (record; venue confirmed on the ICLR 2026 site)'],
('Sharma','2023'):['- Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R. et al. 2023. Towards understanding sycophancy in language models. arXiv:2310.13548. † (record)'],
('Williams','2025'):['- Williams, M., Carroll, M., Narang, A., Weisser, C., Murphy, B. and Dragan, A. 2025. On targeted manipulation and deception when optimizing LLMs for user feedback. *ICLR 2025*; arXiv:2411.02306. † (record)'],
('Panickssery','2024'):['- Panickssery, A., Bowman, S. R. and Feng, S. 2024. LLM evaluators recognize and favor their own generations. arXiv:2404.13076. † (record)'],
('Gardner-Challis','2026'):['- Gardner-Challis, N., Bostock, J., Kozhevnikov, G., Sinclaire, M., Velja, J., Abate, A. et al. 2026. When can we trust untrusted monitoring? A safety case sketch across collusion strategies. arXiv:2602.20628. † (record)'],
('Goldowsky-Dill','2025'):['- Goldowsky-Dill, N., Chughtai, B., Heimersheim, S. and Hobbhahn, M. 2025. Detecting strategic deception using linear probes. arXiv:2502.03407. † (record)'],
('Brown-Cohen','2025'):['- Brown-Cohen, J., Irving, G., Piliouras, G., Chen, L., Li, J. and Xun, Z. 2025. Avoiding obfuscation with prover-estimator debate. arXiv:2506.13609. † (record)'],
('Calvano','2020'):['- Calvano, E., Calzolari, G., Denicolò, V. and Pastorello, S. 2020. Artificial intelligence, algorithmic pricing, and collusion. *American Economic Review* 110(10):3267–3297. † (record)'],
('Fish','2024'):['- Fish, S., Gonczarowski, Y. A. and Shorrer, R. I. 2024. Algorithmic collusion by large language models. arXiv:2404.00806 (EC 2026). † (record)'],
('Khan','2024'):['- Khan, A., Hughes, J., Valentine, D., Ruis, L., Sachan, K., Radhakrishnan, A. et al. 2024. Debating with more persuasive LLMs leads to more truthful answers. *ICML 2024*; arXiv:2402.06782. † (record)'],
('Kenton','2024'):['- Kenton, Z., Siegel, N. Y., Kramár, J., Brown-Cohen, J., Albanie, S., Bulian, J. et al. 2024. On scalable oversight with weak LLMs judging strong LLMs. *NeurIPS 2024*; arXiv:2407.04622. † (record)'],
('Anwar','2026'):['- Anwar, U., Bakker, T., Kianfar, D., Pinneri, C. and Louizos, C. 2026. Analyzing and improving chain-of-thought monitorability through information theory. arXiv:2602.18297. † (record)'],
# not in D4; cited by the V6.2 Supplement; records confirmed on Crossref, 4 October 2026
('Cho','1987'):['- Cho, I.-K. and Kreps, D. M. 1987. Signaling games and stable equilibria. *Quarterly Journal of Economics* 102(2):179–221. † (record)'],
('Wald','1945'):['- Wald, A. 1945. Sequential tests of statistical hypotheses. *Annals of Mathematical Statistics* 16(2):117–186. † (record)'],
# V6.2 verification round (reviews/FIXES-v6.2-verify.md): works added to the core, the Supplement and the registers, with
# records retrieved on 4 October 2026 (arXiv API, Crossref, or the page itself), and two corrections of detail
('Bailey','2024'):['- Bailey, L., Serrano, A., Sheshadri, A., Seleznyov, M., Taylor, J., Jenner, E. et al. 2024. Obfuscated activations bypass LLM latent-space defenses. arXiv:2412.09565. ‡ (abstract)'],
('McGuinness','2025'):['- McGuinness, M., Serrano, A., Bailey, L. and Emmons, S. 2025. Neural chameleons: language models can learn to hide their thoughts from unseen activation monitors. arXiv:2512.11949. ‡ (abstract)'],
('Narayanan','2025'):['- Narayanan, A. and Kapoor, S. 2025. AI as normal technology. Knight First Amendment Institute at Columbia University, 15 April. ‡ (page)'],
('Ding','2024'):['- Ding, J. 2024. *Technology and the Rise of Great Powers: How Diffusion Shapes Economic Competition*. Princeton University Press. † (record)'],
('Acemoglu','2019'):['- Acemoglu, D. and Restrepo, P. 2019. Automation and new tasks: how technology displaces and reinstates labor. *Journal of Economic Perspectives* 33(2):3–30. † (record)'],
('Zhu','2026'):['- Zhu, L. Y. 2026. Silent revision: measuring undisclosed change in the safety frameworks of frontier AI developers. arXiv:2609.08789. ‡ (abstract)'],
('Bingham','1987'):['- Bingham, N. H., Goldie, C. M. and Teugels, J. L. 1987. *Regular Variation*. Encyclopedia of Mathematics and its Applications 27. Cambridge University Press. † (record)'],
('Weitzman','1974'):['- Weitzman, M. L. 1974. Prices vs. quantities. *Review of Economic Studies* 41(4):477–491. † (record)'],
('Kulveit','2025'):['- Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D. and Duvenaud, D. 2025. Position: humanity faces existential risk from gradual disempowerment. *ICML 2025* (position paper track), PMLR 267:81678–81688; arXiv:2501.16946. ‡ (abstract)'],
('Thornley','2024'):['- Thornley, E. 2024. The shutdown problem: an AI engineering puzzle for decision theorists. *Philosophical Studies* 182(7):1653–1680, 2025 (online 2024). † (record)'],
}
for k,v in D4.items(): E[k]=v
# V7.2 inherited lineage for correction through institutional change.
# Retrieval supports the component claims, not a completed institutional design.
E[('Frank','1995a')] = [line.replace(' 1995.', ' 1995a.') for line in E.pop(('Frank','1995'))]
E[('Frank','1995b')] = ['- Frank, S. A. 1995b. Mutual policing and repression of competition in the evolution of cooperative groups. *Nature* 377:520–522. [Author PDF](https://stevefrank.org/reprints-pdf/95Nature-Police.pdf). ‡ (PDF; competition and policing model)']
E[('Soares','2015')] = ['- Soares, N., Fallenstein, B., Yudkowsky, E. and Armstrong, S. 2015. Corrigibility. *AAAI-15 Workshop on AI and Ethics*. [Paper](https://intelligence.org/files/Corrigibility.pdf). ‡ (PDF; definition and successor desiderata, Section 1.1)']
E[('Carey','2023')] = ['- Carey, R. and Everitt, T. 2023. Human control: definitions and algorithms. *Proceedings of Machine Learning Research* 216:271–281. [Proceedings page](https://proceedings.mlr.press/v216/carey23a.html). ‡ (abstract)']
E[('Ames','2017')] = ['- Ames, A. D., Xu, X., Grizzle, J. W. and Tabuada, P. 2017. Control barrier function based quadratic programs for safety critical systems. *IEEE Transactions on Automatic Control* 62(8):3861–3876. [Paper](https://arxiv.org/abs/1609.06408). ‡ (abstract; publication details checked against IEEE)']
E[('Ostrom','2007')] = ['- Ostrom, E. 2007. A diagnostic approach for going beyond panaceas. *Proceedings of the National Academy of Sciences* 104(39):15181–15187. [Article](https://www.pnas.org/doi/10.1073/pnas.0702288104). ‡ (full text; diagnostic framework and adaptive institutional development)']
E[('Meng','2021')] = ['- Meng, Y., Li, Y., Fitzsimmons, M. and Liu, J. 2021. Smooth converse Lyapunov-barrier theorems for asymptotic stability with safety constraints and reach-avoid-stay specifications. arXiv:2009.04432v2, revised 31 December. [Paper](https://arxiv.org/html/2009.04432v2). ‡ (full text; introduction and Section 2.1, Definition 2)']
# Maynard Smith and Szathmary 1995 must be in the data (it was lost to a key collision in v6.1)
assert any('Maynard Smith, J. and Szathmáry, E. 1995. *The Major Transitions in Evolution*. W. H. Freeman' in x for x in E.get(('Maynard','1995'),[]))
_n={}
for l in {x for ls in E.values() for x in ls}:
    p=_parse_entry(l)
    if p and (p[1] or len(p[0])>=3):
        for yr in p[2]: _n[(p[0][0], yr)]=_n.get((p[0][0], yr),0)+1
SHARED.update(k for k,c in _n.items() if c>1)
B={}                                     # {(first, second|'et al.'|'', year): [lines]}
for ls in E.values():
    for l in ls:
        for k in entry_keys(l):
            if l not in B.setdefault(k,[]): B[k].append(l)
def build(doc):
    t=(V61/f'{doc}.md').read_text().split('\n## References')[0]
    cited=citations(t)
    keys={k for k in cited if k in B}; loose=[]; nodata=[]
    for k,v in cited.items():
        if k in B: continue
        near=loose_match(k, B)
        if near: keys.add(near); loose.append(f'{v} -> {B[near][0][2:50]}…')
        else: nodata.append(v)
    if 'Why Nations Fail' in t: keys.add(('Acemoglu','Robinson','2012'))
    items=sorted({legend_form(x) for k in keys for x in B[k]}, key=lambda s: re.sub(r'[*《]','',s).lower())
    return items, sorted(nodata), sorted(loose)
def legend_form(line):
    """Every mark in a form the legend defines (verification round, E16): a bare dagger is a work carried from v6.0
    without a recorded check, read as not retrieved; a bare double dagger, one whose existence and identifier the v6.0
    evidence review checked without recording what was read; four forms outside the legend are mapped onto it."""
    for o,n in ((' † (pages per the v6.1 evidence review)',' † (record)'),(' ‡ (abstract record)',' ‡ (abstract)'),
                (' † (record of the volume)',' † (record)'),(' ‡ (full text and page)',' ‡ (full text)')):
        if line.endswith(o): line=line[:-len(o)]+n
    if line.endswith(' †'): line+=' (not retrieved)'
    elif line.endswith(' ‡'): line+=' (identifier)'
    return line
head="""## References

Marks: ‡ works whose existence and identifier were checked ("full text", "page" or "abstract" says what was read, on 3 or 4 October 2026; "identifier": existence and identifier only, checked by the v6.0 evidence review, which did not record what was read); † works not yet independently verified ("record": the bibliographic record was retrieved; "not retrieved": from prior knowledge, including works carried from v6.0 without a recorded check); unmarked works carried from the verified bibliography of v3.1. A note may follow the qualifier after a semicolon. The forms are those of EVIDENCE.md, where sources of observations are listed with dates and links.

"""
if __name__=='__main__':
    for k,ls in B.items():
        if len(ls)>1: print('  two entries share the key',k,':',' | '.join(x[:60] for x in ls))
    for doc,folder in [('THEORY','core'),('SUPPLEMENT','supp'),('DISCUSSION','disc')]:
        items,nodata,loose=build(doc)
        (V61/'src'/folder/'z9_refs.md').write_text(head+'\n'.join(items)+'\n')
        print(doc,len(items),'entries' + (f'; cited with no entry in the data: {"; ".join(nodata)}' if nodata else '')
              + (f'; listed, but the citation\'s author form differs from the entry: {"; ".join(loose)}' if loose else ''))
