import pygame
from game.game_object import GameObject
import global_services
from renderable import Renderable
from renderable_text import RenderableText
from util.signal import Signal


class Button(GameObject):
    def __init__(self, text: str, renderable: Renderable):
        super().__init__(Renderable("assets/button_bg.png"))
        self.text_renderable = RenderableText(text, "assets/fonts/Roboto-Bold.ttf", 24, (255, 255, 255))
        self.hovered_by_mouse = False
        self.held_down = False
        self.clicked_signal = Signal()

    def tick(self):
        self.hovered_by_mouse = self.rect.collidepoint(pygame.mouse.get_pos())

        events = global_services.get_current_tick_events()
        if self.hovered_by_mouse and any(event.type == pygame.MOUSEBUTTONDOWN for event in events):
            self.held_down = True

        if global_services.event_occured_this_tick(pygame.MOUSEBUTTONUP):
            if self.held_down and self.hovered_by_mouse:
                print("Button clicked")
                self.clicked_signal.trigger(self)
            self.held_down = False

        if self.held_down:
            self.renderable.set_alpha(65)
            self.renderable.set_tint((0, 0, 0), 0.3)
        elif self.hovered_by_mouse:
            self.renderable.set_alpha(50)
            self.renderable.set_tint((255, 255, 255), 0)
        else:
            self.renderable.set_alpha(30)
            self.renderable.set_tint((255, 255, 255), 0)

    def draw(self, screen):
        super().draw(screen)
        # rect to draw the text at the center of the button
        offset_rect = self.rect.copy()
        offset_rect.x = self.rect.centerx - self.text_renderable.get_rect().width / 2
        offset_rect.y = self.rect.centery - self.text_renderable.get_rect().height / 2

        screen.blit(self.text_renderable.get_final_image(), offset_rect)

    def destroy(self):
        self.clicked_signal.clear()
        return super().destroy()
