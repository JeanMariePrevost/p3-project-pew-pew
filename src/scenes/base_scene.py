"""
Parent class for all game screens (e.g. main menu, game screen, game over screen...).
"""

import pygame
import global_events
from util.signal import Signal


class BaseScene:
    def __init__(self):
        """Initialize screen resources."""
        self.fade_out_complete_signal = Signal()
        pass

    def __str__(self):
        return self.__class__.__name__

    def tick(self):
        """
        Core update logic for the screen.
        This method is called in the main game loop to update game objects.
        Logic only, the drawing should be done in the 'draw' method.
        Override in subclasses.
        """
        raise NotImplementedError("The 'tick' method must be implemented in subclasses.")

    def draw(self, screen):
        """
        Render visuals for the screen.
        Rendering only, the logic should be done in the 'tick' method.
        Override in subclasses to draw all necessary elements to the screen.

        :param screen: The pygame display surface to render on.
        """
        raise NotImplementedError("The 'draw' method must be implemented in subclasses.")

    def fade_out_then_destroy(self, duration_in_ms):
        self.fade_out_duration = duration_in_ms
        self.fade_out_start_time = pygame.time.get_ticks()
        global_events.draw_signal.add(self.fade_out_draw, -99)  # Draw the fade out last
        self.destroy()

    def fade_in(self, duration_in_ms):
        self.fade_in_duration = duration_in_ms
        self.fade_in_start_time = pygame.time.get_ticks()
        global_events.draw_signal.add(self.fade_in_draw, -99)

    def fade_out_draw(self, screen):
        # draw a black rectangle over the screen
        time_since_fade_out = pygame.time.get_ticks() - self.fade_out_start_time
        alpha = 255 * time_since_fade_out / self.fade_out_duration
        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.set_alpha(alpha)
        fade_surface.fill((0, 0, 0))
        screen.blit(fade_surface, (0, 0))
        if alpha >= 255:
            # fully faded out, ready for transition
            global_events.draw_signal.remove(self.fade_out_draw)
            self.fade_out_complete_signal.trigger()
            # TODO: implement transition to next scene

    def fade_in_draw(self, screen):
        if self.fade_in_duration == 0:
            global_events.draw_signal.remove(self.fade_in_draw)
            return

        time_since_fade_in = pygame.time.get_ticks() - self.fade_in_start_time
        alpha = 255 - 255 * time_since_fade_in / self.fade_in_duration
        fade_surface = pygame.Surface(screen.get_size())
        fade_surface.set_alpha(alpha)
        fade_surface.fill((0, 0, 0))
        screen.blit(fade_surface, (0, 0))
        if alpha <= 0:
            global_events.draw_signal.remove(self.fade_in_draw)

    def destroy(self):
        """Hook to stop and clean up the screen resources."""
        self.fade_out_complete_signal.clear()
        pass
