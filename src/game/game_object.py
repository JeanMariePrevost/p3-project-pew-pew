from game.collision_type_set import CollisionType, CollisionTypeSet
import global_events
import global_services
from renderable import Renderable


class GameObject:
    """
    Base class for all objects in the game that need to tick and be drawn.
    Includes hooks for drawing effects like flashes
    """

    def __init__(self, renderable: Renderable):
        self.renderable = renderable
        self.rect = self.renderable.get_rect()
        self.hit_mask = self.renderable.get_collision_mask()
        self.was_destroyed = False
        self._draw_signal_priority = 0 if not hasattr(self, "_draw_signal_priority") else self._draw_signal_priority
        if not hasattr(self, "collision_class"):
            self.__collision_class = CollisionTypeSet()  # By default, a GameObject won't be collidable with anything

        if not hasattr(self, "collision_targets"):
            self.__collision_targets = CollisionTypeSet()  # By default, a GameObject won't collide with anything

        global_events.tick_signal.add(self.tick)
        # HACK - add draw signal THROUGH the first tick, so that the object is guaranteed to have applied its position before drawing
        global_events.tick_signal.add(self.register_to_draw_signal_on_first_tick)
        global_events.current_scene_destroyed.add(self.destroy)

        global_services.get_collision_manager().add_game_object(self)

    def register_to_draw_signal_on_first_tick(self):
        global_events.tick_signal.remove(self.register_to_draw_signal_on_first_tick)
        if not self.was_destroyed:
            global_events.draw_signal.add(self.draw, self._draw_signal_priority)

    def set_collision_types(self, collision_class: CollisionType = None, collision_targets: CollisionTypeSet = None):
        assert isinstance(collision_class, CollisionType) or collision_class is None
        assert isinstance(collision_targets, CollisionTypeSet) or collision_targets is None
        self.__collision_class = collision_class if collision_class is not None else CollisionType.NONE
        self.__collision_targets = collision_targets if collision_targets is not None else CollisionTypeSet()

    def get_collision_class(self):
        return self.__collision_class

    def get_collision_targets(self):
        return self.__collision_targets

    def on_collision_with_target(self, other):
        # No default behavior
        pass

    def tick(self):
        # No default behavior
        pass

    def destroy(self):
        global_services.get_collision_manager().remove_game_object(self)
        global_events.tick_signal.remove(self.tick)
        global_events.draw_signal.remove(self.draw)
        global_events.current_scene_destroyed.remove(self.destroy)
        self.renderable.destroy()
        self.was_destroyed = True

    def set_scale(self, scale):
        self.renderable.set_scale(scale)
        self.hit_mask = self.renderable.get_collision_mask()

    def draw(self, screen):
        screen.blit(self.renderable.get_final_image(), self.rect)
