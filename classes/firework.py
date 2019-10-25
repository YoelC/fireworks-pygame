import pygame
from random import randint, uniform
from classes.explosion import Explosion
from math import radians, sin, cos


def rotate_center(surface, angle, pos):
    to_draw = pygame.transform.rotate(surface, angle)
    new_rect = to_draw.get_rect(center=surface.get_rect(topleft=(pos[0], pos[1])).center)
    return to_draw, new_rect


class Firework:
    width, height = 10, 10

    def __init__(self, pos):
        self.tick = 0
        self.lifetime = randint(24, 100)
        self.x, self.y = pos
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.firework_over = False

        self.explosion = None

        self.angle = randint(80, 100)
        self.vel = uniform(1, 16)
        self.x_vel = cos(radians(self.angle)) * self.vel
        self.y_vel = sin(radians(self.angle)) * self.vel

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(self.color)

    def move(self):
        if self.tick < self.lifetime:
            self.x += self.x_vel
            self.y -= self.y_vel
        elif self.tick > self.lifetime and not self.firework_over:
            self.explosion = Explosion(parent=self)
            self.firework_over = True
        elif self.explosion is not None:
            self.explosion.move()

        self.tick += 1

    def draw(self, surface):
        if not self.firework_over:
            to_draw, new_rect = rotate_center(self.surface, self.angle, (self.x + self.width/2, self.y + self.height/2))
            surface.blit(to_draw, new_rect)
        else:
            self.explosion.draw(surface)
