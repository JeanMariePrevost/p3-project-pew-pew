import os

import pygame


class Animation:
    def create_from_folder(folder_path, loop=False, ticks_per_frame=1):
        # Load all images from a folder and create an animation from them
        frames = []
        for file in os.listdir(folder_path):
            if file.endswith(".png"):
                print(f"Loading {file}")
                frames.append(pygame.image.load(os.path.join(folder_path, file)))
        return Animation(*frames, loop=loop, ticks_per_frame=ticks_per_frame)

    def __init__(self, *frames, loop=False, ticks_per_frame=1):
        self.frames = frames
        self.ticks_per_frame = ticks_per_frame
        self.current_frame = 0
        self.ticks_until_next_frame = ticks_per_frame
        self.loop = loop
        self.x = 0
        self.y = 0
        self.scale = 1.0

    def tick(self):
        self.ticks_until_next_frame -= 1
        if self.ticks_until_next_frame <= 0:
            self.ticks_until_next_frame = self.ticks_per_frame
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1

    def draw(self, screen):
        # Get the current frame's surface
        current_image = self.frames[self.current_frame]

        if self.scale != 1.0:
            scaled_width = int(current_image.get_width() * self.scale)
            scaled_height = int(current_image.get_height() * self.scale)
            current_image = pygame.transform.scale(current_image, (scaled_width, scaled_height))

        # Calculate the top-left position to center the scaled image at (self.x, self.y)
        position = (self.x - current_image.get_width() // 2, self.y - current_image.get_height() // 2)

        # Blit the scaled image at the calculated position
        screen.blit(current_image, position)
