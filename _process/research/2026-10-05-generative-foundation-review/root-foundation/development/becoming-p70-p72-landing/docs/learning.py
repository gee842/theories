"""Text that depends on whether P73's Becoming.Learning landed before P70–P72.

apply_docs.py and make_records.py read FIRST when the receipt's Becoming.Description declares
lasso_iff_sameAhead (learning_patch.py was applied), and SECOND otherwise.
"""

FIRST = {
    # Study, P70's integration line.
    '{LASSO_INTEGRATION}': '，即 P73 的 Lasso（`lasso_iff_sameAhead`、`finitely_many_states_iff_lasso`）；'
                           '`Law.goAlike_process_iff` 是 P73 的 `goAlike_iff_lumped` 的实例（两者各自写成，P73 先落地）',
    '{LASSO_STUDY_ZH}': ('\n8. **与 P73 的关系。** P73 先落地，所以由本节写出同一：`Law.goAlike_process_iff` 与 `Becoming.Learning` 的 '
                         '`goAlike_iff_lumped` 是同一定律，各自写成、证明相同，这里取为它的实例（名称与陈述不变）；P73 的 Lasso 就是两个时刻是同一状态'
                         '（`lasso_iff_sameAhead`），所以状态有限就是 Lasso（`finitely_many_states_iff_lasso`）。本模块因此导入 `Becoming.Learning`，'
                         '在 L4。'),
    '{LASSO_STUDY_EN}': (" P73 landed first, so this section states the identities: `Law.goAlike_process_iff` is the instance of "
                         "`Becoming.Learning`'s identical `goAlike_iff_lumped`, written independently, and finitely many states is P73's "
                         "lasso (`lasso_iff_sameAhead`, `finitely_many_states_iff_lasso`)."),
    '{LASSO_ROW_ZH}': '；状态有限就是 P73 的 Lasso（`finitely_many_states_iff_lasso`）',
    '{LASSO_ROW_EN}': "; finitely many states is P73's lasso (`finitely_many_states_iff_lasso`)",
    '{LAYER}': 'L4',
    '{IMPORTS_ZH}': '导入 Unfolding（P69）、Diagonal、Context 与 Learning（P73）',
    '{IMPORTS_EN}': 'importing Unfolding (P69), Diagonal, Context and Learning (P73)',
    '{FURTHER_LASSO_ZH}': '',
    '{FURTHER_LASSO_EN}': '',
    '{LEARNING_IMPORT_ZH}': '，以及 `Becoming.Learning`（P73）',
    '{LEARNING_IMPORT_EN}': ' and `Becoming.Learning` (P73)',
    '{SPINE_AFTER}': '| L4 | [Becoming.Learning]',
}

SECOND = {
    '{LASSO_INTEGRATION}': '；与 P73 的 Lasso 的实例定理（`Learning.Lasso o i q` 即 `SameAhead o i (i + (q + 1))`）由 P73 写出，'
                           '它的 `goAlike_iff_lumped` 与本节的 `Law.goAlike_process_iff` 是同一定律，各自写成',
    '{LASSO_STUDY_ZH}': ('\n8. **与 P73 的关系。** P73（`Becoming.Learning`）的 `goAlike_iff_lumped` 与本节的 `Law.goAlike_process_iff` 是同一定律，'
                         '各自写成、证明相同；P73 的 Lasso 就是两个时刻是同一状态。按两个所有者的约定，后落地者写出同一与实例定理，不重证。'),
    '{LASSO_STUDY_EN}': (" P73's `goAlike_iff_lumped` (`Becoming.Learning`) is the same law as `Law.goAlike_process_iff`, written "
                         "independently, and P73's lasso is two moments being one state; by the owners' agreement whichever lands "
                         "second states the identities and proves nothing again."),
    '{LASSO_ROW_ZH}': '',
    '{LASSO_ROW_EN}': '',
    '{LAYER}': 'L3',
    '{IMPORTS_ZH}': '导入 Unfolding（P69）、Diagonal 与 Context',
    '{IMPORTS_EN}': 'importing Unfolding (P69), Diagonal and Context',
    '{FURTHER_LASSO_ZH}': '与 P73 的 `Lasso` 的实例定理（状态有限即某个 `SameAhead o i (i + (q + 1))`，由后落地者写出）；',
    '{FURTHER_LASSO_EN}': "the instance theorem to P73's `Lasso` (finitely many states as some `SameAhead o i (i + (q + 1))`, by whichever lands second); ",
    '{LEARNING_IMPORT_ZH}': '',
    '{LEARNING_IMPORT_EN}': '',
    '{SPINE_AFTER}': '| L3 | [Becoming.Unfolding]',
}
