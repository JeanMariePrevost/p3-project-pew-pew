from game.enemy_ship_basic import EnemyShipBasic
from game.game_object import GameObject
from game.powerup import Powerup
import global_events
from renderable_text import RenderableText


class GameScore(GameObject):
    """Current score and its GUI representation"""

    def __init__(self):
        text_renderable = RenderableText("Score: 0", "assets/fonts/Roboto-Bold.ttf", 24, (255, 255, 255))
        super().__init__(text_renderable)
        self.score = 0
        self.refresh_text_from_score()
        self._draw_signal_priority = -10

        global_events.enemy_destroyed.add(self.on_enemy_destroyed)
        global_events.item_collected_by_player.add(self.on_item_collected_by_player)
        global_events.powerup_collected_when_weapon_maxed.add(self.on_powerup_collected_when_weapon_maxed)

    def on_enemy_destroyed(self, enemy_ship_object: EnemyShipBasic):
        self.score += enemy_ship_object.score_value
        self.refresh_text_from_score()

    def on_item_collected_by_player(self, item: Powerup):
        self.score += 150
        self.refresh_text_from_score()

    def on_powerup_collected_when_weapon_maxed(self):
        self.score += 500
        self.refresh_text_from_score()

    def refresh_text_from_score(self):
        self.renderable.set_text(f"Score: {self.score}")
