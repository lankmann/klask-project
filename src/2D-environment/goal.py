from vector import Vector
from ball import Ball
import pygame as pg

class Goal:
  def __init__(self, x, y, id) -> None:
    self.id = id
    self.pos = Vector(x, y)
    self.radius = 3
  
  def display(self, surface, screen):
    color = (8, 67, 92)
    position = screen.worldToScreen(self.pos).toTuple()
    radius = screen.worldToScreen(self.radius)
    pg.draw.circle(surface, color, position, radius)

  def score(self, ball: Ball):
    if self.has_score(ball):
      ball.pos.set(22.5, 17.5)
      ball.vel.set(0, 0)
  
  # return id of goal of score, else 0
  def has_score(self, ball: Ball):
    if (ball.pos - self.pos).sqMag() < self.radius ** 2:
      return self.id
    return 0