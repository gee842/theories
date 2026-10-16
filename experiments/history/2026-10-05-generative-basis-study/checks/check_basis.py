"""Exact finite checks for declared quotient and guarded-program constructions.

Standard library only. No imports from the producing formal note or earlier
simulation implementations. Outputs are mathematical witnesses, not data fits.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(name, condition):
    assert condition, name
    CHECKS.append(name)


@dataclass(frozen=True)
class System:
    labels: tuple
    kernels: tuple  # action, source, target
    available: tuple = ()

    @property
    def n(self):
        return len(self.labels)

    def enabled(self, s):
        return self.available[s] if self.available else tuple(True for _ in self.kernels)

    def valid(self):
        assert all(len(k) == self.n for k in self.kernels)
        assert all(len(row) == self.n and sum(row) == 1 and all(p >= 0 for p in row)
                   for kernel in self.kernels for row in kernel)


def canonical(groups):
    return tuple(sorted((tuple(sorted(g)) for g in groups), key=lambda g: g[0]))


def grouped(keys):
    groups = defaultdict(list)
    for s, key in enumerate(keys):
        groups[key].append(s)
    return canonical(groups.values())


def block_sums(system, s, blocks):
    return tuple(tuple(sum(kernel[s][t] for t in block) for block in blocks)
                 if system.enabled(s)[a] else None
                 for a, kernel in enumerate(system.kernels))


def refine(system):
    system.valid()
    blocks = grouped([(system.labels[s], system.enabled(s)) for s in range(system.n)])
    trace = [blocks]
    while True:
        ids = {s: b for b, group in enumerate(blocks) for s in group}
        updated = grouped([(ids[s], block_sums(system, s, blocks)) for s in range(system.n)])
        if updated == blocks:
            return blocks, trace
        blocks = updated
        trace.append(blocks)


def all_partitions(n):
    # Restricted-growth strings; independent of iterative refinement.
    def rec(seq, largest):
        if len(seq) == n:
            yield canonical([[s for s, b in enumerate(seq) if b == j] for j in range(largest+1)])
        else:
            for b in range(largest+2):
                yield from rec(seq+[b], max(largest, b))
    yield from rec([0], 0)


def stable(system, blocks):
    for block in blocks:
        s = block[0]
        for t in block[1:]:
            if system.labels[s] != system.labels[t] or system.enabled(s) != system.enabled(t):
                return False
            for a, kernel in enumerate(system.kernels):
                if system.enabled(s)[a]:
                    for target in blocks:
                        if sum(kernel[s][u] for u in target) != sum(kernel[t][u] for u in target):
                            return False
    return True


def finer(left, right):
    return all(any(set(a) <= set(b) for b in right) for a in left)


def exhaustive_check(name, system):
    blocks, trace = refine(system)
    candidates = [p for p in all_partitions(system.n) if stable(system, p)]
    check(name+' stable output', stable(system, blocks))
    check(name+' coarser than every exact partition', all(finer(p, blocks) for p in candidates))
    check(name+' unique least-block stable answer', [p for p in candidates if len(p) == min(map(len, candidates))] == [blocks])
    return {'states': system.n, 'actions': len(system.kernels), 'blocks': blocks,
            'refinement_rounds': len(trace)-1, 'stable_partitions_examined': len(candidates),
            'all_partitions_examined': sum(1 for _ in all_partitions(system.n))}


def deterministic(targets):
    return tuple(tuple(F(int(j == t)) for j in range(len(targets))) for t in targets)


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(a))) for i in range(len(a)))


def quotient(kernel, blocks):
    return tuple(tuple(sum(kernel[block[0]][t] for t in target) for target in blocks) for block in blocks)


def mixed(a, b, weight):
    return tuple(tuple(weight*x+(1-weight)*y for x, y in zip(ar, br)) for ar, br in zip(a,b))


# Executable language: halt, write one bit, sequence, single-bit guard,
# and a rational coin writing one scratch bit. Old and next state banks differ.
def writes(code, width):
    return ('seq', tuple(('write', width+i, (code >> i) & 1) for i in range(width)))


def sample_program(row, width):
    choices = [(j, p) for j, p in enumerate(row) if p]
    target, probability = choices[0]
    if len(choices) == 1:
        return writes(target, width)
    remainder = list(row)
    remainder[target] = F(0)
    remainder = tuple(p/(1-probability) for p in remainder)
    return ('seq', (('coinwrite', 2*width, probability),
                    ('ifbit', 2*width, 1, writes(target,width), sample_program(remainder,width))))


def compile_kernel(kernel):
    n = len(kernel)
    width = max(1, (n-1).bit_length())
    program = writes(0,width)  # fixed output on unused binary source codes
    for s in reversed(range(n)):
        bits = tuple((s >> i) & 1 for i in range(width))
        success = sample_program(kernel[s], width)
        for i in reversed(range(width)):
            success = ('ifbit', i, bits[i], success, program)
        program = success
    return width, program


def execute(program, memory):
    op = program[0]
    if op == 'halt':
        return {memory: F(1)}
    if op == 'write':
        out = list(memory); out[program[1]] = program[2]
        return {tuple(out): F(1)}
    if op == 'ifbit':
        return execute(program[3] if memory[program[1]] == program[2] else program[4], memory)
    if op == 'coinwrite':
        dist = defaultdict(F)
        for value, probability in [(1,program[2]), (0,1-program[2])]:
            out = list(memory); out[program[1]] = value
            dist[tuple(out)] += probability
        return dict(dist)
    if op == 'seq':
        dist = {memory: F(1)}
        for instruction in program[1]:
            updated = defaultdict(F)
            for state, mass in dist.items():
                for out, conditional in execute(instruction, state).items():
                    updated[out] += mass*conditional
            dist = dict(updated)
        return dist
    raise AssertionError(op)


def compiler_check(name, kernel):
    width, program = compile_kernel(kernel)
    for s, row in enumerate(kernel):
        old_bits = tuple((s >> i) & 1 for i in range(width))
        memory = old_bits + (0,)*(width+1)
        dist = execute(program, memory)
        observed = defaultdict(F)
        for bits,p in dist.items():
            observed[sum(bit << i for i,bit in enumerate(bits[width:2*width]))] += p
            assert bits[:width] == old_bits
        check(name+f' compiled row {s}', all(observed.get(t, F(0)) == p for t,p in enumerate(row)) and
              all(t < len(kernel) for t in observed) and sum(observed.values()) == 1)
    return {'width': width, 'rows': len(kernel)}


def main():
    rng = random.Random(20261005)
    systems = {}
    random_results = []
    for case in range(36):
        n = 2+case%5
        kernels = []
        for action in range(1+case%3):
            rows = []
            for s in range(n):
                weights = [rng.randrange(5) for _ in range(n)]
                if not any(weights):
                    weights[s] = 1
                rows.append(tuple(F(w, sum(weights)) for w in weights))
            kernels.append(tuple(rows))
        system = System(tuple(s%2 for s in range(n)), tuple(kernels))
        systems[f'rational_{case}'] = system
        random_results.append(exhaustive_check(f'rational {case}', system))

    # Internal transitions differ, but all protected block sums coincide.
    paired = System((0,0,1,1), (
        ((F(1,3),F(1,3),F(1,3),F(0)), (F(2,3),F(0),F(0),F(1,3)),
         (F(1,4),F(0),F(3,4),F(0)), (F(0),F(1,4),F(0),F(3,4))),
        ((F(1,2),F(0),F(0),F(1,2)), (F(0),F(1,2),F(1,2),F(0)),
         (F(0),F(1,5),F(4,5),F(0)), (F(1,5),F(0),F(0),F(4,5)))
    ))
    systems['paired'] = paired
    paired_result = exhaustive_check('paired', paired)
    check('paired coarsest partition', refine(paired)[0] == ((0,1),(2,3)))

    # Immediate output and one-step output agree at states0,1; two-step output differs.
    delayed = System((0,0,0,0,1), (deterministic((2,3,4,3,4)),))
    systems['delayed'] = delayed
    delayed_blocks, delayed_trace = refine(delayed)
    check('one-step cannot separate delayed pair', any(0 in b and 1 in b for b in delayed_trace[1]))
    check('later refinement separates delayed pair', not any(0 in b and 1 in b for b in delayed_blocks))
    delayed_result = exhaustive_check('delayed', delayed)

    # Probe distinguishes two currently equal states while their old wait law did not.
    base = System((0,0,1), (deterministic((0,1,2)),))
    expanded = System(base.labels, base.kernels+(deterministic((2,1,2)),))
    systems['old_interface'] = base; systems['new_interface'] = expanded
    old_blocks = refine(base)[0]; new_blocks = refine(expanded)[0]
    check('expanded intervention interface strictly refines', finer(new_blocks, old_blocks) and len(new_blocks)>len(old_blocks))

    # Identical physical behavior, different publicly revealed individual burden/refusal label.
    normative = System(((0,'can-refuse'),(0,'cannot-refuse'),(1,'can-refuse')), base.kernels)
    systems['expanded_normative_labels'] = normative
    check('new refusal distinction refines without changing dynamics', finer(refine(normative)[0], old_blocks) and len(refine(normative)[0])>len(old_blocks))
    availability = System(base.labels, base.kernels, ((True,),(False,),(True,)))
    systems['availability'] = availability
    check('enabled action interface is preserved', len(refine(availability)[0]) == 3)
    for name in ['old_interface','new_interface','expanded_normative_labels','availability']:
        exhaustive_check(name, systems[name])

    blocks = refine(paired)[0]
    a,b = paired.kernels
    check('composition exact on common quotient', quotient(matmul(a,b), blocks) == matmul(quotient(a,blocks), quotient(b,blocks)))
    check('quotient-measurable constant mixture exact', quotient(mixed(a,b,F(2,7)),blocks) == mixed(quotient(a,blocks),quotient(b,blocks),F(2,7)))
    state_guard = tuple(a[s] if s%2 == 0 else b[s] for s in range(paired.n))
    check('hidden-dependent guard destroys exactness', not stable(System(paired.labels,(state_guard,)),blocks))
    independent = {(a,b):F(1,4) for a,b in product((0,1),repeat=2)}
    shared = {(0,0):F(1,2),(1,1):F(1,2)}
    independent_equal = sum(p for (a,b),p in independent.items() if a == b)
    shared_equal = sum(p for (a,b),p in shared.items() if a == b)
    check('identical fair marginals do not determine joint law', independent_equal != shared_equal)
    check('marginals match under shared and independent noise', all(
        sum(p for state,p in shared.items() if state[i] == value) ==
        sum(p for state,p in independent.items() if state[i] == value)
        for i,value in product((0,1),repeat=2)))

    compilers = {}
    for name, system in systems.items():
        for a,kernel in enumerate(system.kernels):
            compilers[f'{name}/{a}'] = compiler_check(f'{name} action {a}',kernel)
    third = F(1,3)
    check('one third is not dyadic', third.denominator & (third.denominator-1) != 0)
    # A finite prefix illustrates, but does not prove, the unbounded-state theorem.
    counter_pairs = 0
    for n in range(21):
        for m in range(n+1,21):
            check(f'counter witness {n},{m}', max(n-n,0) == 0 and max(m-n,0)>0)
            counter_pairs += 1
    safe = System(('safe',), (((F(1),),),))
    check('fixed safe rule requires no active renewal in this domain', stable(safe,((0,),)) and safe.kernels[0][0][0] == 1)

    # Action-label monotonicity across all generated systems and deterministic labels.
    for name, system in systems.items():
        narrower = System(system.labels, system.kernels[:1], tuple((system.enabled(s)[0],) for s in range(system.n)))
        check(name+' action monotonicity', finer(refine(system)[0],refine(narrower)[0]))
        more_labels = System(tuple((system.labels[s],s%3) for s in range(system.n)),system.kernels,system.available)
        check(name+' observable monotonicity', finer(refine(more_labels)[0],refine(system)[0]))

    results = {
        'status': 'exact rational constructed mathematical checks, not empirical evidence',
        'checkplan_sha256': hashlib.sha256((ROOT/'CHECKPLAN.md').read_bytes()).hexdigest(),
        'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks_passed': len(CHECKS), 'checks': CHECKS,
        'supplementary_system_count': len(random_results), 'random_seed': 20261005,
        'supplementary_partition_results': random_results, 'paired': paired_result,
        'delayed': delayed_result, 'delayed_trace': delayed_trace,
        'old_interface_partition': old_blocks, 'expanded_interface_partition': new_blocks,
        'normative_partition': refine(normative)[0], 'compiler_results': compilers,
        'counter_prefix_pair_witnesses': counter_pairs,
        'joint_noise_witness': {'independent_probability_equal': str(independent_equal),'shared_probability_equal':str(shared_equal)},
        'limitations': ['Compiler is a representation result using supplied kernel coefficients.',
                        'Atomic macrostep compilation does not preserve intermediate timing, work cost or observability.',
                        'A finite generating program can have infinitely many causal states.',
                        'Refinement need not give agents access to the distinctions it retains.',
                        'Exact partition minimality is not minimality among all latent stochastic models.']
    }
    (ROOT/'checks/results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:results[k] for k in ['checks_passed','supplementary_system_count','paired','delayed','old_interface_partition','expanded_interface_partition','normative_partition','counter_prefix_pair_witnesses']}))


if __name__ == '__main__':
    main()
