import pygame as pg
import random
from screen import Screen
from physicsBall import PhysicsBall

balls: list[PhysicsBall] = []

def setup():
  global screen
  screen = Screen(45, 35)
  global surface
  surface = pg.display.set_mode(screen.worldToScreen().toTuple())

  for i in range(10):
    r = random.random() * 2 + 0.5
    balls.append(PhysicsBall(random.random() * screen.width, random.random() * screen.height, r, r*r, 0.5))
  # balls.append(PhysicsBall(screen.width - r, screen.height / 2 - 0.1, r, r*r, 1))
  # balls[1].vel.x = -0.5

def draw(frameCount):
  surface.fill((16, 125, 172))
  for ball in balls:
    fill(0, 0, 0)
    circle(ball.pos, ball.radius)
    ball.collide_with_balls(balls)
    ball.update()

def fill(r, g, b):
  global fillColor
  fillColor = (r, g, b)

def circle(center, r):
  pg.draw.circle(surface, fillColor, screen.worldToScreen(center).toTuple(), screen.worldToScreen(r))