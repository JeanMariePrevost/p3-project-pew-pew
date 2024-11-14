import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_mid import PlayerProjectileRegularMid
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic3(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        from game.player_weapon_basic4 import PlayerWeaponBasic4
        from game.player_weapon_basic2 import PlayerWeaponBasic2

        super().__init__(player_ship)
        self.seconds_betwen_shots = 0.33
        self.level = 3

        self._next_weapon_class = PlayerWeaponBasic4
        self._previous_weapon_class = PlayerWeaponBasic2

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegular(player_x, player_y, -90)
        PlayerProjectileRegularMid(player_x - 30, player_y + 20, -94)
        PlayerProjectileRegularMid(player_x + 30, player_y + 20, -86)
