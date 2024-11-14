from enum import Enum, auto


class CollisionType(Enum):
    NONE = auto()
    PLAYER = auto()
    ENEMY = auto()
    PLAYER_SHOT = auto()
    ENEMY_SHOT = auto()
    POWERUP = auto()


class CollisionTypeSet:
    """
    Defines what a given object can collide with.
    E.g. a player shot can collide with an enemy ship, but not with another player shot.
    """

    def __init__(self, *collision_types: CollisionType):
        self.__collision_types = set(collision_types)

    def can_collide_with(self, collision_type: CollisionType):
        """True if this set can collide with a given CollisionType."""
        return collision_type in self.__collision_types

    def add_collision_type(self, collision_type):
        self.types.add(collision_type)

    def remove_collision_type(self, collision_type):
        self.types.discard(collision_type)
