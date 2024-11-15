import pygame
from game.game_object import GameObject
from game.starfield_background import StarFieldBackground
import global_services
from menu.button import Button
from renderable_text import RenderableText
from scenes.base_scene import BaseScene


class HighscoreScene(BaseScene):

    DEFAULT_HIGHSCORES = [
        ("AAA", 20000),
        ("ZZZ", 16000),
        ("THEBOSS", 14000),
        ("COINOP", 12000),
        ("PLAYER1", 10000),
        ("BILLYKID", 7777),
        ("L00SER", 5000),
        ("UHOH", 2500),
        ("WHYME", 1000),
        ("N00B", 100),
    ]

    def __init__(self):
        super().__init__()
        self.title_text = GameObject(RenderableText("Highscores", "assets/fonts/Roboto-Bold.ttf", 48, (255, 255, 255)))
        self.title_text.rect.centerx = global_services.get_screen().get_width() / 2
        self.title_text.rect.y = 50

        self.startfield_bg = StarFieldBackground(global_services.get_screen())

        # bgm if not currently playing
        if pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.load("assets/stg_theme007_88pro-loop.ogg")
            pygame.mixer.music.play(-1)

        self.scores = self.read_scores_from_file()

        self.score_objects = []

        for i, score in enumerate(self.scores):
            print(f"{i + 1}. {score}")
            color = (255 - i * 20, 255 - i * 20, 255 - i * 20)
            if i == 0:
                size = 48
                spacing = 0
            elif i == 1:
                size = 36
                spacing = 65
            elif i == 2:
                size = 28
                spacing = 120
            else:
                size = 24
                spacing = i * 40 + 45
            print(f"Color: {color}, Size: {size}, Spacing: {spacing}")
            formatted_score = f"{score[1]:,}"
            score_text = GameObject(RenderableText(f"{i + 1}. {score[0]} - {formatted_score}", "assets/fonts/Roboto-Bold.ttf", size, color))
            score_text.rect.centerx = global_services.get_screen().get_width() / 2
            score_text.rect.y = 130 + spacing
            self.score_objects.append(score_text)

        self.score_texts = [RenderableText(f"{i + 1}. {score}", "assets/fonts/Roboto-Bold.ttf", 24, (255, 255, 255)) for i, score in enumerate(self.scores)]

        self.back_button = Button("Back", None, "assets/NotEnoughEnergy.wav")
        self.back_button.rect.centerx = global_services.get_screen().get_width() / 2
        self.back_button.rect.y = global_services.get_screen().get_height() - 100 - self.back_button.rect.height
        self.back_button.clicked_signal.add(self.on_back_button_clicked)

        # DEBUG - print received score
        received_score = global_services.get_current_game_over_score()
        print(f"Received score: {received_score}")
        global_services.set_current_game_over_score(0)

    def read_scores_from_file(self):
        try:
            with open("gamedata/highscores.dat", "r") as file:
                scores_strings = [line.strip() for line in file.readlines()]  # remove newline characters
        except FileNotFoundError:
            print("Highscores file not found, returning default scores")
            return HighscoreScene.DEFAULT_HIGHSCORES

        scores = []
        for score_string in scores_strings:
            name, score = score_string.split(",")
            scores.append((name, int(score)))
        return scores

    def write_scores_to_file(self):
        with open("gamedata/highscores.dat", "w") as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def on_back_button_clicked(self, button):
        import main

        print("Back button clicked on highscores screen")
        self.write_scores_to_file()
        # pygame.mixer.music.stop()
        main.start_scene_transition(self, main.MainMenuScene, fadeout_ms=300, pause_ms=300, fadein_ms=300)

    def draw(self, screen):
        # Clear sceen with black
        screen.fill((0, 0, 0))
        self.startfield_bg.draw()

    def tick(self):
        self.startfield_bg.tick()
