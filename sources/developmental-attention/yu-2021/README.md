# Public coded naming and gaze records

Original public files accompanying Chen Yu, Yayun Zhang, Lauren K. Slone and Linda B. Smith (2021), *The infant's view redefines the problem of referential uncertainty in early word learning*, [PNAS DOI](https://doi.org/10.1073/pnas.2107019118). Dataset: [OSF mvz78](https://osf.io/mvz78/). Retrieved 8 October 2026.

The eight deposited files are unchanged: the authors' `readme.txt` and seven CSVs. [PROVENANCE.json](PROVENANCE.json) records download links, byte counts and SHA-256 values. Every original matches the hash returned by OSF. The public [node metadata](node-api.json) and [file-list metadata](files-api.json) are also preserved. The node declares no dataset license; no license has been inferred from the article. The article was consulted through the [institutional deposited PDF](https://ueaeprints.uea.ac.uk/id/document/91113). Its source bytes were not imported into this directory.

Each CSV contains the same 1,508 participant/event identities from 36 participants, measured over different nominal durations. The first line is a unit annotation, the second column headers. Gaze values are stored as fractions between zero and one despite the percentage wording. The four-second file includes two extra columns, `expID` and `trialsID`; the other six files have seven columns. The extra experiment column is uniformly 12, not two experimental groups. Original headers and rows are preserved.

Some exported intervals are shorter than their nominal duration. Tiny target-plus-other sums above one, at most 0.000005, are retained as deposited rounding differences. Source records do not separately identify tracking loss and looking away from coded objects. “Others” combines objects rather than identifying each competitor. These limitations are material to interpretation.

The paper's method codes gaze and naming during parent–infant toy play. It distinguishes tracking failure from off-object looking in the underlying video. Those distinctions cannot be recovered separately from these summary fields. The files do not provide child word-learning outcomes or parent-gaze trajectories. No private video was requested or downloaded.

The [analysis plan and reproducible calculations](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/naming-attention/README.md) retain all rows. They assess an operational gaze-coverage assumption without claiming an exact reproduction of every published analysis or identifying infants' learning algorithms.
