import pygame
from game.game_object import GameObject
from game.starfield_background import StarFieldBackground
import global_services
from menu.button import Button
from renderable import Renderable
from renderable_text import RenderableText
from scenes.base_scene import BaseScene


class HighscoreScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.title_text = GameObject(RenderableText("Highscores", "assets/fonts/Roboto-Bold.ttf", 48, (255, 255, 255)))
        self.title_text.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_text.rect.y = 50

        # TODO: load scores from file, WITH exception handling
        # TODO: create 1 text element per score, or 1 with line breaks if it's also possible
        # Could have a slight color difference from top to worst

        self.play_button = Button("Back", None, "assets/NotEnoughEnergy.wav")
        self.play_button.rect.centerx = global_services.get_screen().get_width() / 2
        self.play_button.rect.y = global_services.get_screen().get_height() - 100 - self.play_button.rect.height
        self.play_button.clicked_signal.add(self.on_back_button_clicked)

        # bgm
        pygame.mixer.music.load("assets/stg_theme007_88pro-loop.ogg")
        pygame.mixer.music.play(-1)

    def on_back_button_clicked(self, button):
        import main

        print("Back button clicked on highscores screen")
        pygame.mixer.music.stop()
        main.start_scene_transition(self, main.MainMenuScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def draw(self, screen):
        # Clear sceen with black
        screen.fill((0, 0, 0))

    def tick(self):
        pass
