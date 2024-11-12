import pygame

from renderable import Renderable


class GameObject:
    """
    Base class for all objects in the game that need to tick and be drawn.
    Includes hooks for drawing effects like flashes
    """

    def __init__(self, renderable: Renderable):
        self.renderable = renderable
        self.rect = self.renderable.get_rect()
        self.hit_mask = self.renderable.get_collision_mask()

    def tick(self):
        # No default behavior
        pass

    def set_scale(self, scale):
        self.renderable.set_scale(scale)
        self.hit_mask = self.renderable.get_collision_mask()
        # TODO: Need to update the reference to the rect and hit mask? Test it out.

    def draw(self, screen):
        screen.blit(self.renderable.get_final_image(), self.rect)
