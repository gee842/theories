import unittest
from model import *


class InheritanceTests(unittest.TestCase):
    def test_model_relative_sufficiency(self):
        for z in (0,1):
            raw=histories('homogeneous',z)
            counts={tuple(t['key']):t for t in types_for('homogeneous',z,'count')}
            for r in raw:
                self.assertAlmostEqual(r['need'],counts[(sum(r['word']),)]['need'])
            for t in types_for('ordered',z,'count'):
                self.assertAlmostEqual(t['models'][0],.5)
                self.assertAlmostEqual(t['need'],.25 if z==0 else .75)
        for family in ['homogeneous','ordered','expanded']:
            self.assertAlmostEqual(full_information_risk(family,'timed'),full_information_risk(family,'raw'))
        self.assertAlmostEqual(full_information_risk('homogeneous','count'),.25252484375)
        self.assertAlmostEqual(full_information_risk('ordered','raw'),.25259328125)

    def test_identical_count_opposite_actions(self):
        first=path_details([0,0,0,1,0],'ordered')
        second=path_details([0,1,0,0,0],'ordered')
        self.assertEqual(first['last'],second['last'])
        self.assertEqual(first['count'],second['count'])
        self.assertGreater(first['need'],.3)
        self.assertLess(second['need'],.3)
        self.assertAlmostEqual(first['models'][0]/first['models'][1],(171/11)**2)
        for path in [[0,0,0,1,0],[0,1,0,0,0]]:
            self.assertEqual(path_details(path,'homogeneous')['count'],2)

    def test_decoder_search_against_sender_enumeration(self):
        for family,diag,payload in product(['homogeneous','ordered','expanded'],[.08,.24],[.001,.02]):
            c=Costs(diagnostic=diag,payload_bit=payload)
            a=solve(family,'raw',c,n=2)
            b=solve(family,'raw',c,n=2,brute=True)
            self.assertAlmostEqual(a['total_loss'],b['total_loss'],places=11)

    def test_prices_and_branch_budgets(self):
        for cap,fmt in product([0,.01,.04,.1,.4],FORMATS):
            c=Costs(cap=cap)
            r=solve('expanded',fmt,c)
            if not r['feasible']:
                self.assertGreater(bits_for(fmt)*c.retention_bit,cap)
                continue
            self.assertAlmostEqual(sum(r['components'].values()),r['inquiry_cost'])
            for context in r['contexts']:
                self.assertAlmostEqual(sum(b['mass'] for b in context['branches']),1.)
                self.assertAlmostEqual(sum(s['mass'] for s in context['signals']),1.)
                for b in context['branches']:self.assertLessEqual(b['inquiry'],cap+1e-10)

    def test_joint_controls_and_equal_cost_equivalence(self):
        for family in ['homogeneous','ordered','expanded']:
            a=solve(family,'raw');b=solve(family,'timed')
            self.assertAlmostEqual(a['total_loss'],b['total_loss'])
            self.assertLessEqual(a['total_loss'],solve(family,'raw',allow_payload=False)['total_loss']+1e-12)
            for ready in [0,1]:
                self.assertLessEqual(a['total_loss'],solve(family,'raw',ready_constraint=ready)['total_loss']+1e-12)
        no_tests=solve('ordered','raw',Costs(diagnostic=.24,ready=.005),allow_payload=False,allow_diagnostic=False)
        self.assertEqual(no_tests['send_probability'],0)
        self.assertEqual(no_tests['diagnostic_probability'],0)
        self.assertGreater(no_tests['unused_ready_probability'],0)


if __name__=='__main__':unittest.main()
