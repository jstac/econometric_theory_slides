import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

# == Pair 1 == #
xvec = (3, 4, 2)
yvec = (3, -4, 1)
uvec = (-3, 4, -1)

# == Pair 2 == #
#xvec = (1, 4, 2)
#yvec = (-3, -4, -1)


# == Linear function, to generate a plane == #
a1, a2, a3 = np.cross(xvec, yvec)
def f(s, t):
    return (- s * a1 - t * a2) / a3

# == Set up plot == #
x_min, x_max = -10, 10
y_min, y_max = -10, 10
gs = 3
z = np.linspace(x_min, x_max, gs)
x = np.zeros(gs)
y = np.zeros(gs)

# Vector coordinates
x_coords = np.array((xvec[0], yvec[0], uvec[0]))
y_coords = np.array((xvec[1], yvec[1], uvec[1]))
z_coords = np.array((xvec[2], yvec[2], uvec[2]))

fig = plt.figure(figsize=plt.figaspect(0.6))



# First plot
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Set limits
ax.set_xlim((x_min, x_max))
ax.set_ylim((x_min, x_max))
ax.set_zlim((x_min, x_max))

# View angle
ax.view_init(elev=45, azim=-105)


# Add axes
ax.set_xticks((0,))
ax.set_yticks((0,))
ax.set_zticks((0,))
ax.plot(x, y, z, 'k-', lw=1, alpha=0.5)
ax.plot(z, x, y, 'k-', lw=1, alpha=0.5)
ax.plot(y, z, x, 'k-', lw=1, alpha=0.5)

# Add vector text
for i in (0, 1, 2):
    ax.text(x_coords[i], y_coords[i], z_coords[i], r'$\mathbf a_{}$'.format(i+1), fontsize=16)

# Draw lines to vectors
for i in (0, 1, 2):
    xx = (0, x_coords[i])
    yy = (0, y_coords[i])
    zz = (0, z_coords[i])
    ax.plot(xx, yy, zz, 'b-', lw=2, alpha=0.8)
    
# Draw a dot representing b
b = (-4, -4, 8)
ax.plot([b[0]], [b[1]], [b[2]], 'ro', alpha=0.8)
ax.text(b[0], b[1], 1.1*b[2], r'$\mathbf b$', fontsize=16)


# Then draw plane 
grid_size = 2
xr2 = np.linspace(x_min, x_max, grid_size)
yr2 = np.linspace(y_min, y_max, grid_size)
x2, y2 = np.meshgrid(xr2, yr2)
z2 = f(x2, y2)
ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap=cm.gray,
        linewidth=0, antialiased=True, alpha=0.3)



plt.show()


