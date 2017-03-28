import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 1)

def customize(ax):
    "Custom subplots with axes throught the origin"

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    
    return ax


x = np.linspace(-2, 2, 2)

for i, alpha in enumerate((0.2, 0)):
    ax = customize(axes[i])
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks((-0.4, 0.4))
    y = alpha * x
    label_string = r'$Tx = \alpha x$ with $\alpha = {}$'.format(alpha)
    ax.plot(x, y, '-', linewidth=2.5, label=label_string, alpha=0.4)
    ax.legend(loc='lower right')

plt.show()
