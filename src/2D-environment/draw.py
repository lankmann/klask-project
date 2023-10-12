import pygame as pg
import random
from screen import Screen
from striker import Striker
from vector import Vector
from ball import Ball
from moutain import Mountain
from goal import Goal

goals: list[Goal] = []
mountains = []

def setup():
  global screen
  screen = Screen(45, 35)
  global surface
  surface = pg.display.set_mode(screen.worldToScreen().toTuple())
  global physicsObjects
  physicsObjects = []
  global player1
  player1 = Striker(2, screen.height / 2)
  global player2
  player2 = Striker(screen.width - 2, screen.height / 2)
  global ball
  ball = Ball(screen.width / 2, screen.height / 2)

  for i in range(3):
    mountains.append(Mountain(random.random() * screen.width, random.random() * screen.height))

  goals.append(Goal(4, screen.height / 2))
  goals.append(Goal(screen.width - 4, screen.height / 2))

  physicsObjects.append(player1)
  physicsObjects.append(player2)
  physicsObjects.append(ball)
  physicsObjects += mountains

  # for i in range(10):
  #   r = random.random() * 2 + 0.5
  #   balls.append(PhysicsBall(random.random() * screen.width, random.random() * screen.height, r, r*r, 0.5))
  # balls.append(PhysicsBall(screen.width - r, screen.height / 2 - 0.1, r, r*r, 1))
  # balls[1].vel.x = -0.5

def draw(frameCount):
  surface.fill((16, 125, 172))

  for goal in goals:
    goal.display(surface, screen)
    goal.score(ball)

  for obj in physicsObjects:
    obj.display(surface, screen)
    obj.collide_with_objects(physicsObjects)
    obj.update()

  keys = pg.key.get_pressed()

  player1.movement.set(0, 0)
  if keys[pg.K_w]:
    player1.movement.y = -1
  if keys[pg.K_s]:
    player1.movement.y += 1
  if keys[pg.K_a]:
    player1.movement.x = -1
  if keys[pg.K_d]:
    player1.movement.x += 1
  player1.move(player1.movement)

  player2.movement.set(0, 0)
  if keys[pg.K_UP]:
    player2.movement.y = -1
  if keys[pg.K_DOWN]:
    player2.movement.y += 1
  if keys[pg.K_LEFT]:
    player2.movement.x = -1
  if keys[pg.K_RIGHT]:
    player2.movement.x += 1
  player2.move(player2.movement)

  mouse_position = screen.screenToWorld(Vector.fromTuple(pg.mouse.get_pos()))
  # player1.track(mouse_position)
