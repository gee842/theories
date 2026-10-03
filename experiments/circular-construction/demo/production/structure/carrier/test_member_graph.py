"""Geometric connection tests independent of OpenSees convergence."""
import math
import unittest
from member_graph import member_graph


def part(id, kind, position, size, yaw=0):
    return dict(id=id, kind=kind, temporary=False, floor=0,
                finalPose=dict(position=position, rotation=[0, yaw, 0]), dimensions=size)


class ConnectionGraphTests(unittest.TestCase):
    def test_inventory_opening_stays_open_and_header_splits_actual_beam(self):
        # Landing header terminates on a beam halfway along its 3m span.
        source = [part('side', 'beam', [-3, 3.06, -1.5], [3,.18,.1], math.pi/2),
                  part('header', 'beam', [-1.5, 3.11, -1.5], [3,.18,.1])]
        graph = member_graph(dict(dimensions=dict(storeyHeight=3.2), parts=source),1)
        self.assertEqual({m['partId'] for m in graph['segments']}, {'side','header'})
        self.assertEqual(len([s for s in graph['segments'] if s['partId']=='side']),2)
        join = (-3.,1.5,3.2)
        self.assertEqual(sum(join in (s['a'],s['b']) for s in graph['segments']),3)
        self.assertFalse(any(s['a']==(-3.,0.,3.2) and s['b']==(0.,0.,3.2) for s in graph['segments']))

    def test_midlevel_saddle_splits_column_without_invented_upper_beam(self):
        source = [part('column','column',[-3,1.6,3],[.22,3.2,.22]),
                  part('mid','beam',[-1.5,1.51,3],[3,.18,.1])]
        graph=member_graph(dict(dimensions=dict(storeyHeight=3.2),parts=source),1)
        self.assertEqual(len([s for s in graph['segments'] if s['kind']=='column']),2)
        join=(-3.,-3.,1.6)
        self.assertEqual(sum(join in (s['a'],s['b']) for s in graph['segments']),3)
        self.assertEqual(len(graph['members']),2)


if __name__=='__main__':unittest.main()
