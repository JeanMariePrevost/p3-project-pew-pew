import enum
import math
import pygame

from game.game_object import GameObject
import global_services
from renderable import Renderable


class CollisionType(enum.Enum):
    PLAYER_SHOT = 1
    ENEMY_SHOT = 2
    ENVIRONMENT = 3
    # Add more collision types as needed


class Projectile(GameObject):
    OUT_OF_BOUNDS_EXTRA_SPACE = 200

    def __init__(self, x, y, speed, direction_in_degrees, image_asset_path):

        self.x = x
        self.y = y
        self.speed = speed
        self.direction_in_radians = direction_in_degrees * math.pi / 180

        if not hasattr(self, "damage"):
            self.damage = 1

        # Currently hard-coded impact sound
        self.impact_sound = global_services.safe_load_sound("assets/HitTheGround_edit.wav")
        self.impact_sound.set_volume(0.5)

        super().__init__(Renderable(image_asset_path))

    def tick(self):
        # Default behavior, move in a straight line at constant speed
        self.x += self.speed * math.cos(self.direction_in_radians)
        self.y += self.speed * math.sin(self.direction_in_radians)

        # update position from center point
        self.rect.center = self.x, self.y

        self.destroy_if_out_of_bounds()

    def destroy_if_out_of_bounds(self):
        from global_services import get_screen

        screen_rect = get_screen().get_rect()
        # If the projectile is out of screen bounds with an additional buffer, destroy it
        if not screen_rect.inflate(self.OUT_OF_BOUNDS_EXTRA_SPACE, self.OUT_OF_BOUNDS_EXTRA_SPACE).colliderect(self.rect):
            self.destroy()

    def hit_damageable_object(self, damageable_object):
        damageable_object.take_damage(self.damage)
        self.impact_sound.play()
        self.destroy()
