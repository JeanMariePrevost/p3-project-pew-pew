import pygame
import sys
from game.player_ship import PlayerShip
from global_services import get_screen, BG_COLOR, clock_tick

# Initialize Pygame
pygame.init()

# player ship
player_ship = PlayerShip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen = get_screen()
    screen.fill(BG_COLOR)  # Fill the background

    player_ship.tick()
    player_ship.draw(screen)

    pygame.display.flip()  # Update the display
    clock_tick()  # Cap the frame rate

# Game loop has ended, quit Pygame
pygame.quit()
sys.exit()
