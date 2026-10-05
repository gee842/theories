"""Exact finite verification of the consequence-preserving quotient theorem.

Checks supplied deterministic tables, not humans, wisdom, or physical laws.
Uses three independent formulations: direct congruence tests over every
partition, iterative partition refinement, and explicit distinguishing words.
"""

from collections import Counter, deque
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def canonical(labels):
    lookup = {}
    answer = []
    for label in labels:
        if label not in lookup:
            lookup[label] = len(lookup)
        answer.append(lookup[label])
    return tuple(answer)


def all_partitions(n):
    return sorted({canonical(p) for p in product(range(n), repeat=n)})


def refines(fine, coarse):
    return all(fine[x] != fine[y] or coarse[x] == coarse[y]
               for x in range(len(fine)) for y in range(len(fine)))


def direct_faithful(partition, transitions, output):
    # Direct equations: every merged pair has the same output and every
    # action sends it to another merged pair. No refinement procedure here.
    for x in range(len(output)):
        for y in range(x + 1, len(output)):
            if partition[x] == partition[y]:
                if output[x] != output[y]:
                    return False
                for transition in transitions:
                    if partition[transition[x]] != partition[transition[y]]:
                        return False
    return True


def refinement(transitions, output):
    partition = canonical(output)
    strict_steps = 0
    while True:
        new_partition = canonical(tuple(
            (output[x],) + tuple(partition[t[x]] for t in transitions)
            for x in range(len(output))))
        if new_partition == partition:
            return partition, strict_steps
        if not refines(new_partition, partition):
            raise AssertionError("A refinement merged previously split states")
        partition = new_partition
        strict_steps += 1


def distinguishing_word(transitions, output, x, y):
    # An independent finite pair-state graph search. Returns None exactly
    # when the pair has equal outputs along every reachable continuation.
    pending = deque([(x, y, ())])
    visited = {(x, y)}
    while pending:
        u, v, word = pending.popleft()
        if output[u] != output[v]:
            return word
        for action, transition in enumerate(transitions):
            successor = (transition[u], transition[v])
            if successor not in visited:
                visited.add(successor)
                pending.append((*successor, word + (action,)))
    return None


def execute(transitions, start, word):
    state = start
    for action in word:
        state = transitions[action][state]
    return state


def quotient_tables(partition, transitions, output):
    representatives = [partition.index(block)
                       for block in range(max(partition) + 1)]
    abstract_transitions = tuple(
        tuple(partition[t[x]] for x in representatives) for t in transitions)
    abstract_output = tuple(output[x] for x in representatives)
    for state in range(len(output)):
        if abstract_output[partition[state]] != output[state]:
            raise AssertionError("Output transport failed")
        for action, transition in enumerate(transitions):
            if abstract_transitions[action][partition[state]] != partition[transition[state]]:
                raise AssertionError("Dynamics transport failed")
    return abstract_transitions, abstract_output


def transported(transitions, output, permutation):
    n = len(output)
    inverse = [permutation.index(x) for x in range(n)]
    moved_transitions = tuple(tuple(permutation[t[inverse[x]]] for x in range(n))
                              for t in transitions)
    moved_output = tuple(output[inverse[x]] for x in range(n))
    return moved_transitions, moved_output


