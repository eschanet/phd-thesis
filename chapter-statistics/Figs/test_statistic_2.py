import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from matplotlib import rc

rc("font", **{"size":12,"family": "serif", "serif": ["Computer Modern"]})
rc("text", usetex=True)

lim = -44
x = np.linspace(-80, 0, 5000)
mu1 = -28
sigma1 = 7
mu2 = -52
sigma2 = 8

y1 = stats.norm(mu1, sigma1)
y2 = stats.norm(mu2, sigma2)

fig, ax = plt.subplots()
fig.set_figheight(3)
fig.set_figwidth(4)

p1, = ax.plot(x, y1.pdf(x),label='$f(\\tilde{q}_\\mu\\vert 0)$')
p2, = ax.plot(x, y2.pdf(x),label='$f(\\tilde{q}_\\mu\\vert 1)$')

mx = x[np.where(x < lim)]
px = x[np.where(x > lim)]
ax.fill_between(
    mx,
    y1.pdf(mx),
    color="cornflowerblue",
    alpha=0.5,
    linewidth=0,
)

ax.fill_between(
    px,
    y2.pdf(px),
    color="orange",
    alpha=0.5,
    linewidth=0,
)

ax.vlines(x=lim, ymin=0, ymax=0.06, color="black")
ax.text(-42, 0.055, '$\\tilde{q}_{\\mu,\\mathrm{obs}}$', fontsize=13)


# ax.annotate(
#     "",
#     xy=(-4.2, 0.4),
#     xycoords="data",
#     xytext=(-0.8, 0.1),
#     textcoords="data",
#     arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
# )

ax.legend(loc='upper left',
          ncol=1, fancybox=False, shadow=False)

ax.set_ylim(ymin=0, ymax=0.075)
ax.set_ylabel("$f(\\tilde{q}_\\mu)$")
ax.set_xlabel("$\\tilde{q}_\\mu$")

fig.tight_layout()
fig.savefig("cls_2.pdf")
