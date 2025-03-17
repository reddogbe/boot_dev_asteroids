# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables,drawables)
    Asteroid.containers = (updatables,drawables,asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables,shots)


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0,255))
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over")
                return
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.kill()
                    shot.kill()
        pygame.display.flip()
        
        dt = timer.tick(60.0) / 1000




if __name__ == "__main__":
    main()
    