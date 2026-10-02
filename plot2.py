import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, np.exp(x), "r-", label=r"$\exp(x)$")

ax.set(
    xlim=(0, 2 * np.pi),
    ylim=(-0.2, None),
    xlabel=(r"$x$")
)

ax.legend()
fig.savefig("plot2.pdf")
