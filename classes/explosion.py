from random import uniform, randint
from classes.particle import Particle


class Explosion:
    def __init__(self, parent):
        self.x, self.y, self.width, self.height = parent.x + parent.width/2, parent.y + parent.height/2, parent.width, parent.height
        self.color = parent.color
        self.explosion_number = randint(20, 180)
        self.max_vel = randint(4, 10)
        self.particles = [Particle(pos=(self.x, self.y, self.width/uniform(2, 3), self.height/uniform(2, 3)),
                                   vel=uniform(0, self.max_vel),
                                   angle=i*(360 / self.explosion_number),
                                   color=self.color) for i in range(self.explosion_number)]

    def move(self):
        for i, particle in enumerate(self.particles):
            if particle.dead:
                self.particles.pop(i)
                continue
            particle.move()

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
