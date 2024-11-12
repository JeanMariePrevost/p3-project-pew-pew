from game.collision_mask import CollisionType


class CollisionManager:
    # def __init__(self):

    def tick(self):
        self.check_all_collisions()
        pass

    def draw(self, screen):
        pass

    def check_all_collisions(self):
        from global_services import get_enemy_manager, get_projectile_manager

        # TODO: Implement player colliding with enemies

        # Projectiles
        all_projectiles = get_projectile_manager().projectiles
        all_enemies = get_enemy_manager().enemies

        # print(f"Checking {len(all_projectiles)} projectiles against {len(all_enemies)} enemies")

        for projectile in all_projectiles:
            if projectile.collision_mask.can_collide_with(CollisionType.ENEMY):
                for enemy in all_enemies:
                    if projectile.rect.colliderect(enemy.rect):
                        print("Projectile hit enemy!")
                        enemy.destroy()
                        projectile.destroy()

        pass
