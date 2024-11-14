import random

import pygame


class StarFieldBackground:
    def __init__(self, screen):
        self.screen = screen
        self.stars = []
        self.generate_stars()

    def generate_stars(self):
        for i in range(40):
            x = random.uniform(0, self.screen.get_width())
            y = random.uniform(0, self.screen.get_height())
            size = random.uniform(1, 4)
            speed = random.uniform(0.3, 1)
            brightness = random.uniform(0, 255)
            self.stars.append((x, y, size, speed, brightness))

    def tick(self):
        for i in range(len(self.stars)):
            x, y, size, speed, brightness = self.stars[i]
            y += speed
            if y > self.screen.get_height() + size:
                y = -20
            self.stars[i] = (x, y, size, speed, brightness)

    def draw(self):
        for star in self.stars:
            x, y, size, speed, brightness = star
            pygame.draw.circle(self.screen, (brightness, brightness, brightness), (int(x), int(y)), int(size))
