import pygame
from random import randint
from classes.firework import Firework

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 800
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

fireworks = []

run = True
tick = 0
while run:
    clock.tick(30)
    pygame.display.set_caption(f'fps: {clock.get_fps()}')
    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        run = False

    if tick % 8 == 0:
        fireworks.append(
            Firework(pos=(randint(0, WINDOW_WIDTH), WINDOW_HEIGHT)
                     ))

    for firework in fireworks:
        firework.move()

    fill = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    fill.fill((0, 0, 0, 64))
    win.blit(fill, (0, 0))
    for firework in fireworks:
        firework.draw(win)
    pygame.display.update(win.get_rect())

    tick += 1