def main():
    n = 3
    partitions = all_partitions(n)
    if len(partitions) != 5:
        raise AssertionError("Expected all five partitions of a three-state set")
    counts = Counter()
    minimal_sizes = Counter()
    faithful_counts = Counter()
    witness_lengths = Counter()
    refinement_steps = Counter()
    witness_digest = hashlib.sha256()
    finite_system_digest = hashlib.sha256()

    for flat in product(range(n), repeat=2*n):
        transitions = (flat[:n], flat[n:])
        counts['transition_tables'] += 1
        for output in product(range(2), repeat=n):
            counts['systems'] += 1
            finite_system_digest.update(repr((transitions, output)).encode())
            faithful = [p for p in partitions
                        if direct_faithful(p, transitions, output)]
            counts['partition_checks'] += len(partitions)
            expected = [p for p in faithful
                        if all(refines(other, p) for other in faithful)]
            if len(expected) != 1:
                raise AssertionError(("No unique direct coarsest partition",
                                      transitions, output, faithful))
            actual, steps = refinement(transitions, output)
            if actual != expected[0]:
                raise AssertionError(("Refinement mismatch", actual, expected))
            quotient_tables(actual, transitions, output)
            minimal_sizes[max(actual)+1] += 1
            faithful_counts[len(faithful)] += 1
            refinement_steps[steps] += 1

            for p in faithful:
                counts['faithful_partitions'] += 1
                if not refines(p, actual):
                    raise AssertionError("A faithful partition does not factor")
                # Build the factor h independently on each abstract block.
                h = {p[x]: actual[x] for x in range(n)}
                if any(h[p[x]] != actual[x] for x in range(n)):
                    raise AssertionError("Factorization failed")

            for x in range(n):
                for y in range(x+1, n):
                    counts['pair_searches'] += 1
                    word = distinguishing_word(transitions, output, x, y)
                    if (word is None) != (actual[x] == actual[y]):
                        raise AssertionError("Behavioral search disagrees with quotient")
                    if word is not None:
                        counts['distinguished_state_pairs'] += 1
                        witness_lengths[len(word)] += 1
                        ox = output[execute(transitions, x, word)]
                        oy = output[execute(transitions, y, word)]
                        if ox == oy:
                            raise AssertionError("Invalid distinguishing witness")
                        witness_digest.update(repr((transitions, output, x, y, word, ox, oy)).encode())
                    else:
                        counts['equivalent_state_pairs'] += 1

            for permutation in permutations(range(n)):
                moved_transitions, moved_output = transported(transitions, output, permutation)
                moved, _ = refinement(moved_transitions, moved_output)
                for x in range(n):
                    for y in range(n):
                        if (actual[x] == actual[y]) != (moved[permutation[x]] == moved[permutation[y]]):
                            raise AssertionError("Coordinate covariance failed")
                counts['coordinate_transports'] += 1

    # Presently identical visible bits conceal future response differences.
    states = tuple(product(range(2), repeat=2))
    output = tuple(v for v, hidden in states)
    reveal = tuple(states.index((hidden, hidden)) for v, hidden in states)
    identity = tuple(range(4))
    coarse_before, _ = refinement((identity,), output)
    repaired, _ = refinement((identity, reveal), output)
    hidden_word = distinguishing_word((identity, reveal), output, 0, 1)
    if max(coarse_before)+1 != 2 or max(repaired)+1 != 4:
        raise AssertionError("Hidden-state repair did not have expected size")
    if direct_faithful(coarse_before, (identity, reveal), output):
        raise AssertionError("Coarse visible-state model should fail under revealing action")

    # A separately targeted deeper system exercises repeated refinement and
    # a distinction that appears only after three actions. This is one
    # five-state witness, not enumeration of all five-state systems.
    chain_output = (0, 0, 0, 0, 1)
    chain_step = (1, 2, 3, 4, 4)
    chain_wait = tuple(range(5))
    chain_transitions = (chain_step, chain_wait)
    chain_partitions = all_partitions(5)
    if len(chain_partitions) != 52:
        raise AssertionError("Expected all 52 partitions of a five-state set")
    chain_faithful = [p for p in chain_partitions
                      if direct_faithful(p, chain_transitions, chain_output)]
    chain_direct_coarsest = [p for p in chain_faithful
                            if all(refines(other, p) for other in chain_faithful)]
    chain_actual, chain_strict_steps = refinement(chain_transitions, chain_output)
    if chain_actual != tuple(range(5)) or chain_strict_steps != 3:
        raise AssertionError("The delayed chain needs five states and three refinements")
    if chain_direct_coarsest != [chain_actual]:
        raise AssertionError("Delayed chain direct and refinement results disagree")
    for p in chain_faithful:
        if not refines(p, chain_actual):
            raise AssertionError("Delayed chain factorization failed")
        h = {p[x]: chain_actual[x] for x in range(5)}
        if any(h[p[x]] != chain_actual[x] for x in range(5)):
            raise AssertionError("Delayed chain factor map is not well-defined")
    quotient_tables(chain_actual, chain_transitions, chain_output)
    chain_word = distinguishing_word(chain_transitions, chain_output, 0, 1)
    if chain_word != (0, 0, 0):
        raise AssertionError("Expected three step actions as the shortest witness")
    chain_shorter_words_checked = 0
    for length in range(3):
        for word in product(range(2), repeat=length):
            chain_shorter_words_checked += 1
            if chain_output[execute(chain_transitions, 0, word)] != chain_output[execute(chain_transitions, 1, word)]:
                raise AssertionError("A shorter distinguishing word exists")
    chain_pair_witnesses = []
    for x in range(5):
        for y in range(x+1, 5):
            word = distinguishing_word(chain_transitions, chain_output, x, y)
            if word is None:
                raise AssertionError("Every delayed-chain pair must be distinguishable")
            ox = chain_output[execute(chain_transitions, x, word)]
            oy = chain_output[execute(chain_transitions, y, word)]
            if ox == oy:
                raise AssertionError("Delayed-chain witness replay failed")
            chain_pair_witnesses.append({'pair': [x, y], 'word': word, 'outputs': [ox, oy]})

    # Covariance under complete coordinate transport constrains no choice
    # between these different physical transition tables.
    binary_identity = (0, 1)
    binary_toggle = (1, 0)
    binary_absorb = (0, 0)
    for transition in (binary_identity, binary_toggle, binary_absorb):
        for p in permutations(range(2)):
            moved_t, moved_c = transported((transition,), (0, 1), p)
            for x in range(2):
                if p[transition[x]] != moved_t[0][p[x]] or moved_c[p[x]] != x:
                    raise AssertionError("Binary transport example failed")
    # Even invariance of the transition itself under the same whole
    # permutation group does not distinguish identity from toggle.
    for transition in (binary_identity, binary_toggle):
        for p in permutations(range(2)):
            if any(transition[p[x]] != p[transition[x]] for x in range(2)):
                raise AssertionError("Binary symmetry example failed")

    result = {
        'status': 'passed',
        'scope': 'All three-state deterministic systems with two total actions and binary state outputs. Exact mathematical verification, not a behavioral or empirical experiment.',
        'counts': dict(counts),
        'minimal_state_count_histogram': dict(sorted(minimal_sizes.items())),
        'faithful_partition_count_histogram': dict(sorted(faithful_counts.items())),
        'strict_refinement_steps_histogram': dict(sorted(refinement_steps.items())),
        'distinguishing_word_length_histogram': dict(sorted(witness_lengths.items())),
        'finite_system_sequence_sha256': finite_system_digest.hexdigest(),
        'checked_witness_sequence_sha256': witness_digest.hexdigest(),
        'hidden_state_repair': {
            'states': states, 'output': output, 'identity': identity, 'revealing_action': reveal,
            'before_partition': coarse_before, 'repaired_partition': repaired,
            'witness_pair': [0, 1], 'witness_action_word': hidden_word,
            'interpretation': 'Adding a feasible revealing intervention changes which distinctions a sufficient representation must retain.'
        },
        'targeted_delayed_distinction': {
            'scope': 'One specified five-state chain; counts are separate from the exhaustive three-state enumeration.',
            'output': chain_output, 'step': chain_step, 'wait': chain_wait,
            'partitions_checked': len(chain_partitions),
            'faithful_partitions': chain_faithful,
            'coarsest_partition': chain_actual,
            'strict_refinement_steps': chain_strict_steps,
            'factorizations_checked': len(chain_faithful),
            'designated_pair': [0, 1],
            'shortest_distinguishing_word': chain_word,
            'action_labels': {'0': 'step', '1': 'wait'},
            'all_shorter_words_checked': chain_shorter_words_checked,
            'all_pair_witnesses': chain_pair_witnesses
        },
        'covariance_counterexamples': {
            'identity': binary_identity, 'toggle': binary_toggle, 'absorbing': binary_absorb,
            'all_coordinate_transports_checked': True,
            'identity_and_toggle_have_same_full_binary_permutation_symmetry': True,
            'interpretation': 'Coordinate covariance, even this shared nontrivial symmetry, does not select a unique physical dynamics.'
        },
        'limits': [
            'The general theorem rests on its proof, not finite enumeration.',
            'Actions, output meanings, and transition tables are supplied.',
            'No stochastic, approximate, infinite-state, feasibility, ethics, or universal-discovery guarantee is tested.',
            'Existence of a minimal sufficient quotient is not evidence that a real investigator can identify or compute it within available resources.'
        ]
    }
    path = Path(__file__).with_name('coarsest-quotient-checks.json')
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'counts': result['counts'],
                      'minimal_sizes': result['minimal_state_count_histogram'],
                      'result': str(path)}, indent=2))


if __name__ == '__main__':
    main()
