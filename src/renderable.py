import pygame


class Renderable:
    """
    Wrapper for visual assets to allow for easier scaling, flashing and the likes
    """

    def __init__(self, asset_path):
        self.__scale = 1.0
        self.__tint = (255, 255, 255)
        self.__tint_alpha = 0

        self.load_asset(asset_path)
        self.set_scale(1.0)
        self.set_tint((255, 255, 255), 0)

    def load_asset(self, asset_path):
        self.__source_image = pygame.image.load(asset_path)
        self.refresh_final_image()

    def set_scale(self, scale):
        self.__scale = scale
        self.refresh_final_image()
        self.update_collision_mask()

    def update_collision_mask(self):
        self.__collision_mask = pygame.mask.from_surface(self.__final_image)

    def get_collision_mask(self):
        return self.__collision_mask

    def get_rect(self):
        return self.__final_image.get_rect()

    def get_scale(self):
        return self.__scale

    def set_tint(self, color_rgb, alpha):
        self.__tint = color_rgb
        self.__tint_alpha = alpha
        self.refresh_final_image()

    def refresh_final_image(self):
        # Apply scale
        self.__final_image = pygame.transform.scale(
            self.__source_image, (int(self.__source_image.get_width() * self.__scale), int(self.__source_image.get_height() * self.__scale))
        )
        # Apply tint
        # TODO - Tint alpha
        inverse_color = (255 - self.__tint[0], 255 - self.__tint[1], 255 - self.__tint[2])
        self.__final_image.fill(inverse_color, special_flags=pygame.BLEND_RGB_SUB)
        self.__final_image.fill(self.__tint, special_flags=pygame.BLEND_RGB_ADD)

    def get_final_image(self):
        return self.__final_image

    # def draw(self, screen):
    #     screen.blit(self.__final_image, self.rect)
