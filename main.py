import pygame
from settings import *
from sprites import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player()
playerGroup.add(player)
ground = Ground()


while gameRun:
    clock.tick(fps)
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            gameRun = False

    screen.fill((white))

    playerGroup.draw(screen)
    playerGroup.update()

    ground.draw(screen)
    ground.update(fps)

    ground.get_rect()
    pygame.display.update()
