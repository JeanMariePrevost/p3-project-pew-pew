import random
from game.enemy_ship_basic import EnemyShipBasic
from game.powerup import Powerup
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
        self.set_scale(0.66)

    def fire(self):
        # Disable firing
        pass

    def on_health_depleted(self):
        # TODO: Implement powerup spawning
        Powerup(self.x, self.y)
        return super().on_health_depleted()
