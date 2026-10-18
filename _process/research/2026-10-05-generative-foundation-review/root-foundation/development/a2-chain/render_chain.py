#!/usr/bin/env python3
"""A2: render GENERATIVITY-CHAIN.md from the chain's data alone. `generative_chain.py --render` refuses while linked
sources are pending; P129 rendered the page from the data after `validate` passed, and A2 does the same, so the
page shows the data as reviewed and the pending sources stay listed by `--changes`.

usage (from the repository root): python3 -B render_chain.py
"""
import sys

sys.path.insert(0, '.')
from tools.research import generative_chain as chain  # noqa: E402


def main():
    data = chain.read_data()
    errors = chain.validate(data)
    if errors:
        raise SystemExit('\n'.join(errors))
    content = chain.render(data)
    if chain.OUTPUT.read_text() != content:
        chain.OUTPUT.write_text(content)
    delta = chain.changes(data)
    print(f"rendered; {len(delta['modified_sources'])} sources pending, {len(delta['missing_sources'])} missing, "
          f"{len(delta['new_pages'])} new pages, {len(delta['removed_pages'])} removed")


if __name__ == '__main__':
    main()
