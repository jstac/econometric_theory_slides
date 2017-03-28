
import matplotlib.pyplot as plt
import numpy as np


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

a, b = 1, -2
c, d = 1, -2


xmin, xmax = -20, 20
fig, ax = subplots()  # Call the local version, not plt.subplots()
ax.set_xlim(xmin, xmax)
x = np.linspace(xmin, xmax, 200)
ax.set_ylim(xmin, xmax)


ax.plot(x, -2 + 2 * x, 'b-', lw=2, alpha=0.6)

plt.show()
