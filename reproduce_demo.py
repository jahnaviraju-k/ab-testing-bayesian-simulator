from __future__ import annotations
import json
from pathlib import Path
from abtest.simulate import sequential_stream
from abtest.decision import decide_bayes
from abtest.bayes import beta_posterior

CONFIG = {
    "true_cr_a": 0.050,
    "true_cr_b": 0.055,
    "chunk": 200,
    "max_n": 10000,
    "prior_alpha": 1.0,
    "prior_beta": 1.0,
    "decision_threshold": 0.95,
    "seed": 42,
}

def main():
    steps = []
    decision_payload = None
    for i, s in enumerate(
        sequential_stream(
            CONFIG["true_cr_a"],
            CONFIG["true_cr_b"],
            chunk=CONFIG["chunk"],
            max_n=CONFIG["max_n"],
            seed=CONFIG["seed"],
        ),
        start=1,
    ):
        d = decide_bayes(
            s["succ_a"], s["fail_a"], s["succ_b"], s["fail_b"],
            prior=(CONFIG["prior_alpha"], CONFIG["prior_beta"]),
            prob_win=CONFIG["decision_threshold"],
            seed=CONFIG["seed"],
        )
        # Keep a compact trace to make diffs small
        steps.append({
            "step": i,
            "n_a": s["n_a"], "n_b": s["n_b"],
            "succ_a": s["succ_a"], "succ_b": s["succ_b"],
            "p_win": round(d["p_win"], 6),
            "uplift_ci": [round(d["uplift_ci"][0], 6), round(d["uplift_ci"][1], 6)],
            "decision": d["decision"],
        })
        if d["decision"] != "keep_running":
            decision_payload = d
            break

    result = {
        "config": CONFIG,
        "final_step": steps[-1]["step"],
        "final_state": steps[-1],
        "decision": decision_payload or {"decision": "keep_running"},
    }

    out_dir = Path(__file__).parent
    (out_dir / "last_run.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
