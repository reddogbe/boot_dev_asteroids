import pygame
import random

from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):        
        self.position +=  self.velocity * dt
    
    def kill(self):
        super().kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20,50)
            rotation_one = self.velocity.rotate(new_angle)
            rotation_two = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius * 1.2)
            asteroid_one.velocity = rotation_one
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius * 1.2) 
            asteroid_two.velocity = rotation_two