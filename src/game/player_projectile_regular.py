import pygame

from animated_renderable import AnimatedRenderable
from animation import Animation
from game.collision_type_set import CollisionType, CollisionTypeSet
from game.damageable_game_object import DamageableGameObject
from game.projectile import Projectile
from particle import Particle


class PlayerProjectileRegular(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        # self.damage = 0.1
        super().__init__(
            spawn_x,
            spawn_y,
            speed=10,
            direction_in_degrees=direction,
            image_asset_path="assets/laserGreen08.png",
        )
        self.renderable.set_rotation(90 - direction)
        self.set_collision_types(collision_class=CollisionType.PLAYER_SHOT, collision_targets=CollisionTypeSet(CollisionType.ENEMY, CollisionType.POWERUP))

    def on_collision_with_target(self, other):
        if isinstance(other, DamageableGameObject):
            self.hit_damageable_object(other)

    def hit_damageable_object(self, damageable_object):
        self.spawn_hit_particle()
        super().hit_damageable_object(damageable_object)

    def spawn_hit_particle(self):
        animation = AnimatedRenderable("assets/Simple explosion", loop=False, ticks_per_frame=3, auto_tick=True)
        hit_particle = Particle(self.rect.centerx, self.rect.centery, animation)
        hit_particle.set_scale(0.5)
