from objects import Body, Cell
import initialization

class tree:
  def __init__(self, bodies, G, universe_size, dt, theta, chi):

    self.bodies = bodies
    self.dt = dt
    self.theta = theta
    self.chi = chi
    self.G = G
    self.universe_size = universe_size

  def advance(self, G):

    origin = Cell(-self.universe_size, self.universe_size, -self.universe_size, self.universe_size)
    for body in self.bodies:
      origin.add(body)

    self.bodies = origin.bodies()

    for body in self.bodies:

      cells = [origin]
      while cells:

        cell = cells.pop()

        if cell.far_enough(body, self.theta, self.chi):
          if cell.n > 0:
            body.euler(cell, G, self.dt, self.chi)
        else:
          cells.extend(cell.children)
      body.position_step(self.dt)
