import os
import pygame


class GameObject:
    """
    Base class for all objects in the game that need to tick and be drawn.
    Includes hooks for drawing effects like flashes
    """

    def __init__(self, image_asset_path):
        self.image = pygame.image.load(image_asset_path)
        self.rect = self.image.get_rect()
        self.hit_mask = pygame.mask.from_surface(self.image)
        pass

    def tick(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
