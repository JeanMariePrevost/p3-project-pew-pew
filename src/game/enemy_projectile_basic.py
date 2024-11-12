import pygame

from game.collision_mask import CollisionMask
from game.projectile import Projectile


class EnemyProjectileBasic(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        self.image = pygame.image.load("assets/laserRed04_edited.png")
        self.rect = self.image.get_rect()
        super().__init__(spawn_x, spawn_y, speed=4, direction_in_degrees=direction, collision_mask=CollisionMask.get_new_default_enemy_shot_mask())

    # def tick(self):

    def draw(self, screen):
        screen.blit(self.image, self.rect)
