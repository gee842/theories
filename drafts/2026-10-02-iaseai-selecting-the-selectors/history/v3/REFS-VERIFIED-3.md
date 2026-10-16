# Verified references, batch 3 (economics and game theory)

Checked 2026-10-02/03. I verified the bibliographic fields of every entry against publisher metadata (Crossref API; for JSTOR-registered DOIs, which list only the first page, I took the last page from RePEc/IDEAS, EconPapers, the Econometric Society page, or the article PDF). Content glosses rest on publisher, PubMed or RePEc abstracts, or on the article text where I could get it. Where no abstract was available, the gloss rests on named secondary sources, and I say so. I did not edit `references.bib` or `REFS-VERIFIED-2.md`.

None of these 24 keys is in `references.bib` yet. `schaffer1988` (the biology paper) is in the bib; `schaffer1989` below is the economics paper. `aaai2027.bst` ignores `doi` and `url`. I kept them because they cost nothing.

## At a glance

All 24 entries are **VERIFIED** for bibliographic data. None failed. Points to act on:

| Key | Issue |
|---|---|
| `greenporter1984` | **Gloss warning.** Green & Porter show that collusion *survives* imperfect monitoring, with recurrent price wars on the equilibrium path. They do not show that it fails. R-economics says cooperation "fails ... under imperfect monitoring (Green & Porter 1984)", which overstates it. The draft remark's wording ("degrades the public signal on which reversion depends") is safe. |
| `kleinleffler1981` | **Gloss warning.** The repeat-purchase mechanism needs buyers to detect non-performance after purchase (experience goods). It does not cover pure credence goods, which is how R-economics frames it ("credence-good markets"). |
| `aronsson2008` | **Gloss warning.** This is an optimal-taxation model with government provision of the public good, not a voluntary-contribution game. Its public-good result is that whether the provision rule should change depends on how preferences are elicited. It does not show that status concern undermines voluntary provision. It is weak support for "Prop. 2 is the linear VCM with status concern". |
| `milinski2008` | **Gloss caution.** The target is known; what varies is the *probability* of loss. Even at high risk only half the groups reached the target. Do not cite it for "coordination is assured". That finding is Barrett & Dannenberg's, for a certain threshold. |
| `barrett2013` | **Gloss caution.** Treaties coordinate below a known threshold only when the benefit of avoiding catastrophe is high relative to the cost. When it is not, they sustain only modest cuts. |
| `algerweibull2013` | **Gloss caution.** The stable weight is on a Kantian goal ("what if everyone did as I do"), equal to the index of assortativity. "Internalizes a fraction of the harm equal to assortativity" is an interpretation that holds in linear public-goods/commons games, not the paper's wording. |
| `becker1983` | **Gloss caution.** In Becker, opposing pressure grows with the *deadweight cost* of taxes and subsidies. "Mobilize in proportion to the harm they perceive" and the linear form $d=d_0+\kappa(K-\tilde V)$ are the author's stylization. Write "in the spirit of" or "following". |
| `peltzman1976` | **Gloss caution.** The "losers mobilize as deadweight loss grows" mechanism is Becker's. Peltzman's interior outcome comes from a support-maximizing regulator, which limits the dominant group's gains. |
| `strausz2005` | **Note.** The same paper finds that honest certification is a natural monopoly and that price competition tends to monopolize certification. That is relevant to the paper's concentration argument and cuts both ways. |
| `olson1993` | **Note.** If it is cited for "encompassing interests" of universal owners: the 1993 paper applies the logic to a secure autocrat. The general statement is Olson (1982), *The Rise and Decline of Nations*, which is not in this batch. |
| `kraakman1986`, `shavell1986` | No abstract was available. The glosses come from secondary sources with pin cites (named below). The bibliographic data are publisher-verified. |
| `salop1983` | Has no DOI (`doi.org/10.2307/1816853` returns 404). It appeared in the May 1983 *Papers and Proceedings* issue of the AER; I put that in `note`. |
| `schaffer1989` | Crossref drops the subtitle. The publisher, RePEc and the author's institutional page include it. |
| `holmstrom1982` | The journal and JSTOR print "Holmstrom" without the umlaut. Either spelling is acceptable. I used `Holmstr{\"o}m`. |

