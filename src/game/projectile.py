import enum
import math
import pygame

from game.collision_type_set import CollisionTypeSet
from game.game_object import GameObject
from global_services import get_projectile_manager, get_screen


class CollisionType(enum.Enum):
    PLAYER_SHOT = 1
    ENEMY_SHOT = 2
    ENVIRONMENT = 3
    # Add more collision types as needed


class Projectile(GameObject):
    OUT_OF_BOUNDS_EXTRA_SPACE = 200

    def __init__(self, x, y, speed, direction_in_degrees, collision_type_set: CollisionTypeSet, image_asset_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction_in_radians = direction_in_degrees * math.pi / 180
        self.collision_type_set = collision_type_set

        super().__init__(image_asset_path)

        get_projectile_manager().add_projectile(self)

    def tick(self):
        # Default behavior, move in a straight line at constant speed
        self.x += self.speed * math.cos(self.direction_in_radians)
        self.y += self.speed * math.sin(self.direction_in_radians)

        # update position from center point
        self.rect.center = self.x, self.y

        self.destroy_if_out_of_bounds()

    def destroy_if_out_of_bounds(self):
        screen_rect = get_screen().get_rect()
        # If the projectile is out of screen bounds with an additional buffer, destroy it
        if not screen_rect.inflate(self.OUT_OF_BOUNDS_EXTRA_SPACE, self.OUT_OF_BOUNDS_EXTRA_SPACE).colliderect(self.rect):
            self.destroy()

    def draw(self, screen):
        # Currently, all graphics are implemented entirely by the subclass
        pass

    def destroy(self):
        get_projectile_manager().remove_projectile(self)
        del self
