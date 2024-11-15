import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic4(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        from game.player_weapon_basic5 import PlayerWeaponBasic5
        from game.player_weapon_basic3 import PlayerWeaponBasic3

        super().__init__(player_ship)
        self.seconds_betwen_shots = 0.17
        self.level = 4
        self.on_left_shot = True

        self._next_weapon_class = PlayerWeaponBasic5
        self._previous_weapon_class = PlayerWeaponBasic3

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()

        if self.on_left_shot:
            PlayerProjectileRegular(player_x + 18, player_y, -90)
            PlayerProjectileRegularWeak(player_x - 30, player_y + 20, -100)
            self.on_left_shot = False
        else:
            PlayerProjectileRegular(player_x - 18, player_y, -90)
            PlayerProjectileRegularWeak(player_x + 30, player_y + 20, -80)
            self.on_left_shot = True
