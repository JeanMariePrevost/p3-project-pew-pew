import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic2(PlayerWeaponBasic):
    """
    Basic weapon level 2
    """

    def __init__(self, player_ship) -> None:
        super().__init__(player_ship)
        self.on_left_shot = True
        self.level = 2
        self.seconds_betwen_shots = 0.2

    def on_item_collected_by_player(self, item_object):
        from game.player_weapon_basic3 import PlayerWeaponBasic3

        if isinstance(item_object, Powerup):
            self.player_ship.change_weapon(PlayerWeaponBasic3(self.player_ship))

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        if self.on_left_shot:
            PlayerProjectileRegularWeak(player_x - 30, player_y + 20, -94)
            PlayerProjectileRegularWeak(player_x + 30, player_y + 20, -86)
            self.on_left_shot = False
        else:
            PlayerProjectileRegular(player_x, player_y, -90)
            self.on_left_shot = True
