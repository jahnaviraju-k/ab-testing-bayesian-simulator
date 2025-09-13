from __future__ import annotations
import numpy as np
from scipy.stats import beta as beta_dist

def beta_posterior(alpha0: float, beta0: float, successes: int, failures: int):
    return alpha0 + successes, beta0 + failures

def prob_b_better(alpha_a, beta_a, alpha_b, beta_b, draws: int = 100_000, seed: int | None=None):
    r = np.random.default_rng(seed)
    a = r.beta(alpha_a, beta_a, size=draws)
    b = r.beta(alpha_b, beta_b, size=draws)
    return float((b > a).mean())

def uplift_ci(alpha_a, beta_a, alpha_b, beta_b, q=(0.025, 0.975), draws=100_000, seed=None):
    r = np.random.default_rng(seed)
    a = r.beta(alpha_a, beta_a, size=draws)
    b = r.beta(alpha_b, beta_b, size=draws)
    uplift = (b - a) / np.maximum(a, 1e-9)
    return np.quantile(uplift, q)
