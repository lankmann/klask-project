import math

class Vector:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __add__(self, o):
    return Vector(self.x + o.x, self.y + o.y)

  def __sub__(self, o):
    return Vector(self.x - o.x, self.y - o.y)

  def __mul__(self, *args):
    if type(args[0]) == Vector:
      return Vector(self.x * args[0].x, self.y * args[0].y)
    else:
      return Vector(self.x * args[0], self.y * args[0])
    
  def __truediv__(self, *args):
    if type(args[0]) == Vector:
      return Vector(self.x / args[0].x, self.y / args[0].y)
    elif args[0] != 0:
      return Vector(self.x / args[0], self.y / args[0])
    
  def __getitem__(self, key):
      if key == 0:
        return self.x
      else:
        return self.y
      
  def toTuple(self):
    return (self.x, self.y)
  
  def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y
  
  def normalize(self):
    mag = self.mag()
    if mag != 0:
      self.x /= mag
      self.y /= mag
  
  def mag(self):
    return math.sqrt(self.x ** 2 + self.y ** 2)