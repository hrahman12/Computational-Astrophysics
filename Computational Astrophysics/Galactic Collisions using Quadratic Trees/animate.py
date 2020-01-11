from tree import tree as tree
from initialization import make_galaxy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

G = 0.0044995611
dt = 1 # Myrs
universe_size = 50
theta = 1.
N = 50
chi = 10. #softening

bodies = make_galaxy(N,chi,G)


sys = tree(bodies, G, universe_size, dt, theta, chi)


fig, (ax) = plt.subplots(1,1)
ax.set_xlim(-universe_size/2., universe_size/2.)
ax.set_ylim(-universe_size/2., universe_size/2.)

ax.set_title('N =' + str(N))

points = ax.plot( *([[], []]*N), marker="o", color='black', markersize=1) #change the size

def init():
    for j in range(N):
        points[j].set_data([], [])
    return(points)

def update(n):
    i = n % 10000
    sys.advance(G)

    x = [body.x for body in sys.bodies]
    y = [body.y for body in sys.bodies]


    for j in range(len(x)):
        points[j].set_data(x[j],y[j])


ani = animation.FuncAnimation(fig, update, init_func=init, frames=10000, interval=1)
plt.show()
