"""
GameManager is a class responsible for managing the entire game logic and flow.
It handles the initialization, updates, and overall state of the "shooter" part
of the game, ensuring that all game components interact correctly and the game
progresses smoothly.
"""

from game.enemy_ship_basic import EnemyShipBasic
from game.player_ship import PlayerShip
from game.powerup_container import PowerupContainer
from global_services import BG_COLOR, get_collision_manager, get_enemy_manager, get_screen
from global_events import all_enemies_destroyed
from scenes.base_scene import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        print("MainGameScene initialized")
        self._current_level = 1
        self.player_ship = PlayerShip()

        all_enemies_destroyed.add(self.on_all_enemies_destroyed)

        self.trigger_next_wave()

    def tick(self):
        # Core game loop
        screen = get_screen()
        screen.fill(BG_COLOR)  # Fill the background to "refresh" the screen

        self.player_ship.tick()

        get_enemy_manager().tick()
        get_collision_manager().tick()

    def draw(self, screen):
        get_enemy_manager().draw(screen)
        self.player_ship.draw(screen)

    def destroy(self):
        # Currently doesn't need to do anything beyond stop ticking, which is already handled by the main loop
        pass

    def on_all_enemies_destroyed(self):
        self._current_level += 1
        self.trigger_next_wave()

    def trigger_next_wave(self):
        # TODO Implement a more complex wave system
        print(f"Triggering wave {self._current_level}")
        for _ in range(3 + int((self._current_level - 1) / 2)):
            EnemyShipBasic()

        # power up spawns every other level
        if self._current_level % 2 == 0:
            PowerupContainer()
