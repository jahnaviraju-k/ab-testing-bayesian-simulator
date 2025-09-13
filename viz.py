import matplotlib.pyplot as plt
import numpy as np

def plot_posterior(alpha, beta, title="Posterior"):
    x = np.linspace(0.0001, 0.9999, 500)
    from scipy.stats import beta as beta_dist
    y = beta_dist.pdf(x, alpha, beta)
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("Conversion rate"); plt.ylabel("Density")
    return plt.gcf()
