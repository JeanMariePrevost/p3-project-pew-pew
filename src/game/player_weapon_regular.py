import pygame

from game.player_projectile_regular import PlayerProjectileRegular
from global_services import get_screen


class PlayerWeaponBasic:
    """
    Handles the firing of projectiles for the player.
    """

    def __init__(self) -> None:
        self.seconds_betwen_shots = 0.5
        self.time_at_last_shot = 0
        self.sound = pygame.mixer.Sound("assets/MiniShot2.wav")
        # self.sound.set_volume(0.05)

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
            self.time_at_last_shot = pygame.time.get_ticks()
            # play the sound
            self.sound.play()
            PlayerProjectileRegular(player_x, player_y, -90)
        pass

    def weapon_on_cooldown(self) -> bool:
        return pygame.time.get_ticks() - self.time_at_last_shot < self.seconds_betwen_shots * 1000
