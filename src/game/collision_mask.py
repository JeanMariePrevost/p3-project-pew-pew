from enum import Enum, auto


class CollisionType(Enum):
    PLAYER = auto()
    ENEMY = auto()
    PLAYER_SHOT = auto()
    ENEMY_SHOT = auto()
    ENVIRONMENT = auto()


class CollisionMask:
    """
    Defines what a given object can collide with.
    E.g. a player shot can collide with an enemy ship, but not with another player shot.
    """

    def __init__(self, *collision_targets: CollisionType):
        self.collision_targets = set(collision_targets)

    def can_collide_with(self, collision_type: CollisionType):
        """True if this mask can collide with the given type."""
        return collision_type in self.collision_targets

    @classmethod
    def get_new_default_player_shot_mask(cls):
        return cls(CollisionType.ENEMY_SHOT, CollisionType.ENVIRONMENT, CollisionType.ENEMY)

    @classmethod
    def get_new_default_enemy_shot_mask(cls):
        return cls(CollisionType.PLAYER_SHOT, CollisionType.ENVIRONMENT)

    def add_collision_type(self, collision_type):
        self.types.add(collision_type)

    def remove_collision_type(self, collision_type):
        self.types.discard(collision_type)
