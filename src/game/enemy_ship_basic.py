import os
import pygame

from global_services import get_enemy_manager, get_screen


class EnemyShipBasic:

    def __init__(self):
        self.speed: float = 3
        self.x: float = 0
        self.y: float = 50
        # Load the spaceship image from assets
        self.image = pygame.image.load(os.path.join("assets", "enemyBlack2.png"))
        self.rect = self.image.get_rect()

        get_enemy_manager().add_enemy(self)

    def tick(self):
        # TODO
        self.x += self.speed
        self.rect.center = self.x, self.y
        # if enemy hits the right bounds, flip its speed
        if self.speed > 0 and self.rect.right >= get_screen().get_rect().right:
            self.speed = -self.speed
        elif self.speed < 0 and self.rect.left <= get_screen().get_rect().left:
            self.speed = -self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
