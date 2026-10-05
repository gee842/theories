# Historical quoting correction before completed replay

6 October 2026. The first attempted replay exited before writing any results or aggregate, because the initial implementation omitted the historical loader's global string representer. This is an implementation correction from additional source inspection, not a changed outcome criterion.

The preserved `yaml_loader.py` registers a representer that double-quotes every string when `read_suite_file` dumps parsed YAML. Plain `yaml.dump` without that registration instead single-quotes some injection placeholders and fails on apostrophes in inserted attack text. Replay now supplies an explicit local **SafeDumper** string representer with the same double-quote style. Parsing remains SafeLoader with no custom constructors, includes, imports or evaluation. The loader source joins the frozen source hash set. This preserves the historical formatting side effect without importing or executing the benchmark.

An earlier invocation also exited before reading data because the experiment directory selected a Python installation without PyYAML. The executable used for the retry is `/Users/ren/.pyenv/versions/3.11.2/bin/python3`, with PyYAML 6.0.2. These failed attempts supplied no replay aggregates; the original contract and source-clarification bytes are unchanged.
