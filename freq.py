from __future__ import annotations
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

def two_prop_ztest(succ_a, n_a, succ_b, n_b, alternative="larger"):
    count = np.array([succ_b, succ_a])
    nobs = np.array([n_b, n_a])
    stat, p = proportions_ztest(count, nobs, alternative=alternative)
    return float(stat), float(p)
