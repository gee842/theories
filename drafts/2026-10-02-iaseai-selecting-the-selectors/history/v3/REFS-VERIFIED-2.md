# Verified references, round 2 (Selecting the Selectors v3)

Checked 2026-10-02/03 against Crossref (api.crossref.org), the arXiv API (export.arxiv.org), publisher and proceedings pages, official government and UN sources, and the UN Official Document System (meeting records). Each entry says VERIFIED or UNVERIFIED and gives the URL(s) checked. A field that could not be confirmed is left out.

House style follows the existing `references.bib`: arXiv items are `@article` with `journal = {arXiv preprint arXiv:NNNN.NNNNN}`. Web and policy documents are `@misc` with the URL in `howpublished` as `\url{...}`, because aaai2027.bst ignores `doi` and `url`. A `doi` field is added where Crossref confirms one. It does no harm and helps a reader of the .bib.

None of the keys below is already in `references.bib`. Two extra entries are optional, with keys that do not clash: `idais2024venice` and `kratsios2025`. A third, `usun2026panel`, is in section 7.

---

## 1. AI races and governance

### han2020 — VERIFIED
Checked: Crossref DOI 10.1613/jair.1.12225; https://jair.org/index.php/jair/article/view/12225 (abstract, vol. 69, published 22 Nov 2020; pages 881–921 from Crossref).

```bibtex
@article{han2020,
  author  = {Han, The Anh and Pereira, Lu{\'i}s Moniz and Santos, Francisco C. and Lenaerts, Tom},
  title   = {To Regulate or Not: A Social Dynamics Analysis of an Idealised {AI} Race},
  journal = {Journal of Artificial Intelligence Research},
  volume  = {69},
  pages   = {881--921},
  year    = {2020},
  doi     = {10.1613/jair.1.12225}
}
```
What it establishes: an evolutionary game model of an AI race. The time to supremacy decides the outcome. In a short race, those who ignore safety win, at a cost to society. Even so, a real dilemma between individual and collective interest arises only for specific risk and timing conditions, so blanket regulation can misfire. In some long-race conditions, social welfare is better served by promoting risk-taking than by enforcing compliance. The results hold for two or many players. The author order differs from han2021 (here Santos comes before Lenaerts), and this order matches the publisher.

### cave2018 — VERIFIED
Checked: Crossref DOI 10.1145/3278721.3278780 (title "An AI Race for Strategic Advantage", subtitle "Rhetoric and Risks"; pp. 36–40); abstract from Semantic Scholar.

```bibtex
@inproceedings{cave2018,
  author    = {Cave, Stephen and {\'O}h{\'E}igeartaigh, Se{\'a}n S.},
  title     = {An {AI} Race for Strategic Advantage: Rhetoric and Risks},
  booktitle = {Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society},
  pages     = {36--40},
  publisher = {ACM},
  year      = {2018},
  doi       = {10.1145/3278721.3278780}
}
```
What it establishes: a conceptual paper, with no model. It argues that both the *rhetoric* of an AI race and an actual race carry risks, namely corner-cutting on safety and governance and a higher risk of conflict. It discusses how the research community could respond and how AI development could be framed to favour collaboration.

### ho2023 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2307.04699 (v2, 11 Jul 2023). No later venue found.

```bibtex
@article{ho2023,
  author  = {Ho, Lewis and Barnhart, Joslyn and Trager, Robert and Bengio, Yoshua and Brundage, Miles and Carnegie, Allison and Chowdhury, Rumman and Dafoe, Allan and Hadfield, Gillian and Levi, Margaret and Snidal, Duncan},
  title   = {International Institutions for Advanced {AI}},
  journal = {arXiv preprint arXiv:2307.04699},
  year    = {2023}
}
```
What it establishes: a design taxonomy, with no empirical claims. It sets out four institutional models: a Commission on Frontier AI (expert consensus), an Advanced AI Governance Organization (standards, possibly compliance monitoring), a Frontier AI Collaborative (access), and an AI Safety Project (joint safety research). It also lists open questions about whether each is viable.

### trager2023 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2308.15514 (v2, 11 Sep 2023); Crossref SSRN record 10.2139/ssrn.4579899 (same author list).

```bibtex
@article{trager2023,
  author  = {Trager, Robert and Harack, Ben and Reuel, Anka and Carnegie, Allison and Heim, Lennart and Ho, Lewis and Kreps, Sarah and Lall, Ranjit and Larter, Owen and {\'O} h{\'E}igeartaigh, Se{\'a}n and Staffell, Simon and Villalobos, Jos{\'e} Jaime},
  title   = {International Governance of Civilian {AI}: A Jurisdictional Certification Approach},
  journal = {arXiv preprint arXiv:2308.15514},
  year    = {2023}
}
```
What it establishes: a policy proposal. An International AI Organization (IAIO) would certify *jurisdictions*, not firms, against international oversight standards. States would enforce this through import bans on goods whose supply chains embody AI from uncertified jurisdictions, and through export controls on inputs such as chips. The design borrows from ICAO, IMO and FATF.

### cihon2020 — VERIFIED
Checked: Crossref DOI 10.1145/3375627.3375857 (subtitle "Design Lessons from History"; pp. 228–234); abstract from Semantic Scholar.

