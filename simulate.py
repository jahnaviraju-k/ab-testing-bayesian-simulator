from __future__ import annotations
import numpy as np
rng = np.random.default_rng()

def bernoulli_ab(n_a: int, p_a: float, n_b: int, p_b: float, seed: int | None = None):
    r = np.random.default_rng(seed)
    a = r.binomial(1, p_a, size=n_a)
    b = r.binomial(1, p_b, size=n_b)
    return a.sum(), n_a - a.sum(), b.sum(), n_b - b.sum()

def sequential_stream(p_a: float, p_b: float, chunk: int = 100, max_n: int = 100_000, seed: int | None=None):
    r = np.random.default_rng(seed)
    seen_a = seen_b = succ_a = succ_b = 0
    while seen_a < max_n or seen_b < max_n:
        da = r.binomial(1, p_a, size=chunk)
        db = r.binomial(1, p_b, size=chunk)
        succ_a += da.sum(); succ_b += db.sum()
        seen_a += da.size;  seen_b += db.size
        yield dict(succ_a=succ_a, fail_a=seen_a - succ_a, succ_b=succ_b, fail_b=seen_b - succ_b,
                   n_a=seen_a, n_b=seen_b)
