"""
GameManager is a class responsible for managing the entire game logic and flow.
It handles the initialization, updates, and overall state of the "shooter" part
of the game, ensuring that all game components interact correctly and the game
progresses smoothly.
"""

import pygame
from game.enemy_ship_basic import EnemyShipBasic
from game.gui_power_bar import GuiPowerBar
from game.game_score import GameScore
from game.player_ship import PlayerShip
from game.powerup_container import PowerupContainer
from game.starfield_background import StarFieldBackground
from global_services import BG_COLOR, get_collision_manager, get_enemy_manager, get_screen, update_current_game_level
import global_events
from scenes.base_scene import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        print("MainGameScene initialized")
        self._current_level = 1
        self.player_ship = PlayerShip()
        self.bg = StarFieldBackground(get_screen())
        pygame.mixer.music.load("assets/stg_st008_88pro-loop.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely

        global_events.all_enemies_destroyed.add(self.on_all_enemies_destroyed)
        global_events.player_died.add(self.on_player_death)

        self.gui_power_bar = GuiPowerBar()
        self.gui_score = GameScore()

        self.trigger_next_wave()

    def tick(self):
        # Core game loop
        self.bg.tick()

        get_enemy_manager().tick()
        get_collision_manager().tick()

    def draw(self, screen):
        screen = get_screen()
        screen.fill(BG_COLOR)  # Fill the background to "refresh" the screen
        self.bg.draw()
        get_enemy_manager().draw(screen)

    def destroy(self):
        global_events.all_enemies_destroyed.remove(self.on_all_enemies_destroyed)
        pygame.mixer.music.stop()
        pass

    def on_all_enemies_destroyed(self):
        self._current_level += 1
        update_current_game_level(self._current_level)
        self.trigger_next_wave()

    def on_player_death(self):
        # TODO Implement game over screen
        print("Player died, game over!")
        # fade ther music out
        pygame.mixer.music.fadeout(3000)
        self.destroy()

    def trigger_next_wave(self):
        # TODO Implement a more complex wave system
        print(f"Triggering wave {self._current_level}")
        for _ in range(3 + int((self._current_level - 1) / 2)):
            EnemyShipBasic()

        # power up spawns every other level
        if self._current_level % 2 == 0:
            PowerupContainer()
