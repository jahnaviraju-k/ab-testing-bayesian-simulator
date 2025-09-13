from abtest.bayes import beta_posterior, prob_b_better
def test_beta_update():
    a,b = beta_posterior(1,1,10,90)
    assert (a,b) == (11,91)

def test_prob_b_better_monotonic():
    p = prob_b_better(11,91,12,90, draws=10_000, seed=0)
    assert 0.4 < p < 0.7
