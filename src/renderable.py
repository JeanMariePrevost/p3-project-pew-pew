import pygame


class Renderable:
    """
    Wrapper for visual assets to allow for easier scaling, flashing and the likes
    """

    @classmethod
    def get_default_surface(cls):
        """Returns a pink square, used for when an image fails to load"""
        surface = pygame.Surface((50, 50))
        surface.fill((255, 0, 255))
        return surface

    def __init__(self, asset_path):
        self._scale_x = 1.0
        self._scale_y = 1.0
        self._rotation = 0
        self._tint = (255, 255, 255)
        self._tint_alpha = 0
        self._alpha = 255

        self.load_asset(asset_path)

    def load_asset(self, asset_path):
        try:
            self._source_image = pygame.image.load(asset_path)
        except:
            print(f"Failed to load image: {asset_path}")
            self._source_image = self.get_default_surface()
        self.set_scale(1.0)
        self.set_tint((255, 255, 255), 0)

    def set_scale(self, scale):
        self.set_scale_non_uniform(scale, scale)

    def set_scale_non_uniform(self, scale_x, scale_y):
        self._scale_x = scale_x
        self._scale_y = scale_y
        self.refresh_final_image()
        self.update_collision_mask()

    def set_alpha(self, alpha):
        self._alpha = alpha
        self.refresh_final_image()

    def set_rotation(self, angle):
        self._rotation = angle
        self.refresh_final_image()
        self.update_collision_mask()

    def update_collision_mask(self):
        self._collision_mask = pygame.mask.from_surface(self._final_image)

    def get_collision_mask(self):
        return self._collision_mask

    def get_rect(self):
        return self._final_image.get_rect()

    def get_scale_x(self):
        return self._scale_x

    def get_scale_y(self):
        return self._scale_y

    def set_tint(self, color_rgb, alpha):
        self._tint = color_rgb
        self._tint_alpha = alpha
        self.refresh_final_image()

    def refresh_final_image(self):
        self._final_image = self.get_scaled_version_of(self._source_image)
        self._final_image = self.get_tinted_version_of(self._final_image)
        self._final_image = self.get_rotated_version_of(self._final_image)
        self._final_image.set_alpha(self._alpha)

    def get_scaled_version_of(self, image):
        return pygame.transform.scale(image, (int(image.get_width() * self._scale_x), int(image.get_height() * self._scale_y)))

    def get_tinted_version_of(self, image):
        # HACK: applies it to the image directly, side effect, doesn't matter for now
        additive_color = (self._tint[0] * self._tint_alpha, self._tint[1] * self._tint_alpha, self._tint[2] * self._tint_alpha)
        subtractive_color = ((255 - self._tint[0]) * self._tint_alpha, (255 - self._tint[1]) * self._tint_alpha, (255 - self._tint[2]) * self._tint_alpha)
        image.fill(subtractive_color, special_flags=pygame.BLEND_RGB_SUB)
        image.fill(additive_color, special_flags=pygame.BLEND_RGB_ADD)
        return image

    def get_rotated_version_of(self, image):
        rot_image = pygame.transform.rotate(image, self._rotation)
        # rot_rect = rot_image.get_rect(cente=image.get_rect().center)
        # return rot_image, rot_rect
        return rot_image

    def get_final_image(self):
        return self._final_image

    def destroy(self):
        pass
