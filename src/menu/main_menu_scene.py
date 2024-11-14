from game.game_object import GameObject
import global_services
from menu.button import Button
from renderable import Renderable
from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def __init__(self):
        self.title_card = GameObject(Renderable("assets/P3.png"))
        self.title_card.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_card.rect.y = 50

        self.play_button = Button("Play", None)
        self.play_button.clicked_signal.add(self.on_play_button_clicked)
        pass

    def on_play_button_clicked(self, button):
        print("Play button clicked on main menu")

    def tick(self):
        pass

    def draw(self, screen):
        # Clear sceen with black
        screen.fill((0, 0, 0))
        pass
