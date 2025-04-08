# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    initialitation = pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)  # Update game state first

        screen.fill("black")  # Clear screen before drawing
        player.draw(screen)  # Draw everything
        
        pygame.display.flip()  # Show the frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()