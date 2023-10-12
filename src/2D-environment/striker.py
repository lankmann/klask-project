from physicsBall import PhysicsBall
import pygame as pg
from vector import Vector

class Striker(PhysicsBall):
  def __init__(self, x, y) -> None:
    striker_radius = 1
    striker_mass = 1
    striker_elasticity = 0.7
    striker_drag = 0.92
    self.movement = Vector(0, 0)
    super().__init__(x, y, striker_radius, striker_mass, striker_elasticity, striker_drag)

  def display(self, surface, screen):
    color = (0, 0, 0)
    position = screen.worldToScreen(self.pos).toTuple()
    radius = screen.worldToScreen(self.radius)
    pg.draw.circle(surface, color, position, radius)
    
  def track(self, pos: Vector):
    target_velocity = pos - self.pos
    self.move(target_velocity)

  def move(self, target_velocity: Vector):
    acceleration = 0.08
    movement = target_velocity - self.vel
    movement.normalize()
    self.vel += movement * acceleration