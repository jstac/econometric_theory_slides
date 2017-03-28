import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp2d

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

# Set up

c1, c2 = 0.4, -0.5

# Fixed linear function, to generate a plane

def f(x, y):
    return c1 * x + c2 * y

x_min, x_max = -10, 10
y_min, y_max = -10, 10

gs = 3
z = np.linspace(x_min, x_max, gs)
x = np.zeros(gs)
y = np.zeros(gs)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.set_xlim((x_min, x_max))
ax.set_ylim((x_min, x_max))
ax.set_zlim((x_min, x_max))

# Add axes
ax.set_xticks((0,))
ax.set_yticks((0,))
ax.set_zticks((0,))
ax.plot(x, y, z, 'k-', lw=1, alpha=0.5)
ax.plot(z, x, y, 'k-', lw=1, alpha=0.5)
ax.plot(y, z, x, 'k-', lw=1, alpha=0.5)

# Draw the plane
grid_size = 2
xr2 = np.linspace(x_min, x_max, grid_size)
yr2 = np.linspace(y_min, y_max, grid_size)
x2, y2 = np.meshgrid(xr2, yr2)
z2 = f(x2, y2)
ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=True, alpha=0.4)

plt.show()


