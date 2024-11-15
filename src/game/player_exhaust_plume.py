import random
from game.game_object import GameObject
import global_events
from renderable import Renderable


class PlayerExhaustPlume(GameObject):
    def __init__(self, player_ship):
        self._draw_signal_priority = 1  # To draw behind the player ship
        super().__init__(Renderable("assets/fire.png"))
        self.player_ship = player_ship
        self.min_scale = 0.8
        self.max_scale = 1.2
        self.max_jitter = 0.05

    def tick(self):
        current_scale_y = self.renderable.get_scale_y()
        target_scale_y = random.uniform(self.min_scale, self.max_scale)
        # move towards the target scale at a maximum speed of max_jitter per tick
        if current_scale_y < target_scale_y:
            new_scale_y = min(current_scale_y + self.max_jitter, target_scale_y)
        else:
            new_scale_y = max(current_scale_y - self.max_jitter, target_scale_y)
        self.renderable.set_scale_non_uniform(1, new_scale_y)
        self.rect = self.renderable.get_rect()
        self.rect.centerx = self.player_ship.rect.centerx
        self.rect.y = self.player_ship.rect.bottom - 40
        return super().tick()
