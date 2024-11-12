import pygame

from game.collision_type_set import CollisionTypeSet
from game.projectile import Projectile


class PlayerProjectileRegular(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        super().__init__(
            spawn_x,
            spawn_y,
            speed=7,
            direction_in_degrees=direction,
            collision_type_set=CollisionTypeSet.get_new_default_player_shot_mask(),
            image_asset_path="assets/laserGreen08.png",
        )
