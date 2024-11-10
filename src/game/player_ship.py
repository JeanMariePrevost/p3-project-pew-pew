import os
import pygame

class PlayerShip:
    def __init__(self):
        # Load the spaceship image from assets
        self.image = pygame.image.load(os.path.join("assets", "playerShip1_blue.png"))
        self.rect = self.image.get_rect()

    def tick(self):
        # Set position based on mouse cursor
        self.rect.center = pygame.mouse.get_pos()

    def draw(self, screen):
        # Draw the spaceship on the given screen
        screen.blit(self.image, self.rect)
