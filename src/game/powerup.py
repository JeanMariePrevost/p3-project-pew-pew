from animated_renderable import AnimatedRenderable
from game.collision_type_set import CollisionType, CollisionTypeSet
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
        self.set_collision_types(collision_class=CollisionType.POWERUP, collision_targets=CollisionTypeSet(CollisionType.PLAYER))
        global_events.tick_signal.add(self.tick)
        global_events.draw_signal.add(self.draw)

    def tick(self):
        self.rect.y += 3

        if self.rect.top > global_services.get_screen().get_rect().height:
            self.destroy()
        # print(f"Powerup at {self.rect.x}, {self.rect.y}")

    def on_collision_with_target(self, other):
        if other == global_services.get_player():
            print("Player collided with powerup")
            global_events.item_collected_by_player.trigger(self)
            self.destroy()
        return super().on_collision_with_target(other)
