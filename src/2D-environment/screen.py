from vector import Vector

scale = 1000 / 45

class Screen:
  width = 0
  height = 0

  def __init__(self, width, height) -> None:
    self.dimensions = Vector(width, height)
    self.width = width
    self.height = height
    Screen.width = width
    Screen.height = height

  def worldToScreen(self, *args):
    if len(args) == 0:
      return self.dimensions * scale
    elif len(args) == 1:
      return args[0] * scale
    else:
      return Vector(args[0] * scale, args[1] * scale)
  
  def screenToWorld(self, *args):
    if len(args) == 1:
      return args[0] / scale
    else:
      return Vector(args[0] / scale, args[1] / scale)
