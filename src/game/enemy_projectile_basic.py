from animated_renderable import AnimatedRenderable
from game.collision_type_set import CollisionType, CollisionTypeSet
from game.projectile import Projectile
import global_events
import global_services
from particle import Particle
from renderable_flash_wrapper import RenderableFlashWrapper


class EnemyProjectileBasic(Projectile):
    def __init__(self, spawn_x, spawn_y, direction) -> None:

        super().__init__(
            spawn_x,
            spawn_y,
            speed=4 + global_services.get_current_game_level() / 6,
            direction_in_degrees=direction,
            image_asset_path="assets/laserRed04_edited.png",
        )
        self.set_collision_types(collision_class=CollisionType.ENEMY_SHOT, collision_targets=CollisionTypeSet(CollisionType.PLAYER))

    def on_collision_with_target(self, other):
        if other == global_services.get_player():
            global_events.player_took_damage.trigger(self)
            RenderableFlashWrapper(global_services.get_player().renderable, (255, 0, 0), 0.4, 12)
            animation = AnimatedRenderable("assets/Simple explosion", loop=False, ticks_per_frame=3, auto_tick=True)
            hit_particle = Particle(self.rect.centerx, self.rect.centery, animation)
            hit_particle.set_scale(0.5)
        self.destroy()