```bibtex
@inproceedings{cihon2020,
  author    = {Cihon, Peter and Maas, Matthijs M. and Kemp, Luke},
  title     = {Should Artificial Intelligence Governance be Centralised? Design Lessons from History},
  booktitle = {Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society},
  pages     = {228--234},
  publisher = {ACM},
  year      = {2020},
  doi       = {10.1145/3375627.3375857}
}
```
What it establishes: a historical and comparative argument. Centralisation brings gains (efficiency, political power, deterring forum shopping) and costs (slowness, brittleness, a trade-off between participation and stringency). Locking in an inadequate central structure "may pose a fate worse than fragmentation". For now, fragmentation is likely to persist.

### narayanan2025 — VERIFIED
Checked: https://knightcolumbia.org/content/ai-as-normal-technology (authors, 15 April 2025, Knight First Amendment Institute).

```bibtex
@misc{narayanan2025,
  author       = {Narayanan, Arvind and Kapoor, Sayash},
  title        = {{AI} as Normal Technology},
  howpublished = {Knight First Amendment Institute at Columbia University, 15 April 2025. \url{https://knightcolumbia.org/content/ai-as-normal-technology}},
  year         = {2025}
}
```
What it establishes: a position essay. AI should be treated as a normal transformative technology whose effects arrive over decades of diffusion, not as an imminent superintelligence. It argues for resilience as the governing policy aim and explicitly against nonproliferation, which it says reduces resilience. It also argues against drastic interventions premised on uncontrollable superintelligence.

### hendrycks2025superintelligence — VERIFIED (title note)
Checked: arXiv API, https://arxiv.org/abs/2503.05628 (v2, 14 Apr 2025). **The arXiv title is "Superintelligence Strategy: Expert Version".** The companion site is https://nationalsecurity.ai/. If you cite the arXiv record, use the arXiv title.

```bibtex
@article{hendrycks2025superintelligence,
  author  = {Hendrycks, Dan and Schmidt, Eric and Wang, Alexandr},
  title   = {Superintelligence Strategy: Expert Version},
  journal = {arXiv preprint arXiv:2503.05628},
  year    = {2025}
}
```
What it establishes: a strategy paper. It introduces Mutual Assured AI Malfunction (MAIM), a deterrence regime in which any state's bid for unilateral AI dominance is met with preventive sabotage by rivals. It claims MAIM already describes the strategic situation. Its three-part strategy is deterrence, nonproliferation to rogue actors, and competitiveness.

### anderljung2023 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2307.03718 (v4, 7 Nov 2023; author order corrected by the authors in v2). No journal version found.

```bibtex
@article{anderljung2023,
  author  = {Anderljung, Markus and Barnhart, Joslyn and Korinek, Anton and Leung, Jade and O'Keefe, Cullen and Whittlestone, Jess and Avin, Shahar and Brundage, Miles and Bullock, Justin and Cass-Beggs, Duncan and Chang, Ben and Collins, Tantum and Fist, Tim and Hadfield, Gillian and Hayes, Alan and Ho, Lewis and Hooker, Sara and Horvitz, Eric and Kolt, Noam and Schuett, Jonas and Shavit, Yonadav and Siddarth, Divya and Trager, Robert and Wolf, Kevin},
  title   = {Frontier {AI} Regulation: Managing Emerging Risks to Public Safety},
  journal = {arXiv preprint arXiv:2307.03718},
  year    = {2023}
}
```
What it establishes: a regulatory proposal. Frontier models are hard to regulate for three reasons: dangerous capabilities emerge unexpectedly, misuse is hard to prevent, and capabilities proliferate. It proposes three building blocks: standard-setting, registration and reporting, and compliance mechanisms, possibly licensing. It also proposes initial safety standards: pre-deployment risk assessment, external scrutiny, risk-informed deployment, and post-deployment monitoring. It treats industry self-regulation as a first step only.

### shevlane2023 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2305.15324 (v2, 22 Sep 2023).

```bibtex
@article{shevlane2023,
  author  = {Shevlane, Toby and Farquhar, Sebastian and Garfinkel, Ben and Phuong, Mary and Whittlestone, Jess and Leung, Jade and Kokotajlo, Daniel and Marchal, Nahema and Anderljung, Markus and Kolt, Noam and Ho, Lewis and Siddarth, Divya and Avin, Shahar and Hawkins, Will and Kim, Been and Gabriel, Iason and Bolina, Vijay and Clark, Jack and Bengio, Yoshua and Christiano, Paul and Dafoe, Allan},
  title   = {Model Evaluation for Extreme Risks},
  journal = {arXiv preprint arXiv:2305.15324},
  year    = {2023}
}
```
What it establishes: a framework paper. Developers need "dangerous capability evaluations" and "alignment evaluations" to inform decisions on training, deployment and security, and to keep policymakers informed.

### karnofsky2024 — VERIFIED
Checked: https://carnegieendowment.org/research/2024/09/if-then-commitments-for-ai-risk-reduction (author, 13 Sep 2024, type "Paper", Carnegie California program).

```bibtex
@misc{karnofsky2024,
  author       = {Karnofsky, Holden},
  title        = {If-Then Commitments for {AI} Risk Reduction},
  howpublished = {Carnegie Endowment for International Peace, 13 September 2024. \url{https://carnegieendowment.org/research/2024/09/if-then-commitments-for-ai-risk-reduction}},
  year         = {2024}
}
```
What it establishes: it defines and explains if-then commitments, of the form "If an AI model has capability X, risk mitigations Y must be in place". These can be adopted voluntarily or enforced by regulators. It works through an example on chemical and biological weapons uplift.

