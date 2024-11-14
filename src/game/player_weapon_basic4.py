import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic4(PlayerWeaponBasic):
    """
    Basic weapon level 2
    """

    def __init__(self, player_ship) -> None:
        super().__init__(player_ship)
        self.seconds_betwen_shots = 0.1

    def on_item_collected_by_player(self, item_object):
        if isinstance(item_object, Powerup):
            # self.player_ship.change_weapon(PlayerWeaponBasic2(self.player_ship))
            # TODO : Level 3 weapon
            print("Player weapon maxed! (TODO)")

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegular(player_x - 15, player_y, -97)
        PlayerProjectileRegular(player_x, player_y, -90)
        PlayerProjectileRegular(player_x + 15, player_y, -83)
        PlayerProjectileRegularWeak(player_x - 25, player_y - 15, -110)
        PlayerProjectileRegularWeak(player_x + 25, player_y - 15, -70)
