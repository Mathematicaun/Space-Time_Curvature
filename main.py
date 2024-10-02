  import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.animation import FuncAnimation
do = 1e-6
def length_x(t1, o):
    return -np.sqrt(5**2-t1**2)+5+o

def length_y(t1, o):
    return -np.sqrt(5**2-t1**2)+5+o
    
to = 2*np.pi
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
i = np.linspace(0, to, 10**3)
t1, t2 = np.meshgrid(i, 10/to*(i-0)-5)
path1, path2 = 10*i, -10/to*(i-to/2)

def simualtion(t):
    def X(j1, j2):
        return np.cos(j1)*length_x(j2, 3/10*(t+5))
    def Y(j1, j2):
        return np.sin(j1)*length_y(j2, 3/10*(t+5))
    def Z(j2):
        return j2
    
    def dX(j1, j2):
        return (X(j1+do, j2+do)-X(j1, j2))/do
    def dY(j1, j2):
        return (Y(j1+do, j2+do)-Y(j1, j2))/do
    def dZ(j2):
        return (Z(j2+do)-Z(j2))/do
    
    predicted_mag = np.sqrt(dX(path1, path2)**2 + dY(path1, path2)**2 + dZ(path2)**2)
    norm = Normalize(predicted_mag.min(), predicted_mag.max())
    j1, j2 = 10*to/10*(t+5), -t
    mag = np.sqrt(dX(j1, j2)**2 + dY(j1, j2)**2 + dZ(j2)**2)
    color = plt.get_cmap('plasma')(norm(mag))
    
    ax.clear()
    plt.title("The Space-Time Curvature", fontsize=25, color='#a73b3c', family='serif')
    ax.plot(X(path1, path2), Y(path1, path2), Z(path2), color='#ffcd02')
    ax.quiver(0, 0, 0, X(j1, j2), Y(j1, j2), Z(j2), arrow_length_ratio=.1, color='#a83a3a')
    ax.quiver(X(j1, j2), Y(j1, j2), Z(j2), dX(j1, j2)/mag, dY(j1, j2)/mag, dZ(j2)/mag, color=color)
    # ax.scatter(X(j1, j2), Y(j1, j2), Z(j2), s=40, color='black')
    ax.set(xlim=[-5, 5], ylim=[-5, 5], zlim=[-5, 5])
    # ax.plot_surface(X(t1, t2), Y(t1, t2), Z(t2), edgecolor='black', color='#ad7ac5', alpha=.1, linewidth=.1)
    
ani = FuncAnimation(fig, simualtion, frames=np.linspace(-5, 5, 10**2+300), interval=0, blit=0)
plt.show()
