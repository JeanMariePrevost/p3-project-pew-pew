import pygame  # Assuming Pygame is being used for masks and rectangles
import enum


class EnemyManager:
    def __init__(self):
        self.enemies = []  # List of all active enemies

    def add_enemy(self, enemy):
        print(f"Added enemy {enemy} to the enemy manager, {len(self.enemies)} enemies active")
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def tick(self):
        for enemy in self.enemies:
            enemy.tick()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
