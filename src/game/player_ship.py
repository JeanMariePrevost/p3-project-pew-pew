import os
import pygame
from game.player_weapon_regular import PlayerWeaponBasic
from global_services import get_screen, event_occured_this_tick


class PlayerShip:

    def __init__(self):
        self.speed: float = 7.5  # Speed of the player ship
        self.x: float = 0  # Needed because rect use integers only, think subpixels on the NES
        self.y: float = 0
        self.using_mouse_controls: bool = False  # Dynamically changes control style. Tru when the mouse is moved or clicked, False when a key is pressed
        self.weapon: PlayerWeaponBasic = PlayerWeaponBasic()
        # Load the spaceship image from assets
        self.image = pygame.image.load(os.path.join("assets", "playerShip1_blue.png"))
        self.rect = self.image.get_rect()

    def tick(self):
        global using_mouse_controls
        if event_occured_this_tick(pygame.MOUSEMOTION) or event_occured_this_tick(pygame.MOUSEBUTTONDOWN):
            self.using_mouse_controls = True
        elif event_occured_this_tick(pygame.KEYDOWN):
            self.using_mouse_controls = False

        if self.using_mouse_controls:
            self.calculate_position_using_mouse_controls()
        else:
            self.calculate_position_using_keyboard_controls()

        # Update the position of the ship
        self.rect.center = self.x, self.y

        # Restrict ship position to screen bounds
        screen_rect = get_screen().get_rect()
        self.rect.clamp_ip(screen_rect)

        # HACK: prevent self.x and self.y from drifting too far outside the screen, since they aren't clamped but the rect is
        center_x, center_y = self.rect.center  # Unpack rect.center
        if abs(self.x - center_x) > 1.5:
            self.x = center_x
        if abs(self.y - center_y) > 1.5:
            self.y = center_y

        # Weapon logic
        self.weapon.tick(self.x, self.y)

    def calculate_position_using_mouse_controls(self):
        # Set position based on mouse cursor
        self.x, self.y = pygame.mouse.get_pos()

    def calculate_position_using_keyboard_controls(self):
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Move the ship based on arrow key input
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
