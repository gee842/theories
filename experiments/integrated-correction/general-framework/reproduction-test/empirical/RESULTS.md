# Institutional agreement persists; renewal remains unidentified

The frozen analysis finds a positive contrast on retained permission to sanction: **+42.59 percentage points** for facilitated versus ordinary discussion, approximate 95% interval **[22.02, 63.17]**. But **66 of 72 groups kept exactly the same recorded enforcement-system category throughout all three communication opportunities**. Initial formation followed by an unchanged agreement is therefore a strong competing explanation. This study does not establish repeated endogenous institutional renewal or succession.

This is an exploratory reanalysis of [DeCaro et al. (2024)](https://doi.org/10.1371/journal.pone.0307832), whose published findings were already known. The [protocol](PROTOCOL.md) was frozen before reading group outcome records, not before the source study or its publication. The source was selected for its design and measurements; no outcome-driven switch to another dataset occurred.

## Frozen primary result

The endpoint is a group having an enforcement-system code of 2 or 3 in **both** its second and third communication opportunities. Code 2 permits independent sanctions against violations; code 3 coordinates sanctions. These record an agreement expressed by at least two members. They do not measure universal consent, actual punishment, moral alignment, or payment to maintain the enforcement apparatus.

Each session's group outcomes were averaged first. The primary contrast equally weights the three initial-regime comparisons below. All 72 groups and 31 actual sessions enter; no primary observations were missing.

| Initial regime and treatment pair | Ordinary discussion: retained groups / all groups | Facilitated: retained groups / all groups | Sessions, ordinary / facilitated | Difference in session means |
|---|---:|---:|---:|---:|
| Immediate communication: CNN / FNN | 1 / 11 | 5 / 11 | 4 / 5 | +41.67 pp |
| Initially no communication or sanctions: NCN / NFN | 1 / 11 | 7 / 14 | 4 / 6 | +41.67 pp |
| Initially sanctions without communication: PCN / PFN | 1 / 13 | 6 / 12 | 6 / 6 | +44.44 pp |

Across equally weighted regimes, the session-weighted endpoint averages are 7.41% under ordinary discussion and 50.00% under facilitation. The approximate Welch–Satterthwaite calculation gives standard error 8.74 pp, 7.18 degrees of freedom, and two-sided p = .00169. The frozen group-weighting sensitivity is +39.86 pp. The small number of sessions per treatment makes the interval approximate, not an exact randomization guarantee.

**Assignment qualification:** the paper reports random assignment of groups, but every actual session in the archive contains only one treatment. The archive's `SessID` is a group-session identifier, not an independent session identifier. We removed its group prefix and used 31 sessions, rather than treating 72 identifiers as independent sessions or 288 participants as independent treatment units. A subsequent check of the authors' operational protocol confirms that the experimenter loads a treatment scheduled for the day/session, consulting a Treatment Order Log. That log's allocation algorithm has not been verified. Random group membership does not establish randomized treatment order across sessions. Thus this is an observed intervention contrast; a causal interpretation additionally requires credible session allocation or exchangeability, absence of relevant session confounding, and appropriate outcome measurement. Clustering repairs the unit of uncertainty, not an unverified assignment mechanism. See [assignment audit](DESIGN-AUDIT.md).

## Competing explanation: most agreements do not change

The frozen transition diagnostic finds 66/72 groups with identical codes at all three opportunities, and only 3/72 with a change from the second to the third. Counts of constant categories by treatment are CNN 10/11, FNN 11/11, NCN 10/11, NFN 13/14, PCN 12/13, and PFN 10/12. Full category transitions are saved in [transitions.csv](results/transitions.csv).

Thus the primary endpoint captures persistence of an agreement, often already present at the first communication opportunity. It does not establish fresh ratification, expenditure on institutional capacity, replacement of governors, or restoration after damage. The source coding records a system in each round; an unchanged code cannot by itself reveal whether people actively renewed it or simply retained it. Conversely, a changed code does not isolate the cause of that revision.

The main workbook agrees with the first coder on all 216 group-opportunity ES values. The two recorded coders differ on 19/216 values. Independent review located these disagreements in eight groups and found that five of 72 groups would change binary endpoint under the second coder. We preserved the supplied main outcome and did not select a coder or recode transcripts based on the result. This is a measurement limitation, especially when the observed number of transitions is small. The review's coder sensitivity is secondary and does not replace the frozen result.

## Physical and behavioral outcomes remain separate

The frozen descriptive checks use only each group's three communication rounds. Collected tokens are gross resource earnings per person per round; penalties are the mean number triggered by the entire group per round. Neither is the primary institutional endpoint.

| Treatment | Tokens per person per round | Penalties per group per round |
|---|---:|---:|
| CNN | 84.54 | 0.33 |
| FNN | 90.55 | 0.18 |
| NCN | 84.11 | 2.12 |
| NFN | 95.05 | 0.02 |
| PCN | 84.95 | 0.13 |
| PFN | 98.11 | 2.64 |

Permission to sanction plainly does not imply more sanctions in every treatment. These descriptive values do not identify sanctions' effect on resources, mediation of facilitation, or the effect of prior resource failure on later institutional support. Facilitation can directly alter discussion, so it is not a justified instrument for experienced failure. The resource dynamics are simulated while the participants and choices are real; this is not a second independent ecological experiment.

## What this contributes

This provides additional component evidence of different retained enforcement agreements under a deliberative intervention. Interpreting that contrast causally requires the assignment and coding assumptions above. The positive result is consistent with the authors' already published conclusions; it is not a newly discovered general law. The negative diagnostic matters equally: the data predominantly fit initial formation plus static persistence, leaving the stronger self-reproduction mechanism unresolved.

The apparatus, communication window, group membership, and ultimate withdrawal of enforcement were supplied by the experiment. Later inability to sanction must not be described as an endogenous failure to maintain it. The available data do not identify a full outcomes → support → maintained capacity → renewed outcomes loop, and no such causal estimate is reported.

## Provenance and reproducibility

- Original workbooks are preserved unchanged in `data/`; macros were not executed. Main source: `Dataset2_Main.xlsx`; the primary ES inputs are `Data!CD2:CF289`, named `ES Rd1`, `ES Rd2`, and `ES Rd3`. Exact input ranges and file hashes are recorded in [analysis.json](results/analysis.json).
- Source: [public OSF archive](https://osf.io/v3drm/). The article is CC BY. The public archive node declares no separate license; local access and analysis do not establish a redistribution license.
- Frozen protocol SHA256: `d99f55eb37b822aa5baec339bde0ea56e46c92260bde924d8b89ff2472fb4891`.
- [Derived group rows](results/groups.csv), [actual-session rows](results/sessions.csv), and [analysis](results/analysis.json) preserve all observations, treatment-specific contrasts, secondary diagnostics, provenance, and source hashes. The read-only script is `analyze.py`; it uses the bundled workbook libraries and an existing research environment only for the missing Student-t distribution functions.

No prior empirical dossier or result was changed.
