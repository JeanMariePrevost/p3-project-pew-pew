import pygame
from game.game_object import GameObject
from game.starfield_background import StarFieldBackground
import global_services
from menu.button import Button
from renderable_text import RenderableText
from scenes.base_scene import BaseScene


class CreditsScene(BaseScene):

    ASSETS_ATTRIBUTIONS = r"""P3: Project Pew Pew is a game developed by
Jean-Marie Prévost

Assets Used:
Spaceship Shooter Environment (ansimuz) (CC0v1)
https://ansimuz.itch.io/spaceship-shooter-environment

Kenney Game Assets All-in-1 (Kenney) (CC0v1)
https://kenney.nl/assets/game-assets-all-in-one
  
SHMUP BGM Pack (doranarasi) (CC0v1)
https://doranarasi.itch.io/shmup-bgm-pack

Basic Pixel Health Bar and Scroll Bar (BDragon1727) (CC0v1)
https://bdragon1727.itch.io/basic-pixel-health-bar-and-scroll-bar

Roboto Font (Google) (Apache License 2.0)
https://fonts.google.com/specimen/Roboto"""

    def __init__(self):
        super().__init__()
        self.title_text = GameObject(RenderableText("Credits", "assets/fonts/Roboto-Bold.ttf", 48, (255, 255, 255)))
        self.title_text.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_text.rect.y = 50

        self.startfield_bg = StarFieldBackground(global_services.get_screen())

        # assets_attributions_object = GameObject(RenderableText(CreditsScene.ASSETS_ATTRIBUTIONS, "assets/fonts/Roboto-Bold.ttf", 18, (255, 255, 255)))
        # assets_attributions_object.rect.centerx = global_services.get_screen().get_width() / 2
        # assets_attributions_object.rect.y = 130
        self.add_attributions_to_scene()

        self.back_button = Button("Back", None, "assets/NotEnoughEnergy.wav")
        self.back_button.rect.centerx = global_services.get_screen().get_width() / 2
        self.back_button.rect.y = global_services.get_screen().get_height() - 70 - self.back_button.rect.height
        self.back_button.clicked_signal.add(self.on_back_button_clicked)

    def add_attributions_to_scene(self):
        lines = CreditsScene.ASSETS_ATTRIBUTIONS.splitlines()

        # Position stuff
        vertical_spacing = 28
        base_y = 130  # Starting Y position

        # List to hold GameObject instances
        self.assets_attributions_elements = []

        # Create one GameObject for each line
        for index, line in enumerate(lines):
            color = (255, 255, 255) if "https" not in line else (140, 140, 140)
            renderable_text = RenderableText(line, "assets/fonts/Roboto-Regular.ttf", 18, color)
            assets_attributions_object = GameObject(renderable_text)

            assets_attributions_object.rect.centerx = global_services.get_screen().get_width() / 2
            assets_attributions_object.rect.y = base_y + (index * vertical_spacing)

            self.assets_attributions_elements.append(assets_attributions_object)

    def on_back_button_clicked(self, button):
        import main

        print("Back button clicked on credits screen")
        # pygame.mixer.music.stop()
        main.start_scene_transition(self, main.MainMenuScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def draw(self, screen):
        # Clear sceen with black
        screen.fill((0, 0, 0))
        self.startfield_bg.draw()

    def tick(self):
        self.startfield_bg.tick()
