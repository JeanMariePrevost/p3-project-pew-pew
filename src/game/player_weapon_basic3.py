import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup


class PlayerWeaponBasic3(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        super().__init__(player_ship)
        self.seconds_betwen_shots = 0.1
        self.on_left_shot = True

    def on_item_collected_by_player(self, item_object):
        from game.player_weapon_basic4 import PlayerWeaponBasic4

        if isinstance(item_object, Powerup):
            self.player_ship.change_weapon(PlayerWeaponBasic4(self.player_ship))

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
