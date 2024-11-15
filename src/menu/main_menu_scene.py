import pygame
from game.game_object import GameObject
from game.starfield_background import StarFieldBackground
import global_services
from menu.button import Button
from menu.credits_scene import CreditsScene
from menu.highscore_scene import HighscoreScene
from renderable import Renderable
from scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.title_card = GameObject(Renderable("assets/P3.png"))
        self.title_card.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_card.rect.y = 100

        self.play_button = Button("Play", None, "assets/NotEnoughEnergy.wav")
        self.play_button.rect.centerx = global_services.get_screen().get_width() / 2
        self.play_button.rect.y = 420
        self.play_button.clicked_signal.add(self.on_play_button_clicked)

        self.highscores = Button("Highscores", None, "assets/NotEnoughEnergy.wav")
        self.highscores.rect.centerx = global_services.get_screen().get_width() / 2
        self.highscores.rect.y = self.play_button.rect.y + 70
        self.highscores.clicked_signal.add(self.on_highscores_button_clicked)

        self.credits = Button("Credits", None, "assets/NotEnoughEnergy.wav")
        self.credits.rect.centerx = global_services.get_screen().get_width() / 2
        self.credits.rect.y = self.play_button.rect.y + 70 * 2
        self.credits.clicked_signal.add(self.on_credits_button_clicked)

        self.exit = Button("Exit", None, "assets/NotEnoughEnergy.wav")
        self.exit.rect.centerx = global_services.get_screen().get_width() / 2
        self.exit.rect.y = self.play_button.rect.y + 70 * 3
        self.exit.clicked_signal.add(self.on_exit_button_clicked)

        self.startfield_bg = StarFieldBackground(global_services.get_screen())

        # bgm if not currently playing
        if pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.load("assets/stg_theme007_88pro-loop.ogg")
            pygame.mixer.music.play(-1)

    def on_play_button_clicked(self, button):
        import main

        print("Play button clicked on main menu")
        pygame.mixer.music.stop()
        main.start_scene_transition(self, main.MainGameScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def on_highscores_button_clicked(self, button):
        import main

        print("Highscores button clicked on main menu")
        main.start_scene_transition(self, HighscoreScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def on_credits_button_clicked(self, button):
        import main

        print("Credits button clicked on main menu")
        main.start_scene_transition(self, CreditsScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def on_exit_button_clicked(self, button):
        print("Exit button clicked on main menu")
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def tick(self):
        self.startfield_bg.tick()

    def draw(self, screen):
        # Clear sceen with black
        screen.fill((0, 0, 0))
        self.startfield_bg.draw()

    def destroy(self):
        return super().destroy()
