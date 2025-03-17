import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.__cooldown = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw (self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.player_shoot(dt)
        
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def player_shoot(self,dt):
        if self.__cooldown < 0:    
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot = Shot(self.position.x, self.position.y, forward * PLAYER_SHOT_SPEED)
            self.__cooldown = PLAYER_SHOT_COOLDOWN 
        else:
            self.__cooldown -= dt
        