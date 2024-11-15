import pygame
from animated_renderable import AnimatedRenderable
from game.collision_type_set import CollisionType, CollisionTypeSet
from game.game_object import GameObject
from game.player_exhaust_plume import PlayerExhaustPlume
from game.player_weapon_basic import PlayerWeaponBasic
import global_events
import global_services
from particle import Particle
from renderable import Renderable


class PlayerShip(GameObject):

    def __init__(self):
        self.speed: float = 7.5  # Speed of the player ship
        self.x: float = 0  # Needed because rect use integers only, think subpixels on the NES
        self.y: float = 0
        self.using_mouse_controls: bool = False  # Dynamically changes control style. Tru when the mouse is moved or clicked, False when a key is pressed
        self.i_frames: int = 90  # Invincibility frames
        super().__init__(Renderable("assets/playerShip1_blue.png"))
        self.change_weapon(PlayerWeaponBasic(self))
        self.set_collision_types(collision_class=CollisionType.PLAYER, collision_targets=CollisionTypeSet(CollisionType.ENEMY))

        self.exhaust_plume = PlayerExhaustPlume(self)
        self.sound_take_damage = global_services.safe_load_sound("assets/SpaceGunFire.wav")
        self.sound_death = global_services.safe_load_sound("assets/MissileLaunch.wav")

        global_services.set_player(self)
        global_events.player_took_damage.add(self.on_player_took_damage)

    def change_weapon(self, weapon):
        print(f"PlayerShip has weapon: {hasattr(self, '_weapon')}")
        if hasattr(self, "_weapon"):
            self._weapon.destroy()
        self._weapon = weapon
        global_events.player_weapon_changed.trigger(weapon)
        print("Weapon changed to", weapon)

    def on_player_took_damage(self, enemy_projectile):
        if self.i_frames > 0:
            print("Player took a hit, but has i-frames")
        else:
            print("Player took damage!")
            if self._weapon.level > 1:
                self.sound_take_damage.play()
                self._weapon.decresase_level()
            else:
                self.kill_player()

    def kill_player(self):
        if self.i_frames > 0:
            print("Player would have died, but has i-frames")
        else:
            self.sound_death.play()
            animation = AnimatedRenderable("assets/Simple explosion", loop=False, ticks_per_frame=5, auto_tick=True)
            hit_particle = Particle(self.rect.centerx, self.rect.centery, animation)
            hit_particle.set_scale(2)
            global_events.player_died.trigger()
            print("Game over")
            self.destroy()

    def tick(self):
        global using_mouse_controls
        if global_services.event_occured_this_tick(pygame.MOUSEMOTION) or global_services.event_occured_this_tick(pygame.MOUSEBUTTONDOWN):
            self.using_mouse_controls = True
        elif global_services.event_occured_this_tick(pygame.KEYDOWN):
            self.using_mouse_controls = False

        if self.using_mouse_controls:
            self.calculate_position_using_mouse_controls()
        else:
            self.calculate_position_using_keyboard_controls()

        # Update the position of the ship
        self.rect.center = self.x, self.y

        # Restrict ship position to screen bounds
        screen_rect = global_services.get_screen().get_rect()
        self.rect.clamp_ip(screen_rect)

        # HACK: prevent self.x and self.y from drifting too far outside the screen, since they aren't clamped but the rect is
        center_x, center_y = self.rect.center  # Unpack rect.center
        if abs(self.x - center_x) > 1.5:
            self.x = center_x
        if abs(self.y - center_y) > 1.5:
            self.y = center_y

        # Weapon logic
        self._weapon.tick(self.x, self.y)

        # Invincibility frames logic
        if self.i_frames > 0:
            self.i_frames -= 1
            if self.i_frames <= 0:
                self.renderable.set_tint((255, 255, 255), 0)
            else:
                # Make the player ship flash while invincible
                if self.i_frames % 15 == 0:
                    if self.i_frames % 30 == 0:
                        self.renderable.set_tint((255, 255, 255), 0.3)
                    else:
                        self.renderable.set_tint((0, 0, 0), 0.3)

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

    def on_collision_with_target(self, other):
        if other.get_collision_class() == CollisionType.ENEMY:
            print("Player collided with enemy!")
            self.kill_player()

    def destroy(self):
        global_events.player_took_damage.remove(self.on_player_took_damage)
        self.exhaust_plume.destroy()
        super().destroy()
