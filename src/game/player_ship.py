import os
import pygame
from global_services import get_screen


class PlayerShip:
    speed = 7.5  # Speed of the player ship
    x, y = 0, 0  # Needed because rect use integers only, think subpixels on the NES

    def __init__(self):
        # Load the spaceship image from assets
        self.image = pygame.image.load(os.path.join("assets", "playerShip1_blue.png"))
        self.rect = self.image.get_rect()

    def tick(self):
        # Set position based on mouse cursor
        # self.rect.center = pygame.mouse.get_pos()

        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Move the ship based on arrow key input
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Update the position of the ship
        self.rect.x = self.x
        self.rect.y = self.y

        # Restrict ship position to screen bounds
        screen_rect = get_screen().get_rect()
        self.rect.clamp_ip(screen_rect)

        # HACK: prevent self.x and self.y from drifting too far outside the screen, since they aren't clamped but the rect is
        if abs(self.x - self.rect.x) > 1.5:
            self.x = self.rect.x
        if abs(self.y - self.rect.y) > 1.5:
            self.y = self.rect.y

    def draw(self, screen):
        # Draw the spaceship on the given screen
        screen.blit(self.image, self.rect)
