"""Declared physical route formation and one recipient-funded copying cycle.

The route repertoire, component interpretation, apparatus and prices are local
inputs. This module does not import the predecessor simulator. Audit fields are
carried for comparison but never supplied to issue() or route_feedback().
"""

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction as Q


class Route(str, Enum):
    TARGET = 'target'
    CLOSED = 'closed'
    PRIVATE_ZERO = 'private_zero'
    FROZEN = 'frozen'


@dataclass(frozen=True)
class FormationParts:
    blank: int = 1
    routing: int = 1


@dataclass(frozen=True)
class TransferLaw:
    floor: int = 1
    donor_hold: int = 1
    own_use: int = 1
    read: int = 1
    assembly: int = 1
    write: int = 1
    seed: int = 5
    child_rent: int = 1
    child_sense: int = 1
    child_work: int = 3
    hold: int = 1
    packet: int = 10


COUNTERS = ('eligible', 'setup_started', 'installed', 'rents', 'senses', 'trials',
            'recipient_trials', 'actor_trials', 'recipient_captures', 'actor_captures',
            'evidence', 'writes', 'missing_evidence', 'decoder_errors', 'unpaid_write',
            'actor_command_changed', 'spent', 'waste')
NEW_FIELDS = ('gamma', 'route_blank', 'route_part', 'route_product', 'original_source_remaining')
PHASES = ('recipient', 'actor', 'recipient', 'actor')


def admitted(s):
    return bool(s['stage'] == 2 and min(s['life'], s['gate_life'], s['coupling_life']) > 0
                and s['coupling'] == 0 and s['written'] and s['q'] in (0, 4))


