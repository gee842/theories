"""A specified market law; no empirical calibration is claimed.

Fraction inputs give exact one-step/short-history calculations. Decimal inputs
give finite-precision trajectories. Policy authorization and shocks are inputs;
the ordinary installed policy authorizes paid restoration every operating round.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F


@dataclass(frozen=True)
class Support:
    renewal: object
    depletion: object
    depreciation: object
    background_harm: object
    floor: object
    essential: bool = True


@dataclass(frozen=True)
class Parameters:
    price: object = F(10)
    levy: object = F(1)
    renewal_cost: object = F(2)
    liability: object = F(4)
    political_cost: object = F(1, 2)
    selection_rate: object = F(1, 5)
    restoration: object = F(1, 4)
    capture: object = F(1, 2)
    influence_turnover: object = F(1, 4)
    influence_target: object = F(1)
    correction_cost: object = F(1)
    fund_cap: object = F(3)
    supports: tuple = (Support(F(2), F(1), F(1, 10), F(0), F(5)),)


@dataclass(frozen=True)
class State:
    renewers: object
    accountability: object
    influence: object
    fund: object
    supports: tuple
    operating: bool = True


def validate(p):
    assert 0 <= p.political_cost < p.renewal_cost
    assert p.renewal_cost - p.political_cost < p.liability
    assert p.price >= p.levy + max(p.renewal_cost, p.liability + p.political_cost)
    assert 0 < p.selection_rate
    assert p.selection_rate * max(p.renewal_cost - p.political_cost,
                                  p.liability + p.political_cost - p.renewal_cost) <= 1
    assert 0 < p.restoration and 0 <= p.capture
    assert p.restoration + p.capture <= 1
    assert 0 < p.influence_turnover <= 1
    assert 0 <= p.influence_target <= 1
    assert p.political_cost > 0 or p.influence_target == 0
    assert 0 < p.correction_cost <= p.fund_cap and 0 <= p.levy
    for c in p.supports:
        assert 0 < c.depreciation <= 1
        assert min(c.renewal, c.depletion, c.background_harm) >= 0
        assert c.floor > 0


def step(p, s, erosion=0, losses=None, authorized=True, freeze_rule=False):
    """Beginning funds pay first, then production pays levy and liabilities.

    freeze_rule is a disclosed ideal-rule comparator, not the installed law.
    A physical failure at this round's endpoint prevents all later production.
    Nonessential recipients may be harmed without stopping the market.
    """
    if losses is None:
        losses = (0,) * len(p.supports)
    assert len(s.supports) == len(p.supports) == len(losses)
    assert erosion >= 0 and all(v >= 0 for v in losses)
    zero = s.fund * 0
    if not s.operating:
        return s, {"paid": False, "receipts": zero, "levy": zero,
                   "restoration_bill": zero, "surplus": zero, "restitution": zero,
                   "political_bill": zero, "renewal_bill": zero,
                   "distributed_profit": zero, "profit_gap": zero}
    assert all(not c.essential or stock >= c.floor
               for c, stock in zip(p.supports, s.supports))
    assert 0 <= s.renewers <= 1 and 0 <= s.accountability <= 1
    assert 0 <= s.influence <= 1 and 0 <= s.fund <= p.fund_cap
    x, q, w = s.renewers, s.accountability, s.influence
    paid = authorized and s.fund >= p.correction_cost
    bill = p.correction_cost if paid else zero
    profit_r = p.price - p.levy - p.renewal_cost
    profit_e = p.price - p.levy - p.liability * q - p.political_cost
    gap = profit_r - profit_e
    x_next = x + p.selection_rate * x * (1 - x) * gap
    w_next = ((1 - p.influence_turnover) * w
              + p.influence_turnover * p.influence_target * (1 - x))
    repair = p.restoration if paid else zero
    q_next = min(1, max(0, (1 - repair - p.capture * w) * q + repair - erosion))
    if freeze_rule:
        q_next = q
    before_cap = s.fund - bill + p.levy
    fund_next = min(p.fund_cap, before_cap)
    surplus = max(zero, before_cap - p.fund_cap)
    stocks = tuple(max(0, (1 - c.depreciation) * stock
                       + (c.renewal + c.depletion) * x
                       - c.depletion - c.background_harm - loss)
                   for c, stock, loss in zip(p.supports, s.supports, losses))
    operating = all(not c.essential or stock >= c.floor
                    for c, stock in zip(p.supports, stocks))
    nxt = State(x_next, q_next, w_next, fund_next, stocks, operating)
    ledger = {"paid": paid, "receipts": p.price, "levy": p.levy,
              "restoration_bill": bill, "surplus": surplus,
              "restitution": (1 - x) * p.liability * q,
              "political_bill": (1 - x) * p.political_cost,
              "renewal_bill": x * p.renewal_cost,
              "distributed_profit": x * profit_r + (1 - x) * profit_e,
              "profit_gap": gap}
    return nxt, ledger


def rectangle_margins(p, x_low, q_low, w_high, erosion_max, loss_max):
    """Signed sufficient-condition margins, independent of measured outcomes."""
    return {
        "selection": p.liability * q_low + p.political_cost - p.renewal_cost,
        "influence": w_high - p.influence_target * (1 - x_low),
        "accountability": p.restoration * (1 - q_low)
            - p.capture * w_high * q_low - erosion_max,
        "funding": p.levy - p.correction_cost,
        "supports": tuple((c.renewal + c.depletion) * x_low
                           - c.depletion - c.background_harm - loss
                           - c.depreciation * c.floor
                           for c, loss in zip(p.supports, loss_max)),
    }


def in_rectangle(p, s, x_low=F(3, 4), q_low=F(1, 2), w_high=F(1, 4)):
    return (s.operating and x_low <= s.renewers <= 1
            and q_low <= s.accountability <= 1 and 0 <= s.influence <= w_high
            and p.correction_cost <= s.fund <= p.fund_cap
            and all(v >= c.floor for v, c in zip(s.supports, p.supports)))
