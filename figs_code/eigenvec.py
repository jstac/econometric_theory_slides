"""
Illustrates eigenvectors.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eig

from matplotlib import rc

rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


A = ((1, 2),
     (2, 1))
A = np.array(A)
evals, evecs = eig(A)
evecs = evecs[:,0], evecs[:,1]

fig, ax = plt.subplots()
# Set the axes through the origin
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')
ax.grid(alpha=0.4)
    
xmin, xmax = -3, 3
ymin, ymax = -3, 3
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
#ax.set_xticks(())
#ax.set_yticks(())

# Plot each eigenvector
for v, i in zip(evecs, (1, 2)):
    ax.annotate(r'', xy=v, xytext=(0, 0), 
                arrowprops=dict(facecolor='blue', 
                    shrink=0, 
                    alpha=0.6,
                    width=0.5))
    txt = r'$\mathbf x_{}$'.format(i)
    ax.text(v[0], v[1]+0.2, txt, fontsize=15)

# Plot the image of each eigenvector
for v, i in zip(evecs, (1, 2)):
    v = np.dot(A, v)
    ax.annotate(r'', xy=v, xytext=(0, 0), 
                arrowprops=dict(facecolor='red', 
                    shrink=0, 
                    alpha=0.6,
                    width=0.5))
    txt = r'$\mathbf A \mathbf x_{} = \lambda_{} \mathbf x_{}$'.format(i, i, i)
    ax.text(v[0]-0.3, v[1]-0.6, txt, fontsize=15)


# Plot the lines they run through
x = np.linspace(xmin, xmax, 3)
for v in evecs:
    a = v[1] / v[0]
    ax.plot(x, a * x, 'b-', lw=0.4)


plt.show()

