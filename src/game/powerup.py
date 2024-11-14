from animated_renderable import AnimatedRenderable
from game.game_object import GameObject
import global_events
import global_services


class Powerup(GameObject):
    def __init__(self, x, y):
        renderable = AnimatedRenderable("assets/powerup", loop=True, ticks_per_frame=4, auto_tick=True)
        super().__init__(renderable)
        self.rect.centerx = x
        self.rect.centery = y
        # print("Powerup spawned at", x, y)
        self.set_scale(0.7)
        global_events.tick_signal.add(self.tick)
        global_events.draw_signal.add(self.draw)

    def tick(self):
        self.rect.y += 3

        if self.rect.top > global_services.get_screen().get_rect().height:
            self.destroy()
        # print(f"Powerup at {self.rect.x}, {self.rect.y}")

    def destroy(self):
        global_events.tick_signal.remove(self.tick)
        global_events.draw_signal.remove(self.draw)

    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)

    # def handle_collision(self, player):
    #     if self.rect.colliderect(player.rect):
    #         if self.powerup_type == "health":
    #             player.health += 1
    #         elif self.powerup_type == "shield":
    #             player.shield += 1
    #         elif self.powerup_type == "laser":
    #             player.laser_level +=