### seoul2024 — VERIFIED
Checked: GOV.UK content API for https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024 (first published 2024-05-21; last updated 2025-02-07).
- Original 16 signatories (21 May 2024): Amazon, Anthropic, Cohere, Google, G42, IBM, Inflection AI, Meta, Microsoft, **Mistral AI** (France), Naver, OpenAI, Samsung Electronics, Technology Innovation Institute, xAI, **Zhipu.ai** (China).
- Added later: Magic, **Minimax** (China), **01.ai** (China), NVIDIA. That makes 20.
- So US, European (Mistral AI) and Chinese (Zhipu.ai; later Minimax and 01.ai) firms are all confirmed.
- Content: firms committed to publish a safety framework focused on severe risks before the AI Summit in France. They also committed, "in the extreme", not to develop or deploy a model at all if mitigations cannot keep risks below thresholds.

```bibtex
@misc{seoul2024,
  author       = {{UK Department for Science, Innovation and Technology}},
  title        = {Frontier {AI} Safety Commitments, {AI} {Seoul} Summit 2024},
  howpublished = {GOV.UK, 21 May 2024 (signatory list last updated 7 February 2025). \url{https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024}},
  year         = {2024}
}
```
Note: the page itself says "The UK and Republic of Korea governments announced that the following organisations have agreed". The author field names DSIT as the publishing department. You could instead use `author = {{Governments of the United Kingdom and the Republic of Korea}}`.

### idais2024 — VERIFIED (IDAIS-Beijing)
Checked: https://idais.ai/dialogue/idais-beijing/ (statement text and signatory list).
- Title: "Consensus Statement on Red Lines in Artificial Intelligence". Beijing, China, 10–11 March 2024.
- The red lines are introduced as "a non-exhaustive list". The five named red lines are Autonomous Replication or Improvement, Power Seeking, Assisting Weapon Development, Cyberattacks, and Deception. A short quote under 15 words: "No AI system should be able to copy or improve itself without explicit human approval".
- Signatories include US-based scientists: Stuart Russell (UC Berkeley), Dawn Song (UC Berkeley), Dylan Hadfield-Menell (MIT) and Gillian Hadfield (listed now at Johns Hopkins). Chinese signatories include Andrew Yao (Tsinghua), Ya-Qin Zhang (Tsinghua), Xue Lan (Tsinghua), Fu Ying, Zeng Yi (CAS), HongJiang Zhang and Huang Tiejun (BAAI), Zhang Peng (Zhipu AI) and Li Hang (ByteDance). Also Hinton and Bengio (Canada).
- Caution: the website lists signatories' *current* affiliations, which may differ from March 2024.

```bibtex
@misc{idais2024,
  author       = {{International Dialogues on AI Safety}},
  title        = {{IDAIS-Beijing}: Consensus Statement on Red Lines in Artificial Intelligence},
  howpublished = {Beijing, 10--11 March 2024. \url{https://idais.ai/dialogue/idais-beijing/}},
  year         = {2024}
}
```

Optional second entry, IDAIS-Venice — VERIFIED. Checked: https://idais.ai/dialogue/idais-venice/.
- Title: "Consensus Statement on AI Safety as a Global Public Good". Venice, Italy, 5–8 September 2024.
- Signatories include Stuart Russell (UC Berkeley), Gillian Hadfield (Johns Hopkins) and Mariano-Florentino Cuéllar (Carnegie Endowment). Chinese signatories include Andrew Yao, Xue Lan, Fu Ying, Zeng Yi and Tang Jie (Zhipu AI).
- The statement calls for recognising "AI safety as a global public good" and working towards global governance of these risks.

```bibtex
@misc{idais2024venice,
  author       = {{International Dialogues on AI Safety}},
  title        = {{IDAIS-Venice}: Consensus Statement on {AI} Safety as a Global Public Good},
  howpublished = {Venice, 5--8 September 2024. \url{https://idais.ai/dialogue/idais-venice/}},
  year         = {2024}
}
```

