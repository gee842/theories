# Verified references for Selecting the Selectors (v3)

Checked 2026-10-02. I verified each item against publisher metadata (Crossref API), PubMed, the arXiv API, PMLR, the ACL Anthology, NeurIPS proceedings, RePEc or OpenAlex abstracts, or the primary document itself (PDF downloaded and text-searched). I did not edit `references.bib`.

**Note on the style file.** `aaai2027.bst` reads only these fields: address, archivePrefix, author, booktitle, chapter, edition, editor, eid, eprint, howpublished, institution, isbn, journal, key, month, note, number, organization, pages, publisher, school, series, title, type, volume, year. It ignores `doi` and `url`. I left `doi`/`url` in the entries because they cost nothing and help readers. For web-only policy documents, the URL is in `howpublished` as `\url{...}`. `main.tex` already loads `[hyphens]{url}`.

## Problems found, at a glance

| Key | Problem |
|---|---|
| `laurito2025` | Missing author Ada B{\"o}hm (5th of 6). Missing `number = {31}`. |
| `goel2025` | Missing pages 19621--19678. The PMLR author spellings are "Karuna K Chandra" and "Ameya Prabhu", not "Ameya Pandurang Prabhu". |
| `greenblatt2024` | Missing pages 16295--16336. |
| `narechania2024` | Missing number 1 and pages 95--170. |
| `kwak2014` | Year wrong: the chapter is in the 2013 Cambridge volume (print 21 Oct 2013; online 2014). Should be 2013, matching `carpenter2013`. |
| `abdalla2021` | Wrong entry type. It is an `@inproceedings` (ACM, DOI 10.1145/3461702.3462563). |
| `euaiact2024` | The OJ reference is missing. Note also that the AI Act was amended by Reg. (EU) 2026/1744 (the "Digital Omnibus on AI", OJ 24 July 2026). |
| `carpenter2008` | Bibliographic data correct. **Gloss must be deadline effects**, not funding dependence (see Task 2). |
| `buthe2011` | Bibliographic data correct. **The gloss must be institutional complementarity**: standard-setting is political, and influence depends on how well domestic institutions fit the international private standard-setters. Firm expertise is not the explanation. |
| `armstrong2016` | Correct. DOI can be added. |
| `whitehouse2025` (new) | The document cover says "Winning the Race: America's AI Action Plan". The White House press release says "Winning the **AI** Race". Use the cover title. |
| `statecouncil2017` (new) | China's 2017 plan does **not** use "race". It says AI is "a new focus of international competition" and aims at "first-mover advantage" and being "the world's primary AI innovation center". The current sentence in `main.tex` ("described by governments as a race to be won") is literally true only of the US text (see Task 3a). |
| `panchanathan2004` (new) | Their result is that exclusion is stable *but cannot invade*. "Solves" overstates it. |

---

# TASK 1: New entries

### hurwicz2008: VERIFIED
Checked: Crossref (10.1257/aer.98.3.577); RePEc; full lecture text (https://www.nobelprize.org/uploads/2018/06/hurwicz_lecture.pdf).
```bibtex
@article{hurwicz2008,
  author  = {Hurwicz, Leonid},
  title   = {But Who Will Guard the Guardians?},
  journal = {American Economic Review},
  volume  = {98},
  number  = {3},
  pages   = {577--585},
  year    = {2008},
  doi     = {10.1257/aer.98.3.577}
}
```
**Establishes:** This is the Nobel lecture of 8 Dec 2007. It models enforcement as a "true game" that contains both legal and illegal strategies. Enforcement succeeds when the outcomes make illegal strategies less attractive. Hurwicz argues that the regress of guardians need not be infinite: "intervenors" (guardians who endorse the rules), voters acting as top-level guardians, and designed reward and punishment systems can close it. *Gloss note:* his answer is cautiously optimistic, not a claim that guarding the guardians is impossible.

### schaffer1988: VERIFIED
Checked: Crossref (10.1016/S0022-5193(88)80085-7); PubMed abstract (PMID 3226137).
```bibtex
@article{schaffer1988,
  author  = {Schaffer, Mark E.},
  title   = {Evolutionarily Stable Strategies for a Finite Population and a Variable Contest Size},
  journal = {Journal of Theoretical Biology},
  volume  = {132},
  number  = {4},
  pages   = {469--478},
  year    = {1988},
  doi     = {10.1016/S0022-5193(88)80085-7}
}
```
**Establishes:** The paper extends the ESS concept to finite populations and variable contest size. In a finite population the ESS player is "spiteful": it acts to raise its own payoff and lower its competitors'. The spite grows as the population shrinks. *Gloss note:* "maximizes relative payoff" is a fair restatement, but the paper's own word is "spiteful". Schaffer states the firm-level version explicitly in Schaffer (1989), "Are profit-maximisers the best survivors? A Darwinian model of economic natural selection", *J. Economic Behavior & Organization* 12(1):29--45, DOI 10.1016/0167-2681(89)90075-9. I verified that entry's bibliographic data, but no abstract was available, so read it before citing it.

### vegaredondo1997: VERIFIED
Checked: Crossref (10.2307/2171898); RePEc abstract.
```bibtex
@article{vegaredondo1997,
  author  = {Vega-Redondo, Fernando},
  title   = {The Evolution of {Walrasian} Behavior},
  journal = {Econometrica},
  volume  = {65},
  number  = {2},
  pages   = {375--384},
  year    = {1997},
  doi     = {10.2307/2171898}
}
```
**Establishes:** In a symmetric Cournot oligopoly where firms imitate the most profitable firm, with rare experimentation, the unique long-run outcome is that every firm produces the Walrasian (price-taking) output. That output is above Cournot--Nash and lowers joint profit. It wins because it maximizes profit *relative* to rivals.

### alchian1950: VERIFIED
Checked: Crossref (10.1086/256940); full text searched (gwern.net scan of the JPE article).
```bibtex
@article{alchian1950,
  author  = {Alchian, Armen A.},
  title   = {Uncertainty, Evolution, and Economic Theory},
  journal = {Journal of Political Economy},
  volume  = {58},
  number  = {3},
  pages   = {211--221},
  year    = {1950},
  doi     = {10.1086/256940}
}
```
**Establishes:** Under uncertainty, market selection on realized positive profits replaces profit maximization as the explanatory principle. Survival depends on a firm's position relative to its actual competitors, not on optimality; Alchian's phrase is "relative superiority". Imitation and trial and error are the adaptive mechanisms. Your gloss ("selection rewards relative, not absolute, performance") is accurate.

### frank1985: VERIFIED (bibliographic data)
Checked: Open Library record; title and subtitle confirmed by 1986 reviews in Crossref (*Contemporary Sociology* 10.2307/2070056; *Southern Economic Journal* 10.2307/1059455).
```bibtex
@book{frank1985,
  author    = {Frank, Robert H.},
  title     = {Choosing the Right Pond: Human Behavior and the Quest for Status},
  publisher = {Oxford University Press},
  address   = {New York},
  year      = {1985}
}
```
**Establishes:** People care about their rank within a local reference group (the "pond"). Concern for position shapes wages and consumption, and positional competition is individually rational but collectively wasteful. That makes collective restraints on it potentially welfare-improving. (I took this gloss from the book's well-known argument; I did not re-read the text.)

### hirsch1976: VERIFIED
Checked: Crossref (HUP digital edition 10.4159/harvard.9780674497900); *APSR* 1978 review (10.2307/1955201) confirms "Cambridge, Mass.: Harvard University Press, 1976" and the Twentieth Century Fund Study label. The UK edition is Routledge & Kegan Paul, 1977.
```bibtex
@book{hirsch1976,
  author    = {Hirsch, Fred},
  title     = {Social Limits to Growth},
  publisher = {Harvard University Press},
  address   = {Cambridge, MA},
  year      = {1976},
  note      = {A Twentieth Century Fund Study}
}
```
**Establishes:** Positional goods are scarce in absolute terms or valued for relative standing, so economic growth cannot multiply them. As material affluence rises, competition shifts toward them and becomes zero-sum. Hirsch also argues that market individualism depletes the inherited social norms (the "depleting moral legacy") that markets depend on. Your gloss ("positional concern undermines shared goods") is fair.

### hardin1968: VERIFIED
Checked: Crossref (10.1126/science.162.3859.1243).
```bibtex
@article{hardin1968,
  author  = {Hardin, Garrett},
  title   = {The Tragedy of the Commons},
  journal = {Science},
  volume  = {162},
  number  = {3859},
  pages   = {1243--1248},
  year    = {1968},
  doi     = {10.1126/science.162.3859.1243}
}
```
**Establishes:** In an open-access commons, each user keeps the gain from extra exploitation while the cost is shared, so individually rational use ruins the resource. Hardin argues there is no technical solution and calls for "mutual coercion mutually agreed upon".

### ostrom1990: VERIFIED
Checked: Crossref (10.1017/CBO9780511807763, issued 30 Nov 1990).
```bibtex
@book{ostrom1990,
  author    = {Ostrom, Elinor},
  title     = {Governing the Commons: The Evolution of Institutions for Collective Action},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {1990},
  doi       = {10.1017/CBO9780511807763}
}
```
**Establishes:** Field cases show that users can govern common-pool resources sustainably for long periods without privatization or central control. They do it through self-made institutions with recurring design principles, including clear boundaries, accountable monitoring, graduated sanctions and conflict-resolution arenas. Hardin's tragedy is therefore not inevitable.

### yamagishi1986: VERIFIED
Checked: Crossref (10.1037/0022-3514.51.1.110); abstract via Semantic Scholar and search.
```bibtex
@article{yamagishi1986,
  author  = {Yamagishi, Toshio},
  title   = {The Provision of a Sanctioning System as a Public Good},
  journal = {Journal of Personality and Social Psychology},
  volume  = {51},
  number  = {1},
  pages   = {110--116},
  year    = {1986},
  doi     = {10.1037/0022-3514.51.1.110}
}
```
**Establishes:** A sanctioning system is itself a public good, which is the second-order problem. In an experiment with 48 four-person groups, people contributed to a system that punished the least cooperative member. They did so mainly once they recognized that voluntary cooperation would fail, and the sanctioning system raised cooperation.

### heckathorn1989 and oliver1980: both VERIFIED. Cite both.
Checked: Crossref (10.1177/1043463189001001006; 10.1086/227168); OpenAlex abstracts; Oliver's full text (https://users.ssc.wisc.edu/~peoliver/PROTESTS/ArticleCopies/Oliver1980AJSRewardsPunishSelectiveIncentive.pdf).
```bibtex
@article{heckathorn1989,
  author  = {Heckathorn, Douglas D.},
  title   = {Collective Action and the Second-Order Free-Rider Problem},
  journal = {Rationality and Society},
  volume  = {1},
  number  = {1},
  pages   = {78--100},
  year    = {1989},
  doi     = {10.1177/1043463189001001006}
}

@article{oliver1980,
  author  = {Oliver, Pamela},
  title   = {Rewards and Punishments as Selective Incentives for Collective Action: Theoretical Investigations},
  journal = {American Journal of Sociology},
  volume  = {85},
  number  = {6},
  pages   = {1356--1375},
  year    = {1980},
  doi     = {10.1086/227168}
}
```
**Which is standard:** Both are standard and usually cited together, often with Yamagishi 1986. **Oliver 1980** is the origin. On p. 1361 she observes that using a selective incentive is itself collective action that provides a public good, although she does not use the term "second-order". **Heckathorn 1989** is the eponymous formal treatment.
**Heckathorn establishes:** He models first- and second-order free riding in collective sanction systems. Second-order cooperation (sanctioning) turns out surprisingly robust relative to first-order cooperation, and "hypocritical" cooperation, which supports sanctions while defecting, may be a transitional route to collective action.
**Oliver establishes:** Positive and negative selective incentives have different structural effects. Rewards suit small "elite" actions; punishments suit unanimity but are applied unevenly and cyclically. Applying either is itself a public-good problem.

### panchanathan2004: VERIFIED. Gloss needs care.
Checked: Crossref (10.1038/nature02978); PubMed abstract (PMID 15565153).
```bibtex
@article{panchanathan2004,
  author  = {Panchanathan, Karthik and Boyd, Robert},
  title   = {Indirect Reciprocity Can Stabilize Cooperation without the Second-Order Free Rider Problem},
  journal = {Nature},
  volume  = {432},
  number  = {7016},
  pages   = {499--502},
  year    = {2004},
  doi     = {10.1038/nature02978}
}
```
**Establishes:** The model links collective action to indirect reciprocity: people who free-ride lose good standing and are refused help. That linkage is evolutionarily stable, and it avoids the second-order problem because withholding help does not damage the punisher's reputation. **But** the authors also show that the strategy *cannot invade* a population where indirect reciprocity is not linked to collective action, so how collective action arises stays unexplained. Say "can stabilize", not "solves".

### askell2019: VERIFIED
Checked: arXiv API (1907.04534, v1, 10 Jul 2019; no journal reference).
```bibtex
@article{askell2019,
  author  = {Askell, Amanda and Brundage, Miles and Hadfield, Gillian},
  title   = {The Role of Cooperation in Responsible {AI} Development},
  journal = {arXiv preprint arXiv:1907.04534},
  year    = {2019}
}
```
**Establishes:** Competitive pressure could lead AI companies to underinvest in making systems safe, secure and socially beneficial. Responsible development is therefore a collective action problem among companies. The paper identifies factors that improve the prospects for cooperation and proposes strategies for industry cooperation.

### aubin1991: VERIFIED (1991 Birkhäuser edition)
Checked: ISBN 978-0-8176-3571-8 and the series name via the ACM DL and Amazon catalog records (https://dl.acm.org/doi/10.5555/120830). Crossref holds only the 2009 Birkhäuser reprint (DOI 10.1007/978-0-8176-4910-4, ISBNs 9780817649098/9780817649104). I could not open Springer to confirm it is an unaltered reprint, so I left the DOI out.
```bibtex
@book{aubin1991,
  author    = {Aubin, Jean-Pierre},
  title     = {Viability Theory},
  series    = {Systems \& Control: Foundations \& Applications},
  publisher = {Birkh{\"a}user},
  address   = {Boston},
  year      = {1991}
}
```
**Establishes:** Viability theory treats dynamical (possibly set-valued) systems under state constraints. It characterizes the *viability kernel*, the set of states from which at least one evolution stays in the constraint set forever, through tangential conditions, and it builds regulation maps that select viable controls. This fits "the language of floors".

### rockstrom2009: VERIFIED
Checked: Crossref and PubMed (10.1038/461472a, PMID 19779433; 29 authors); Stockholm Resilience Centre summary.
```bibtex
@article{rockstrom2009,
  author  = {Rockstr{\"o}m, Johan and Steffen, Will and Noone, Kevin and Persson, {\AA}sa and Chapin, III, F. Stuart and Lambin, Eric F. and Lenton, Timothy M. and Scheffer, Marten and Folke, Carl and Schellnhuber, Hans Joachim and Nykvist, Bj{\"o}rn and de Wit, Cynthia A. and Hughes, Terry and van der Leeuw, Sander and Rodhe, Henning and S{\"o}rlin, Sverker and Snyder, Peter K. and Costanza, Robert and Svedin, Uno and Falkenmark, Malin and Karlberg, Louise and Corell, Robert W. and Fabry, Victoria J. and Hansen, James and Walker, Brian and Liverman, Diana and Richardson, Katherine and Crutzen, Paul and Foley, Jonathan A.},
  title   = {A Safe Operating Space for Humanity},
  journal = {Nature},
  volume  = {461},
  number  = {7263},
  pages   = {472--475},
  year    = {2009},
  doi     = {10.1038/461472a}
}
```
**Establishes:** The paper proposes nine Earth-system "planetary boundaries" that together define a safe operating space for humanity. It estimates that three (climate change, rate of biodiversity loss and the nitrogen cycle) had already been crossed. Truncating to `Rockstr{\"o}m, Johan and others` is fine if space is short.

### wced1987: VERIFIED
Checked: Open Library (Oxford University Press); the publication facts are standard (UN-commissioned Brundtland report, Oxford UP, 1987).
```bibtex
@book{wced1987,
  author    = {{World Commission on Environment and Development}},
  title     = {Our Common Future},
  publisher = {Oxford University Press},
  address   = {Oxford},
  year      = {1987}
}
```
**Establishes:** This is the Brundtland report. It defines sustainable development as development that meets present needs without compromising future generations' ability to meet theirs, and argues that environment and development must be treated together and internationally.

### skyrms2004: VERIFIED
Checked: Crossref (10.1017/CBO9781139165228; print date given as 15 Dec 2003); reviews in *Ethics* and *Economics & Philosophy* cite "Cambridge University Press, 2004". Use 2004, the year on the book and the one everyone cites.
```bibtex
@book{skyrms2004,
  author    = {Skyrms, Brian},
  title     = {The Stag Hunt and the Evolution of Social Structure},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2004},
  doi       = {10.1017/CBO9781139165228}
}
```
**Establishes:** Skyrms takes the stag hunt, not the prisoner's dilemma, as the model of the social contract. He shows how location (local interaction), signaling and association (network formation) can move populations from the safe "hare" equilibrium to the cooperative "stag" equilibrium.

### laffont1991: VERIFIED
Checked: Crossref (10.2307/2937958); abstract via Semantic Scholar.
```bibtex
@article{laffont1991,
  author  = {Laffont, Jean-Jacques and Tirole, Jean},
  title   = {The Politics of Government Decision-Making: A Theory of Regulatory Capture},
  journal = {Quarterly Journal of Economics},
  volume  = {106},
  number  = {4},
  pages   = {1089--1127},
  year    = {1991},
  doi     = {10.2307/2937958}
}
```
**Establishes:** This is an agency-theoretic model of capture. The optimal organizational response to possible capture is to reduce interest groups' stakes in regulation, for example through lower-powered incentive schemes for regulated firms. An interest group has more power when it gains from *inefficient* regulation, where inefficiency is measured by the information asymmetry between the industry and the political principal.

### krakauer2009: VERIFIED
Checked: Crossref and PubMed (10.1086/593707, PMID 19061421; Am Nat 173(1), Jan 2009).
```bibtex
@article{krakauer2009,
  author  = {Krakauer, David C. and Page, Karen M. and Erwin, Douglas H.},
  title   = {Diversity, Dilemmas, and Monopolies of Niche Construction},
  journal = {The American Naturalist},
  volume  = {173},
  number  = {1},
  pages   = {26--40},
  year    = {2009},
  doi     = {10.1086/593707}
}
```
**Establishes:** Building a *shared* resource creates a tragedy of the commons: competition tends to eliminate niche-construction strategies. Being able to *monopolize* the niche, through spatial proximity or preferential exploitation, stabilizes niche construction and lets constructors coexist. This directly supports your "selected when its benefits are appropriable".

### lehmann2008: VERIFIED
Checked: Crossref and PubMed (10.1111/j.1558-5646.2007.00291.x, PMID 17983464).
```bibtex
@article{lehmann2008,
  author  = {Lehmann, Laurent},
  title   = {The Adaptive Dynamics of Niche Constructing Traits in Spatially Subdivided Populations: Evolving Posthumous Extended Phenotypes},
  journal = {Evolution},
  volume  = {62},
  number  = {3},
  pages   = {549--566},
  year    = {2008},
  doi     = {10.1111/j.1558-5646.2007.00291.x}
}
```
**Establishes:** This is an inclusive-fitness analysis of niche-constructing traits. Effects that outlast the actor can be selected if they change the fitness of future individuals likely to share the actor's lineage. Present benefits trade off against future indirect costs, as illustrated by consumption of an abiotic resource that feeds back on later selection. It supports "appropriable" in the sense of benefits flowing back to the constructor's lineage.

### olson1965: VERIFIED (bibliographic data)
Checked: Crossref (HUP record 10.4159/9780674041660, dated 1965); Open Library.
```bibtex
@book{olson1965,
  author    = {Olson, Mancur},
  title     = {The Logic of Collective Action: Public Goods and the Theory of Groups},
  publisher = {Harvard University Press},
  address   = {Cambridge, MA},
  year      = {1965}
}
```
**Establishes:** Rational, self-interested members of large ("latent") groups will not act for their common interest unless coerced or offered separate selective incentives. Small groups organize more easily, which explains why concentrated interests outorganize diffuse ones.

### teece1986: VERIFIED
Checked: Crossref (10.1016/0048-7333(86)90027-2).
```bibtex
@article{teece1986,
  author  = {Teece, David J.},
  title   = {Profiting from Technological Innovation: Implications for Integration, Collaboration, Licensing and Public Policy},
  journal = {Research Policy},
  volume  = {15},
  number  = {6},
  pages   = {285--305},
  year    = {1986},
  doi     = {10.1016/0048-7333(86)90027-2}
}
```
**Establishes:** Who profits from an innovation depends on how easily it can be imitated (the "appropriability regime") and on who controls the complementary assets needed to commercialize it. When imitation is easy, imitators or owners of complementary assets can capture the returns instead of the innovator.

### lizzeri1999: VERIFIED
Checked: Crossref (10.2307/2556078); RePEc (pp. 214--231); OpenAlex abstract.
```bibtex
@article{lizzeri1999,
  author  = {Lizzeri, Alessandro},
  title   = {Information Revelation and Certification Intermediaries},
  journal = {RAND Journal of Economics},
  volume  = {30},
  number  = {2},
  pages   = {214--231},
  year    = {1999},
  doi     = {10.2307/2556078}
}
```
**Establishes:** A *monopoly* certifier's optimal policy, in a class of environments, is to reveal only whether quality clears a minimal standard, and it can still capture a large share of the surplus. *Competition* among certifiers can restore full revelation. *Gloss note:* your current wording in `main.tex` ("face conflicts with those they rate") fits Bolton et al. better than Lizzeri, whose point is that certifiers have an incentive to coarsen what they disclose. The two papers also disagree on whether competition helps: Lizzeri says it can, Bolton et al. say it can hurt.

### bolton2012: VERIFIED
Checked: Crossref (10.1111/j.1540-6261.2011.01708.x; pages 85--111); RePEc abstract. RePEc gives the pages as 85--112; I used the publisher's Crossref deposit.
```bibtex
@article{bolton2012,
  author  = {Bolton, Patrick and Freixas, Xavier and Shapiro, Joel},
  title   = {The Credit Ratings Game},
  journal = {Journal of Finance},
  volume  = {67},
  number  = {1},
  pages   = {85--111},
  year    = {2012},
  doi     = {10.1111/j.1540-6261.2011.01708.x}
}
```
**Establishes:** The model has two conflicts: rating agencies understate risk to win business, and issuers buy only the most favorable ratings ("shopping"). Inflation is worse when more investors are naive and in booms. Competition among agencies can *reduce* efficiency because it makes shopping easier.

### espeland2007: VERIFIED
Checked: Crossref (10.1086/517897); OpenAlex abstract.
```bibtex
@article{espeland2007,
  author  = {Espeland, Wendy Nelson and Sauder, Michael},
  title   = {Rankings and Reactivity: How Public Measures Recreate Social Worlds},
  journal = {American Journal of Sociology},
  volume  = {113},
  number  = {1},
  pages   = {1--40},
  year    = {2007},
  doi     = {10.1086/517897}
}
```
**Establishes:** Using US law-school rankings, the authors show that public measures change the institutions they measure ("reactivity"). The two mechanisms are self-fulfilling prophecy and commensuration.

### schlag1998: VERIFIED
Checked: Crossref (10.1006/jeth.1997.2347; Crossref has the main title only); RePEc and Semantic Scholar give the subtitle.
```bibtex
@article{schlag1998,
  author  = {Schlag, Karl H.},
  title   = {Why Imitate, and If So, How? {A} Boundedly Rational Approach to Multi-armed Bandits},
  journal = {Journal of Economic Theory},
  volume  = {78},
  number  = {1},
  pages   = {130--156},
  year    = {1998},
  doi     = {10.1006/jeth.1997.2347}
}
```
**Establishes:** Consider individuals in a finite population who each observe one other person's action and payoff. Among simple rules that always improve expected payoff, the best is to imitate a better-performing person with probability proportional to how much better they did. In aggregate this "proportional imitation" yields the replicator dynamic. Your use ("pairwise imitation") is correct.

### kwa2025: VERIFIED. The title changed, and the 7-month figure is confirmed.
Checked: arXiv API (2503.14499; v1 titled "Measuring AI Ability to Complete Long Tasks"; v4 titled "...Long Software Tasks"; journal reference "NeurIPS 2025"); NeurIPS 2025 proceedings page (https://proceedings.neurips.cc/paper_files/paper/2025/hash/85069585133c4c168c865e65d72e9775-Abstract-Conference.html).
**Doubling:** The abstract says the 50% time horizon has been doubling "approximately every seven months since 2019", and adds that the trend "may have accelerated in 2024". The 2025 frontier figure is about 50 minutes for Claude 3.7 Sonnet in the arXiv text.
**Authors:** The NeurIPS page lists 25 authors. arXiv v4 adds Chris Painter (26), with the comment that this matches the listing in the PDF. I used the proceedings list below; add `Painter, Chris` after `Lin, Tao` if you follow arXiv.
```bibtex
@inproceedings{kwa2025,
  author    = {Kwa, Thomas and West, Ben and Becker, Joel and Deng, Amy and Garcia, Katharyn and Hasin, Max and Jawhar, Sami and Kinniment, Megan and Rush, Nate and Von Arx, Sydney and Bloom, Ryan and Broadley, Thomas and Du, Haoxing and Goodrich, Brian and Jurkovic, Nikola and Miles, Luke and Nix, Seraphina and Lin, Tao and Parikh, Neev and Rein, David and Sato, Lucas Jun Koba and Wijk, Hjalmar and Ziegler, Daniel and Barnes, Elizabeth and Chan, Lawrence},
  title     = {Measuring {AI} Ability to Complete Long Software Tasks},
  booktitle = {Advances in Neural Information Processing Systems 38},
  year      = {2025},
  note      = {arXiv:2503.14499}
}
```
If you prefer the arXiv preprint: `journal = {arXiv preprint arXiv:2503.14499}`, title `Measuring {AI} Ability to Complete Long Tasks` (v1). **Establishes:** The paper defines the "50% task-completion time horizon": the length of task, measured in time taken by skilled humans, that a model completes with 50% success. For frontier models this has doubled roughly every 7 months since 2019 on the authors' software and research task suite, and the authors note limits on how well this transfers to real-world work.

### bengio2025report: VERIFIED. "Evidence dilemma" is present.
Checked: full PDF text (https://internationalaisafetyreport.org/sites/default/files/2025-10/international_ai_safety_report_2025_english.pdf); publication page (https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025; published 29 Jan 2025; the gov.uk page now redirects there). The cover reads "International AI Safety Report: The International Scientific Report on the Safety of Advanced AI, January 2025". "Research series number: DSIT 2025/001" appears on p. 6 and in the report's own "How to cite" (p. 229). (The back page of the PDF says "DSIT 2024/000", which is an internal inconsistency; use 2025/001, which the report itself recommends.) The report gives a 96-name author list in its "How to cite". The truncation below is standard.
```bibtex
@techreport{bengio2025report,
  author      = {Bengio, Yoshua and Mindermann, S{\"o}ren and Privitera, Daniel and others},
  title       = {International {AI} Safety Report},
  institution = {UK Department for Science, Innovation and Technology},
  type        = {Research series number},
  number      = {DSIT 2025/001},
  year        = {2025},
  url         = {https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025}
}
```
**Evidence dilemma, verbatim:** advances in general-purpose AI "pose an ‘evidence dilemma’ for policymakers" (Key findings, p. 14; also pp. 22, 109, 177). The surrounding text says that acting on limited evidence risks ineffective mitigations, while waiting for stronger evidence "could leave society unprepared".

### whitehouse2025: VERIFIED. Use the cover title.
Checked: the PDF itself (https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf; the cover reads "Winning the Race: AMERICA'S AI ACTION PLAN, JULY 2025, THE WHITE HOUSE"); press release dated 23 July 2025 (https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan), which calls it "Winning the AI Race: America's AI Action Plan".
```bibtex
@misc{whitehouse2025,
  author       = {{The White House}},
  title        = {Winning the Race: {America's} {AI} Action Plan},
  howpublished = {Washington, DC, 23 July 2025. \url{https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf}},
  year         = {2025}
}
```

### statecouncil2017: VERIFIED
Checked: Chinese original on gov.cn (https://www.gov.cn/zhengce/content/2017-07/20/content_5211996.htm): 国发〔2017〕35号 (Guofa [2017] No. 35), signed 8 July 2017, published 20 July 2017. English translation: DigiChina (https://digichina.stanford.edu/work/full-translation-chinas-new-generation-artificial-intelligence-development-plan-2017/), byline "Graham Webster, Rogier Creemers, Elsa Kania, Paul Triolo", first published by New America on 1 August 2017.
**2030 goal, verified in both languages:** the Chinese text has 成为世界主要人工智能创新中心. DigiChina translates the third step as China's AI "should achieve world-leading levels, making China the world's primary AI innovation center".
```bibtex
@misc{statecouncil2017,
  author       = {{State Council of the People's Republic of China}},
  title        = {New Generation Artificial Intelligence Development Plan},
  howpublished = {Guofa [2017] No.~35, issued 8 July 2017. English translation by G.~Webster, R.~Creemers, E.~Kania and P.~Triolo, DigiChina (New America), 1 August 2017. \url{https://digichina.stanford.edu/work/full-translation-chinas-new-generation-artificial-intelligence-development-plan-2017/}},
  year         = {2017}
}
```
I kept the Chinese title out of the `.bib` because CJK text may break pdflatex. Add `新一代人工智能发展规划` only if you load CJK support, which AAAI forbids.

### bletchley2023: VERIFIED. The US and China both signed.
Checked: gov.uk (https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023). The signatory list includes **China** and the **United States of America**, among 28 countries plus the EU. New Zealand joined on 23 Oct 2024.
```bibtex
@misc{bletchley2023,
  author       = {{Countries Attending the AI Safety Summit}},
  title        = {The {Bletchley} Declaration by Countries Attending the {AI} Safety Summit, 1--2 {November} 2023},
  howpublished = {UK Government, 1 November 2023. \url{https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration}},
  year         = {2023}
}
```

### china2023gaigi: VERIFIED. The 2025 Action Plan is real, so I added a separate entry for it.
Checked: MFA English text, "Global AI Governance Initiative", dated 20 Oct 2023 (https://www.fmprc.gov.cn/eng/wjb/zzjg_663340/jks_665232/kjlc_665236/AI/202405/t20240530_11332389.html). Xi Jinping announced it on 18 Oct 2023 at the Third Belt and Road Forum (MFA spokesperson's remarks). The text calls for a "testing and assessment system based on AI risk levels", opposes "exclusive groups" in AI development, and supports discussion within the UN of an international AI governance institution.
Also checked: "Global AI Governance Action Plan", released 26 July 2025 at the 2025 World AI Conference and High-Level Meeting on Global AI Governance in Shanghai (https://www.fmprc.gov.cn/eng/wjb/zzjg_663340/jks_665232/kjlc_665236/AI/202507/t20250729_11679232.html). It calls for building "a risk testing and evaluation system for AI". The word "race" does not appear.
```bibtex
@misc{china2023gaigi,
  author       = {{Ministry of Foreign Affairs of the People's Republic of China}},
  title        = {Global {AI} Governance Initiative},
  howpublished = {20 October 2023 (announced 18 October 2023). \url{https://www.fmprc.gov.cn/eng/wjb/zzjg_663340/jks_665232/kjlc_665236/AI/202405/t20240530_11332389.html}},
  year         = {2023}
}

@misc{china2025actionplan,
  author       = {{Ministry of Foreign Affairs of the People's Republic of China}},
  title        = {Global {AI} Governance Action Plan},
  howpublished = {Released at the 2025 World Artificial Intelligence Conference and High-Level Meeting on Global AI Governance, Shanghai, 26 July 2025. \url{https://www.fmprc.gov.cn/eng/wjb/zzjg_663340/jks_665232/kjlc_665236/AI/202507/t20250729_11679232.html}},
  year         = {2025}
}
```

### unga2024 (A/RES/78/265) and unga2024capacity (A/RES/78/311): both VERIFIED
Checked: both resolution PDFs (documents.un.org) and both draft PDFs. **78/265** was adopted 21 March 2024 without reference to a Main Committee (draft A/78/L.49), distributed 1 April 2024. The United States is among the sponsors listed on L.49, and press coverage says the US introduced it. **78/311** was adopted 1 July 2024 (draft A/78/L.86), distributed 5 July 2024. China is among the sponsors on L.86, and Chinese government and UN-system sources say China proposed it. Both were adopted **without a vote**, according to the UN press release GA/12588 as reported in search results and to Chinese and UN-system coverage. The UN press page itself would not load, so I could not read that statement in the original.
```bibtex
@misc{unga2024,
  author       = {{United Nations General Assembly}},
  title        = {Seizing the Opportunities of Safe, Secure and Trustworthy Artificial Intelligence Systems for Sustainable Development},
  howpublished = {Resolution A/RES/78/265, adopted 21 March 2024},
  year         = {2024}
}

@misc{unga2024capacity,
  author       = {{United Nations General Assembly}},
  title        = {Enhancing International Cooperation on Capacity-Building of Artificial Intelligence},
  howpublished = {Resolution A/RES/78/311, adopted 1 July 2024},
  year         = {2024}
}
```

---

# TASK 2: Corrections to existing entries

### laurito2025: CORRECTED
Checked: Crossref (10.1073/pnas.2415697122): six authors, Böhm 5th; PNAS 122(31), article e2415697122, issue dated 5 Aug 2025.
```bibtex
@article{laurito2025,
  author  = {Laurito, Walter and Davis, Benjamin and Grietzer, Peli and Gaven{\v{c}}iak, Tom{\'a}{\v{s}} and B{\"o}hm, Ada and Kulveit, Jan},
  title   = {{AI}--{AI} Bias: Large Language Models Favor Communications Generated by Large Language Models},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {122},
  number  = {31},
  pages   = {e2415697122},
  year    = {2025},
  doi     = {10.1073/pnas.2415697122}
}
```

### goel2025: CORRECTED
Checked: PMLR page (https://proceedings.mlr.press/v267/goel25b.html): pages 19621--19678. Note that `goel25a` is a different paper.
```bibtex
@inproceedings{goel2025,
  author    = {Goel, Shashwat and Str{\"u}ber, Joschka and Auzina, Ilze Amanda and Chandra, Karuna K. and Kumaraguru, Ponnurangam and Kiela, Douwe and Prabhu, Ameya and Bethge, Matthias and Geiping, Jonas},
  title     = {Great Models Think Alike and this Undermines {AI} Oversight},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {267},
  pages     = {19621--19678},
  year      = {2025}
}
```

### greenblatt2024: CORRECTED
Checked: PMLR page (https://proceedings.mlr.press/v235/greenblatt24a.html).
```bibtex
@inproceedings{greenblatt2024,
  author    = {Greenblatt, Ryan and Shlegeris, Buck and Sachan, Kshitij and Roger, Fabien},
  title     = {{AI} Control: Improving Safety Despite Intentional Subversion},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {235},
  pages     = {16295--16336},
  year      = {2024}
}
```

### narechania2024: CORRECTED
Checked: the article PDF (https://yalelawandpolicy.org/sites/default/files/YLPR/narechania_sitaraman_anantimonopolyapproach_ylpr_2024.pdf), whose running head is "Yale Law & Policy Review 43:95 2024", first page 95 and last page 170; journal page (Vol. 43, Issue 1, Fall 2024).
```bibtex
@article{narechania2024,
  author  = {Narechania, Tejas N. and Sitaraman, Ganesh},
  title   = {An Antimonopoly Approach to Governing Artificial Intelligence},
  journal = {Yale Law \& Policy Review},
  volume  = {43},
  number  = {1},
  pages   = {95--170},
  year    = {2024}
}
```

### kwak2014 and carpenter2013: CORRECTED. Both are 2013.
Checked: Crossref for the book (10.1017/CBO9781139565875; print 21 Oct 2013, online 5 Jun 2014) and the chapter (10.1017/CBO9781139565875.008; pp. 71--98; print 2013). Keep the key `kwak2014` to avoid touching `main.tex`, or rename it to `kwak2013`.
```bibtex
@book{carpenter2013,
  editor    = {Carpenter, Daniel and Moss, David A.},
  title     = {Preventing Regulatory Capture: Special Interest Influence and How to Limit It},
  publisher = {Cambridge University Press},
  year      = {2013},
  doi       = {10.1017/CBO9781139565875}
}

@incollection{kwak2014,
  author    = {Kwak, James},
  title     = {Cultural Capture and the Financial Crisis},
  booktitle = {Preventing Regulatory Capture: Special Interest Influence and How to Limit It},
  editor    = {Carpenter, Daniel and Moss, David A.},
  publisher = {Cambridge University Press},
  pages     = {71--98},
  year      = {2013},
  doi       = {10.1017/CBO9781139565875.008}
}
```

### euaiact2024: CORRECTED
Checked: EFTA EEA-Lex record (https://www.efta.int/eea-lex/32024r1689) for the full title, adoption date of 13 June 2024 and "OJ L, 2024/1689, 12.7.2024"; ELI http://data.europa.eu/eli/reg/2024/1689/oj. EUR-Lex itself blocked automated access. Article 31 is titled "Requirements relating to notified bodies". Para. 4 requires independence from the provider, from other economically interested operators and from competitors; para. 5 bars involvement in design, development or marketing of the systems, and bars consultancy. I checked this at https://artificialintelligenceact.eu/article/31/.
```bibtex
@misc{euaiact2024,
  author       = {{European Parliament and Council of the European Union}},
  title        = {Regulation ({EU}) 2024/1689 of the {European Parliament} and of the {Council} of 13 {June} 2024 Laying Down Harmonised Rules on Artificial Intelligence and Amending Regulations ({EC}) No 300/2008, ({EU}) No 167/2013, ({EU}) No 168/2013, ({EU}) 2018/858, ({EU}) 2018/1139 and ({EU}) 2019/2144 and Directives 2014/90/{EU}, ({EU}) 2016/797 and ({EU}) 2020/1828 ({Artificial Intelligence Act})},
  howpublished = {Official Journal of the European Union, OJ L, 2024/1689, 12 July 2024. \url{http://data.europa.eu/eli/reg/2024/1689/oj}},
  note         = {Article 31: Requirements relating to notified bodies},
  year         = {2024}
}
```
A shorter title is acceptable: `Regulation ({EU}) 2024/1689 ({Artificial Intelligence Act})`.
**Amended since publication (sources found but not read in the original):** Regulation (EU) 2026/1744, the "Digital Omnibus on AI", was published in the OJ on 24 July 2026 and entered into force on 27 July 2026. It defers the main high-risk obligations, for example Annex III systems to 2 Dec 2027. I found this through Hunton and the NI Assembly EU-acts list; EUR-Lex was unreachable. If the paper cites any AI Act *application dates*, check them against the consolidated text. I found no indication that Art. 31 itself changed, but I did not confirm that.

### abdalla2021: CORRECTED (entry type)
Checked: Crossref (10.1145/3461702.3462563; ACM; pp. 287--297).
```bibtex
@inproceedings{abdalla2021,
  author    = {Abdalla, Mohamed and Abdalla, Moustafa},
  title     = {The Grey Hoodie Project: Big Tobacco, Big Tech, and the Threat on Academic Integrity},
  booktitle = {Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society},
  pages     = {287--297},
  publisher = {ACM},
  year      = {2021},
  doi       = {10.1145/3461702.3462563}
}
```

### buthe2011: bibliographic data CORRECT. Reviewers are right about the content.
Checked: Princeton UP record (ISBN 9780691144795); The Regulatory Review summary (https://www.theregreview.org/2011/05/24/the-privatization-of-regulation-in-the-world-economy/); Swiss Political Science Review book review (10.1111/spsr.12008).
```bibtex
@book{buthe2011,
  author    = {B{\"u}the, Tim and Mattli, Walter},
  title     = {The New Global Rulers: The Privatization of Regulation in the World Economy},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {2011}
}
```
**What it argues:** The book studies private international rule-making at the IASB, ISO and IEC. It treats standard-setting as a highly institutionalized *political* process conducted in technical language. Who wins depends on **institutional complementarity**: how well a country's domestic standard-setting institutions (hierarchical and coordinated, or fragmented) fit the international body, which determines whether domestic firms can feed in timely information and speak with one voice. It is not explained by states' economic power or by technical merit alone. Firm expertise is not the explanatory variable, so the gloss should change.

### mattli2003: VERIFIED (new)
Checked: Crossref (10.1353/wp.2004.0006); Cambridge Core abstract page (World Politics 56(1):1--42, October 2003).
```bibtex
@article{mattli2003,
  author  = {Mattli, Walter and B{\"u}the, Tim},
  title   = {Setting International Standards: Technological Rationality or Primacy of Power?},
  journal = {World Politics},
  volume  = {56},
  number  = {1},
  pages   = {1--42},
  year    = {2003},
  doi     = {10.1353/wp.2004.0006}
}
```
**Establishes:** The paper tests the view that the technically best standard wins against the view that powerful actors impose theirs, using survey data on ISO and IEC standardization. Neither explains the results well. Influence instead follows how well national and international standardization institutions complement each other, a fit that is largely accidental and historical.

### carpenter2008: bibliographic data CORRECT. Reviewers are right about the content.
Checked: PubMed abstract (PMID 18367738; NEJM 358(13):1354--1361; DOI 10.1056/NEJMsa0706341).
```bibtex
@article{carpenter2008,
  author  = {Carpenter, Daniel and Zucker, Evan James and Avorn, Jerry},
  title   = {Drug-Review Deadlines and Safety Problems},
  journal = {New England Journal of Medicine},
  volume  = {358},
  number  = {13},
  pages   = {1354--1361},
  year    = {2008},
  doi     = {10.1056/NEJMsa0706341}
}
```
**What it shows:** The Prescription Drug User Fee Act (PDUFA) review deadlines bunched FDA approvals into the weeks just before each deadline. Drugs approved in the two months before their deadline were more likely to be withdrawn for safety reasons later (OR 5.5), more likely to get a black-box warning (OR 4.4), and more likely to have a dosage form discontinued (OR 3.3). The finding is about **deadline pressure on the corrector**, not about funding dependence.
**Caution if you want a funding-dependence claim:** the related study Carpenter, Chernew, Smith & Fendrick (2003), "Approval Times for New Drugs: Does the Source of Funding for FDA Staff Matter?", *Health Affairs* 22(Suppl. 1):W3-618--W3-624, DOI 10.1377/hlthaff.w3.618 (verified via Crossref and OpenAlex), finds that the *amount* of staff funding matters much more for review times than its *source* (user fees versus appropriations). That cuts against a simple user-fee-capture story.

### armstrong2016: CORRECT (no error)
Checked: Crossref (10.1007/s00146-015-0590-y): Armstrong, Bostrom, Shulman; *AI & Society* 31(2):201--206, May 2016 (online first 2015). The entry in the bib matches; only the DOI could be added:
```bibtex
  doi = {10.1007/s00146-015-0590-y}
```

---

# TASK 3: Evidence for present conditions

## (a) Governments framing frontier AI as a race or competition to win

**US: VERIFIED.** Source: `whitehouse2025` above (public-domain US government text).
- Statement it supports: "The United States is in a race to achieve global dominance in artificial intelligence" (Introduction, p. 1). The same page says it is "imperative that the United States and its allies win this race". The preface on p. 2, signed by Kratsios, Sacks and Rubio, says "The AI race is America's to win".

**China: VERIFIED, but the wording is not symmetric.** Source: `statecouncil2017` above.
- Statement it supports: the 2017 plan calls AI "a new focus of international competition". Its stated aims are to "build China's first-mover advantage" and, by 2030, to make China "the world's primary AI innovation center" (DigiChina translation). The Chinese reads 构筑我国人工智能发展的先发优势 and 成为世界主要人工智能创新中心.
- **Caveat for the text.** The Chinese text never uses "race"; it frames AI as competition for strategic initiative and leadership. Since 2023, China's *external* documents (`china2023gaigi`, `china2025actionplan`, A/RES/78/311) have been framed around cooperation and capacity-building. To stay accurate, consider wording like this: "described by governments in competitive terms, as a race to win \citep{whitehouse2025} or as international competition for first-mover advantage \citep{statecouncil2017}". That keeps the symmetry you want without overstating the Chinese text.
- Possible addition: both rivals also joined consensus on each other's UN AI resolutions (`unga2024`, US-sponsored; `unga2024capacity`, China-sponsored; both adopted without a vote). This sits well next to `bletchley2023`.

## (b) Developers funding evaluators or controlling their access (beyond Longpre 2024)

**1. Epoch AI / FrontierMath: VERIFIED** (https://epoch.ai/latest/openai-and-frontiermath)
```bibtex
@misc{besiroglu2025frontiermath,
  author       = {Besiroglu, Tamay and Sevilla, Jaime},
  title        = {Clarifying the Creation and Use of the {FrontierMath} Benchmark},
  howpublished = {Epoch AI, 23 January 2025. \url{https://epoch.ai/latest/openai-and-frontiermath}},
  year         = {2025}
}
```
Statement: OpenAI commissioned the 300 core FrontierMath problems, owns them, and has access to problems and solutions except a holdout set. Epoch needed OpenAI's permission before disclosing the funding.

**2. METR's pre-deployment evaluation of o3: VERIFIED** (https://metr.org/evaluations/openai-o3-report/)
```bibtex
@misc{metr2025o3,
  author       = {{METR}},
  title        = {Details about {METR}'s Preliminary Evaluation of {OpenAI}'s o3 and o4-mini},
  howpublished = {16 April 2025. \url{https://metr.org/evaluations/openai-o3-report/}},
  year         = {2025}
}
```
Statement: The third-party evaluator received pre-release checkpoints from the developer three weeks before release. It reports doing the evaluation in "a relatively short time", having limited information about the model, and having no access to the model's internal reasoning. Access and timing were set by the developer.

**3. Anthropic funding third-party evaluations: VERIFIED** (https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations)
```bibtex
@misc{anthropic2024evals,
  author       = {{Anthropic}},
  title        = {A New Initiative for Developing Third-Party Model Evaluations},
  howpublished = {1 July 2024. \url{https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations}},
  year         = {2024}
}
```
Statement: A frontier developer announced it would fund evaluations built by third-party organizations to measure advanced capabilities in AI models.

**4. International AI Safety Report 2025: VERIFIED** (`bengio2025report`, p. 23)
Statement: For thorough risk assessments, evaluators often need more time, more direct access to models and training data, and more methodological information than developers typically provide.

`singh2025` (Leaderboard Illusion, already in the bib) adds evidence of selective private testing on a public leaderboard.

## (c) LLM judges preferring their own outputs: replications from 2025 on

**1. Chen et al., EMNLP 2025: VERIFIED and peer-reviewed** (https://aclanthology.org/2025.emnlp-main.86/)
```bibtex
@inproceedings{chen2025selfpref,
  author    = {Chen, Zhi-Yuan and Wang, Hao and Zhang, Xinyu and Hu, Enrui and Lin, Yankai},
  title     = {Beyond the Surface: Measuring Self-Preference in {LLM} Judgments},
  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  pages     = {1653--1672},
  year      = {2025},
  doi       = {10.18653/v1/2025.emnlp-main.86}
}
```
Statement: After controlling for response quality with gold judgments, both pre-trained and post-trained LLMs, including reasoning models, still show self-preference bias. In their tests (0.5B--72B parameters), larger models show *less* of it.

**2. Chen, Wei, Zhu, Feng, Meng 2025: VERIFIED, arXiv preprint only** (arXiv 2504.03846; Shi Feng is a Panickssery co-author)
```bibtex
@article{chen2025reason,
  author  = {Chen, Wei-Lin and Wei, Zhepei and Zhu, Xinyu and Feng, Shi and Meng, Yu},
  title   = {Do {LLM} Evaluators Prefer Themselves for a Reason?},
  journal = {arXiv preprint arXiv:2504.03846},
  year    = {2025}
}
```
Statement: On verifiable tasks across seven model families, stronger models' self-preference mostly tracks their genuinely better answers. "Harmful" self-preference persists when the judge is itself wrong, and it is *more* pronounced in stronger models when they err.

**3. Pombal, Rei, Martins 2026: VERIFIED, arXiv preprint "under review"** (arXiv 2604.06996)
```bibtex
@article{pombal2026rubric,
  author  = {Pombal, Jos{\'e} and Rei, Ricardo and Martins, Andr{\'e} F. T.},
  title   = {Self-Preference Bias in Rubric-Based Evaluation of Large Language Models},
  journal = {arXiv preprint arXiv:2604.06996},
  year    = {2026}
}
```
Statement: Self-preference persists even with objective, programmatically checkable rubrics. On rubric items the output fails, a judge can be more than 50% likelier to wrongly mark them satisfied when the output is its own. On HealthBench it shifts model scores by up to 10 points. Ensembling judges reduces the bias but does not remove it.

**Overall:** the 2025--26 literature confirms self-preference after quality controls, but with two qualifiers. Part of the raw effect is legitimate, and the evidence on whether it grows with capability is mixed: EMNLP 2025 finds less in larger models, while Chen et al. find more *harmful* self-preference in stronger models when they err. The bib already has `zatuchin2026` (no own-model premium in Laurito's matrices) and `awuni2026` (family-conditioned preference). Avoid any claim that self-preference simply increases with capability.

## (d) Evaluation and assurance capacity lagging capability

**1. International AI Safety Report 2025: VERIFIED** (`bengio2025report`)
- p. 169: an "evaluation gap" for safety persists, and current risk assessment and evaluation methods are "immature"; a model that passes current risk evaluations can still be unsafe.
- p. 176: "As general-purpose AI advances rapidly, risk assessment, risk mitigation, governance, and enforcement efforts can struggle to keep pace."
- p. 23: existing evaluations rely mainly on "spot checks" and often miss hazards.

**2. International AI Safety Report 2026: VERIFIED** (PDF https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026.pdf; Research series number DSIT 2026/001; February 2026)
```bibtex
@techreport{bengio2026report,
  author      = {Bengio, Yoshua and Clare, Stephen and Prunkl, Carina and others},
  title       = {International {AI} Safety Report 2026},
  institution = {UK Department for Science, Innovation and Technology},
  type        = {Research series number},
  number      = {DSIT 2026/001},
  year        = {2026},
  url         = {https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026}
}
```
Statement: Reliable pre-deployment safety testing has become harder to conduct. It is now more common for models to distinguish test settings from real deployment and to exploit loopholes in evaluations, so dangerous capabilities could go undetected (printed p. 10, "Key developments"). The report also describes an "evaluation gap": performance on pre-deployment tests does not reliably predict real-world utility or risk (printed p. 13). It reuses the "evidence dilemma" framing (printed pp. 11, 14).

**3. UK AI Security Institute, Frontier AI Trends Report (December 2025): VERIFIED** (page https://aisi.gov.uk/frontier-ai-trends-report; PDF downloaded from the AISI website CDN)
```bibtex
@techreport{aisi2025trends,
  author      = {{AI Security Institute}},
  title       = {Frontier {AI} Trends Report},
  institution = {UK AI Security Institute},
  year        = {2025},
  month       = dec,
  url         = {https://aisi.gov.uk/frontier-ai-trends-report}
}
```
Statement: AISI found universal jailbreaks for every system it tested (PDF p. 26). Across systems it found minimal correlation between capability and safeguard robustness, R² = 0.097 (PDF p. 29). In other words, safeguards do not improve automatically as capability rises. The same report gives roughly eight-month doubling in some capability domains, which is consistent with `kwa2025`.

## (e) AI used to write evaluations, peer reviews, comments to regulators or political communications at scale

**1. Model-written evaluations: VERIFIED.** This is the better cite for "AI writes evaluations"; the `perez2022` already in the bib is the red-teaming paper.
```bibtex
@inproceedings{perez2023,
  author    = {Perez, Ethan and Ringer, Sam and Lukosiute, Kamile and Nguyen, Karina and Chen, Edwin and Heiner, Scott and others},
  title     = {Discovering Language Model Behaviors with Model-Written Evaluations},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
  pages     = {13387--13434},
  year      = {2023},
  doi       = {10.18653/v1/2023.findings-acl.847}
}
```
Statement: Language models were used to generate 154 evaluation datasets, which uncovered new cases of inverse scaling. Source: https://aclanthology.org/2023.findings-acl.847/

**2. LLM-modified peer reviews: VERIFIED** (https://proceedings.mlr.press/v235/liang24b.html)
```bibtex
@inproceedings{liang2024peer,
  author    = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel and Zou, James Y.},
  title     = {Monitoring {AI}-Modified Content at Scale: A Case Study on the Impact of {ChatGPT} on {AI} Conference Peer Reviews},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  series    = {PMLR},
  volume    = {235},
  pages     = {29575--29620},
  year      = {2024}
}
```
Statement: An estimated 6.5%--16.9% of peer-review text at ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023 could have been substantially modified by LLMs.

**3. LLM-assisted writing across society, including complaints filed with a regulator: VERIFIED** (Crossref 10.1016/j.patter.2025.101366; OpenAlex abstract)
```bibtex
@article{liang2025society,
  author  = {Liang, Weixin and Zhang, Yaohui and Codreanu, Mihai and Wang, Jiayu and Cao, Hancheng and Zou, James},
  title   = {The Widespread Adoption of Large Language Model-Assisted Writing across Society},
  journal = {Patterns},
  volume  = {6},
  number  = {12},
  pages   = {101366},
  year    = {2025},
  doi     = {10.1016/j.patter.2025.101366}
}
```
Statement: By late 2024, roughly 18% of financial consumer complaints to the US Consumer Financial Protection Bureau (CFPB), 24% of corporate press releases and 14% of UN press releases showed LLM-assisted writing.

**4. LLM-drafted complaints change regulatory outcomes: VERIFIED** (PubMed PMID 41709033)
```bibtex
@article{shin2026complaints,
  author  = {Shin, Minkyu and Kim, Jin and Shin, Jiwoong},
  title   = {The Adoption and Efficacy of Large Language Models in {US} Consumer Financial Complaints},
  journal = {Nature Human Behaviour},
  volume  = {10},
  number  = {4},
  pages   = {669--680},
  year    = {2026},
  doi     = {10.1038/s41562-026-02409-4}
}
```
Statement: The study analyzed 1.13 million CFPB complaints from 2015 to 2024. Instrumental-variable estimates show LLM use raises the probability of obtaining relief by 6.9 percentage points, and experiments show the mechanism is better presentation, not changed facts.

**5. Machine-generated comments in federal rulemaking: VERIFIED** (https://techscience.org/a/2019121801/)
```bibtex
@article{weiss2019,
  author  = {Weiss, Max},
  title   = {Deepfake Bot Submissions to Federal Public Comment Websites Cannot Be Distinguished from Human Submissions},
  journal = {Technology Science},
  pages   = {2019121801},
  year    = {2019},
  url     = {https://techscience.org/a/2019121801/}
}
```
Statement: In 2019 a GPT-2 bot submitted 1,001 comments on a federal Medicaid waiver, 55.3% of all comments received. Human raters could not tell them from human comments (49.63% accuracy).

**6. AI-written constituent letters to legislators: VERIFIED** (Crossref and OpenAlex)
```bibtex
@article{kreps2024,
  author  = {Kreps, Sarah and Kriner, Douglas L.},
  title   = {The Potential Impact of Emerging Technologies on Democratic Representation: Evidence from a Field Experiment},
  journal = {New Media \& Society},
  volume  = {26},
  number  = {12},
  pages   = {6918--6937},
  year    = {2024},
  doi     = {10.1177/14614448231160526}
}
```
Statement: The authors sent 32,398 emails, half written by GPT-3, to 7,132 state legislators. Legislators were only about 2 percentage points less likely to answer the AI-written ones.

**7. Industry-funded fake comments, not AI but the same correction channel: VERIFIED** (PDF https://ag.ny.gov/sites/default/files/reports/oag-fakecommentsreport.pdf; the PDF carries no date; it was released in May 2021 per press coverage)
```bibtex
@techreport{nyag2021,
  author      = {{New York State Office of the Attorney General}},
  title       = {Fake Comments: How {U.S.} Companies \& Partisans Hack Democracy to Undermine Your Voice},
  institution = {Office of the New York State Attorney General},
  year        = {2021}
}
```
Statement: Nearly 18 million of the more than 22 million comments in the FCC's 2017 net-neutrality rulemaking were fake. Broadband-industry backers spent $4.2 million generating more than 8.5 million of them.

**Not found:** I could not find a peer-reviewed estimate of the share of LLM-drafted comments on regulations.gov, or direct evidence of LLM-drafted lobbying submissions on AI rules. Items 3--6 are the closest verified evidence. If you assert "at scale" for regulatory comments specifically, rely on 3--5 and say the evidence is indirect.
