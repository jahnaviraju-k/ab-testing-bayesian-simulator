from abtest.simulate import bernoulli_ab
def test_sim_counts():
    sa,fa,sb,fb = bernoulli_ab(1000,0.05,1000,0.06,seed=1)
    assert sa+fa == 1000 and sb+fb == 1000
