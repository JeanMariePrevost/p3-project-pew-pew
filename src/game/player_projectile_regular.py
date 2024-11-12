import pygame

from game.collision_type_set import CollisionTypeSet
from game.projectile import Projectile


class PlayerProjectileRegular(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        self.image = pygame.image.load("assets/laserGreen08.png")
        self.rect = self.image.get_rect()
        super().__init__(spawn_x, spawn_y, speed=7, direction_in_degrees=direction, collision_type_set=CollisionTypeSet.get_new_default_player_shot_mask())

    # def tick(self):

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # DEBUG: Draw the hit mask
        # screen.blit(self.hit_mask.to_surface(), self.rect)
