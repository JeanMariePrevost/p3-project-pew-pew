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

        self.flash_color = None
        self.flash_ticks_duration = 0
        self.flash_ticks_remaining = 0
        pass

    def tick(self):
        pass

    def draw(self, screen):
        if self.flash_ticks_remaining > 0:
            self.flash_ticks_remaining -= 1

            # Calculate flassh effect fade factor
            fade_factor = self.flash_ticks_remaining / self.flash_ticks_duration
            fade_factor *= self.flash_alpha

            # Calculate the additive and subtractive colors for the flash effect
            sub_color = (
                int((255 - self.flash_color[0]) * fade_factor),
                int((255 - self.flash_color[1]) * fade_factor),
                int((255 - self.flash_color[2]) * fade_factor),
            )

            add_color = (
                int(self.flash_color[0] * fade_factor),
                int(self.flash_color[1] * fade_factor),
                int(self.flash_color[2] * fade_factor),
            )

            # Create a tinted version of the image
            tinted_image = self.image.copy()

            # Subtract then add the fill colors to create an overlay effect that respects transparency
            tinted_image.fill(sub_color, special_flags=pygame.BLEND_RGB_SUB)
            tinted_image.fill(add_color, special_flags=pygame.BLEND_RGB_ADD)

            # Blit the final tinted image onto the screen
            screen.blit(tinted_image, self.rect)
        else:
            # Draw the object normally
            screen.blit(self.image, self.rect)

    def flash(self, color_rgb, alpha, duration_ticks):
        """Makes the object flash a color for a certain number of ticks"""
        self.flash_color = color_rgb
        self.flash_alpha = alpha
        self.flash_ticks_duration = duration_ticks
        self.flash_ticks_remaining = duration_ticks
        pass
