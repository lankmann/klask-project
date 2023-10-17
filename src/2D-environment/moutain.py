from physicsBall import PhysicsBall
import pygame as pg
from striker import Striker
from vector import Vector

class Mountain(PhysicsBall):
  def __init__(self, x, y) -> None:
    mountain_radius = 0.5
    mountain_mass = 0.1
    mountain_elasticity = 0.7
    mountain_drag = 0.9
    self.stuck = None
    self.stuck_offset = Vector(0, 0)
    super().__init__(x, y, mountain_radius, mountain_mass, mountain_elasticity, mountain_drag)

  def display(self, surface, screen):
    color = (255, 255, 255)
    position = screen.worldToScreen(self.pos).toTuple()
    radius = screen.worldToScreen(self.radius)
    pg.draw.circle(surface, color, position, radius)

  def applyMagneticForce(self, strikers: list[Striker]):
    for striker in strikers:
      if self.stuck == striker:
        self.pos = striker.pos + self.stuck_offset
        self.vel.set(0, 0)
        continue
      direction = striker.pos - self.pos
      radius_sq = direction.sqMag()
      relative_velocity = self.vel - striker.vel
      if radius_sq <= (self.radius + striker.radius) ** 2 and relative_velocity.sqMag() < 4:
        self.stuck = striker
        self.stuck_offset = direction.normalize() * -(self.radius + striker.radius)
        continue
      force_magnitude = 0.2 * (striker.mass * self.mass) / radius_sq
      direction.normalize()
      force_vector = direction * force_magnitude
      self.vel += force_vector / self.mass
      striker.vel -= force_vector / striker.mass