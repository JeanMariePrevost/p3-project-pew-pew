import pygame  # Assuming Pygame is being used for masks and rectangles
import enum
from global_events import all_enemies_destroyed


class EnemyManager:
    def __init__(self):
        self.enemies = []  # List of all active enemies

    def add_enemy(self, enemy):
        print(f"Added enemy {enemy} to the enemy manager, {len(self.enemies)} enemies active")
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if len(self.enemies) == 0:
            print("No more enemies left")
            all_enemies_destroyed.trigger()

    def tick(self):
        # for enemy in self.enemies:
        # enemy.tick()
        pass

    def draw(self, screen):
        # for enemy in self.enemies:
        # enemy.draw(screen)
        pass
