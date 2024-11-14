"""
"Blackboard" type module where global events can be registered and triggered.
e.g. enemies being destroyed, player death, etc.
"""

from util.signal import Signal


current_scene_destroyed = Signal()  # payload: None

# "Unsafe" tick and draw signals, great for visuals and non-critical / non order-sensitive logic
# E.g. usage: tick_signal.add(my_function)
tick_signal = Signal()
draw_signal = Signal()


# Main game event signals
enemy_destroyed = Signal()  # payload: EnemyShipBasic
all_enemies_destroyed = Signal()  # payload: None
item_collected_by_player = Signal()  # payload: Powerup
player_weapon_changed = Signal()  # payload: PlayerWeaponBasic
powerup_collected_when_weapon_maxed = Signal()  # payload: None
player_took_damage = Signal()  # payload: EnemyProjectileBasic
player_died = Signal()  # payload: None
