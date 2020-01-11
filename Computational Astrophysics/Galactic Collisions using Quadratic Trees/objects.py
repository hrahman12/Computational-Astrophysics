import math

class Body:
  def __init__(self, x, y, vx, vy, mass):
    self.x, self.y = x, y
    self.vx, self.vy = vx, vy
    self.mass = mass

  def dist(self, cell):
    dx = cell.xcen - self.x
    dy = cell.ycen - self.y
    return (dx*dx + dy*dy , dx, dy)

  def euler(self, cell, G, dt, chi):
    r2, dx, dy = self.dist(cell)

    if r2 > chi*chi:
        fx = G * dt * cell.mass / r2
        fy = G * dt * cell.mass / r2
        self.vx += fx * (dx / math.sqrt(r2))
        self.vy += fy * (dy / math.sqrt(r2))
    else:
        r = r2/2.
        x = r / chi
        f = x * (8 - 9 * x + 2 * x * x * x)
        self.vx += G * dt * f * dx * cell.mass / (chi*chi*r)
        self.vy += G * dt * f * dy * cell.mass / (chi*chi*r)


  def position_step(self, dt):
    self.x += self.vx * dt
    self.y += self.vy * dt

class Cell:
  def __init__(self, xmin, xmax, ymin, ymax):
    self.xmin, self.xmax = xmin, xmax
    self.ymin, self.ymax = ymin, ymax
    self.n = 0
    self.xcen, self.ycen = 0, 0
    self.children = []
    self.body = None
    self.mass = 0

  def inside(self, body):
    if body.x > self.xmin and body.x <= self.xmax and body.y > self.ymin and body.y <= self.ymax:
      return True
    else:
      return False

  def add(self, body):
     if not self.inside(body):
       return


     if self.n > 0:

       if self.n == 1:
         self.makechildren()
         for child in self.children:
           child.add(self.body)
         self.body = None

       for child in self.children:
         child.add(body)

     else:
       self.body = body

     self.xcen = (self.mass * self.xcen + body.x) / float(self.mass + 1)
     self.ycen = (self.mass * self.ycen + body.y) / float(self.mass + 1)
     self.mass += body.mass

     self.n += 1

  def makechildren(self):
    xhalf = (self.xmin + self.xmax) / 2.
    yhalf = (self.ymin + self.ymax) / 2.
    SW = Cell(self.xmin, xhalf, self.ymin, yhalf)
    SE = Cell(xhalf, self.xmax, self.ymin, yhalf)
    NW = Cell(self.xmin, xhalf, yhalf, self.ymax)
    NE = Cell(xhalf, self.xmax, yhalf, self.ymax)
    self.children = [SW, SE, NW, NE]


  def bodies(self):
    if self.body:
      return [self.body]

    elif self.children:
      body_list = []
      for child in self.children:
        body_list.extend(child.bodies())
      return body_list
    else:
      return []

  def far_enough(self, body, theta, chi):

     if self.children:
       s = self.xmax - self.xmin
       dx = body.x - self.xcen
       dy = body.y - self.ycen
       d  = (dx*dx + dy*dy)**0.5

       return (d/s) > theta and d>chi

     else:
       return self.body != body
