from IPython import get_ipython


get_ipython().system('pip install pygame')
import pygame

pygame.init()

pygame.mixer.init()


pygame.display.set_mode()

surface objects = images


pygame.image.load()

surface.blit()


while:
    for:
        if:
screen.fill(black)


pygame.time.Clock()
clock.tick()
pygame.display.flip()


import sys, pygame
pygame.init()

size = width, height = 1440, 850
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60.0

shape = pygame.Surface((30,30)).convert()
shape.fill((255,0,0))
shaperect = shape.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    shaperect = shaperect.move(speed)
    if shaperect.left < 0 or shaperect.right > width:
        speed[0] = -speed[0]
    if shaperect.top < 0 or shaperect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(shape, shaperect)
    pygame.display.flip()
    clock.tick(FPS)
