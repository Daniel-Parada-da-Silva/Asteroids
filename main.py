# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    initialitation = pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for pla in updatable:
            pla.update(dt)  # Update game state first
        
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")  # Clear screen before drawing
        for pla in drawable:
            pla.draw(screen)  # Draw everything
        
        pygame.display.flip()  # Show the frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()