---

### barrett2013: VERIFIED (https://doi.org/10.1016/j.jeem.2012.12.004)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/eee/jeeman/v66y2013i2p235-250.html).
```bibtex
@article{barrett2013,
  author  = {Barrett, Scott},
  title   = {Climate Treaties and Approaching Catastrophes},
  journal = {Journal of Environmental Economics and Management},
  volume  = {66},
  number  = {2},
  pages   = {235--250},
  year    = {2013},
  doi     = {10.1016/j.jeem.2012.12.004}
}
```
**Establishes:** Theory. If the catastrophic threshold is known with certainty *and* the benefit of avoiding catastrophe is high relative to the cost, treaties easily coordinate countries to stay below it. Where the net benefit is lower, treaties sustain only modest cuts. Uncertainty about the *impact* of catastrophe changes nothing, but uncertainty about the threshold's *location* normally makes coordination collapse, whether the tails are thin or fat.

### barrettdannenberg2012: VERIFIED (https://doi.org/10.1073/pnas.1208417109)
Checked: Crossref; PubMed abstract (PMID 23045685).
```bibtex
@article{barrettdannenberg2012,
  author  = {Barrett, Scott and Dannenberg, Astrid},
  title   = {Climate Negotiations under Scientific Uncertainty},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {109},
  number  = {43},
  pages   = {17372--17376},
  year    = {2012},
  doi     = {10.1073/pnas.1208417109}
}
```
**Establishes:** A lab experiment grounded in a model. Fear of crossing a known dangerous threshold turns the prisoners' dilemma into a coordination game, and collective action to avoid the threshold becomes almost certain. This survives uncertainty about the impact of crossing. Uncertainty about where the threshold *lies* turns the game back into a dilemma, and cooperation collapses. This matches the draft remark's use exactly.

### milinski2008: VERIFIED (https://doi.org/10.1073/pnas.0709546105)
Checked: Crossref; PubMed abstract (PMID 18287081).
```bibtex
@article{milinski2008,
  author  = {Milinski, Manfred and Sommerfeld, Ralf D. and Krambeck, Hans-J{\"u}rgen and Reed, Floyd A. and Marotzke, Jochem},
  title   = {The Collective-Risk Social Dilemma and the Prevention of Simulated Dangerous Climate Change},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {105},
  number  = {7},
  pages   = {2291--2294},
  year    = {2008},
  doi     = {10.1073/pnas.0709546105}
}
```
**Establishes:** This paper introduces the collective-risk social dilemma in the lab. Groups make successive contributions toward a fixed target. If they miss it, each member loses all remaining money with a given probability. When the risk is high, half the groups reach the target and the rest narrowly miss. When the risk is no higher than the required average investment, groups generally fail. *Caution:* the threshold is known; only the probability of loss varies.

### greenporter1984: VERIFIED (https://doi.org/10.2307/1911462)
Checked: Crossref (first page only); pages 87--100 from RePEc, the Econometric Society page, and the published PDF (Caltech repository, printed folios 87--100).
```bibtex
@article{greenporter1984,
  author  = {Green, Edward J. and Porter, Robert H.},
  title   = {Noncooperative Collusion under Imperfect Price Information},
  journal = {Econometrica},
  volume  = {52},
  number  = {1},
  pages   = {87--100},
  year    = {1984},
  doi     = {10.2307/1911462}
}
```
**Establishes:** A cartel under demand uncertainty is enforced noncooperatively. Firms see only the market price, not rivals' output. Collusion is sustained by reverting to punishment when price falls below a trigger. Because low demand and cheating look alike, punishment episodes ("price wars") happen on the equilibrium path even though nobody cheats. **Gloss warning:** this result says collusion survives imperfect public monitoring, at the cost of recurrent punishment phases. It does not say collusion fails.

