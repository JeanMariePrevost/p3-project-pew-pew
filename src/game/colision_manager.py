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
        from global_services import get_player

        # TODO: Implement player colliding with enemies

        # Projectiles
        all_projectiles = get_projectile_manager().projectiles
        all_enemies = get_enemy_manager().enemies

        # print(f"Checking {len(all_projectiles)} projectiles against {len(all_enemies)} enemies")

        for projectile in all_projectiles:
            if projectile.collision_type_set.can_collide_with(CollisionType.ENEMY):
                for enemy in all_enemies:
                    if self.check_collision_using_masks(projectile, enemy):
                        enemy.take_damage(1)
                        projectile.destroy()
            if projectile.collision_type_set.can_collide_with(CollisionType.PLAYER):
                if self.check_collision_using_masks(projectile, get_player()):
                    projectile.destroy()
                    print("Player hit!")
                    get_player().flash((255, 0, 0), 0.4, 12)
                    # TODO: Implement player taking damage

    def check_collision_using_masks(self, object1, object2) -> bool:
        """
        Check for pixel-perfect collision between two objects using their hit masks
        Requires both objects to have a rect and a hit_mask attribute
        """
        offset = (object1.rect.x - object2.rect.x, object1.rect.y - object2.rect.y)
        overlap = object2.hit_mask.overlap_mask(object1.hit_mask, offset)

        if overlap.count() > 0:
            # Some overlap
            overlap_rect = overlap.get_bounding_rects()[0]
            if overlap_rect.width > COLLISION_TOLERANCE or overlap_rect.height > COLLISION_TOLERANCE:
                return True
        return False
