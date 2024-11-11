import pygame

from game.projectile import CollisionMask, Projectile


class PlayerProjectileRegular(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        self.image = pygame.image.load("assets/laserGreen08.png")
        self.rect = self.image.get_rect()
        super().__init__(spawn_x, spawn_y, speed=7, direction_in_degrees=direction, collision_mask=CollisionMask.PLAYER_SHOT)

    # def tick(self):

    def draw(self, screen):
        screen.blit(self.image, self.rect)
