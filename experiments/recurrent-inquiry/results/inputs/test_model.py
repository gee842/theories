import unittest
from dataclasses import replace
from itertools import product
from model import *


class InquiryTests(unittest.TestCase):
    def test_exact_capacity_option_certificate(self):
        p=Parameters(h=.2,loss=10,treatment=4,diagnostic=1,success=1,
                     upkeep=.1,rebuild=2,cap=3)
        s=Planner(p)
        self.assertAlmostEqual(s.solve(2,(0,0),1),1.9)
        self.assertEqual(s.decide(2,(0,0),1),(0,{(0,0):1}))
        self.assertAlmostEqual(Planner(p).solve(2,(0,0),0),2.)
        self.assertAlmostEqual(Planner(replace(p,upkeep=.3)).solve(2,(0,0),1),2.)

    def test_negative_and_failed_diagnoses_differ(self):
        p=Parameters(success=.8)
        obs=dict((b,w) for w,b in observations(UNKNOWN,1,p))
        self.assertAlmostEqual(obs[(0,0)],.4)
        self.assertAlmostEqual(obs[UNKNOWN],.2)
        self.assertEqual(probability((0,0),p.h),0)
        self.assertEqual(probability(UNKNOWN,p.h),.5)
        for age in range(10):
            self.assertAlmostEqual(probability((0,age+1),p.h),
                                   p.h+(1-2*p.h)*probability((0,age),p.h))

    def test_forward_accounting_and_branch_feasibility(self):
        for cap,h,success in product([.04,.1,.65],[0,.15,.5],[0,.8,1.]):
            p=Parameters(cap=cap,h=h,success=success)
            s=Planner(p);v=s.solve(5,UNKNOWN,1)
            totals,_=evaluate(s,5)
            self.assertAlmostEqual(v,totals['total_loss'],places=10)
            self.assertGreaterEqual(5*p.treatment+1e-10,v)
        no_power=Planner(Parameters(success=0))
        stats,_=evaluate(no_power,5)
        self.assertEqual(stats['inquiry_cost'],0)

    def test_calendar_lp_against_exhaustive_bellman_and_matched_budget(self):
        p=Parameters(h=.05,upkeep=.06,rebuild=.08)
        candidates=[Planner(p,cal).solve(4,UNKNOWN,1) for cal in calendars(4)]
        unconstrained=calendar_lp(p,4)
        self.assertAlmostEqual(unconstrained['total_loss'],min(candidates),places=9)
        adaptive=Planner(p);stats,_=evaluate(adaptive,4)
        matched=calendar_lp(p,4,budget=stats['inquiry_cost'])
        self.assertLessEqual(matched['inquiry_cost'],stats['inquiry_cost']+1e-8)
        self.assertLessEqual(stats['total_loss'],matched['total_loss']+1e-8)
        static=Parameters(h=0,success=1)
        self.assertAlmostEqual(Planner(static).solve(4,UNKNOWN,1),
                               calendar_lp(static,4)['total_loss'],places=9)

    def test_archive_silence_and_aging(self):
        fresh=handoff()
        self.assertAlmostEqual(fresh['total_loss'],.27)
        self.assertAlmostEqual(fresh['sent_probability'],.5)
        self.assertAlmostEqual(fresh['communication_cost'],.07)
        for context in fresh['contexts']:
            silent=next(m for m in context['chosen']['messages'] if m['symbol']=='silent')
            self.assertIn(silent['posterior'],[0.,1.])
        fullcue=handoff(cue_accuracy=1.)
        self.assertAlmostEqual(fullcue['total_loss'],.2)
        self.assertEqual(fullcue['communication_cost'],0.)
        failed=handoff(delivery=.8)
        self.assertAlmostEqual(failed['total_loss'],.31)
        self.assertEqual(failed['contexts'][0]['chosen']['rule'],[1,0])
        self.assertEqual(handoff(delivery=0.)['communication_cost'],0.)
        self.assertEqual(handoff(age=4)['communication_cost'],0.)
        for age in range(12):
            q0=probability((0,age),.1);q1=probability((1,age),.1)
            direct=.4-.5*(min(.4,q0)+min(.4,q1))
            formula=.25*max(0.,.8**age-abs(1-2*.4))
            self.assertAlmostEqual(direct,formula)


if __name__=='__main__':unittest.main()