### algerweibull2013: VERIFIED (https://doi.org/10.3982/ECTA10637)
Checked: Crossref (authors from OpenAlex); abstract on RePEc (https://ideas.repec.org/a/ecm/emetrp/v81y2013i6p2269-2302.html).
```bibtex
@article{algerweibull2013,
  author  = {Alger, Ingela and Weibull, J{\"o}rgen W.},
  title   = {{Homo Moralis}---Preference Evolution under Incomplete Information and Assortative Matching},
  journal = {Econometrica},
  volume  = {81},
  number  = {6},
  pages   = {2269--2302},
  year    = {2013},
  doi     = {10.3982/ECTA10637}
}
```
**Establishes:** When preferences are private information and matching is assortative, the evolutionarily stable preferences are "homo moralis". These are a convex combination of material self-interest and a Kantian goal: the payoff one would get if everyone acted likewise. The stable weight on morality equals the index of assortativity. With no assortativity, the stable type is homo oeconomicus. *Caution:* see the table on the "fraction of harm" reading.

### becker1983: VERIFIED (https://doi.org/10.2307/1886017)
Checked: Crossref (first page only); pages 371--400 and abstract from EconPapers (RePEc:oup:qjecon:v:98:y:1983:i:3:p:371-400) and OpenAlex.
```bibtex
@article{becker1983,
  author  = {Becker, Gary S.},
  title   = {A Theory of Competition among Pressure Groups for Political Influence},
  journal = {Quarterly Journal of Economics},
  volume  = {98},
  number  = {3},
  pages   = {371--400},
  year    = {1983},
  doi     = {10.2307/1886017}
}
```
**Establishes:** Political equilibrium depends on four things: each group's efficiency at producing pressure, how pressure translates into influence, group sizes, and the deadweight costs of taxes and subsidies. Higher deadweight costs discourage pressure by subsidized groups and encourage pressure by taxpayers. So competition among groups favours efficient methods of redistribution. This unifies the "government corrects market failures" view with the "government favours the powerful" view.

### peltzman1976: VERIFIED (https://doi.org/10.1086/466865)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/ucp/jlawec/v19y1976i2p211-40.html).
```bibtex
@article{peltzman1976,
  author  = {Peltzman, Sam},
  title   = {Toward a More General Theory of Regulation},
  journal = {Journal of Law and Economics},
  volume  = {19},
  number  = {2},
  pages   = {211--240},
  year    = {1976},
  doi     = {10.1086/466865}
}
```
**Establishes:** Peltzman formalizes and generalizes Stigler. The cost of using the political process limits both the size of the dominant group and its *gains*, because transfers provoke opposition. So a support-maximizing regulator does not serve one interest exclusively, and the paper derives the implications for entry into regulation and for regulated price structures.

### kraakman1986: VERIFIED (https://doi.org/10.1093/oxfordjournals.jleo.a036906)
Checked: OUP article page (Reinier H. Kraakman; vol. 2, no. 1, pp. 53--104, Spring 1986); RePEc. No abstract is published. The gloss rests on secondary sources: Tuch, "Multiple Gatekeepers", 96 *Va. L. Rev.* 1583 (2010), which quotes the definition at p. 53 and summarizes pp. 61--62 and 72--74; and "Pharmaceutical Gatekeepers", 47 *Ind. L. Rev.* 363 (2014), which quotes the four criteria at p. 61.
```bibtex
@article{kraakman1986,
  author  = {Kraakman, Reinier H.},
  title   = {Gatekeepers: The Anatomy of a Third-Party Enforcement Strategy},
  journal = {Journal of Law, Economics, and Organization},
  volume  = {2},
  number  = {1},
  pages   = {53--104},
  year    = {1986},
  doi     = {10.1093/oxfordjournals.jleo.a036906}
}
```
**Establishes:** Kraakman defines gatekeepers as "private parties who are able to disrupt misconduct by withholding their cooperation from wrongdoers" (p. 53). He asks when liability on them is an efficient enforcement strategy. His four criteria (p. 61) are: misconduct that penalties on wrongdoers cannot deter; weak private gatekeeping incentives; gatekeepers who can reliably prevent misconduct whatever wrongdoers prefer; and detection that legal rules can induce at reasonable cost. He also notes that wrongdoers can evade by shopping among gatekeepers (pp. 72--74). His gatekeepers (lawyers, accountants, underwriters) are broader than certifiers.

### shavell1986: VERIFIED (https://doi.org/10.1016/0144-8188(86)90038-4)
Checked: Crossref (vol. 6, no. 1, pp. 45--58, June 1986); Harvard Law School faculty bibliography. The publisher withholds the abstract. The gloss rests on Shavell's own later summary in NBER WP 10341 (2004), especially n. 22, and standard secondary accounts.
```bibtex
@article{shavell1986,
  author  = {Shavell, Steven},
  title   = {The Judgment Proof Problem},
  journal = {International Review of Law and Economics},
  volume  = {6},
  number  = {1},
  pages   = {45--58},
  year    = {1986},
  doi     = {10.1016/0144-8188(86)90038-4}
}
```
**Establishes:** A party whose assets are less than the harm it may cause is "judgment proof". Because it does not internalize the full loss, it takes too little care and engages in risky activities too much. The paper also analyses liability insurance: per Shavell (2004), when insurers can observe care, the optimal compulsory insurance requirement in Shavell (1986) is full coverage. This supports "judgment-proofness caps $\tau$ below $\nu$".

### bradford2020: VERIFIED (https://doi.org/10.1093/oso/9780190088583.001.0001)
Checked: Crossref book record (Oxford University Press, New York; print 27 Feb 2020; online 19 Dec 2019; ISBN 9780190088583) and its abstract. The five conditions come from secondary summaries (cep Input No. 3; European Law Blog review).
```bibtex
@book{bradford2020,
  author    = {Bradford, Anu},
  title     = {The {Brussels} Effect: How the {European Union} Rules the World},
  publisher = {Oxford University Press},
  address   = {New York},
  year      = {2020},
  isbn      = {9780190088583},
  doi       = {10.1093/oso/9780190088583.001.0001}
}
```
**Establishes:** The EU can regulate global markets unilaterally, without international agreements or coercion. Market forces do the work: multinationals voluntarily extend the EU rule to their global operations in order to keep access to the EU market. Bradford's conditions are market size, regulatory capacity, stringent standards, inelastic targets and non-divisibility. *Note:* if a firm can cheaply offer an EU-only variant (divisible conduct), her framework predicts no global spillover.

### nordhaus2015: VERIFIED (https://doi.org/10.1257/aer.15000001)
Checked: Crossref with publisher abstract.
```bibtex
@article{nordhaus2015,
  author  = {Nordhaus, William},
  title   = {Climate Clubs: Overcoming Free-Riding in International Climate Policy},
  journal = {American Economic Review},
  volume  = {105},
  number  = {4},
  pages   = {1339--1370},
  year    = {2015},
  doi     = {10.1257/aer.15000001}
}
```
**Establishes:** Theory plus an empirical model (C-DICE). Without sanctions on non-participants, the only stable coalitions involve minimal abatement. A club that puts small trade penalties on non-participants can induce a large stable coalition with high abatement. The penalty works by making it worthwhile for outsiders to join.

### olson1993: VERIFIED (https://doi.org/10.2307/2938736)
Checked: Crossref; abstract via Semantic Scholar (publisher abstract).
```bibtex
@article{olson1993,
  author  = {Olson, Mancur},
  title   = {Dictatorship, Democracy, and Development},
  journal = {American Political Science Review},
  volume  = {87},
  number  = {3},
  pages   = {567--576},
  year    = {1993},
  doi     = {10.2307/2938736}
}
```
**Establishes:** This is the "roving vs. stationary bandit" argument. A secure autocrat has an *encompassing interest* in his domain, so he provides order and other productivity-raising public goods. An autocrat with a short horizon instead confiscates. Because succession is uncertain, autocracies rarely perform well for more than a generation. The conditions for lasting democracy are the same as those for secure property and contract rights.

### bombardini2008: VERIFIED (https://doi.org/10.1016/j.jinteco.2008.03.003)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/eee/inecon/v75y2008i2p329-348.html).
```bibtex
@article{bombardini2008,
  author  = {Bombardini, Matilde},
  title   = {Firm Heterogeneity and Lobby Participation},
  journal = {Journal of International Economics},
  volume  = {75},
  number  = {2},
  pages   = {329--348},
  year    = {2008},
  doi     = {10.1016/j.jinteco.2008.03.003}
}
```
**Establishes:** If channelling political contributions carries a fixed cost, it is efficient for a lobby to consist of the largest firms in a sector. Sectors with a larger share of firms above a size threshold (greater size dispersion) are more politically active and obtain more trade protection. The model is tested against "Protection for Sale" with firm-level contribution data.

### strausz2005: VERIFIED (https://doi.org/10.1016/j.ijindorg.2004.09.002)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/eee/indorg/v23y2005i1-2p45-62.html).
```bibtex
@article{strausz2005,
  author  = {Strausz, Roland},
  title   = {Honest Certification and the Threat of Capture},
  journal = {International Journal of Industrial Organization},
  volume  = {23},
  number  = {1--2},
  pages   = {45--62},
  year    = {2005},
  doi     = {10.1016/j.ijindorg.2004.09.002}
}
```
**Establishes:** The paper derives conditions under which reputation lets certifiers resist capture. External certification is demanded despite its cost and capture risk. At low discount factors, honest certification requires a price *above* the static monopoly price. Price competition tends to monopolize certification, and honest certification has economies of scale: it is a natural monopoly.

### schaffer1989: VERIFIED (https://doi.org/10.1016/0167-2681(89)90075-9)
Checked: Crossref (title without subtitle); RePEc and Semantic Scholar (with subtitle); Heriot-Watt research portal (abstract).
```bibtex
@article{schaffer1989,
  author  = {Schaffer, Mark E.},
  title   = {Are Profit-Maximisers the Best Survivors? {A} {Darwinian} Model of Economic Natural Selection},
  journal = {Journal of Economic Behavior \& Organization},
  volume  = {12},
  number  = {1},
  pages   = {29--45},
  year    = {1989},
  doi     = {10.1016/0167-2681(89)90075-9}
}
```
**Establishes:** Schaffer refutes Friedman's conjecture that profit maximization captures the conditions for survival. When firms have market power, a firm can deviate from profit maximization in a way that hurts its profit-maximizing rivals more than itself. That "spiteful" firm is then more likely to survive than they are. So profit maximizers are not necessarily the best survivors.

### kockesen2000: VERIFIED (https://doi.org/10.1006/jeth.1999.2587)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/eee/jetheo/v92y2000i2p274-299.html).
```bibtex
@article{kockesen2000,
  author  = {Ko{\c{c}}kesen, Levent and Ok, Efe A. and Sethi, Rajiv},
  title   = {The Strategic Advantage of Negatively Interdependent Preferences},
  journal = {Journal of Economic Theory},
  volume  = {92},
  number  = {2},
  pages   = {274--299},
  year    = {2000},
  doi     = {10.1006/jeth.1999.2587}
}
```
**Establishes:** The setting is classes of supermodular and submodular games that are symmetric in material payoffs. There, players who also care about their payoff *relative* to others earn strictly higher material payoffs than pure material-payoff maximizers at all intragroup-symmetric equilibria. The conditions hold in several economically important games, including Cournot competition. The authors draw implications for preference evolution.

### gordon1954: VERIFIED (https://doi.org/10.1086/257497)
Checked: Crossref; OpenAlex; first-page abstract via Semantic Scholar; section title confirmed in Parent et al. (2023), *J. Hist. Econ. Thought*, DOI 10.1017/S1053837223000056.
```bibtex
@article{gordon1954,
  author  = {Gordon, H. Scott},
  title   = {The Economic Theory of a Common-Property Resource: The Fishery},
  journal = {Journal of Political Economy},
  volume  = {62},
  number  = {2},
  pages   = {124--142},
  year    = {1954},
  doi     = {10.1086/257497}
}
```
**Establishes:** Under common property with individualistic competition, the resource yields no economic rent, because effort expands until the rent is dissipated. "Overexploitation" problems are manifestations of this. Section 4 is titled "The Bionomic Equilibrium of the Fishing Industry". Gordon says the logic applies to all common-property resources. This supports the review's reading: open access means dissipated rent, not necessarily extinction.

### salop1983: VERIFIED (https://www.jstor.org/stable/1816853)
Checked: RePEc (https://ideas.repec.org/a/aea/aecrev/v73y1983i2p267-71.html: vol. 73, no. 2, pp. 267--271, May 1983); JSTOR issue listing (Vol. 73, No. 2, May 1983, Papers and Proceedings of the 95th Annual Meeting); Salop's CV (Georgetown, Dec 2025), which gives JSTOR 1816853; text of the FTC working-paper version (BE WP 81, Jan 1983). There is no DOI.
```bibtex
@article{salop1983,
  author  = {Salop, Steven C. and Scheffman, David T.},
  title   = {Raising Rivals' Costs},
  journal = {American Economic Review},
  volume  = {73},
  number  = {2},
  pages   = {267--271},
  year    = {1983},
  note    = {Papers and Proceedings},
  url     = {https://www.jstor.org/stable/1816853}
}
```
**Establishes:** Raising rivals' costs is a more credible exclusionary strategy than predatory pricing. It can pay even if rivals do not exit, needs no short-run sacrifice of profit, and can be made irreversible. Their examples include boycotts, exclusive dealing, industry-wide wage contracts, and product standards and other government regulation that raise rivals' *relative* compliance costs. The last example is the one the review uses.

### kleinleffler1981: VERIFIED (https://doi.org/10.1086/260996)
Checked: Crossref; first page of the article (JSTOR 1833028), which carries the abstract.
```bibtex
@article{kleinleffler1981,
  author  = {Klein, Benjamin and Leffler, Keith B.},
  title   = {The Role of Market Forces in Assuring Contractual Performance},
  journal = {Journal of Political Economy},
  volume  = {89},
  number  = {4},
  pages   = {615--641},
  year    = {1981},
  doi     = {10.1086/260996}
}
```
**Establishes:** Under repeat-purchase enforcement, a firm performs if and only if price exceeds salvageable production cost by enough that the rents lost on future sales outweigh the gain from cheating. So the price is above the competitive level, which rationalizes firm-specific (non-salvageable) investments. Advertising then signals likely performance. **Gloss warning:** this needs buyers to observe non-performance after purchase, so it does not cover pure credence goods.

### holmstrom1982: VERIFIED (https://doi.org/10.2307/3003457)
Checked: Crossref (first page only); pages 324--340 (Autumn 1982) and abstract from EconPapers (RePEc:rje:bellje:v:13:y:1982:i:autumn:p:324-340) and OpenAlex.
```bibtex
@article{holmstrom1982,
  author  = {Holmstr{\"o}m, Bengt},
  title   = {Moral Hazard in Teams},
  journal = {Bell Journal of Economics},
  volume  = {13},
  number  = {2},
  pages   = {324--340},
  year    = {1982},
  doi     = {10.2307/3003457}
}
```
**Establishes:** When only joint output is observable, free riding means no budget-balancing sharing rule makes team members supply efficient effort. A principal who breaks the budget restores incentives. That favours firms that separate ownership from labour over partnerships that split output. Competition through relative performance evaluation has value only as a way to extract information.

### gurerk2006: VERIFIED (https://doi.org/10.1126/science.1123633)
Checked: Crossref with publisher abstract; PubMed (PMID 16601192).
```bibtex
@article{gurerk2006,
  author  = {G{\"u}rerk, {\"O}zg{\"u}r and Irlenbusch, Bernd and Rockenbach, Bettina},
  title   = {The Competitive Advantage of Sanctioning Institutions},
  journal = {Science},
  volume  = {312},
  number  = {5770},
  pages   = {108--111},
  year    = {2006},
  doi     = {10.1126/science.1123633}
}
```
**Establishes:** In a lab experiment, participants repeatedly choose between a sanction-free institution and a sanctioning one (peer punishment and reward). Despite initial aversion, the whole population migrates step by step to the sanctioning institution and cooperates strongly, and the sanction-free one empties. A preregistered multilab replication (Lo Iacono et al. 2023, *PNAS Nexus* 2(5):pgad091) met all criteria in 5 of 7 labs and was weaker but in the same direction in the other two.

### sigmund2010: VERIFIED (https://doi.org/10.1038/nature09203)
Checked: Crossref; PubMed abstract (PMID 20631710).
```bibtex
@article{sigmund2010,
  author  = {Sigmund, Karl and De Silva, Hannelore and Traulsen, Arne and Hauert, Christoph},
  title   = {Social Learning Promotes Institutions for Governing the Commons},
  journal = {Nature},
  volume  = {466},
  number  = {7308},
  pages   = {861--863},
  year    = {2010},
  doi     = {10.1038/nature09203}
}
```
**Establishes:** Under social learning, the paper compares peer punishment with *pool* punishment, where resources for sanctions are committed before the joint effort. Pool punishment exposes second-order free riders. Without second-order punishment, peer punishers do better. With it, pool punishment prevails and is stable, so efficiency is traded for stability. Rudimentary sanctioning institutions can emerge without other-regarding preferences, group selection or a higher authority. *Caution:* the result depends on pool punishers also punishing second-order free riders.

### benshahar2012: VERIFIED (https://doi.org/10.36644/mlr.111.2.outsourcing)
Checked: Crossref with abstract; Michigan Law Review repository metadata (vol. 111, iss. 2, pp. 197--248; https://repository.law.umich.edu/mlr/vol111/iss2/2/).
```bibtex
@article{benshahar2012,
  author  = {Ben-Shahar, Omri and Logue, Kyle D.},
  title   = {Outsourcing Regulation: How Insurance Reduces Moral Hazard},
  journal = {Michigan Law Review},
  volume  = {111},
  number  = {2},
  pages   = {197--248},
  year    = {2012},
  doi     = {10.36644/mlr.111.2.outsourcing}
}
```
**Establishes:** Private insurers can substitute for government safety regulation. They often have advantages in the information needed to set standards, license conduct, verify outcomes and assess remedies, so they can create better incentives for safe behaviour. Where insurance regulates, law shrinks to simple rules of absolute or no liability. The authors propose extending regulation-through-insurance to consumer protection, food safety and financial statements.

### aronsson2008: VERIFIED (https://doi.org/10.1016/j.jpubeco.2007.12.007)
Checked: Crossref; abstract on RePEc (https://ideas.repec.org/a/eee/pubeco/v92y2008i5-6p986-997.html).
```bibtex
@article{aronsson2008,
  author  = {Aronsson, Thomas and Johansson-Stenman, Olof},
  title   = {When the {Joneses'} Consumption Hurts: Optimal Public Good Provision and Nonlinear Income Taxation},
  journal = {Journal of Public Economics},
  volume  = {92},
  number  = {5--6},
  pages   = {986--997},
  year    = {2008},
  doi     = {10.1016/j.jpubeco.2007.12.007}
}
```
**Establishes:** This is a model of optimal nonlinear income taxation and *government* public-good provision when people care about their consumption relative to others. Positional concern adds corrective terms. Under plausible empirical estimates, the tax formulas imply substantially higher marginal income tax rates. How the public-good provision rule should change depends critically on how preferences are elicited. **Gloss warning:** it is not a voluntary-contribution game and does not show that positional concern undermines voluntary provision. "Positional concerns and public goods" is accurate only in this optimal-policy sense.
