"""
GameManager is a class responsible for managing the entire game logic and flow.
It handles the initialization, updates, and overall state of the "shooter" part
of the game, ensuring that all game components interact correctly and the game
progresses smoothly.
"""

from animation import Animation
from game.enemy_ship_basic import EnemyShipBasic
from game.player_ship import PlayerShip
from global_services import BG_COLOR, get_collision_manager, get_enemy_manager, get_projectile_manager, get_screen
from scenes.base_scene import BaseScene


class MainGameScene(BaseScene):
    def __init__(self):
        print("MainGameScene initialized")
        self.player_ship = PlayerShip()

        # TODO: Move enemies to "waves" or "levels" objects which set up the whole swarm
        for _ in range(10):
            EnemyShipBasic()

        # DEBUG: create a single looping animation while I figure things out
        self.animation = Animation.create_from_folder("assets/Simple explosion", loop=True, ticks_per_frame=2)
        self.animation.x = 200
        self.animation.y = 200
        self.animation.scale = 0.5

    def tick(self):
        # Core game loop
        screen = get_screen()
        screen.fill(BG_COLOR)  # Fill the background to "refresh" the screen

        self.player_ship.tick()

        get_enemy_manager().tick()
        get_projectile_manager().tick()
        get_collision_manager().tick()

        self.animation.tick()

    def draw(self, screen):
        get_enemy_manager().draw(screen)
        get_projectile_manager().draw(screen)
        self.player_ship.draw(screen)

        self.animation.draw(screen)

    def destroy(self):
        # Currently doesn't need to do anything beyond stop ticking, which is already handled by the main loop
        pass
