from game.game_object import GameObject

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

        # TODO: Implement player colliding with enemies

        # Check for collisions between every registerd object in collidable_objects
        print(f"Checking {len(self.collidable_objects)} objects for collisions")
        for game_object in self.collidable_objects:
            for other in self.collidable_objects:
                if game_object == other:
                    continue
                if game_object.get_collision_targets().can_collide_with(other.get_collision_class()):
                    if self.check_collision_using_masks(game_object, other):
                        game_object.on_collision_with_target(other)

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
