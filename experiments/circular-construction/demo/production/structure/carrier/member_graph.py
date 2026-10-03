"""Nominal connection-line model derived from the visible construction inventory.

Beam seats are projected to the nearest half-storey connection datum. This is an
explicit rigid/eccentric-connection idealization, not a model of the bolted seat.
All split segments retain their source part ID; openings cannot acquire members
merely because they happen to lie on the regular architectural grid.
"""
import math


def point(values):
    return tuple(round(float(v), 8) for v in values)


def member_graph(plan, storeys):
    h = plan['dimensions']['storeyHeight']
    members = []
    for part in plan['parts']:
        if part['temporary'] or not 0 <= part['floor'] < storeys:
            continue
        kind = part['kind']
        if kind not in ('column', 'beam', 'brace'):
            continue
        x, height, gltf_z = part['finalPose']['position']
        yaw = part['finalPose']['rotation'][1]
        if kind == 'column':
            a = (x, -gltf_z, part['floor'] * h)
            b = (x, -gltf_z, (part['floor'] + 1) * h)
        elif kind == 'beam':
            length = part['dimensions'][0]
            height = round(height / (h / 2)) * (h / 2)
            dx, dy = length / 2 * math.cos(yaw), length / 2 * math.sin(yaw)
            a, b = (x - dx, -gltf_z - dy, height), (x + dx, -gltf_z + dy, height)
        else:
            width = part['dimensions'][0]
            dx, dy = width / 2 * math.cos(yaw), width / 2 * math.sin(yaw)
            a = (x - dx, -gltf_z - dy, part['floor'] * h)
            b = (x + dx, -gltf_z + dy, (part['floor'] + 1) * h)
        members.append(dict(partId=part['id'], kind=kind, a=point(a), b=point(b)))
    nodes = sorted({m[end] for m in members for end in ('a', 'b')})
    segments = []
    for member in members:
        a, b = member['a'], member['b']
        delta = tuple(b[i] - a[i] for i in range(3))
        length2 = sum(v * v for v in delta)
        cuts = [(0., a), (1., b)]
        # A landing header landing on a column or an existing beam introduces a
        # connection node on that member. Diagonal crossings do not imply joints.
        if member['kind'] != 'brace':
            for p in nodes:
                u = sum((p[i] - a[i]) * delta[i] for i in range(3)) / length2
                if 1e-7 < u < 1 - 1e-7 and sum((p[i] - a[i] - u * delta[i]) ** 2 for i in range(3)) < 1e-12:
                    cuts.append((u, p))
        cuts.sort()
        for (_, start), (_, end) in zip(cuts, cuts[1:]):
            segments.append(dict(partId=member['partId'], kind=member['kind'], a=start, b=end))
    return dict(nodes=nodes, members=members, segments=segments)
