import pygame  # Assuming Pygame is being used for masks and rectangles
import enum


class ProjectileManager:
    def __init__(self):
        self.projectiles = []  # List of all active projectiles

    def add_projectile(self, shot):
        self.projectiles.append(shot)

    def remove_projectile(self, shot):
        try:
            self.projectiles.remove(shot)
        except:
            print(f"Error: Tried to remove non-existent projectile {shot}")

    def tick(self):
        for shot in self.projectiles:
            shot.tick()

    def draw(self, screen):
        for shot in self.projectiles:
            shot.draw(screen)