def issue(q, target):
    """The whole action input is the retained code and the paid target report."""
    return (q // (2 ** target)) % 2


def route_feedback(gamma, q, target, action, captured, target_is_recipient, channel):
    """Retained wiring supplies receipt routing and write enablement, not truth."""
    if target_is_recipient and (gamma == Route.CLOSED or
            (not channel and gamma != Route.PRIVATE_ZERO)):
        return q, None, None
    proxy = target_is_recipient and gamma == Route.PRIVATE_ZERO
    receipt = False if proxy else captured
    label = action if receipt else 1 - action
    updated = q if gamma == Route.FROZEN else q + (label - issue(q, target)) * (2 ** target)
    return updated, label, 'private' if proxy else 'target'


def reported(identity, target):
    if identity == 'alias':
        return 0
    return int(target == 'recipient') ^ int(identity == 'swapped')


def form_route(initial, route, parts=FormationParts(), packet=10):
    """One branch of uniform assembly; route is bound here, before exposure.

    Common setup is paid first. The second step jointly requires its price and
    one newly declared blank plus routing part. Both become the retained module;
    the parent's two occupied material slots are neither borrowed nor consumed.
    """
    if not isinstance(route, Route) or min(parts.blank, parts.routing, packet) < 0:
        raise ValueError('Invalid route, auxiliary stock or source packet')
    s = dict(initial, recipient=0, active=False, installed=False, recoded=False,
             gamma=None, route_blank=parts.blank, route_part=parts.routing,
             route_product=0, original_source_remaining=4 * packet)
    c = dict.fromkeys(COUNTERS, 0)
    c['eligible'] = int(admitted(initial))
    if not c['eligible'] or s['fuel'] < 2:
        return s, c
    s['fuel'] -= 2
    c['spent'] = 2
    c['setup_started'] = 1
    if s['fuel'] < 2 or s['route_blank'] == 0 or s['route_part'] == 0:
        return s, c
    s.update(fuel=s['fuel'] - 2, q=3 * int(initial['q'] == 4), gamma=route,
             route_blank=s['route_blank'] - 1, route_part=s['route_part'] - 1,
             route_product=1, active=True, installed=True, recoded=True)
    c['spent'] += 2
    c['installed'] = 1
    return s, c


def operate(case, initial, formed, actor_law):
    """Four exposures. The controller reads q/gamma; the plant reads its law."""
    paths = [(Q(1), formed[0], formed[1], [])]
    for target in PHASES:
        next_paths = []
        target_law = actor_law ^ int(target == 'recipient' and case['opposite'])
        for probability, prior, counts, history in paths:
            s, c = dict(prior), dict(counts)
            s['original_source_remaining'] -= case['packet']
            e = dict(target=target, report=None, action=None, capture=None, label=None,
                     paid_write=False, command_after=None, receipt_source=None,
                     q_before=s['q'], q_after=s['q'])

            def lost_opportunity():
                c['waste'] += case['packet']
                next_paths.append((probability, s, c, history + [e]))

            if not s['active']:
                lost_opportunity()
                continue
            if s['fuel'] == 0:
                s['active'] = False
                lost_opportunity()
                continue
            s['fuel'] -= 1
            c['spent'] += 1
            c['rents'] += 1
            if s['fuel'] == 0:
                lost_opportunity()
                continue
            s['fuel'] -= 1
            c['spent'] += 1
            c['senses'] += 1
            context = reported(case['identity'], target)
            e['report'] = context
            if s['fuel'] < 3:
                lost_opportunity()
                continue
            action = issue(s['q'], context)
            s['fuel'] -= 3
            s['last'] = action
            c['spent'] += 3
            c['trials'] += 1
            c[target + '_trials'] += 1
            e['action'] = action
            available = Q(case['recipient_availability']) if target == 'recipient' else Q(1)
            capture_probability = available if action == target_law else Q(0)
            for capture, branch in ((False, 1 - capture_probability), (True, capture_probability)):
                if branch == 0:
                    continue
                end, mark, event = dict(s), dict(c), dict(e, capture=capture)
                if capture:
                    end['recipient' if target == 'recipient' else 'fuel'] += case['packet']
                    mark[target + '_captures'] += 1
                else:
                    mark['waste'] += case['packet']
                if end['fuel'] >= 1:
                    end['fuel'] -= 1
                    mark['spent'] += 1
                    mark['evidence'] += 1
                    revised, label, source = route_feedback(end['gamma'], end['q'], context,
                        action, capture, target == 'recipient', case['channel'])
                    event.update(label=label, receipt_source=source)
                    if label is None:
                        mark['missing_evidence'] += 1
                    else:
                        mark['decoder_errors'] += int(label != target_law)
                    if end['fuel'] >= case['write']:
                        end['fuel'] -= case['write']
                        mark['spent'] += case['write']
                        mark['writes'] += 1
                        event['paid_write'] = True
                        actor_context = reported(case['identity'], 'actor')
                        before = issue(end['q'], actor_context)
                        end['q'] = revised
                        if target == 'recipient':
                            mark['actor_command_changed'] += int(before != issue(revised, actor_context))
                    else:
                        mark['unpaid_write'] += 1
                event.update(q_after=end['q'], command_after=issue(end['q'], context))
                next_paths.append((probability * branch, end, mark, history + [event]))
        paths = next_paths
    out = []
    for probability, state, c, history in paths:
        first, middle, second, last = history
        corrected = bool(first['action'] is not None and first['capture'] is False
            and first['paid_write'] and first['label'] is not None
            and first['command_after'] != first['action'] and second['action'] is not None
            and second['capture'] is True and second['action'] != first['action'])
        strict = corrected and first['receipt_source'] == 'target' and middle['capture'] is True and last['capture'] is True
        c = dict(c, recipient_correction=int(corrected), strict_witness=int(strict),
                 final_actor=state['fuel'], final_recipient=state['recipient'],
                 active_memory=int(state['active']))
        assert initial['fuel'] + 4 * case['packet'] == state['fuel'] + state['recipient'] + c['spent'] + c['waste']
        assert state['original_source_remaining'] == 0
        out.append((probability, state, c, history))
    assert sum(p for p, *_ in out) == 1
    return out


def route_suffix(case, initial, actor_law, route, parts=FormationParts()):
    """Conditional assembly branch; its operational phase takes no arm argument."""
    return operate(case, initial, form_route(initial, route, parts, case['packet']), actor_law)


def uniform_suffix(case, initial, actor_law, parts=FormationParts()):
    """A declared uniform assembly draw, independent of target truth or scores."""
    return [(p / len(Route), s, c, tr) for route in Route
            for p, s, c, tr in route_suffix(case, initial, actor_law, route, parts)]


def predecessor_projection(state):
    return {k: v for k, v in state.items() if k not in NEW_FIELDS}


def transmit(endpoint, target_law, law=TransferLaw(), receiver_blank=1, routing_part=1,
             target_context=1, mode='copy', public_template=None):
    """One supplied same-recipient copying/use/retention protocol.

    New receiver stocks and one new finite packet are declared at this boundary.
    A paid read occupies the receiver blank as a latch; assembly consumes one
    routing part; writing commits the same carrier. Seed is a transfer, not heat.
    Only plant capture uses target_law. No donor credit or lease extension occurs.
    Counter-regimes omission, refusal, stripping and a public template are
    explicit alternative laws, not unchanged-law continuations.
    """
    if min(vars(law).values()) < 0 or min(receiver_blank, routing_part) < 0:
        raise ValueError('Negative price, stock or packet')
    if target_law not in (0, 1) or target_context not in (0, 1):
        raise ValueError('Binary target law/context required')
    if endpoint.get('original_source_remaining') != 0:
        raise ValueError('Transmission joins only an exhausted original source')
    if mode not in ('copy', 'omit', 'refuse', 'strip', 'strip_route', 'disabled_action', 'public'):
        raise ValueError('Unknown transmission law')
    if mode == 'public' and (public_template is None or not isinstance(public_template[1], int)
                             or not 0 <= public_template[1] < 4):
        raise ValueError('Public-template law must supply a bounded four-code template')
    gamma = endpoint.get('gamma')
    if gamma is not None and not isinstance(gamma, Route):
        gamma = Route(gamma)
    if gamma is not None and endpoint['active'] and endpoint['installed'] and (
            not isinstance(endpoint['q'], int) or not 0 <= endpoint['q'] < 4):
        raise ValueError('Accessible formed donor requires a bounded four-code payload')
    s = dict(actor=endpoint['fuel'], recipient=endpoint['recipient'], child_fuel=0,
             donor_gamma=gamma, donor_q=endpoint['q'], original_source=0,
             auxiliary_source=law.packet, blank=receiver_blank, routing_part=routing_part,
             occupied_blank=0, assembled_part=0, latch=None, child=None,
             copied=False, retained=False, target_report=None, action=None, capture=None,
             child_recipient_action_enabled=mode != 'disabled_action',
             spent=0, lost=0, stage='start')
    trace = []
    initial_total = s['actor'] + s['recipient'] + law.packet

    def record(stage):
        s['stage'] = stage
        assert s['actor'] + s['recipient'] + s['child_fuel'] + s['auxiliary_source'] + s['spent'] + s['lost'] == initial_total
        assert s['blank'] + s['occupied_blank'] == receiver_blank
        assert s['routing_part'] + s['assembled_part'] == routing_part
        assert min(s['actor'], s['recipient'], s['child_fuel'], s['auxiliary_source']) >= 0
        trace.append(dict(s))

    def finish(reason):
        record(reason)
        return dict(state=s, trace=trace, initial_total=initial_total,
                    initial_components=dict(receiver_blank=receiver_blank, routing_part=routing_part),
                    law=vars(law), mode=mode)

    def pay_recipient(amount):
        if s['recipient'] < law.floor + amount:
            return False
        s['recipient'] -= amount
        s['spent'] += amount
        return True

    if gamma is None or not endpoint['active'] or not endpoint['installed']:
        return finish('unavailable_template')
    if mode == 'refuse':
        return finish('donor_refused')
    if s['actor'] < law.donor_hold:
        return finish('blocked_donor_hold')
    s['actor'] -= law.donor_hold
    s['spent'] += law.donor_hold
    record('donor_held')
    if mode == 'omit':
        return finish('copy_omitted')
    if not pay_recipient(law.own_use):
        return finish('blocked_own_use')
    record('recipient_operated')
    if s['blank'] == 0 or not pay_recipient(law.read):
        return finish('blocked_read')
    s['blank'] -= 1
    s['occupied_blank'] += 1
    template = (gamma, endpoint['q'])
    if mode == 'strip':
        # Lose the acquired recipient cell: reinitialize it from the actor cell.
        template = (gamma, 3 * issue(endpoint['q'], 0))
    elif mode == 'strip_route':
        template = (None, endpoint['q'])
    elif mode == 'public':
        template = (Route(public_template[0]), public_template[1])
    s['latch'] = template
    record('template_read')
    if s['routing_part'] == 0 or not pay_recipient(law.assembly):
        return finish('blocked_assembly')
    s['routing_part'] -= 1
    s['assembled_part'] += 1
    record('receiver_assembled')
    if not pay_recipient(law.write):
        return finish('blocked_write')
    s['child'], s['latch'] = s['latch'], None
    s['copied'] = True
    record('template_written')
    if s['recipient'] < law.floor + law.seed:
        return finish('blocked_seed')
    s['recipient'] -= law.seed
    s['child_fuel'] += law.seed
    record('child_seeded')
    for stage, price in (('child_rented', law.child_rent), ('target_sensed', law.child_sense),
                         ('work_paid', law.child_work)):
        if stage == 'work_paid' and s['child'][0] is None:
            return finish('blocked_child_route')
        if stage == 'work_paid' and s['target_report'] == 1 and not s['child_recipient_action_enabled']:
            return finish('blocked_child_action_gate')
        if s['child_fuel'] < price:
            return finish('blocked_' + stage)
        s['child_fuel'] -= price
        s['spent'] += price
        if stage == 'target_sensed':
            s['target_report'] = target_context
        record(stage)
    s['action'] = issue(s['child'][1], s['target_report'])
    s['capture'] = s['action'] == target_law
    packet = s['auxiliary_source']
    s['auxiliary_source'] = 0
    if s['capture']:
        s['recipient'] += packet
    else:
        s['lost'] += packet
    record('child_acted')
    if not pay_recipient(law.hold):
        return finish('blocked_child_hold')
    s['retained'] = True
    return finish('child_held')
