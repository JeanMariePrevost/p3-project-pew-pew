from game.collision_type_set import CollisionType

COLLISION_TOLERANCE = 12  # Define minimum number of pixels to count as a collision, letting "graze" shots not count


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
            if projectile.collision_type_set.can_collide_with(CollisionType.ENEMY):
                for enemy in all_enemies:

                    offset = (enemy.rect.x - projectile.rect.x, enemy.rect.y - projectile.rect.y)
                    overlap = projectile.hit_mask.overlap_mask(enemy.hit_mask, offset)

                    if overlap.count() > 0:
                        # Some overlap
                        overlap_rect = overlap.get_bounding_rects()[0]
                        if overlap_rect.width > COLLISION_TOLERANCE or overlap_rect.height > COLLISION_TOLERANCE:
                            enemy.destroy()
                            projectile.destroy()
