import pygame
from screen import Screen
from vector import Vector
from draw import setup, draw



pygame.init()


def main():
  setup()
  clock = pygame.time.Clock()

  running = True
  frameCount = 0
  
  while running:
    clock.tick(60)
    draw(frameCount)
    frameCount += 1
    pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

if __name__ == '__main__':
  main()