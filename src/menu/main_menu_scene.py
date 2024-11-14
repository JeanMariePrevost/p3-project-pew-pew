from game.game_object import GameObject
import global_services
from renderable import Renderable
from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def __init__(self):
        self.title_card = GameObject(Renderable("assets/P3.png"))
        self.title_card.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_card.rect.y = 50
        pass

    def tick(self):
        pass

    def draw(self, screen):
        pass
