import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.player_projectile_regular_mid import PlayerProjectileRegularMid
from game.player_projectile_regular_weak import PlayerProjectileRegularWeak
from game.player_weapon_basic import PlayerWeaponBasic
from game.powerup import Powerup
import global_events


class PlayerWeaponBasic5(PlayerWeaponBasic):

    def __init__(self, player_ship) -> None:
        super().__init__(player_ship)
        self.level = 5
        self.seconds_betwen_shots = 0.25

    def on_item_collected_by_player(self, item_object):
        # Weapon maxed out
        global_events.powerup_collected_when_weapon_maxed.trigger()

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegularWeak(player_x - 30, player_y + 20, -105)
        PlayerProjectileRegularMid(player_x - 15, player_y + 5, -97)
        PlayerProjectileRegular(player_x, player_y, -90)
        PlayerProjectileRegularMid(player_x + 15, player_y + 5, -83)
        PlayerProjectileRegularWeak(player_x + 30, player_y + 20, -75)
