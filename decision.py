from __future__ import annotations
from .bayes import beta_posterior, prob_b_better, uplift_ci

def decide_bayes(succ_a, fail_a, succ_b, fail_b,
                 prior=(1.,1.), prob_win=0.95, rope=(-0.01, 0.01), seed=None):
    a1, a2 = beta_posterior(prior[0], prior[1], succ_a, fail_a)
    b1, b2 = beta_posterior(prior[0], prior[1], succ_b, fail_b)
    p_win = prob_b_better(a1, a2, b1, b2, seed=seed)
    lo, hi = uplift_ci(a1, a2, b1, b2, seed=seed)
    decision = "keep_running"
    if p_win >= prob_win and lo > rope[1]:
        decision = "ship_B"
    elif (1 - p_win) >= prob_win and hi < rope[0]:
        decision = "ship_A"
    elif lo >= rope[0] and hi <= rope[1]:
        decision = "no_material_difference"
    return dict(p_win=p_win, uplift_ci=(float(lo), float(hi)), decision=decision)
