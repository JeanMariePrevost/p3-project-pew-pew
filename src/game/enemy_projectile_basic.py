import pygame

from game.collision_type_set import CollisionType, CollisionTypeSet
from game.projectile import Projectile
import global_services
from renderable_flash_wrapper import RenderableFlashWrapper


class EnemyProjectileBasic(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:

        super().__init__(
            spawn_x,
            spawn_y,
            speed=4 + global_services.get_current_game_level() / 6,
            direction_in_degrees=direction,
            image_asset_path="assets/laserRed04_edited.png",
        )
        self.set_collision_types(collision_class=CollisionType.ENEMY_SHOT, collision_targets=CollisionTypeSet(CollisionType.PLAYER))

    def on_collision_with_target(self, other):
        self.destroy()
        print("Player hit!")
        RenderableFlashWrapper(global_services.get_player().renderable, (255, 0, 0), 0.4, 12)
        # TODO: Implement player taking damage
