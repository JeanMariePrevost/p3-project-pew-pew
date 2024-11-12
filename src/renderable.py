import pygame


class Renderable:
    """
    Wrapper for visual assets to allow for easier scaling, flashing and the likes
    """

    def __init__(self, asset_path):
        self.load_asset(asset_path)
        self.__scale = 1.0

    def load_asset(self, asset_path):
        self.__source_image = pygame.image.load(asset_path)
        self.__scaled_image = self.source_image

    def set_scale(self, scale):
        self.__scale = scale
        self.__scaled_image = pygame.transform.scale(
            self.__source_image, (int(self.__source_image.get_width() * scale), int(self.__source_image.get_height() * scale))
        )

    def get_scale(self):
        return self.__scale

    def draw(self, screen):
        screen.blit(self.__scaled_image, self.rect)