### paris2025 — VERIFIED
Checked: https://www.elysee.fr/en/emmanuel-macron/2025/02/11/statement-on-inclusive-and-sustainable-artificial-intelligence-for-people-and-the-planet ("Posted on 11 February 2025"; full signatory list on the page).
- The exact title is confirmed: "Statement on Inclusive and Sustainable Artificial Intelligence for People and the Planet". The summit was held on 10–11 February 2025.
- **China is on the signatory list. The United States and the United Kingdom are not** (the UK name appears on the page only in a footnote about another initiative's membership).
- The current page lists 63 countries plus the African Union Commission and the EU. Press reports on the day gave about 60 (for example, Computer Weekly, "UK and US refuse to sign"). The list grew later, so do not give an exact count without a date.
- Footnote 1 of the statement says it covers civil applications only.

```bibtex
@misc{paris2025,
  author       = {{AI Action Summit}},
  title        = {Statement on Inclusive and Sustainable Artificial Intelligence for People and the Planet},
  howpublished = {Paris, 11 February 2025. Published by the {\'E}lys{\'e}e. \url{https://www.elysee.fr/en/emmanuel-macron/2025/02/11/statement-on-inclusive-and-sustainable-artificial-intelligence-for-people-and-the-planet}},
  year         = {2025}
}
```

### unpanel2025 — VERIFIED
Checked: the resolution PDF https://www.un.org/pga/wp-content/uploads/sites/110/2025/12/A_RES_79_325-EN.pdf (symbol, date, title, "without reference to a Main Committee (A/79/L.118)"). Also the UN Scientific Panel FAQ, https://www.un.org/independent-international-scientific-panel-ai/en/faq ("adopted by consensus on 26 August 2025").
- Number: **A/RES/79/325**. Adopted **26 August 2025**. Distributed 27 August 2025. Adopted by consensus.
- Exact title: "Terms of reference and modalities for the establishment and functioning of the Independent International Scientific Panel on Artificial Intelligence and the Global Dialogue on Artificial Intelligence Governance".
- The panel has 40 members serving three-year terms. It produces an annual "policy-relevant but non-prescriptive" report. The resolution is limited to the non-military domain.

```bibtex
@misc{unpanel2025,
  author       = {{United Nations General Assembly}},
  title        = {Terms of Reference and Modalities for the Establishment and Functioning of the Independent International Scientific Panel on Artificial Intelligence and the Global Dialogue on Artificial Intelligence Governance},
  howpublished = {Resolution A/RES/79/325, adopted 26 August 2025. \url{https://www.un.org/pga/wp-content/uploads/sites/110/2025/12/A_RES_79_325-EN.pdf}},
  year         = {2025}
}
```

### tc260framework2024 — VERIFIED (from secondary sources; official PDF link now redirects)
Checked:
- Lexology summary: "National Technical Committee 260 on Cybersecurity of SAC released the AI Safety Governance Framework (Version 1.0)" on 9 September 2024.
- datenrecht.ch, OneTrust and Trivium (11 Sep 2024) all give the release date as 9 September 2024.
- The official English PDF URL, https://www.tc260.org.cn/upload/2024-09-09/1725849192841090989.pdf, now serves the TC260 homepage, so I could not read the cover directly.
- Chinese: 全国网络安全标准化技术委员会,《人工智能安全治理框架》1.0版.
- A Version 2.0 was released on 15 September 2025 (SESEC), so cite 1.0 explicitly.

```bibtex
@misc{tc260framework2024,
  author       = {{National Technical Committee 260 on Cybersecurity of Standardization Administration of China (TC260)}},
  title        = {{AI} Safety Governance Framework (Version 1.0)},
  howpublished = {Beijing, 9 September 2024. \url{https://www.tc260.org.cn/upload/2024-09-09/1725849192841090989.pdf}},
  year         = {2024}
}
```

### gpaicode2025 — VERIFIED
Checked: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai (title "The General-Purpose AI Code of Practice", published 10 July 2025, prepared by independent experts in a multi-stakeholder process and published by the European Commission; chapters Transparency, Copyright, Safety and Security).
- On 1 August 2025 the Commission and the AI Board confirmed the Code as an adequate voluntary tool. Source: the Commission opinion at https://digital-strategy.ec.europa.eu/en/library/commission-opinion-assessment-general-purpose-ai-code-practice, as reported in search results; I did not open the opinion PDF itself.
- Reported in the press, not checked against an official list: Meta declined to sign, and xAI signed only the Safety and Security chapter.

```bibtex
@misc{gpaicode2025,
  author       = {{European Commission}},
  title        = {The General-Purpose {AI} Code of Practice},
  howpublished = {Published 10 July 2025; prepared by independent experts in a multi-stakeholder process facilitated by the {AI} Office. \url{https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai}},
  year         = {2025}
}
```

### sb53 — VERIFIED
Checked: https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB53 (Wiener; topic "Artificial intelligence models: large developers"; approved by the Governor 29 Sep 2025; "Chaptered by Secretary of State. Chapter 138, Statutes of 2025"). Also the bill text, which adds Bus. & Prof. Code §22757.10: "This chapter shall be known as the Transparency in Frontier Artificial Intelligence Act".
- The text defines a frontier model as one trained with more than 10^26 operations, and a large frontier developer as one with more than $500M annual revenue. Large frontier developers must publish a frontier AI framework.

```bibtex
@misc{sb53,
  author       = {{California State Legislature}},
  title        = {Senate Bill No.~53: Artificial Intelligence Models: Large Developers ({Transparency} in {Frontier} {Artificial} {Intelligence} {Act})},
  howpublished = {Chapter 138, Statutes of 2025; approved by the Governor 29 September 2025. \url{https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53}},
  year         = {2025}
}
```

---

## 2. Verification and compute governance

### shavit2023 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2303.11341 (v2, 30 May 2023).

```bibtex
@article{shavit2023,
  author  = {Shavit, Yonadav},
  title   = {What does it take to catch a {Chinchilla}? {Verifying} Rules on Large-Scale Neural Network Training via Compute Monitoring},
  journal = {arXiv preprint arXiv:2303.11341},
  year    = {2023}
}
```
What it establishes: a system design for verifying rules on large training runs through the hardware. It has three parts: on-chip firmware weight snapshots, training-run records that inspectors can check (a Proof-of-Learning variant), and supply-chain monitoring of chips. It breaks verification down into narrow open technical problems. It is a design, not a deployed system.

### wasil2024 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2408.16074 (v2, 4 Nov 2024). The exact title uses lowercase after the first word on arXiv. Authors: Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett.

```bibtex
@article{wasil2024,
  author  = {Wasil, Akash R. and Reed, Tom and Miller, Jack William and Barnett, Peter},
  title   = {Verification Methods for International {AI} Agreements},
  journal = {arXiv preprint arXiv:2408.16074},
  year    = {2024}
}
```
What it establishes: a survey of 10 verification methods for two kinds of violation, unauthorized training runs (for example, above a FLOP threshold) and unauthorized data centres. The methods fall into national technical means, access-dependent methods and hardware-dependent methods. For each it gives historical precedents and evasion routes.

### sastry2024 — VERIFIED
Checked: arXiv API, https://arxiv.org/abs/2402.08797 (v1, 13 Feb 2024).

```bibtex
@article{sastry2024,
  author  = {Sastry, Girish and Heim, Lennart and Belfield, Haydn and Anderljung, Markus and Brundage, Miles and Hazell, Julian and O'Keefe, Cullen and Hadfield, Gillian K. and Ngo, Richard and Pilz, Konstantin and Gor, George and Bluemke, Emma and Shoker, Sarah and Egan, Janet and Trager, Robert F. and Avin, Shahar and Weller, Adrian and Bengio, Yoshua and Coyle, Diane},
  title   = {Computing Power and the Governance of Artificial Intelligence},
  journal = {arXiv preprint arXiv:2402.08797},
  year    = {2024}
}
```
What it establishes: compute is an unusually governable input to AI. It is detectable, excludable and quantifiable, and comes from a highly concentrated supply chain. It can support visibility, resource allocation and enforcement. Proposals differ in how ready they are, and naive compute governance carries risks to privacy, economic impacts and centralization of power.

### casper2024 — VERIFIED
Checked: Crossref DOI 10.1145/3630106.3659037 (pp. 2254–2272, FAccT '24, 3–6 June 2024, Rio de Janeiro); arXiv 2401.14446 journal_ref.

```bibtex
@inproceedings{casper2024,
  author    = {Casper, Stephen and Ezell, Carson and Siegmann, Charlotte and Kolt, Noam and Curtis, Taylor Lynn and Bucknall, Benjamin and Haupt, Andreas and Wei, Kevin and Scheurer, J{\'e}r{\'e}my and Hobbhahn, Marius and Sharkey, Lee and Krishna, Satyapriya and Von Hagen, Marvin and Alberti, Silas and Chan, Alan and Sun, Qinyi and Gerovitch, Michael and Bau, David and Tegmark, Max and Krueger, David and Hadfield-Menell, Dylan},
  title     = {Black-Box Access is Insufficient for Rigorous {AI} Audits},
  booktitle = {Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency},
  pages     = {2254--2272},
  publisher = {ACM},
  year      = {2024},
  doi       = {10.1145/3630106.3659037}
}
```
What it establishes: an argument paper. Audits that query outputs only (black-box) are weaker than white-box audits (weights, activations, gradients) and outside-the-box audits (training data, documentation, internal evaluations). Audit results cannot be interpreted without transparency about the access the auditor had. The paper also covers safeguards that reduce the security risks of deeper access.

---

## 3. Evaluation failure modes

### vanderweij2024 — VERIFIED (published at ICLR 2025)
Checked: https://proceedings.iclr.cc/paper_files/paper/2025/hash/b5e5753b0a0e440a6d8dc7e143617cec-Abstract-Conference.html (ICLR 2025; authors Teun van der Weij, Felix Hofstätter, Oliver Jaffe, Samuel Brown, Francis Ward); arXiv 2406.07358v4. The arXiv record lists "Ollie Jaffe", "Samuel F. Brown" and "Francis Rhys Ward". The entry below follows the ICLR proceedings page. The key stays `vanderweij2024` as requested, though the venue year is 2025.

```bibtex
@inproceedings{vanderweij2024,
  author    = {van der Weij, Teun and Hofst{\"a}tter, Felix and Jaffe, Oliver and Brown, Samuel F. and Ward, Francis Rhys},
  title     = {{AI} Sandbagging: Language Models can Strategically Underperform on Evaluations},
  booktitle = {The Thirteenth International Conference on Learning Representations (ICLR)},
  year      = {2025}
}
```
What it establishes: frontier LMs (GPT-4, Claude 3 Opus) can be *prompted* to underperform selectively on dangerous-capability evaluations (WMDP) while keeping general performance. Models can be *fine-tuned* to hide capabilities unless given a password, and this generalizes to held-out benchmarks. Models can also be made to hit target scores. Mimicking a weaker model's answers worked only moderately well. In short, sandbagging is shown to be *possible* (elicited), not observed arising on its own.

### needham2025 — VERIFIED (arXiv; no venue confirmed)
Checked: arXiv API, https://arxiv.org/abs/2505.23836 (v3, 16 Jul 2025); MATS page lists no venue. A search-engine summary claimed ICLR 2026, but I could not confirm it on OpenReview or ICLR proceedings, so I cite it as a preprint.

```bibtex
@article{needham2025,
  author  = {Needham, Joe and Edkins, Giles and Pimpale, Govind and Bartsch, Henning and Hobbhahn, Marius},
  title   = {Large Language Models Often Know When They Are Being Evaluated},
  journal = {arXiv preprint arXiv:2505.23836},
  year    = {2025}
}
```
What it establishes: the authors built a benchmark of 1,000 transcripts drawn from 61 datasets. Frontier models classify evaluation versus deployment transcripts above chance (Gemini-2.5-Pro AUC 0.83), but below a simple human baseline (AUC 0.92). Both models and humans do better on agentic transcripts, and models can often identify what an evaluation is testing for. The paper measures *awareness*; it does not show that behaviour changes as a result.

---

## 4. Cooperation theory

### barrett1994 — VERIFIED
Checked: Crossref DOI 10.1093/oep/46.supplement_1.878 (vol. 46, Supplement_1, pp. 878–894, Oct 1994); abstract on EconPapers RePEc:oup:oxecpp:v:46:y:1994:i:0:p:878-94.

```bibtex
@article{barrett1994,
  author  = {Barrett, Scott},
  title   = {Self-Enforcing International Environmental Agreements},
  journal = {Oxford Economic Papers},
  volume  = {46},
  number  = {Supplement 1},
  pages   = {878--894},
  year    = {1994},
  doi     = {10.1093/oep/46.supplement_1.878}
}
```
What it establishes: international environmental agreements (IEAs) cannot be enforced by a third party. The paper uses two models: a coalition model with the membership decided jointly, and a renegotiation-proof repeated game. Both indicate that self-enforcing IEAs "can do little to improve on the noncooperative outcome when the number of countries ... is large" (abstract). A frequently cited result in the body is that the gain from the stable agreement is inversely related to how many sign. Large coalitions are stable only when the gains from cooperation are small. Secondary sources (Rubio & Ulph 2004, Ivie WP-AD 2004-23) confirm this result; I did not read it in the original full text.

### carraro1993 — VERIFIED
Checked: Crossref DOI 10.1016/0047-2727(93)90037-T (vol. 52, no. 3, pp. 309–328, Oct 1993); abstract on IDEAS (RePEc:eee:pubeco:v:52:y:1993:i:3:p:309-328).

```bibtex
@article{carraro1993,
  author  = {Carraro, Carlo and Siniscalco, Domenico},
  title   = {Strategies for the International Protection of the Environment},
  journal = {Journal of Public Economics},
  volume  = {52},
  number  = {3},
  pages   = {309--328},
  year    = {1993},
  doi     = {10.1016/0047-2727(93)90037-T}
}
```
What it establishes: an environmental coalition forms when it is both profitable and stable, meaning no free riding pays. Such coalitions exist, but only a small number of countries cooperate. The paper studies transfers that could expand the coalition. Large stable coalitions arise when environmental interdependence is low and/or damage functions are near-separable. (IDEAS notes this abstract is "borrowed from another version of this item".)

### hirshleifer1983 — VERIFIED
Checked: Crossref DOI 10.1007/BF00141070 (vol. 41, no. 3, pp. 371–386); abstract on IDEAS (RePEc:kap:pubcho:v:41:y:1983:i:3:p:371-386). Note that a correction exists: Hirshleifer, "From weakest-link to best-shot: Correction", *Public Choice* 46(2), 1985, DOI 10.1007/BF00179743.

```bibtex
@article{hirshleifer1983,
  author  = {Hirshleifer, Jack},
  title   = {From Weakest-Link to Best-Shot: The Voluntary Provision of Public Goods},
  journal = {Public Choice},
  volume  = {41},
  number  = {3},
  pages   = {371--386},
  year    = {1983},
  doi     = {10.1007/BF00141070}
}
```
What it establishes: it compares three aggregation rules for a public good. Under summation, the total is the sum of contributions; under weakest-link, the minimum; under best-shot, the maximum. Compared with summation, underprovision is *moderated* under weakest-link and *aggravated* under best-shot. Disasters approximate weakest-link conditions, which the paper uses to explain unusual unselfishness in disasters.

### hua2021 — VERIFIED
Checked: https://yjolt.org/ai-antitrust-reconciling-tensions-between-competition-law-and-cooperative-ai-development (citation "23 Yale J.L. & Tech. 415"). I also downloaded the article PDF (https://yjolt.org/sites/default/files/23_yale_j.l._tech._415_ai_antitrust_nov_0.pdf). Its header reads "Volume 23, Spring 2021". The numbered text runs from p. 415 to p. 541, followed by unpaginated appendices. Not in Crossref.

```bibtex
@article{hua2021,
  author  = {Hua, Shin-Shin and Belfield, Haydn},
  title   = {{AI} \& Antitrust: Reconciling Tensions Between Competition Law and Cooperative {AI} Development},
  journal = {Yale Journal of Law \& Technology},
  volume  = {23},
  pages   = {415--541},
  year    = {2021}
}
```
What it establishes: it analyses 14 proposed forms of cooperation between AI companies (windfall redistribution, assistance, mutual monitoring, information sharing and others) under *EU* competition law, mainly Article 101 TFEU. It identifies where each carries competition-law risk and proposes mitigations. Its conclusion is that cooperation for safety is often legally feasible if it is designed carefully. It is a doctrinal legal analysis, not an empirical or game-theoretic paper.

---

## 5. Philosophy of modelling

### levins1966 — VERIFIED
Checked: the JSTOR cover page on https://www.zoology.ubc.ca/let/pdfs/Levins1966.pdf ("American Scientist, DECEMBER 1966, Vol. 54, No. 4, pp. 421–431", Sigma Xi, https://www.jstor.org/stable/27836590). Not in Crossref.

```bibtex
@article{levins1966,
  author  = {Levins, Richard},
  title   = {The Strategy of Model Building in Population Biology},
  journal = {American Scientist},
  volume  = {54},
  number  = {4},
  pages   = {421--431},
  year    = {1966}
}
```
What it establishes: no manageable model can maximize generality, realism and precision at once, so modellers trade one off against the others. A result that holds across several models with different simplifications is a "robust theorem". The famous line on p. 423, verified, is: "our truth is the intersection of independent lies". The paper also says a satisfactory theory is usually a cluster of models.

### weisberg2006 — VERIFIED
Checked: Crossref DOI 10.1086/518628 (vol. 73, no. 5, pp. 730–742, Dec 2006; abstract).

```bibtex
@article{weisberg2006,
  author  = {Weisberg, Michael},
  title   = {Robustness Analysis},
  journal = {Philosophy of Science},
  volume  = {73},
  number  = {5},
  pages   = {730--742},
  year    = {2006},
  doi     = {10.1086/518628}
}
```
What it establishes: it gives a new account of robustness analysis (Levins, Wimsatt) and answers Orzack and Sober's charge that robustness is non-empirical confirmation. Once the structure of a robust theorem is spelled out, such theorems carry a degree of confirmation even without direct empirical evidence.

### sugden2000 — VERIFIED
Checked: Crossref DOI 10.1080/135017800362220 (vol. 7, no. 1, pp. 1–31, Jan 2000).

```bibtex
@article{sugden2000,
  author  = {Sugden, Robert},
  title   = {Credible Worlds: The Status of Theoretical Models in Economics},
  journal = {Journal of Economic Methodology},
  volume  = {7},
  number  = {1},
  pages   = {1--31},
  year    = {2000},
  doi     = {10.1080/135017800362220}
}
```
What it establishes: using Akerlof's lemons model and Schelling's checkerboard model, it argues that theoretical models are best read as *credible counterfactual worlds*. They are not abstractions from the real world. They support inductive (abductive) inference to real-world claims when the model world is credible, in the sense that it could be true.

---

## 6. Checks on entries already in references.bib

All Crossref and arXiv checks were run 2026-10-02/03.

| key | status | finding |
|---|---|---|
| han2021 | OK | Crossref 10.1371/journal.pone.0244592: PLOS ONE 16(1) e0244592, 2021. The author order Han, Pereira, Lenaerts, Santos matches the publisher. |
| wei2024 | OK | Crossref 10.1609/aies.v7i1.31745: AIES vol. 7(1), pp. 1539–1555, 2024. |
| ahmed2023 | OK | Crossref 10.1126/science.ade2420: Science 379(6635):884–886. |
| raji2022 | OK | Crossref 10.1145/3514094.3534181: AIES '22, pp. 557–571. |
| costanzachock2022 | OK | Crossref 10.1145/3531146.3533213: FAccT '22, pp. 1571–1583. |
| birhane2024 | OK, incomplete | Crossref 10.1109/SaTML59370.2024.00037. Pages 612–643 could be added (`pages = {612--643}`). Not wrong as it stands. |
| whittaker2021 | OK | Crossref 10.1145/3488666: Interactions 28(6):50–55. |
| scheffer2009 | OK, incomplete | Crossref 10.1038/nature08227: Nature 461(7260):53–59. `number = {7260}` could be added. |
| kleinberg2021 | OK | Crossref 10.1073/pnas.2018340118: PNAS 118(22) e2018340118. |
| bommasani2022 | OK | NeurIPS 35 (2022) main track, confirmed on proceedings.neurips.cc and arXiv 2211.13972 ("Published at NeurIPS 2022"). The official title capitalizes "lead" in lowercase; this does not matter. |
| li2026preference | OK | arXiv 2502.01534v3 comment: "Accepted by ICLR 2026". The nine authors match. |
| awuni2026 | OK (bibliographic); **read the gloss below** | arXiv 2609.17857v1, 15 Sep 2026. The five authors match. |
| zatuchin2026 | OK (bibliographic) | arXiv 2610.00369v1, 30 Sep 2026. The author and title match. `{\.Z}atuchin` is the correct rendering of "Żatuchin". |

### What awuni2026 and zatuchin2026 actually find about own-model preference

**zatuchin2026 does find "no detectable own-model premium", but only in the Laurito et al. (PNAS 2025) data.**
- It reanalyses the three 5×5 generator-by-selector matrices from Laurito et al. (21,828 trials). It fits a two-way fixed-effects model with an own-model term γ, tested by exact permutation over 120 relabellings.
- Results: γ = +0.013 for products (p = 0.24), −0.010 for paper abstracts (p = 0.74), +0.054 for films (p = 0.07), and +0.019 pooled (p = 0.14; 95% interval −0.008 to 0.046).
- The same-vendor term for GPT-3.5 and GPT-4 is negative in all three datasets.
- The minimum detectable effect at 80% power is 0.034 pooled. The author says the absence is informative down to about 0.04 share points and "silent below that".
- Caveat: in the 4×4 matrix of Tan et al. (ACL 2024), the same method gives γ = **+0.148**, at the smallest p its 24 relabellings allow, with a same-family term of similar size. The paper therefore does not claim that own-model preference is absent in general. Its claim is that the Laurito data show a *shared* taste for model-written text, not a model favouring its own prose.

**awuni2026 does NOT find "no premium". It finds a positive *family-conditioned* preference, and it does not test own-model self-preference at all.**
- The design is explicit: "No judge evaluates its own generations, so this is not ordinary self-preference."
- Setup: four open-weight families (Llama 3.1, Qwen 2.5, Gemma 2, Yi 1.5), each at two scales, fully crossed, with 9,312 pairwise judgments.
- The naive per-family statistic is confounded with candidate quality (r = 0.95 with Bradley–Terry ability). After correcting for this, **all four families show a positive same-family lift of 3.4–8.4 percentage points**. The global FPS is 0.067 (95% CI [0.053, 0.084], permutation p = 0.0002).
- The effect survives quality controls, a human-consensus anchor and a float16 replication (FPS 0.066). In that replication Gemma and Yi are individually significant; Qwen and Llama point the same way but are not individually significant.
- Adding judge-side likelihood reduces the coefficient by 61%. The authors call this descriptive, not mediation.
- Position is a separate problem: 55.4% of AB/BA pairs reverse, and panel composition changes 18.5% of outcomes.

If the paper pairs these two as evidence of "no own-model premium", only Żatuchin supports that, and only for the Laurito matrices. Awuni is evidence *for* a judge preferring its own family, measured on generations from sibling models, never the judge's own.

### Minor formatting note on the existing bib
`bengio2025report`, `bengio2026report`, `aisi2025trends` and `weiss2019` keep their URL in a `url` field. Because aaai2027.bst ignores `url`, those URLs will not print. Move them into `howpublished` or `note` as `\url{...}` if they should appear.

---

## 7. Other checks

### 2025 US statement at the UN rejecting centralized global AI governance — VERIFIED (exists)
Checked: https://usun.usmission.gov/remarks-at-the-security-councils-open-debate-on-artificial-intelligence-and-international-peace-and-security/ (United States Mission to the UN; dated **September 24, 2025**; Michael Kratsios, Assistant to the President and OSTP Director; "AS PREPARED").
- Exact sentence: "We totally reject all efforts by international bodies to assert centralized control and global governance of AI."
- Venue: this was the **UN Security Council** open debate "Artificial Intelligence and International Peace and Security: Addressing the Complexities, Multifaceted Impacts, and Responsible Use", under the Republic of Korea's presidency. It was *not* the General Assembly, although it took place during the high-level week. NBC's headline says "at U.N. General Assembly", which is imprecise.
- Kratsios repeated the line on X with an added sentence calling "so-called existential risk" a danger to progress. For a formal citation, use the Mission text.

```bibtex
@misc{kratsios2025,
  author       = {Kratsios, Michael},
  title        = {Remarks at the {Security} {Council}'s Open Debate on Artificial Intelligence and International Peace and Security},
  howpublished = {United States Mission to the United Nations, New York, 24 September 2025 (as prepared). \url{https://usun.usmission.gov/remarks-at-the-security-councils-open-debate-on-artificial-intelligence-and-international-peace-and-security/}},
  year         = {2025}
}
```

A related, verified fact that the paper may find useful:
- On **12 February 2026** the US called for a recorded vote on the Secretary-General's appointments to the Independent International Scientific Panel on AI, and voted **No**.
- The tally was 117–2–2: the US and Paraguay against, Tunisia and Ukraine abstaining. Source: UNRIC, https://unric.org/en/general-assembly-appoints-artificial-intelligence-panel/.
- The US statement called the Panel and Global Dialogue "a significant overreach of the UN's mandate and competence". Source: https://usun.usmission.gov/remarks-on-the-appointment-of-members-of-the-independent-international-scientific-panel-on-artificial-intelligence/, by Lauren Lovelace, as delivered.
- If you cite it:

```bibtex
@misc{usun2026panel,
  author       = {{United States Mission to the United Nations}},
  title        = {Remarks on the Appointment of Members of the Independent International Scientific Panel on Artificial Intelligence},
  howpublished = {Delivered by Lauren Lovelace, New York, 12 February 2026. \url{https://usun.usmission.gov/remarks-on-the-appointment-of-members-of-the-independent-international-scientific-panel-on-artificial-intelligence/}},
  year         = {2026}
}
```

### Were A/RES/78/265 and A/RES/78/311 adopted without a vote? — VERIFIED: yes, both
Checked: the official verbatim records from the UN ODS, A/78/PV.63 and A/78/PV.97, and the resolution texts.
- **A/RES/78/265**, "Seizing the opportunities of safe, secure and trustworthy artificial intelligence systems for sustainable development". Adopted **21 March 2024**, 63rd plenary meeting.
  - The President asked "May I take it that the Assembly decides to adopt draft resolution A/78/L.49?", and the record notes "Draft resolution A/78/L.49 was adopted (resolution 78/265)". In other words, it was adopted without a vote.
  - The UN press release GA/12588, as quoted by UN News via GlobalSecurity, says "Adopting a United States-led draft resolution without a vote".
  - The US introduced it, and **China joined as a co-sponsor** (named in the Secretariat's list of additional sponsors).
- **A/RES/78/311**, "Enhancing international cooperation on capacity-building of artificial intelligence". Adopted **1 July 2024**, 97th plenary meeting, without reference to a Main Committee (A/78/L.86).
  - The same procedure applied: "May I take it ... Draft resolution A/78/L.86 was adopted (resolution 78/311)". It was adopted without a vote.
  - China introduced it, and **the United States of America joined as a co-sponsor** (named in the Secretariat's list of additional sponsors).
- The existing `unga2024` and `unga2024capacity` entries have the correct titles and dates.
- A/RES/79/325 (26 August 2025) was also adopted by consensus (UN Scientific Panel FAQ). The resolution header shows no recorded vote.
