from numpy import sqrt, sin, cos, arccos, pi
from random import random, randint
from objects import Body


def make_galaxy(N, a, G):
  x = []
  y = []
  vx = []
  vy = []
  accepted = 0
  while accepted < N:

    radius = a / sqrt(random()**(-1/3) - 1)

    x1 = random()
    y1 = random()*0.1
    if y1 < x1**2 * (1-x1**2)**3.5:
      accepted += 1
      v = x1 * sqrt(2*G*N)*(radius**2+a**2)**(-0.25)

      beta = random()*2*pi
      theta = arccos(random() * 2 - 1)
      x.append(radius*sin(theta)*cos(beta))
      y.append(radius*sin(theta)*sin(beta))

      beta = random()*2*pi
      theta = arccos(random() * 2 - 1)
      vx.append(v*sin(theta)*cos(beta))
      vy.append(v*sin(theta)*sin(beta))

      masses = [randint(1,2) for i in range(N)]
  return [Body(x[i], y[i], vx[i], vy[i], masses[i]) for i in range(N)]
