import pygame


class PlayerWeaponBasic:
    """
    Handles the firing of projectiles for the player.
    """

    def __init__(self) -> None:
        self.rate_of_fire = 0.5  # How many seconds between shots
        self.last_fire_time = 0  # Time of the last shot
        self.sound = pygame.mixer.Sound("assets/Laser_shoot 80_low_quiet.wav")

    def tick(self):
        # Check if the spacebar or LMB are currently pressed
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or mouse_buttons[0]:
            self.run_firing_logic()

    def run_firing_logic(self):
        """
        Fire a projectile from the player's ship.
        """
        if self.weapon_on_cooldown():
            return
        else:
            self.last_fire_time = pygame.time.get_ticks()
            # play the sound
            self.sound.play()
        pass

    def weapon_on_cooldown(self) -> bool:
        return pygame.time.get_ticks() - self.last_fire_time < self.rate_of_fire * 1000
