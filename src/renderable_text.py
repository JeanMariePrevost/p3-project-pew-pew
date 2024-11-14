import pygame
from renderable import Renderable


class RenderableText(Renderable):
    def __init__(self, text: str, font: str, font_size: int, color: tuple[int, int, int]):
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        super().__init__(None)

    def load_asset(self, _):
        self.refresh_font()

    def refresh_font(self):
        self.font = pygame.font.Font(self.font, self.font_size)
        self.refresh_final_image()

    def set_font_size(self, font_size: int):
        self.font_size = font_size
        self.refresh_font()

    def refresh_final_image(self):
        self._source_image = self.font.render(self.text, True, self.color)
        self._final_image = self._source_image
        self.update_collision_mask()

    def set_text(self, text: str):
        self.text = text
        self.refresh_final_image()
