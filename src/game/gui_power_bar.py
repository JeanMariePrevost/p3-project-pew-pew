from animated_renderable import AnimatedRenderable
from game.game_object import GameObject
import global_events
import global_services


class GuiPowerBar(GameObject):
    """Current weapon level and health GUI element"""

    def __init__(self):
        super().__init__(AnimatedRenderable("assets/power_bar", auto_tick=False))
        self.set_scale(4)
        self.rect.x = 10
        self.rect.y = global_services.get_screen().get_height() - self.rect.height - 30
        self._draw_signal_priority = -10
        global_events.player_weapon_changed.add(self.on_player_weapon_changed)

    def on_player_weapon_changed(self, new_weapon):
        self.renderable.set_current_frame(new_weapon.level - 1)

    def draw(self, screen):
        screen.blit(self.renderable.get_final_image(), self.rect)

    def destroy(self):
        global_events.player_weapon_changed.remove(self.on_player_weapon_changed)
        return super().destroy()
