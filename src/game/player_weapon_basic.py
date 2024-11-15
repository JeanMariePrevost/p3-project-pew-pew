import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from game.powerup import Powerup
import global_events
import global_services


class PlayerWeaponBasic:
    """
    Handles the firing of projectiles for the player.
    """

    def __init__(self, player_ship) -> None:
        from game.player_weapon_basic2 import PlayerWeaponBasic2

        self.player_ship = player_ship
        self.seconds_betwen_shots = 0.4
        self.time_at_last_shot = 0
        self.level = 1
        self.sound = global_services.safe_load_sound("assets/MiniShot2.wav")
        self.sound.set_volume(0.4)
        self._next_weapon_class = PlayerWeaponBasic2
        self._previous_weapon_class = None
        global_events.item_collected_by_player.add(self.on_item_collected_by_player)
        self.time_at_creation = pygame.time.get_ticks()  # HACK: to "debounce" the powerup collection

    def on_item_collected_by_player(self, item_object):
        if pygame.time.get_ticks() - self.time_at_creation >= 500:
            if isinstance(item_object, Powerup):
                self.increase_level()

    def increase_level(self):
        if self._next_weapon_class is not None:
            self.player_ship.change_weapon(self._next_weapon_class(self.player_ship))
            print("Player weapon upgraded!")
        else:
            # Maxed out
            global_events.powerup_collected_when_weapon_maxed.trigger()

    def decresase_level(self):
        if self._previous_weapon_class is not None:
            self.player_ship.change_weapon(self._previous_weapon_class(self.player_ship))
            print("Player weapon downgraded!")
        else:
            # Death
            print("Player weapon downgraded to zero, game over")

    def tick(self, player_x, player_y):
        # Check if the spacebar or LMB are currently pressed
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or mouse_buttons[0]:
            self.run_firing_logic(player_x, player_y)

    def run_firing_logic(self, player_x, player_y):
        """
        Fire a projectile from the player's ship.
        """
        if self.weapon_on_cooldown():
            return
        else:
            self.fire(player_x, player_y)

    def fire(self, player_x, player_y):
        self.time_at_last_shot = pygame.time.get_ticks()
        self.sound.play()
        PlayerProjectileRegular(player_x, player_y, -90)

    def weapon_on_cooldown(self) -> bool:
        return pygame.time.get_ticks() - self.time_at_last_shot < self.seconds_betwen_shots * 1000

    def destroy(self):
        global_events.item_collected_by_player.remove(self.on_item_collected_by_player)
