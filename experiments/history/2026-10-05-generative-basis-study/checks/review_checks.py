"""Small independent audit of partition coverage and macrostep scope.

The producer is imported only to inspect its enumerated partitions; the
reference constructs partitions from all functions into an n-element set,
not its restricted-growth recursion. No producer result files are written.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
producer_path = HERE / 'check_basis.py'
spec = importlib.util.spec_from_file_location('reviewed_basis', producer_path)
producer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = producer
spec.loader.exec_module(producer)


def reference_partitions(n):
    found = set()
    for labels in product(range(n), repeat=n):
        groups = {}
        for state, label in enumerate(labels):
            groups.setdefault(label, set()).add(state)
        found.add(frozenset(frozenset(block) for block in groups.values()))
    return found


partition_results = []
for n, bell_number in enumerate((1, 1, 2, 5, 15, 52, 203)):
    if not n:
        continue
    actual_list = list(producer.all_partitions(n))
    actual = {frozenset(frozenset(b) for b in p) for p in actual_list}
    expected = reference_partitions(n)
    assert len(actual_list) == len(actual) == bell_number
    assert actual == expected
    partition_results.append({'states': n, 'all_functions_enumerated': n**n,
                              'distinct_partitions': len(actual)})

# Independent probability enumeration: coincident vs opposite shared bits.
coincident = {(z, z): Fraction(1, 2) for z in (0, 1)}
opposite = {(z, 1-z): Fraction(1, 2) for z in (0, 1)}
for coordinate, value in product((0, 1), repeat=2):
    assert sum(p for s,p in coincident.items() if s[coordinate] == value) == Fraction(1,2)
    assert sum(p for s,p in opposite.items() if s[coordinate] == value) == Fraction(1,2)
equal_coincident = sum(p for s,p in coincident.items() if s[0] == s[1])
equal_opposite = sum(p for s,p in opposite.items() if s[0] == s[1])
assert equal_coincident == 1 and equal_opposite == 0

# A later old-bank transfer of finished next-state code 1 from old state 2
# traverses code 3 when done low bit first. The producer does not expose this
# transfer as part of its output kernel. It illustrates the formal note's
# explicit atomicity boundary, not a claim that its current output writes
# corrupt the preserved old bank.
memory = [0, 1]
trace = [sum(bit << i for i,bit in enumerate(memory))]
for i, bit in enumerate((1, 0)):
    memory[i] = bit
    trace.append(sum(v << j for j,v in enumerate(memory)))
assert trace == [2, 3, 1]
assert trace[-1] == 1 and any(code >= 3 for code in trace[1:-1])


def mechanism_step(state, inputs, noise, badge_mode=False):
    # Direct old-state equation transcription, independent of any network checker.
    c, y, r, k, a, v, m, b, p, j = state
    do_execute, probe, train, propose_veto = inputs
    shock, badge_shock = noise
    authority = bool(p and (a or m) and not v)
    if badge_mode:
        authority = authority and j
    return tuple(map(int, (
        c ^ shock,
        r if a and not v and k and do_execute else y,
        c ^ shock if k and probe else r,
        1 if m and train else k and not shock,
        authority,
        p and propose_veto,
        (b or r) and a and not v,
        (y ^ c) or (m and shock),
        p and (k or not b),
        j ^ badge_shock,
    )))


# Pair every two full states merged by the proposed badge-dropping projection,
# under every input and every common noise value. This checks pathwise closure
# at one step, stronger than equality of marginal coordinate distributions.
branch_pairs = 0
for retained in product((0,1), repeat=9):
    for inputs in product((0,1), repeat=4):
        for noise in product((0,1), repeat=2):
            assert mechanism_step(retained+(0,), inputs, noise)[:9] == mechanism_step(retained+(1,), inputs, noise)[:9]
            branch_pairs += 1
assert branch_pairs == 32768

noise_law = {(0,0): Fraction(3,8), (0,1): Fraction(3,8),
             (1,0): Fraction(1,8), (1,1): Fraction(1,8)}
maintenance_witness = []
for maintenance in (0,1):
    state = (0,0,0,0,0,0,maintenance,0,1,0)
    burden_probability = sum(mass for noise,mass in noise_law.items()
                             if mechanism_step(state,(0,0,0,0),noise)[7])
    maintenance_witness.append(burden_probability)
assert maintenance_witness == [0, Fraction(1,4)]
badge_inputs = (0,0,0,0)
badge_state = (0,0,0,0,1,0,0,0,1)
badge_outputs = [mechanism_step(badge_state+(j,),badge_inputs,(0,0),True)[4]
                 for j in (0,1)]
assert badge_outputs == [0,1]

# Enumerate complete noise words, independently of the producer's recursive
# propagation and state-merging procedure. Three fresh (E,J) draws have 64
# possible words per initial badge value.
proposals = ((0,0,0,0), (1,0,0,0), (0,0,0,0))
protected_burden = []
word_count = 0
for initial_badge in (0,1):
    probability = Fraction(0)
    normalization = Fraction(0)
    for word in product(tuple(noise_law), repeat=3):
        state = (0,0,1,1,1,0,0,0,1,initial_badge)
        weight = Fraction(1)
        for proposal, noise in zip(proposals, word):
            weight *= noise_law[noise]
            state = mechanism_step(state, proposal, noise, True)
        normalization += weight
        probability += weight * state[7]
        word_count += 1
    assert normalization == 1
    protected_burden.append(probability)
assert protected_burden == [Fraction(3,8), Fraction(13,16)]

# Separate closed-form reconstruction: b3=E1 xor E2 for initial badge zero;
# b3=(not E2) or E3 for initial badge one. All E's have probability 1/4.
shock_probability = Fraction(1,4)
analytic_burden = [2*shock_probability*(1-shock_probability),
                   1-shock_probability+shock_probability**2]
assert protected_burden == analytic_burden

structural_producer = HERE/'structural_check.py'
structural_results_path = HERE/'structural_results.json'
structural_results = json.loads(structural_results_path.read_text())
for relative, recorded_hash in structural_results['source_sha256'].items():
    assert hashlib.sha256((HERE.parent/relative).read_bytes()).hexdigest() == recorded_hash
assert structural_results['expanded_original_burden_witness']['final_burden_probabilities'] == list(map(str,protected_burden))
assert structural_results['projected_kernel_pairs_equal'] == 512*16
assert structural_results['baseline_single_bit_comparisons'] == 10*512*16*4
assert structural_results['expanded_single_bit_comparisons'] == 10*512*16*4

results = {
    'producer_sha256': hashlib.sha256(producer_path.read_bytes()).hexdigest(),
    'formal_sha256': hashlib.sha256((HERE.parent/'formal/FORMAL.md').read_bytes()).hexdigest(),
    'review_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'structural_note_sha256': hashlib.sha256((HERE.parent/'formal/STRUCTURAL-CLOSURE.md').read_bytes()).hexdigest(),
    'structural_producer_sha256': hashlib.sha256(structural_producer.read_bytes()).hexdigest(),
    'structural_results_sha256': hashlib.sha256(structural_results_path.read_bytes()).hexdigest(),
    'partition_results': partition_results,
    'shared_noise_equality_probabilities': [str(equal_coincident),str(equal_opposite)],
    'atomicity_witness_register_codes': trace,
    'structural_common_noise_branch_pairs': branch_pairs,
    'structural_maintenance_burden_probabilities': [str(v) for v in maintenance_witness],
    'structural_badge_next_authority': badge_outputs,
    'three_step_complete_noise_words_examined': word_count,
    'three_step_original_burden_probabilities': list(map(str,protected_burden)),
    'three_step_analytic_probabilities': list(map(str,analytic_burden)),
    'status': 'all bounded independent checks passed; proofs still supply universal claims',
}
(HERE/'review_checks.json').write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps(results))
