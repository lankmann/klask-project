import pygame as pg
from screen import Screen
from vector import Vector
from enviornment import Enviornment

class KlaskGame:
  def __init__(self):
    self.env = Enviornment()

    pg.init()
    self.main()

  def main(self):
    clock = pg.time.Clock()

    running = True
    
    while running:
      clock.tick(60)

      # Keyboard input
      keys = pg.key.get_pressed()
      self.env.player1.movement.set(0, 0)
      if keys[pg.K_w]:
        self.env.player1.movement.y = -1
      if keys[pg.K_s]:
        self.env.player1.movement.y += 1
      if keys[pg.K_a]:
        self.env.player1.movement.x = -1
      if keys[pg.K_d]:
        self.env.player1.movement.x += 1

      self.env.player2.movement.set(0, 0)
      if keys[pg.K_UP]:
        self.env.player2.movement.y = -1
      if keys[pg.K_DOWN]:
        self.env.player2.movement.y += 1
      if keys[pg.K_LEFT]:
        self.env.player2.movement.x = -1
      if keys[pg.K_RIGHT]:
        self.env.player2.movement.x += 1

      # TODO: Call player1_move and player2_move in enviornemnt.py instead
      self.env.draw(self.env.player1.movement, self.env.player2.movement)

      self.env.frame_count += 1
      pg.display.update()

      for event in pg.event.get():
        if event.type == pg.QUIT:
          running = False
        # if event.type == pg.KEYDOWN:
        #   keyDown(event.key)
        # if event.type == pg.KEYUP:
        #   keyUp(event.key)

if __name__ == '__main__':
  KlaskGame()