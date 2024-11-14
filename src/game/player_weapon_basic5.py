import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_mid import PlayerProjectileRegularMid
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
import global_events


class PlayerWeaponBasic5(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        from game.player_weapon_basic4 import PlayerWeaponBasic4

        super().__init__(player_ship)
        self.level = 5
        self.seconds_betwen_shots = 0.25

        self._next_weapon_class = None
        self._previous_weapon_class = PlayerWeaponBasic4

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegularWeak(player_x - 30, player_y + 20, -105)
        PlayerProjectileRegularMid(player_x - 15, player_y + 5, -97)
        PlayerProjectileRegular(player_x, player_y, -90)
        PlayerProjectileRegularMid(player_x + 15, player_y + 5, -83)
        PlayerProjectileRegularWeak(player_x + 30, player_y + 20, -75)
