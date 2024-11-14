from game.collision_type_set import CollisionType
from game.game_object import GameObject
from game.player_projectile_regular import PlayerProjectileRegular
from renderable_flash_wrapper import RenderableFlashWrapper

COLLISION_TOLERANCE = 12  # Define minimum number of pixels to count as a collision, letting "graze" shots not count


class CollisionManager:
    def __init__(self):
        self.collidable_objects = []

    def tick(self):
        self.check_all_collisions()
        pass

    def add_game_object(self, game_object: GameObject):
        # Assert the game object has both get_collision_class() and get_collision_targets() methods
        assert hasattr(game_object, "get_collision_class")
        assert hasattr(game_object, "get_collision_targets")
        self.collidable_objects.append(game_object)

    def remove_game_object(self, game_object: GameObject):
        if game_object in self.collidable_objects:
            self.collidable_objects.remove(game_object)
        else:
            print(f"Warning: Tried to remove {game_object} from collision manager, but it wasn't there. Destroyed multiple times?")

    def check_all_collisions(self):
        from global_services import get_enemy_manager, get_projectile_manager
        from global_services import get_player

        # TODO: Implement player colliding with enemies

        # Projectiles
        all_projectiles = get_projectile_manager().projectiles
        all_enemies = get_enemy_manager().enemies

        # print(f"Checking {len(all_projectiles)} projectiles against {len(all_enemies)} enemies")

        # Check for collisions between every registerd object in collidable_objects
        print(f"Checking {len(self.collidable_objects)} objects for collisions")
        for game_object in self.collidable_objects:
            for other in self.collidable_objects:
                if game_object == other:
                    continue
                if game_object.get_collision_targets().can_collide_with(other.get_collision_class()):
                    if self.check_collision_using_masks(game_object, other):
                        game_object.on_collision_with_target(other)
                        # print(f"Collision between {game_object} and {other}")

        # for projectile in all_projectiles:
        #     if projectile.collision_type_set.can_collide_with(CollisionType.ENEMY):
        #         for enemy in all_enemies:
        #             if self.check_collision_using_masks(projectile, enemy):
        #                 projectile.hit_damageable_object(enemy)
        #     if projectile.collision_type_set.can_collide_with(CollisionType.PLAYER):
        #         if self.check_collision_using_masks(projectile, get_player()):
        #             projectile.destroy()
        #             print("Player hit!")
        #             RenderableFlashWrapper(get_player().renderable, (255, 0, 0), 0.4, 12)
        #             # TODO: Implement player taking damage

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
