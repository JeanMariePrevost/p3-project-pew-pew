import enum
import math
import pygame

from global_services import get_projectile_manager


class CollisionMask(enum.Enum):
    PLAYER_SHOT = 1
    ENEMY_SHOT = 2
    ENVIRONMENT = 3
    # Add more collision types as needed


class Projectile:
    def __init__(self, x, y, speed, direction_in_degrees, collision_mask):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction_in_radians = direction_in_degrees * math.pi / 180
        self.collision_mask = collision_mask

        get_projectile_manager().add_projectile(self)

    def tick(self):
        # Default behavior, move in a straight line at constant speed
        self.x += self.speed * math.cos(self.direction_in_radians)
        self.y += self.speed * math.sin(self.direction_in_radians)

        # update position from center point
        self.rect.center = self.x, self.y

    def draw(self, screen):
        # Currently, all graphics are implemented entirely by the subclass
        pass
