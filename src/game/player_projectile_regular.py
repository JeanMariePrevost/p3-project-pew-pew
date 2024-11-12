import pygame

from animation import Animation
from game.collision_type_set import CollisionTypeSet
from game.projectile import Projectile


class PlayerProjectileRegular(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        # self.damage = 0.1
        super().__init__(
            spawn_x,
            spawn_y,
            speed=10,
            direction_in_degrees=direction,
            collision_type_set=CollisionTypeSet.get_new_default_player_shot_mask(),
            image_asset_path="assets/laserGreen08.png",
        )

    def hit_damageable_object(self, damageable_object):
        hit_animation = Animation.create_from_folder("assets/Simple explosion", loop=False, ticks_per_frame=2, auto_tick=True)
        hit_animation.x = self.rect.centerx
        hit_animation.y = self.rect.centery
        hit_animation.scale = 0.5
        return super().hit_damageable_object(damageable_object)
