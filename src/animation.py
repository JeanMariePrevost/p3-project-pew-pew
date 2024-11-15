import os

import pygame

from global_events import tick_signal, draw_signal


class Animation:
    def create_from_folder(folder_path, loop=False, ticks_per_frame=1, auto_tick=True, auto_draw=True):
        # Load all images from a folder and create an animation from them
        frames = []
        for file in os.listdir(folder_path):
            if file.endswith(".png"):
                frames.append(pygame.image.load(os.path.join(folder_path, file)))
        return Animation(*frames, loop=loop, ticks_per_frame=ticks_per_frame, auto_tick=auto_tick, auto_draw=auto_draw)

    def __init__(self, *frames, loop=False, ticks_per_frame=1, auto_tick=True, auto_draw=True):
        self.frames = frames
        self.ticks_per_frame = ticks_per_frame
        self.current_frame = 0
        self.ticks_until_next_frame = ticks_per_frame
        self.loop = loop
        self.x = 0
        self.y = 0
        self.scale = 1.0
        self.remove_when_done = False
        if auto_tick:
            tick_signal.add(self.tick)
        if auto_draw:
            draw_signal.add(self.draw)

    def tick(self):
        self.ticks_until_next_frame -= 1
        if self.ticks_until_next_frame <= 0:
            self.advance_frame()

    def advance_frame(self):
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            if self.loop:
                self.current_frame = 0
            else:
                self.current_frame = len(self.frames) - 1
                if self.remove_when_done:
                    self.destroy()

    def get_current_frame_image(self) -> pygame.Surface:
        return self.frames[self.current_frame]

    def draw(self, screen):
        # Get the current frame's surface
        current_image = self.get_current_frame_image()

        if self.scale != 1.0:
            scaled_width = int(current_image.get_width() * self.scale)
            scaled_height = int(current_image.get_height() * self.scale)
            current_image = pygame.transform.scale(current_image, (scaled_width, scaled_height))

        # Calculate the top-left position to center the scaled image at (self.x, self.y)
        position = (self.x - current_image.get_width() // 2, self.y - current_image.get_height() // 2)

        # Blit the scaled image at the calculated position
        screen.blit(current_image, position)

    def destroy(self):
        tick_signal.remove(self.tick)
        draw_signal.remove(self.draw)
