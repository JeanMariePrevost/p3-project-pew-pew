import os
import pygame

from game.collision_type_set import CollisionTypeSet, CollisionType
from game.damageable_game_object import DamageableGameObject
from game.enemy_projectile_basic import EnemyProjectileBasic
import global_events
from global_services import get_enemy_manager, get_screen, get_current_game_level
import random

from renderable import Renderable
from renderable_flash_wrapper import RenderableFlashWrapper


class EnemyShipBasic(DamageableGameObject):

    def __init__(self, image_asset_path="assets/enemyBlack2.png"):
        # Load the spaceship image from assets
        super().__init__(Renderable(image_asset_path))

        # Set randomized starting position and speed
        self.speed: float = random.choice([-2.5, 2.5])
        self.x: float = random.uniform(self.rect.width / 2, get_screen().get_rect().right - self.rect.width / 2)
        self.y: float = random.uniform(self.rect.height / 2, get_screen().get_rect().height / 3)

        # Unit stats
        self.health = 3 + (get_current_game_level() / 6)
        self.score_value = 100
        self.seconds_between_shots_min = 2 - min(1.5, get_current_game_level() / 3)
        self.seconds_between_shots_max = 12 - min(10, get_current_game_level() / 3)
        self.set_time_for_next_shot()

        # Sound effect
        self.sound = pygame.mixer.Sound("assets/Laser_shoot 123.wav")
        self.sound.set_volume(2)

        self.set_collision_types(collision_class=CollisionType.ENEMY, collision_targets=None)

        # Register with the enemy manager
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

    def take_damage(self, amount):
        RenderableFlashWrapper(self.renderable, (255, 99, 99), 0.45, 9)
        return super().take_damage(amount)

    def on_health_depleted(self):
        global_events.enemy_destroyed.trigger(self)
        self.destroy()

    def destroy(self):
        get_enemy_manager().remove_enemy(self)
        super().destroy()
