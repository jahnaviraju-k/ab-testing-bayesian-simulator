# A/B Testing Simulator (Bayesian + Frequentist)

Simulate A/B tests with Bayesian inference and frequentist z-tests. Includes a Streamlit app for interactive demos.

## Features
- Bernoulli trial simulation
- Bayesian updating (Beta-Binomial)
- Posterior visualization
- Credible intervals for uplift
- Decision rules (ship A, ship B, keep running, no diff)
- Streamlit dashboard

## Quickstart
```bash
pip install -r requirements.txt
export PYTHONPATH=./src
streamlit run app/streamlit_app.py
```

## Example
```bash
python - <<'PY'
from abtest.simulate import bernoulli_ab
from abtest.decision import decide_bayes
sa,fa,sb,fb = bernoulli_ab(5000,0.05,5000,0.055,seed=7)
print(decide_bayes(sa,fa,sb,fb, prior=(1,1), prob_win=0.95))
PY
```

## License
MIT
