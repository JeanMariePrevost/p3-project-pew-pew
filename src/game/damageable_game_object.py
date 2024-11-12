from game.game_object import GameObject


class DamageableGameObject(GameObject):
    def __init__(self, image_asset_path):
        super().__init__(image_asset_path)
        if not hasattr(self, "health"):
            self.health = 1

    def take_damage(self, amount):
        if self.health > 0:
            self.health -= amount
            if self.health <= 0:
                self.on_health_depleted()

    def on_health_depleted(self):
        # Override this method to add custom behavior when health reaches 0
        pass
