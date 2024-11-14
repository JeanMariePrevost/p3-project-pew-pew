from game.player_projectile_regular import PlayerProjectileRegular


class PlayerProjectileRegularWeak(PlayerProjectileRegular):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        super().__init__(spawn_x, spawn_y, direction)
        self.damage = 0.75
        self.set_scale(0.7)
        self.renderable.set_tint((0, 0, 0), 0.33)
