# Experimentation Overview (Bayesian + Frequentist)

## Problem Framing
We simulate a binary conversion experiment comparing two variants (A and B). At each step, new observations arrive and we update our beliefs and our decision.

## Data-Generating Process
- Each arm is modeled as Bernoulli with true conversion rates `p_A` and `p_B`.
- We stream observations in fixed-size chunks to enable sequential monitoring.

## Bayesian Model (Beta–Binomial)
- Prior: `Beta(alpha0, beta0)` on each arm’s conversion rate.
- Posterior update after observing `successes` and `failures`: `Beta(alpha0 + successes, beta0 + failures)`.
- Probability of B outperforming A: sample from both posteriors and compute `P(b > a)`.

## Credible Intervals for Uplift
- Define uplift = `(b - a) / max(a, ε)` and compute a credible interval via posterior sampling.
- We use this to detect “no material difference” when the interval lies fully inside a small ROPE (region of practical equivalence).

## Decision Rule
At each checkpoint we compute:
- `P(B > A)` (probability B wins)
- Credible interval for uplift
Then output one of four outcomes:
1. **ship_B** — if `P(B > A)` exceeds the threshold and the lower bound of uplift is above the ROPE.
2. **ship_A** — symmetric condition in favor of A.
3. **no_material_difference** — if the uplift CI lies entirely within the ROPE.
4. **keep_running** — otherwise collect more data.

The decision threshold tunes risk: higher thresholds reduce false “ships” but increase required sample size.

## Sequential Monitoring
Because Bayesian inference produces a full posterior at each step, we can monitor the experiment sequentially with the same decision threshold. This avoids the alpha-spending complications of repeated looks in a fixed-horizon frequentist design.

## Frequentist Baseline
We also provide a two-proportion z-test as a reference for practitioners who want to compare classical p-values with Bayesian probabilities.

## Reproducibility
- Deterministic seeds for streams and sampling.
- A small verification script (`examples/reproduce_demo.py`) that prints a single JSON payload summarizing the run.
- Unit tests for posterior updates and simulation bookkeeping.
- CI to run tests on a clean environment.

## Interpreting Outputs
- `p_win`: the posterior probability that B’s conversion rate exceeds A’s.
- `uplift_ci`: a credible interval for relative improvement.
- `decision`: the recommended action for the current evidence level.

## Limitations and Extensions
- Bernoulli outcomes and independent arms; does not include covariates or time trends.
- Extensions: multi-variant tests, profit-aware decisions, hierarchical pooling by segment, bandit-style allocation.
