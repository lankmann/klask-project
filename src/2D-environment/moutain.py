from physicsBall import PhysicsBall
import pygame as pg

class Mountain(PhysicsBall):
  def __init__(self, x, y) -> None:
    mountain_radius = 0.5
    mountain_mass = 0.1
    mountain_elasticity = 0.7
    mountain_drag = 0.99
    super().__init__(x, y, mountain_radius, mountain_mass, mountain_elasticity, mountain_drag)

  def display(self, surface, screen):
    color = (255, 255, 255)
    position = screen.worldToScreen(self.pos).toTuple()
    radius = screen.worldToScreen(self.radius)
    pg.draw.circle(surface, color, position, radius)