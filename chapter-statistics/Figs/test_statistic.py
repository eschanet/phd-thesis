import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from matplotlib import rc

rc_fonts = {
    "font.family": "serif",
    "font.size": 13,
    "text.usetex": True,
    'text.latex.preview': True,
    'text.latex.preamble': [
        r"""
        \usepackage{libertine}
        \usepackage[libertine]{newtxmath}
        """],
}

plt.rcParams.update(rc_fonts)

x = np.linspace(-8, 0, 5000)
mu1 = -3.8
sigma1 = 1

mu2 = -4.2
sigma2 = 1.05

y1 = stats.norm(mu1, sigma1)
y2 = stats.norm(mu2, sigma2)

fig, ax = plt.subplots()
fig.set_figheight(3)
fig.set_figwidth(4)

p1, = ax.plot(x, y1.pdf(x),label='$f(\\tilde{q}_\\mu\\vert 0)$')
p2, = ax.plot(x, y2.pdf(x),label='$f(\\tilde{q}_\\mu\\vert 1)$')

lim = -2.2
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

ax.vlines(x=lim, ymin=0, ymax=0.3, color="black")
ax.text(-1.9, 0.28, '$\\tilde{q}_{\\mu,\\mathrm{obs}}$', fontsize=13)


# ax.annotate(
#     "",
#     xy=(-4.2, 0.4),
#     xycoords="data",
#     xytext=(-0.8, 0.1),
#     textcoords="data",
#     arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
# )

ax.legend(loc='upper left',bbox_to_anchor=(0, 1.03), handletextpad=0.5,labelspacing=0.4, frameon=False,
          ncol=1, fancybox=False, shadow=False)
ax.tick_params(direction="in",which='both',length=4)

ax.set_ylim(ymin=0, ymax=0.5)
ax.set_ylabel("$f(\\tilde{q}_\\mu)$")
ax.set_xlabel("$\\tilde{q}_\\mu$")

fig.tight_layout()
fig.savefig("cls_1.pdf")
