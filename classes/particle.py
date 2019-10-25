import pygame
from math import radians, cos, sin, atan2, degrees
from random import randint


def rotate_center(surface, angle, pos):
    to_draw = pygame.transform.rotate(surface, angle)
    new_rect = to_draw.get_rect(center=surface.get_rect(topleft=(pos[0], pos[1])).center)
    return to_draw, new_rect


class Particle:
    def __init__(self, pos, vel=None, angle=None, color=(255, 255, 255)):
        self.x, self.y, self.width, self.height = pos
        self.color = color

        if isinstance(vel, tuple):
            self.x_vel, self.y_vel = vel

        if not isinstance(vel, tuple):
            self.x_vel = cos(radians(angle)) * vel
            self.y_vel = sin(radians(angle)) * vel

        self.angle = degrees(atan2(self.y_vel, self.x_vel))

        self.lifetime = 255
        self.lifetime_rate = randint(6, 12)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(self.color)

        self.dead = False

    def move(self):
        self.x_vel *= 0.98

        self.y_vel -= 0.25

        self.x += self.x_vel
        self.y -= self.y_vel

        self.angle = degrees(atan2(self.y_vel, self.x_vel))

        self.lifetime -= self.lifetime_rate

    def draw(self, surface):
        if self.lifetime < 0:
            self.dead = True
        else:
            self.surface.fill((self.color[0], self.color[1], self.color[2], self.lifetime))

        to_draw, new_rect = rotate_center(self.surface, self.angle, (self.x, self.y))
        surface.blit(to_draw, new_rect)
