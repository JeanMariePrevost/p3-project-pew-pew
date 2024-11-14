"""
GameManager is a class responsible for managing the entire game logic and flow.
It handles the initialization, updates, and overall state of the "shooter" part
of the game, ensuring that all game components interact correctly and the game
progresses smoothly.
"""

from game.enemy_ship_basic import EnemyShipBasic
from game.gui_power_bar import GuiPowerBar
from game.game_score import GameScore
from game.player_ship import PlayerShip
from game.powerup_container import PowerupContainer
from game.starfield_background import StarFieldBackground
from global_services import BG_COLOR, get_collision_manager, get_enemy_manager, get_screen, update_current_game_level
from global_events import all_enemies_destroyed
from scenes.base_scene import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        print("MainGameScene initialized")
        self._current_level = 1
        self.player_ship = PlayerShip()
        self.bg = StarFieldBackground(get_screen())

        all_enemies_destroyed.add(self.on_all_enemies_destroyed)

        self.gui_power_bar = GuiPowerBar()
        self.gui_score = GameScore()

        self.trigger_next_wave()

    def tick(self):
        # Core game loop
        self.bg.tick()

        self.player_ship.tick()

        get_enemy_manager().tick()
        get_collision_manager().tick()

    def draw(self, screen):
        screen = get_screen()
        screen.fill(BG_COLOR)  # Fill the background to "refresh" the screen
        self.bg.draw()
        get_enemy_manager().draw(screen)
        self.player_ship.draw(screen)

    def destroy(self):
        # Currently doesn't need to do anything beyond stop ticking, which is already handled by the main loop
        pass

    def on_all_enemies_destroyed(self):
        self._current_level += 1
        update_current_game_level(self._current_level)
        self.trigger_next_wave()

    def trigger_next_wave(self):
        # TODO Implement a more complex wave system
        print(f"Triggering wave {self._current_level}")
        for _ in range(3 + int((self._current_level - 1) / 2)):
            EnemyShipBasic()

        # power up spawns every other level
        if self._current_level % 2 == 0:
            PowerupContainer()
