import random
from game.enemy_ship_basic import EnemyShipBasic
import global_events
from global_services import get_screen


class PowerupContainer(EnemyShipBasic):
    def __init__(self):
        print("PowerupConatiner spawning")
        # TODO: replace hard-coded powerup with randomized type?
        image_asset_path = "assets/ufoGreen.png"

        super().__init__(image_asset_path)

        self.speed: float = random.choice([-1, 1])
        self.y: float = random.uniform(self.rect.height / 2, get_screen().get_rect().height / 5)

        self.health = 1
        self.change_scale(0.66)

        # global_events.tick_signal.add(self.tick)
        # global_events.draw_signal.add(self.draw)

    def fire(self):
        # Disable firing
        pass

    def on_health_depleted(self):
        # TODO: Implement powerup spawning
        return super().on_health_depleted()

    # def destroy(self):
    # global_events.tick_signal.remove(self.tick)
    # global_events.draw_signal.remove(self.draw)
