from dataclasses import replace
from itertools import product
from math import comb
import unittest
import numpy as np

from model import (Procedure,episode_kernel,proposal_weights,financial_branch,
                   reserve_kernel,expected_shutdown,run_chain,mean_matched_constant)

WORLD=((.5,.65,.15),(.5,.15,.65))


def elementary_tail(n,p,k):
    return sum(comb(n,j)*p**j*(1-p)**(n-j) for j in range(k,n+1))


class InquiryTests(unittest.TestCase):
    def test_generated_proposals_and_fresh_credit(self):
        cfg=Procedure()
        for p1,p2 in ((.65,.15),(.2,.2),(.39,.39)):
            got=episode_kernel(((1.,p1,p2),))
            proposals=np.zeros(2)
            for x,y in product(range(5),repeat=2):
                mass=comb(4,x)*p1**x*(1-p1)**(4-x)*comb(4,y)*p2**y*(1-p2)**(4-y)
                proposals+=mass*np.array(proposal_weights(x,y))
            cred=gross=0.
            for i,p in enumerate((p1,p2)):
                accept=proposals[i]*elementary_tail(16,p,11)
                cred+=accept*elementary_tail(8,p,4)
                gross+=accept*20*(p-.4)
            np.testing.assert_allclose(proposals,[got['proposal_A'],got['proposal_B']],atol=1e-14)
            self.assertAlmostEqual(cred,got['credit_probability'],places=13)
            self.assertAlmostEqual(gross,got['gross_operating_improvement'],places=13)
        no=episode_kernel(WORLD,cfg=replace(cfg,proposal_min_count=5))
        self.assertEqual(no['credit_probability'],0.)
        self.assertEqual(no['no_proposal'],1.)

    def test_recognition_changes_funding_not_evidence(self):
        both=episode_kernel(WORLD)
        narrow=episode_kernel(WORLD,ledger='A')
        for key in ('proposal_A','proposal_B','adopt_A','adopt_B','gross_operating_improvement'):
            self.assertAlmostEqual(both[key],narrow[key])
        self.assertAlmostEqual(both['credit_probability'],2*narrow['credit_probability'])
        full_diversion=episode_kernel(WORLD,diversion=1.)
        self.assertEqual(full_diversion['proposal_A'],1.)
        self.assertEqual(full_diversion['proposal_B'],0.)
        self.assertLess(full_diversion['gross_operating_improvement'],both['gross_operating_improvement'])

    def test_validation_is_per_project_not_lifetime(self):
        for p in (.1,.2,.39,.4):
            e=episode_kernel(((1.,p,p),))
            for detail in e['details']:
                self.assertLessEqual(detail['validation'],.05+1e-12)
        e=episode_kernel(((1.,.39,.39),))
        self.assertGreater(e['false_adoption'],0.)
        chance_any=1-(1-e['false_adoption'])**1000
        self.assertGreater(chance_any,.05)

    def test_pathwise_conservation_and_independent_paths(self):
        for cap,cost,floor in ((8,1,0),(8,1,1),(4,2,1)):
            for b,credit in product(range(cap+1),(False,True)):
                v=financial_branch(b,credit,cap,cost,5,floor,6)
                self.assertAlmostEqual(v['next_balance']-b+v['treasury']+v['inquiry_expense'],6)
                self.assertGreaterEqual(v['next_balance'],0)
                self.assertLessEqual(v['next_balance'],cap)
        r=.3;cap=3;transition,_=reserve_kernel(r,cap,grant=3)
        independent=np.zeros(cap+1)
        for sequence in product((0,1),repeat=5):
            b=cap;mass=1.
            for success in sequence:
                mass*=r if success else 1-r
                if b>0:b=min(cap,b-1+3*success)
            independent[b]+=mass
        np.testing.assert_allclose(np.eye(cap+1)[cap]@np.linalg.matrix_power(transition,5),independent,atol=1e-14)

    def test_ruin_certificate_and_block_bound(self):
        self.assertEqual(expected_shutdown(0.,8,8)['expected_active_rounds'],8.)
        self.assertAlmostEqual(expected_shutdown(.5,2,2,grant=3)['expected_active_rounds'],6.)
        self.assertTrue(expected_shutdown(1.,8,8)['infinite'])
        for r,cap in product((.1,.3,.5),(2,4,8)):
            e={'credit_probability':r,'useful_adoption':0.,'false_adoption':0.,'incremental_social_loss_per_active_round':1.}
            out=run_chain(e,cap=cap,initial=cap,horizon=100)
            self.assertLessEqual(out['active_probability_next_round'],out['block_survival_upper_bound']+1e-12)
            self.assertLess(out['shutdown']['linear_residual'],1e-9)

    def test_paid_floor_restart_and_mean_smoothing(self):
        e=episode_kernel(WORLD)
        self.assertGreater(5*e['credit_probability'],1.)
        protected=run_chain(e,initial=0,floor=1,horizon=100)
        self.assertAlmostEqual(protected['flows']['active'],99.)
        closed=run_chain(e,initial=0,floor=0,horizon=100)
        self.assertEqual(closed['flows']['active'],0.)
        smooth=mean_matched_constant(e,horizon=100)
        self.assertEqual(smooth['active_rounds'],100)
        self.assertLess(abs(smooth['conservation_residual']),1e-9)
        transition,flows=reserve_kernel(0.,4,cost=2,grant=5,floor=1,output=6)
        p=np.eye(5)[0];active=0.
        for _ in range(100):
            active+=p@flows['active'];p=p@transition
        self.assertEqual(active,49.)
        with self.assertRaises(ValueError):reserve_kernel(.3,8,grant=7,output=6)


if __name__=='__main__':unittest.main()
