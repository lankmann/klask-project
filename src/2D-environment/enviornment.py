import pygame as pg
import random
from screen import Screen
from striker import Striker
from vector import Vector
from ball import Ball
from moutain import Mountain
from goal import Goal
from enum import Enum

goals: list[Goal] = []
mountains: list[Mountain] = []

class Reward(Enum):
  OP_MAGNET = 1
  OP_SCORE = -1

  SELF_MAGNET = -1
  SELF_SCORE = 1

class Enviornment:
  def __init__(self, width=45, height=35):
    self.frame_count = 0
    self.screen = Screen(width, height)
    self.surface = pg.display.set_mode(self.screen.worldToScreen().toTuple())

    # TODO: Create new player class
    self.player1 = Striker(3, height / 2, 1)
    self.player2 = Striker(width - 3, height / 2, 2)
    self.player1_score = 0
    self.player2_score = 0

    self.ball = Ball(2, 2)
    self.physicsObjects = []
    
    self.setup()

  def setup(self):
    for i in range(-1, 2, 1):
      mountains.append(Mountain(self.screen.width / 2, self.screen.height / 2 + i * 10))

    goals.append(Goal(4, self.screen.height / 2, 1))
    goals.append(Goal(self.screen.width - 4, self.screen.height / 2, 2))

    self.physicsObjects.append(self.player1)
    self.physicsObjects.append(self.player2)
    self.physicsObjects.append(self.ball)
    self.physicsObjects += mountains

  # for i in range(10):
  #   r = random.random() * 2 + 0.5
  #   balls.append(PhysicsBall(random.random() * screen.width, random.random() * screen.height, r, r*r, 0.5))
  # balls.append(PhysicsBall(screen.width - r, screen.height / 2 - 0.1, r, r*r, 1))
  # balls[1].vel.x = -0.5

  def player1_move(self, player_movement):
    reward = 0
    condition: Reward

    if goals[0].has_score:
        condition = Reward.OP_SCORE
        reward += Reward.OP_SCORE
        self.player2_score += 1

    if goals[1].has_score:
        condition = Reward.SELF_SCORE
        reward += Reward.SELF_SCORE
        self.player1_score += 1

    # TODO: Implement reward and score for mountain

    self.draw(player1_movement=player_movement)

    # reward, done, score
    return condition.value, condition == Reward.OP_SCORE or condition == Reward.SELF_SCORE, reward 
  
  def player2_move(self, player_movement):
    reward = 0
    condition: Reward

    if goals[0].has_score:
        condition = Reward.SELF_SCORE
        reward += Reward.SELF_SCORE
        self.player2_score += 1

    if goals[1].has_score:
        condition = Reward.OP_SCORE
        reward += Reward.OP_SCORE
        self.player1_score += 1

    # TODO: Implement reward and score for mountain

    self.draw(player1_movement=player_movement)

    # reward, done, score
    return condition.value, condition == Reward.OP_SCORE or condition == Reward.SELF_SCORE, reward

  def draw(self, player1_movement=None, player2_movement=None):
    self.surface.fill((16, 125, 172))

    for goal in goals:
      goal.display(self.surface, self.screen)
      goal.score(self.ball)

    for obj in self.physicsObjects:
      obj.display(self.surface, self.screen)
      obj.collide_with_objects(self.physicsObjects)
      obj.update()

    for mountain in mountains:
      if mountain.stuck:
        if mountain in self.physicsObjects:
          self.physicsObjects.remove(mountain)
        mountain.display(self.surface, self.screen)
      mountain.applyMagneticForce([self.player1, self.player2])

    player1_movement != None and self.player1.move(player1_movement)
    player2_movement != None and self.player2.move(player2_movement)

    mouse_position = self.screen.screenToWorld(Vector.fromTuple(pg.mouse.get_pos()))
    # player1.track(mouse_position)

  # TODO: Implement board reset
  def reset():
    pass