import pygame

from renderable import Renderable


class GameObject:
    """
    Base class for all objects in the game that need to tick and be drawn.
    Includes hooks for drawing effects like flashes
    """

    def __init__(self, image_asset_path):
        self.sprite = Renderable(image_asset_path)
        self.rect = self.sprite.get_rect()
        self.hit_mask = self.sprite.get_collision_mask()

        # self.flash_color = None
        # self.flash_ticks_duration = 0
        # self.flash_ticks_remaining = 0

    def tick(self):
        # No default behavior
        pass

    def set_scale(self, scale):
        self.sprite.set_scale(scale)
        # TODO: Need to update the reference to the rect and hit mask? Test it out.

    def draw(self, screen):
        screen.blit(self.sprite.get_final_image(), self.rect)

    def flash(self, color_rgb, alpha, duration_ticks):
        """Makes the object flash a color for a certain number of ticks"""
        self.flash_color = color_rgb
        self.flash_alpha = alpha
        self.flash_ticks_duration = duration_ticks
        self.flash_ticks_remaining = duration_ticks
        pass
