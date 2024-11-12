import os
import pygame

from game.enemy_projectile_basic import EnemyProjectileBasic
from global_services import get_enemy_manager, get_screen
import random


class EnemyShipBasic:

    def __init__(self):
        # Load the spaceship image from assets
        self.image = pygame.image.load(os.path.join("assets", "enemyBlack2.png"))
        self.rect = self.image.get_rect()

        self.speed: float = random.choice([-2.5, 2.5])
        self.x: float = random.uniform(self.rect.width / 2, get_screen().get_rect().right - self.rect.width / 2)
        self.y: float = random.uniform(self.rect.height / 2, get_screen().get_rect().height / 3)

        self.seconds_between_shots_min = 2
        self.seconds_between_shots_max = 12
        self.set_time_for_next_shot()

        self.sound = pygame.mixer.Sound("assets/Laser_shoot 123.wav")
        self.sound.set_volume(2)

        get_enemy_manager().add_enemy(self)

    def tick(self):
        # Movement logic
        self.x += self.speed
        self.rect.center = self.x, self.y
        # if enemy hits the right bounds, flip its speed
        if self.speed > 0 and self.rect.right >= get_screen().get_rect().right:
            self.speed = -self.speed
        elif self.speed < 0 and self.rect.left <= get_screen().get_rect().left:
            self.speed = -self.speed

        # Shooting logic
        # Fire if next shot ready
        if pygame.time.get_ticks() >= self.time_for_next_shot:
            self.fire()
            self.set_time_for_next_shot()

    def set_time_for_next_shot(self):
        delay_in_ms = random.uniform(self.seconds_between_shots_min, self.seconds_between_shots_max) * 1000
        self.time_for_next_shot = pygame.time.get_ticks() + delay_in_ms

    def fire(self):
        EnemyProjectileBasic(self.x, self.y, 90)
        self.sound.play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
