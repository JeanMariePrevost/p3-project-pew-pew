import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_mid import PlayerProjectileRegularMid
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic3(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        super().__init__(player_ship)
        self.seconds_betwen_shots = 0.33
        self.level = 3

    def on_item_collected_by_player(self, item_object):
        from game.player_weapon_basic4 import PlayerWeaponBasic4

        if isinstance(item_object, Powerup):
            self.player_ship.change_weapon(PlayerWeaponBasic4(self.player_ship))

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegular(player_x, player_y, -90)
        PlayerProjectileRegularMid(player_x - 30, player_y + 20, -94)
        PlayerProjectileRegularMid(player_x + 30, player_y + 20, -86)
