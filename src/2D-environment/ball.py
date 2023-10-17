from physicsBall import PhysicsBall
import pygame as pg

class Ball(PhysicsBall):
  def __init__(self, x, y) -> None:
    ball_radius = 0.9
    ball_mass = 0.25
    ball_elasticity = 0.7
    ball_drag = 0.99
    super().__init__(x, y, ball_radius, ball_mass, ball_elasticity, ball_drag)

  def display(self, surface, screen):
    color = (255, 255, 0)
    position = screen.worldToScreen(self.pos).toTuple()
    radius = screen.worldToScreen(self.radius)
    pg.draw.circle(surface, color, position, radius)