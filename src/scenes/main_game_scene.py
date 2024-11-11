"""
GameManager is a class responsible for managing the entire game logic and flow.
It handles the initialization, updates, and overall state of the "shooter" part
of the game, ensuring that all game components interact correctly and the game
progresses smoothly.
"""

from game.player_ship import PlayerShip
from global_services import BG_COLOR, get_projectile_manager, get_screen
from scenes.base_scene import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        print("MainGameScene initialized")
        self.player_ship = PlayerShip()

    def tick(self):
        # Core game loop
        screen = get_screen()
        screen.fill(BG_COLOR)  # Fill the background to "refresh" the screen

        self.player_ship.tick()

        get_projectile_manager().tick()

    def draw(self, screen):
        self.player_ship.draw(screen)
        get_projectile_manager().draw(screen)

    def destroy(self):
        # Currently doesn't need to do anything beyond stop ticking, which is already handled by the main loop
        pass
