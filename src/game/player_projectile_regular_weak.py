from animated_renderable import AnimatedRenderable
from game.player_projectile_regular import PlayerProjectileRegular
from particle import Particle


class PlayerProjectileRegularWeak(PlayerProjectileRegular):
    def __init__(self, spawn_x, spawn_y, direction) -> None:
        super().__init__(spawn_x, spawn_y, direction)
        self.damage = 0.3
        self.set_scale(0.5)
        self.renderable.set_tint((0, 0, 0), 0.6)

    def spawn_hit_particle(self):
        animation = AnimatedRenderable("assets/Simple explosion", loop=False, ticks_per_frame=3, auto_tick=True)
        hit_particle = Particle(self.rect.centerx, self.rect.centery, animation)
        hit_particle.set_scale(0.2)
