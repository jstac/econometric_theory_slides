import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp2d

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

# Set up

alpha, beta = 0.4, 0.2

# Fixed linear function, to generate a plane

def f(x, y):
    return alpha * x + beta * y

x_min, x_max = -10, 10
y_min, y_max = -10, 10

gs = 3
z = np.linspace(x_min, x_max, gs)
x = np.zeros(gs)
y = np.zeros(gs)

x_coords = np.array((3, 3))
y_coords = np.array((4, -4))
z_coords = f(x_coords, y_coords)

fig = plt.figure(figsize=plt.figaspect(0.5))

def setup(ax):
    ax.set_xlim((x_min, x_max))
    ax.set_ylim((x_min, x_max))
    ax.set_zlim((x_min, x_max))

    # Add vector text
    for i in (0, 1):
        ax.text(x_coords[i], y_coords[i], z_coords[i], r'$\mathbf x_{}$'.format(i+1), fontsize=16)

    # Add axes
    ax.set_xticks((0,))
    ax.set_yticks((0,))
    ax.set_zticks((0,))
    ax.plot(x, y, z, 'k-', lw=1, alpha=0.5)
    ax.plot(z, x, y, 'k-', lw=1, alpha=0.5)
    ax.plot(y, z, x, 'k-', lw=1, alpha=0.5)

    # Draw lines to vectors
    for i in (0, 1):
        xx = (0, x_coords[i])
        yy = (0, y_coords[i])
        zz = (0, f(x_coords[i], y_coords[i]))
        ax.plot(xx, yy, zz, 'b-', lw=2, alpha=0.8)


# First plot
ax = fig.add_subplot(1, 2, 1, projection='3d')
setup(ax)


# Second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')
setup(ax)

# Draw the plane
grid_size = 2
xr2 = np.linspace(x_min, x_max, grid_size)
yr2 = np.linspace(y_min, y_max, grid_size)
x2, y2 = np.meshgrid(xr2, yr2)
z2 = f(x2, y2)
ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.gray,
        linewidth=0, antialiased=True, alpha=0.6)

plt.show()


