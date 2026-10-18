#!/usr/bin/env python3
"""A4 (19 October 2026): the work board's register after Ren's answer to Parts C and D, "integrate all, the theory is
a whole, not stitched pieces, go ahead". The section "Decisions pending Ren" loses the D-f row and the Part D list,
which D45 decides, and says what stays Ren's. The section's body must match exactly; if it was already edited, nothing
is done. Run it over the board as it then stands, after rereading the board (rule 4).
usage (from the repository root): python3 -B apply_board.py"""
import sys

BOARD = '_process/BECOMING-WORKBOARD.md'
RF = 'research/2026-10-05-generative-foundation-review/root-foundation/'
SRC = '../sources/15-codex-theory-conversations/'
CHANGES = 'research/2026-10-05-repository-reconciliation/whole-repo-review-2026-10-16/CHANGES.md'
D43 = RF + 'DELEGATED-CHOICES.md#d43-其余的待决读法--the-other-pending-readings'
D45 = RF + 'DELEGATED-CHOICES.md#d45-一个说明中的读法--the-readings-in-one-account'
MARK = 'None since 19 October 2026.'

OLD_BODY = (
    "Since 18 October an AI reading waits here only where it reads Ren's own terms or his voice; the other entries are "
    "decisions, not readings. Every other AI reading keeps its AI label and the work decides it, as with G1's and G2's "
    "([AGENTS.md](../AGENTS.md#scope-and-current-status), [Ren](" + SRC + "2026-10-18-constraints-fix-all.md)). Ren "
    "took the central readings and the brief's Part B on 18 October ([source](" + SRC + "2026-10-18-central-readings-"
    "taken.md)); A1 removed those rows when it landed: D1, D5, D22 and D39 are revised, and the rest are decided as D43 "
    "in [DELEGATED-CHOICES](" + D43 + "). None is a premise. The overall register will be generated (review item B5); "
    "until then this list is the register, built from the old board, [CHANGES.md B5 and B7](" + CHANGES + ") and "
    "chapter §8.\n\n"
    "| Item | Where |\n"
    "|---|---|\n"
    "| D-f (the brief's Part C): whether Ren's 16 October \"agree with other readings\" ratifies the readings of D1-D39 "
    "that Ren has not taken by name (R18 D-f). The brief recommends no blanket ratification: a reading of one of Ren's "
    "phrases waits on his word on that phrase, and a reading of a theorem is decided by argument | [brief, Part C]("
    + RF + "READINGS-PENDING-REN.md#c-the-register-itself-d-f-review-item-50); [DELEGATED-CHOICES.md](" + RF +
    "DELEGATED-CHOICES.md) |\n\n"
    "Also with Ren, from the old board (not readings; the brief's [Part D](" + RF +
    "READINGS-PENDING-REN.md#d-waiting-on-ren-not-readings)): IdealWarrant, join as a candidate under a structural name "
    "(rule 8); the Chinese term, the informal rest heading and the OPENING footnote; the integrator and W-root ownership "
    "questions (CHANGES.md B7); whether R18, an AI read-only review, counts as the review asked for (B6).")

NEW_BODY = (
    "None since 19 October 2026. Ren answered the register as a whole: \"integrate all, the theory is a whole, not "
    "stitched pieces, go ahead\" ([source](" + SRC + "2026-10-19-integrate-all.md)). Every reading is decided by its "
    "place in one account, and the brief's Part D within it: decision [D45](" + D45 + "), board item A4. No reading "
    "waits here any longer, readings of Ren's own terms included; each keeps its AI label, and the work decides it. "
    "D45 item (4) decides Part D: the rest family's Chinese term (停息, with the heading 停息定理; OPENING unchanged); "
    "`IdealWarrant`, joined with `CompletionRole` and `HistoryIdeals` under structural names (sub-item A4-L); the "
    "integrator (rule 3's fallback stands, no session named); W-root (its claim lapsed under rule 4, its target open in "
    "chapter §8.1); and R18 (it counts as the review asked for, stated as an AI review, read-only, that built no Lean).\n\n"
    "What stays Ren's is his own text and his authorizations, not readings. OPENING's body and the generativity chain "
    "change only through proposals to him (A3 holds the chain's relabelling proposal); goal scopes change only with his "
    "approval ([AGENTS.md](../AGENTS.md)); and the licence is his choice before any public release (review item F8).\n\n"
    "Earlier, Ren took the central readings and the brief's Part B on 18 October ([source](" + SRC + "2026-10-18-"
    "central-readings-taken.md)); A1 removed those rows when it landed: D1, D5, D22 and D39 are revised, and the rest "
    "are decided as D43 in [DELEGATED-CHOICES](" + D43 + "). A4 removed the row for D-f (the brief's Part C) and the "
    "list of Part D when D45 landed. None is a premise. The overall register will be generated (review item B5); until "
    "then this section is the register, built from the old board, [CHANGES.md B5 and B7](" + CHANGES + ") and chapter "
    "§8.")


def main():
    text = open(BOARD, encoding='utf-8').read()
    if MARK in text:
        print('already edited', BOARD)
        return
    n = text.count(OLD_BODY)
    if n != 1:
        sys.exit(f'{BOARD}: expected one match of the register, found {n}')
    text = text.replace(OLD_BODY, NEW_BODY)
    open(BOARD, 'w', encoding='utf-8').write(text)
    print('edited', BOARD)


if __name__ == '__main__':
    main()
