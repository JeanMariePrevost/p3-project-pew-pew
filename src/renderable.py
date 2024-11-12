import pygame


class Renderable:
    """
    Wrapper for visual assets to allow for easier scaling, flashing and the likes
    """

    def __init__(self, asset_path):
        self._scale = 1.0
        self._tint = (255, 255, 255)
        self._tint_alpha = 0

        self.load_asset(asset_path)

    def load_asset(self, asset_path):
        self._source_image = pygame.image.load(asset_path)
        self.set_scale(1.0)
        self.set_tint((255, 255, 255), 0)

    def set_scale(self, scale):
        self._scale = scale
        self.refresh_final_image()
        self.update_collision_mask()

    def update_collision_mask(self):
        self._collision_mask = pygame.mask.from_surface(self._final_image)

    def get_collision_mask(self):
        return self._collision_mask

    def get_rect(self):
        return self._final_image.get_rect()

    def get_scale(self):
        return self._scale

    def set_tint(self, color_rgb, alpha):
        self._tint = color_rgb
        self._tint_alpha = alpha
        self.refresh_final_image()

    def refresh_final_image(self):
        self._final_image = self.get_scaled_version_of(self._source_image)
        self._final_image = self.get_tinted_version_of(self._final_image)

    def get_scaled_version_of(self, image):
        return pygame.transform.scale(image, (int(image.get_width() * self._scale), int(image.get_height() * self._scale)))

    def get_tinted_version_of(self, image):
        # HACK: applies it to the image directly, side effect, doesn't matter for now
        additive_color = (self._tint[0] * self._tint_alpha, self._tint[1] * self._tint_alpha, self._tint[2] * self._tint_alpha)
        subtractive_color = ((255 - self._tint[0]) * self._tint_alpha, (255 - self._tint[1]) * self._tint_alpha, (255 - self._tint[2]) * self._tint_alpha)
        image.fill(subtractive_color, special_flags=pygame.BLEND_RGB_SUB)
        image.fill(additive_color, special_flags=pygame.BLEND_RGB_ADD)
        return image

    def get_final_image(self):
        return self._final_image

    def destroy(self):
        pass

    # def draw(self, screen):
    #     screen.blit(self._final_image, self.rect)
