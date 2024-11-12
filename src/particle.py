from animated_renderable import AnimatedRenderable
from game.game_object import GameObject
import global_events


class Particle(GameObject):
    """
    A self-drawing, self-playing, self-destroying, purely visual element
    """

    def __init__(self, x, y, animated_renderable: AnimatedRenderable):
        super().__init__(animated_renderable)
        self.rect.x = x
        self.rect.y = y

        global_events.tick_signal.add(self.tick)
        global_events.draw_signal.add(self.draw)

    def tick(self):
        super().tick()
        if self.renderable.is_animation_finished():
            self.destroy()

    def draw(self, screen):
        offset_rect = self.rect.copy()
        offset_rect.x -= self.renderable.get_final_image().get_width() // 2
        offset_rect.y -= self.renderable.get_final_image().get_height() // 2
        screen.blit(self.renderable.get_final_image(), offset_rect)

    def destroy(self):
        global_events.tick_signal.remove(self.tick)
        global_events.draw_signal.remove(self.draw)

    # def draw(self, screen):
    #     self.renderable.x = self.x
    #     self.renderable.y = self.y
    #     self.renderable.draw(screen)
