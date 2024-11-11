import pygame  # Assuming Pygame is being used for masks and rectangles
import enum


class CollisionMask(enum.Enum):
    PLAYER_SHOT = 1
    ENEMY_SHOT = 2
    ENVIRONMENT = 3
    # Add more collision types as needed


class ProjectileManager:
    def __init__(self):
        self.projectiles = []  # List of all active projectiles

    def add_projectile(self, shot):
        self.projectiles.append(shot)

    def remove_projectile(self, shot):
        self.projectiles.remove(shot)

    def tick(self):
        for shot in self.projectiles:
            shot.tick()

    def draw(self, screen):
        for shot in self.projectiles:
            shot.draw(screen)
