import streamlit as st
from abtest.simulate import sequential_stream
from abtest.bayes import beta_posterior
from abtest.decision import decide_bayes
from abtest.viz import plot_posterior

st.set_page_config(page_title="Bayesian A/B Simulator", layout="wide")
st.title("A/B Testing Simulator (Bayesian + Frequentist)")

col = st.sidebar
p_a = col.number_input("True CR of A", value=0.05, min_value=0.0, max_value=1.0, step=0.001)
p_b = col.number_input("True CR of B", value=0.055, min_value=0.0, max_value=1.0, step=0.001)
chunk = col.number_input("Chunk size", value=100, min_value=10, step=10)
max_n = col.number_input("Max samples per arm", value=10000, min_value=100, step=100)
alpha0 = col.number_input("Prior alpha", value=1.0, min_value=0.1, step=0.1)
beta0  = col.number_input("Prior beta",  value=1.0, min_value=0.1, step=0.1)
prob_win = col.slider("Decision threshold (P(B>A))", 0.5, 0.99, 0.95, 0.01)

placeholder = st.empty()
for step, s in enumerate(sequential_stream(p_a, p_b, chunk=chunk, max_n=max_n, seed=42), start=1):
    d = decide_bayes(s["succ_a"], s["fail_a"], s["succ_b"], s["fail_b"],
                     prior=(alpha0, beta0), prob_win=prob_win, seed=42)
    with placeholder.container():
        st.subheader(f"Step {step} — nA={s['n_a']}, nB={s['n_b']}")
        st.markdown(f"**P(B > A)** = {d['p_win']:.3f} | CI uplift = [{d['uplift_ci'][0]:.3%}, {d['uplift_ci'][1]:.3%}]")
        st.info(f"Decision: **{d['decision']}**")
        a1,a2 = beta_posterior(alpha0, beta0, s["succ_a"], s["fail_a"])
        b1,b2 = beta_posterior(alpha0, beta0, s["succ_b"], s["fail_b"])
        c1, c2 = st.columns(2)
        with c1: st.pyplot(plot_posterior(a1, a2, "Posterior A"))
        with c2: st.pyplot(plot_posterior(b1, b2, "Posterior B"))
    if d["decision"] != "keep_running":
        break
