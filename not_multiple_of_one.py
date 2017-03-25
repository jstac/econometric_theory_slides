import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Set the axes through the origin
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')
    
xmin, xmax = -2, 2
ax.set_xlim(xmin, xmax)
ax.set_ylim(xmin, xmax)
ax.grid()

v = (1.2, -0.6)
ax.annotate('', xy=v, xytext=(0, 0), 
            arrowprops=dict(facecolor='blue', 
                shrink=0, 
                alpha=0.7,
                width=0.5))
ax.text(1.1 * v[0], 1.1 * v[1], r'$(b, -d)$', fontsize=16)

v = (1, 1)
ax.annotate('', xy=v, xytext=(0, 0), 
            arrowprops=dict(facecolor='blue', 
                shrink=0, 
                alpha=0.7,
                width=0.5))

# Plot the lines they run through
x = np.linspace(xmin, xmax, 3)
a = v[1] / v[0]
ax.plot(x, a * x, 'b-', lw=0.8)


plt.show()

