import pygame


class PlayerWeaponRegular:
    """
    Handles the firing of projectiles for the player.
    """

    rate_of_fire = 0.5  # How many seconds between shots
    last_fire_time = 0  # Time of the last shot

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
            print("Pew pew!")
        pass

    def weapon_on_cooldown(self) -> bool:
        return pygame.time.get_ticks() - self.last_fire_time < self.rate_of_fire * 1000
