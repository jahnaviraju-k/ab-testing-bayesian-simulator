# A/B Testing Bayesian Simulator

I built this project to explore how experimentation guides real product decisions in data-driven companies. Instead of stopping at simple statistical tests, I wanted to understand and demonstrate how Bayesian methods, frequentist baselines, and clear decision rules can come together in a realistic workflow.

The result is an A/B Testing Simulator with a Streamlit dashboard that allows anyone to run simulated experiments, track probabilities in real time, and see when a decision can confidently be made.

## What This Project Is

This project is a hands-on implementation of how A/B tests are actually used in practice:

A simulator that generates conversion outcomes for two competing variants.

A Bayesian updating process (Beta–Binomial) that produces posteriors as data accumulates.

A frequentist z-test baseline for comparison.

Decision rules that translate statistical evidence into actions: launch A, launch B, keep testing, or conclude no meaningful difference.

An interactive dashboard that makes the entire process transparent step by step.

## How I Built It

I started with the idea of simulating Bernoulli outcomes for two variants, similar to how an experiment would record conversions in real time. From there:

Simulation engine – I wrote functions to generate data in sequential chunks, letting me mimic how experiments unfold over time.

Bayesian model – Each chunk updates the posterior distribution for A and B. This let me calculate the probability that B outperforms A at every step.

Decision logic – I created a rule set that translates probabilities and credible intervals into actionable outcomes, reducing uncertainty for decision-makers.

Interactive dashboard – I built a Streamlit app so users can adjust parameters (true rates, priors, thresholds) and watch the experiment play out visually.

Reproducibility – I added a verification script that replays the exact scenario used in the demo, producing a JSON summary that anyone can compare against.

## Why This Matters

Product experimentation is not just about running a test; it is about making business decisions with incomplete information. This project shows that I can:

Apply Bayesian inference to real decision problems.

Balance statistical rigor with engineering reproducibility.

Communicate results in a way that is transparent and actionable for non-technical stakeholders.

It highlights my ability to bridge data science, engineering, and business impact—exactly what’s expected in analyst, data engineer, or product analytics roles.

## Demonstration

The dashboard shows posteriors for both variants updating as more data is collected. Uncertainty decreases, and once the probability of B outperforming A passes the threshold, the decision automatically changes from keep running to ship B.

## Reproduce the Demo

To prove the demonstration is reproducible, I fixed the following configuration:

True conversion rate of A: 0.050

True conversion rate of B: 0.055

Sample intake per step: 200 observations per arm

Prior: Beta(1.0, 1.0) for both arms

Decision threshold: P(B > A) ≥ 0.95

Random seed: 42

With these settings you will observe:

The posterior for B shifts to the right of A.

The probability P(B > A) steadily increases and eventually crosses 0.95.

The decision changes from keep running to ship B.

## To reproduce:
```bash
export PYTHONPATH=./src
python examples/reproduce_demo.py
```

This will generate a JSON file (examples/last_run.json) that contains the final state and decision. 
## Try It Yourself

You can run the full interactive dashboard locally:
```bash
git clone https://github.com/jahnaviraju-k/ab-testing-bayesian-simulator.git
cd ab-testing-bayesian-simulator
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=./src
streamlit run app/streamlit_app.py
```

This opens the Streamlit interface where you can adjust parameters and watch how the results change.
