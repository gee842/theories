#!/usr/bin/env python3
"""P127: write docs.json, the texts apply_docs.py places.

usage: python3 -B make_docs_json.py

Kept as data so the texts can be read and reviewed in one place: the root module's bullet, the
checker's scope entry, the Lean README's row, the chapter's §2 clause and paragraph pair, the item
of "Part I stated whole", the §8 status clause and further-proof text, the §9 row and the glossary
rows.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
RECORD = '../results/records/where-a-run-goes-on.md'

docs = {
    'bullet': (
        '* `Becoming.Onward` (L4): where a run goes on, with no premise beyond what each law names. Within\n'
        '  finitely many configurations a run is a course into a return: a run starts at a configuration\n'
        '  exactly where a course as long as the list of configurations does, exactly where courses of\n'
        '  every length do and exactly where a course leads to a configuration that returns, with no\n'
        '  decision and no selection; a run starts at each member of a family that keeps moving and stays\n'
        '  in it, and the laws along runs of `Becoming.Branching` (returning and no rise where nothing\n'
        '  merges, needing openness) hold for every such configuration with no run given. Where a test\n'
        '  recognizes, among enumerated moves, a step staying in the family, a run is built by search,\n'
        '  with no selection. Asked of every process, a run from every member of every family that keeps\n'
        '  moving is exactly dependent choice (`DependentSelection`).'),
    'scope': (
        '    "Onward: within finitely many configurations a run starts at a configuration exactly where a "\n'
        '    "course as long as the list does, exactly where courses of every length do and exactly where "\n'
        '    "a course leads to a return, with no decision and no selection, and whether one starts is "\n'
        '    "decided where the successors are listed; a run starts at each member of a family that keeps "\n'
        '    "moving and stays in it; merging nothing, a configuration returns exactly where a course as "\n'
        '    "long as the list starts there, nothing rises within a family that keeps moving, and a "\n'
        '    "configuration with courses of every length that never returns needs openness; a test "\n'
        '    "recognizing among enumerated moves a step that stays in the family gives a run by search; "\n'
        '    "asked of every process, a run from every member of every family that keeps moving is exactly "\n'
        '    "dependent choice. "\n'),
    'readme_row': (
        '| L4 | [`Becoming.Onward`](Becoming/Onward.lean) | 运行在何处延续（除了各定理所写者不加前提）：从运行的每个配置开始每个长度的'
        '路径，运行的每个配置可从其起点得到（`continues_of_run`、`unbounded_of_run`、`reach_of_run`）；从路径通向之处的运行前接路径，'
        '即得运行（`run_of_trace`、`run_of_reach`），从路径通向返回者之处运行绕返回而行（`run_of_returning`）；有限多配置之内，与列表'
        '一样长的路径通向返回者（`reach_along`、`returning_of_continues`），所以运行恰在这样的路径开始处开始、恰在每个长度的路径都开始'
        '处、恰在路径通向返回者处（`run_of_continues`、`run_iff_continues`、`run_iff_unbounded`、`run_iff_returning`），不需判定也不需'
        '选择，后继列出时运行是否开始已定（`run_decided`）；分支无穷时每个长度的路径不给出运行（`fan_no_run`）；保持运动的族'
        '（`KeepsMoving`、`within`、`ofWithin`、`ofWithin_within`、`KeepsMoving.continues`），运行从每个成员开始并留在族中'
        '（`KeepsMoving.run`）；不合并时配置恰在与列表一样长的路径从它开始处返回（`lossless_returns_iff`、`KeepsMoving.returns`），'
        '族中不上升（`lossless_no_rise`、`rise_needs_merge`），每个长度的路径都开始而不返回者需要开放（`lossless_unlisted`）；测试在'
        '枚举的移动中认出留在族中的一步之处，运行经搜索造出（`Later`、`searchFrom`、`acc_below`、`search`、`Finds`、`searchedStep`、'
        '`searchedRun`、`searchedRun_start`、`searchedRun_within`），步与族已定时逐个测试即是（`decidedTest`、`decidedTest_finds`）；对'
        '每个过程要求的运行恰是依赖选择（`DependentSelection`、`moveOf`、`moveOf_eq`、`runs_iff_selection`）；读法是 AI 的，待 Ren / '
        'where a run goes on (no premise beyond what each theorem names): from each configuration of a run courses of every '
        'length start, and each is had from its start (`continues_of_run`, `unbounded_of_run`, `reach_of_run`); a run from '
        'where a course leads, preceded by the course, is a run (`run_of_trace`, `run_of_reach`), and from where a course '
        'leads to a return a run goes round the return (`run_of_returning`); within finitely many configurations a course '
        'as long as the list leads to a return (`reach_along`, `returning_of_continues`), so a run starts exactly where such '
        'a course does, exactly where courses of every length do and exactly where a course leads to a return '
        '(`run_of_continues`, `run_iff_continues`, `run_iff_unbounded`, `run_iff_returning`), with no decision and no '
        'selection, and whether one starts is decided where the successors are listed (`run_decided`); where branching is '
        'infinite courses of every length give no run (`fan_no_run`); a family that keeps moving (`KeepsMoving`, `within`, '
        '`ofWithin`, `ofWithin_within`, `KeepsMoving.continues`) has a run from each member staying in it '
        '(`KeepsMoving.run`); merging nothing, a configuration returns exactly where a course as long as the list starts '
        'there (`lossless_returns_iff`, `KeepsMoving.returns`), nothing rises within the family (`lossless_no_rise`, '
        '`rise_needs_merge`), and one with courses of every length that never returns needs openness (`lossless_unlisted`); '
        'where a test recognizes among enumerated moves a step staying in the family, a run is built by search (`Later`, '
        '`searchFrom`, `acc_below`, `search`, `Finds`, `searchedStep`, `searchedRun`, `searchedRun_start`, '
        '`searchedRun_within`), testing each move being one where steps and the family are decided (`decidedTest`, '
        '`decidedTest_finds`); asked of every process, the run is exactly dependent choice (`DependentSelection`, '
        '`moveOf`, `moveOf_eq`, `runs_iff_selection`); the readings are the AI\'s, pending Ren |'),
    'branch_zh': (
        '沿运行的定律对每个能继续运动的配置成立，不给定运行：有限多配置之内，运行恰是通向返回的路径，不需判定也不需选择；对每个过程'
        '要求它，恰是依赖选择（`Becoming.Onward`）。'),
    'branch_en': (
        'The laws along runs hold for every configuration that can keep moving, with no run given: within finitely many '
        'configurations a run is a course into a return, with no decision and no selection, and asked of every process it '
        'is exactly dependent choice (`Becoming.Onward`). '),
    'paragraph_zh': (
        '**运行在何处延续（第一部分）。** `Becoming.Branching` 沿运行的定律以运行为给定；从能动的配置造出运行要在每步取一个延续，'
        f'每步都取是核心不假定的选取。这里陈述运行在何处不经选取而延续，除了各定理所写者不加前提（[Becoming.Onward]({LEAN}Onward.lean)）。'
        '有限多配置之内，与列表一样长的路径重复一个配置，被重复者返回；从路径通向返回者之处，运行绕返回而行，前接那段路径。所以运行恰'
        '在与列表一样长的路径开始之处开始，恰在每个长度的路径都开始之处，恰在路径通向返回者之处（`run_iff_continues`、'
        '`run_iff_unbounded`、`run_iff_returning`），不需判定也不需选择；后继列出时，运行是否开始已定（`run_decided`）。分支无穷时，'
        '每个长度的路径不给出运行（`fan_no_run`）。一族保持运动，指从每个成员有一步通向成员（`KeepsMoving`）；有限多配置之内，运行从'
        '每个成员开始并留在族中（`KeepsMoving.run`）。所以沿运行的定律对每个这样的配置成立，不给定运行：不合并时，配置恰在与列表一样'
        '长的路径从它开始处返回（`lossless_returns_iff`），族中没有上升，上升需要合并（`lossless_no_rise`、`rise_needs_merge`），每个'
        '长度的路径都开始而不返回者需要开放（`lossless_unlisted`）。配置不受界时，若一个测试在枚举的移动中认出留在族中的一步（有这样'
        '的一步时它总认出一个），运行经搜索造出，作为数据，不经选取（`Finds`、`search`、`searchedRun`）；步与族已定、步的移动被枚举时，'
        '逐个测试就是这样的测试（`decidedTest_finds`）。对每个过程要求从每个保持运动的族的每个成员出发的运行，恰是依赖选择'
        '（`runs_iff_selection`、`DependentSelection`）。读法（AI 的，待 Ren）：有限多配置之内，无尽地进行者靠回转而进行，路径本身显出'
        '它在何处返回，不需选取，延续从展开读出；配置不受界时，无尽的进行在能搜索移动处给出，对每个过程要求每个能继续'
        '运动的配置都开始一个运行，恰是依赖选择。不推出：核心是否给出依赖选择；有限分支而不搜索时沿无界配置的运行（`Becoming.Lasting` 经 '
        f'`EitherThroughout` 与选取给出）；不列出配置时沿运行的定律。见 [where-a-run-goes-on]({RECORD})。'),
    'paragraph_en': (
        '**Where a run goes on (Part I).** The laws along runs of `Becoming.Branching` take the run as given; building a '
        'run from a configuration that can move takes a continuation at every step, and taking one at every step is a '
        'selection the core does not assume. This states where a run goes on with nothing selected, with no premise '
        f'beyond what each theorem names ([Becoming.Onward]({LEAN}Onward.lean)). Within finitely many configurations, a '
        'course as long as the list repeats a configuration, and the repeated configuration returns; from where a course '
        'leads to a return, a run goes round the return, preceded by the course. So a run starts exactly where a course as '
        'long as the list does, exactly where courses of every length do and exactly where a course leads to a return '
        '(`run_iff_continues`, `run_iff_unbounded`, `run_iff_returning`), with no decision and no selection; where the '
        'successors are listed, whether a run starts is decided (`run_decided`). Where branching is infinite, courses of '
        'every length give no run (`fan_no_run`). A family keeps moving where from each member some step leads to a member '
        '(`KeepsMoving`); within finitely many configurations a run starts at each member and stays in the family '
        '(`KeepsMoving.run`). So the laws along runs hold for every such configuration, with no run given: merging '
        'nothing, a configuration returns exactly where a course as long as the list starts from it '
        '(`lossless_returns_iff`), nothing rises within the family and a rise needs a merge (`lossless_no_rise`, '
        '`rise_needs_merge`), and a configuration with courses of every length that never returns needs openness '
        '(`lossless_unlisted`). Where the configurations are not bounded, a test that recognizes among enumerated moves a '
        'step staying in the family (one wherever there is such a step) gives a run built by search, as data, with no '
        'selection (`Finds`, `search`, `searchedRun`); where the steps and the family are decided and the steps\' moves are '
        'enumerated, testing each move is such a test (`decidedTest_finds`). A run from every member of every family that '
        'keeps moving, asked of every process, is exactly dependent choice (`runs_iff_selection`, `DependentSelection`). '
        'Readings (the AI\'s, pending Ren): within finitely many configurations, whatever goes on without end does so by '
        'coming round; the course itself shows where it returns, nothing is selected, and going on is read off the '
        'unfolding; where the configurations are not bounded, going on without end is given where the moves can be '
        'searched, and asked of every process, that every configuration that can keep moving starts a run is exactly '
        'dependent choice. Not derived: whether the core gives dependent choice; runs along unbounded configurations where '
        'the branching is finite and nothing is searched (given in `Becoming.Lasting` through `EitherThroughout` and a '
        f'selection); the laws along runs where nothing lists the configurations. See [where-a-run-goes-on]({RECORD}).'),
    'whole_zh': (
        '- 有限多配置之内，运行恰是通向返回的路径：运行恰在与列表一样长的路径开始处开始，不需判定也不需选择，保持运动的族的每个成员'
        '都有留在族中的运行，沿运行的定律对每个这样的配置成立；测试认出移动处运行经搜索造出；对每个过程要求运行恰是依赖选择'
        '（`run_iff_returning`、`KeepsMoving.run`、`lossless_returns_iff`、`searchedRun`、`runs_iff_selection`）。'),
    'whole_en': (
        '- Within finitely many configurations a run is a course into a return: a run starts exactly where a course as '
        'long as the list does, with no decision and no selection, each member of a family that keeps moving has a run '
        'staying in it, and the laws along runs hold for every such configuration; where a test recognizes the moves a run '
        'is built by search; asked of every process, a run is exactly dependent choice (`run_iff_returning`, '
        '`KeepsMoving.run`, `lossless_returns_iff`, `searchedRun`, `runs_iff_selection`).'),
    'status_zh': (
        '；运行在何处延续：有限多配置之内运行恰是通向返回的路径，不需判定也不需选择，沿运行的定律对每个能继续运动的配置成立，对每个'
        f'过程要求运行恰是依赖选择（[where-a-run-goes-on]({RECORD})）'),
    'further_zh': (
        '从每个能动的配置出发的运行已给出（`Becoming.Onward`：有限多配置之内运行恰是通向返回的路径，不需判定也不需选择；测试认出移动'
        '处经搜索造出；对每个过程要求它恰是依赖选择）；'),
    'further_en': (
        'a run from every configuration that can move is given (`Becoming.Onward`: within finitely many configurations a '
        'run is a course into a return, with no decision and no selection; where a test recognizes the moves it is built by '
        'search; asked of every process it is exactly dependent choice); '),
    'chapter_row': (
        f'| L4 | [Becoming.Onward]({LEAN}Onward.lean) | 运行在何处延续（除了各定理所写者不加前提）：有限多配置之内，运行恰在与列表'
        '一样长的路径开始处开始，恰在每个长度的路径都开始处，恰在路径通向返回者处，不需判定也不需选择；保持运动的族的每个成员都有留在'
        '族中的运行，沿运行的定律对每个这样的配置成立，不给定运行；测试在枚举的移动中认出留在族中的一步处，运行经搜索造出；对每个过程'
        '要求运行恰是依赖选择。/ Where a run goes on, with no premise beyond what each theorem names: within finitely many '
        'configurations a run starts exactly where a course as long as the list does, exactly where courses of every length '
        'do and exactly where a course leads to a return, with no decision and no selection; each member of a family that '
        'keeps moving has a run staying in it, and the laws along runs hold for every such configuration with no run given; '
        'where a test recognizes among enumerated moves a step staying in the family, a run is built by search; asked of '
        'every process, a run is exactly dependent choice. | 28 |'),
    'glossary': [
        '| 保持运动（族） | keeps moving (a family) | 从每个成员有一步通向成员；有限多配置之内运行从每个成员开始并留在族中，不需判定也不需'
        '选择 | `KeepsMoving`、`KeepsMoving.run` |',
        '| 依赖选择 | dependent choice | 全的关系从每个起点有沿它的序列；对每个过程要求从每个保持运动的族的每个成员出发的运行，恰是它 | '
        '`DependentSelection`、`runs_iff_selection` |'],
}

(HERE / 'docs.json').write_text(json.dumps(docs, ensure_ascii=False, indent=1) + '\n')
print('wrote docs.json')
