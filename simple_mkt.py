

import matplotlib.pyplot as plt
import numpy as np

a, b, c, d = 5, 2, 1, 1.5


def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    ax.grid()
    return fig, ax

xmin, xmax = -3, 5
fig, ax = subplots()  # Call the local version, not plt.subplots()
ax.set_xlim(xmin, xmax)
x = np.linspace(xmin, xmax, 3)
ax.set_ylim(xmin, xmax)

ax.plot(x, a - b * x, 'b-', lw=2, alpha=0.6, label=r'$q = 5 - 2p$')
ax.plot(x, c + d * x, 'g-', lw=2, alpha=0.6, label='$q = 1 + 1.5p$')

q, p = 2.7142857142, 1.142857142
ax.text(1.2*p, q, r'$(q^*, \, p^*)$', fontsize=14) 
ax.plot([p], [q],  'ko', alpha=0.6)


ax.legend(loc='upper left')
plt.show()
