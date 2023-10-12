import math
import random
from vector import Vector
from screen import Screen

class PhysicsBall:
  def __init__(self, x, y, radius, mass, elasticity, drag) -> None:
    self.pos = Vector(x, y)
    self.radius = radius
    self.vel = Vector(random.random() * 2 - 1, random.random() * 2 - 1)
    self.mass = mass
    self.elasticity = elasticity
    self.drag = drag

  def collide_with_borders(self):
    border_drag = 0.99
    border_elasticity = 0.7
    e = min(border_elasticity, self.elasticity)
    if self.pos.y + self.radius > Screen.height:
      self.pos.y = Screen.height - self.radius
      self.vel.y *= -e
      self.vel.x *= border_drag
    if self.pos.y - self.radius < 0:
      self.pos.y = self.radius
      self.vel.y *= -e
      self.vel.x *= border_drag
    if self.pos.x + self.radius > Screen.width:
      self.pos.x = Screen.width - self.radius
      self.vel.x *= -e
      self.vel.y *= border_drag
    if self.pos.x - self.radius < 0:
      self.pos.x = self.radius
      self.vel.x *= -e
      self.vel.y *= border_drag

  def collide_with_objects(self, objects):
    for ball in objects:
      if not ball is self:
        self.solve_collision(ball)

  def solve_collision(self, other):
    # Calculate normal (vector pointing from other to self)
    normal = self.pos - other.pos
    # Calculate distance squared (a^2 + b^2)
    dist_sq = normal.x ** 2 + normal.y ** 2
    # c^2
    sum_radius = self.radius + other.radius
    # If a^2 + b^2 > c^2 balls are not colliding
    if dist_sq > sum_radius * sum_radius:
      return
    
    # Calculate other velocity relative to self
    relative_velocity = other.vel - self.vel
    
    # Calculate relative velocity along normal
    normal.normalize()
    # print(normal.x, normal.y)
    velocity_along_normal = Vector.dot(relative_velocity, normal)

    if velocity_along_normal < 0:
      return
    
    self_inv_mass = 1 / self.mass
    other_inv_mass = 1 / other.mass

    # Calculate impulse magnited
    elasticity = min(self.elasticity, other.elasticity)
    impulse_magnitude = -(1 + elasticity) * velocity_along_normal
    impulse_magnitude /= self_inv_mass + other_inv_mass

    # Apply impulse to both velocities it opposite directions along the collision normal
    impulse = normal * impulse_magnitude
    self.vel -= impulse * self_inv_mass
    other.vel += impulse * other_inv_mass

    # Apply position correction so that balls don't overlap
    overlap = self.radius + other.radius - math.sqrt(dist_sq) + 0.001
    correction = (normal * overlap) / (self_inv_mass + other_inv_mass)
    self.pos += correction * self_inv_mass
    other.pos -= correction * other_inv_mass

  def update(self):
    self.collide_with_borders()
    # self.vel.y += 0.01
    self.vel *= self.drag
    self.pos += self.vel