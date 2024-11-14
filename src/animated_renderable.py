import os

import pygame
import global_events
from renderable import Renderable


# TODO: There should be a common "abstract class/interface" in between Renderable and AnimatedRenderable, as the subclassing feels VERY forced. To consider.
class AnimatedRenderable(Renderable):
    """
    Extends the Renderable class to allow for animated assets in a transparent way
    WARNING:  auto_ticking animations HAVE to be destroyed to prevent memory leaks
    """

    def __init__(self, asset_folder_path, loop=True, ticks_per_frame=1, auto_tick=True):
        self._asset_folder_path = asset_folder_path
        self._loop = loop
        self._ticks_per_frame = ticks_per_frame
        self._auto_tick = auto_tick

        super().__init__(asset_folder_path)

    def load_asset(self, _):
        """Loads a compelte folder instead"""
        self._frames = []
        for file in os.listdir(self._asset_folder_path):
            if file.endswith(".png"):
                self._frames.append(pygame.image.load(os.path.join(self._asset_folder_path, file)))

        self._current_frame = 0
        self._ticks_until_next_frame = self._ticks_per_frame
        if self._auto_tick:
            global_events.tick_signal.add(self.tick)
        self.set_scale(1.0)
        self.set_tint((255, 255, 255), 0)

    def refresh_final_image(self):
        # HACK: Using "_source_image" to store the current frame, as the Renderable class was not designed for this
        self._source_image = self.get_current_frame_image()
        super().refresh_final_image()

    def tick(self):
        self._ticks_until_next_frame -= 1
        if self._ticks_until_next_frame <= 0:
            self._ticks_until_next_frame = self._ticks_per_frame
            self.advance_frame()

    def advance_frame(self):
        self._current_frame += 1
        if self._current_frame >= len(self._frames):
            if self._loop:
                self._current_frame = 0
            else:
                self._current_frame = len(self._frames) - 1
        self.refresh_final_image()

    def set_current_frame(self, frame):
        self._current_frame = frame
        self.refresh_final_image()

    def set_scale(self, scale):
        # TODO : Implement scaling across frames, or dynamically for each current frame?
        super().set_scale(scale)

    def get_current_frame_image(self) -> pygame.Surface:
        return self._frames[self._current_frame]

    def is_animation_finished(self):
        return not self._loop and self._current_frame == len(self._frames) - 1

    def destroy(self):
        global_events.tick_signal.remove(self.tick)
        super().destroy()
