"""
Centralized access point for all shared modules and objects.

This module provides a single location to import and access shared resources
such as configurations, utilities, and common classes used throughout the 
application. It helps in maintaining a clean and organized codebase by 
avoiding circular dependencies and redundant imports.

Since python modules behave like singletons, this module is a quick and dirty way to
make dependencies available to all other modules without having to pass them around
"""

import pygame

from game.collision_manager import CollisionManager
from game.enemy_manager import EnemyManager


# Constants
INTERNAL_WIDTH, INTERNAL_HEIGHT = 700, 800
BG_COLOR = (0, 0, 0)
FPS_CAP = 60

# Set up the display
__screen = pygame.display.set_mode((INTERNAL_WIDTH, INTERNAL_HEIGHT))
pygame.display.set_caption("P3 - Project Pew Pew")

# Set up the clock
__clock = pygame.time.Clock()

__current_tick_events = None


def safe_load_sound(file_path) -> pygame.mixer.Sound:
    try:
        return pygame.mixer.Sound(file_path)
    except FileNotFoundError as e:
        print(f"Error loading sound file '{file_path}': {e}")
        return pygame.mixer.Sound(buffer=bytearray())


def safe_change_bgm(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)
    except:
        print(f"Error loading music file '{file_path}'")


def get_screen():
    """Return the main display surface."""
    return __screen


def clock_tick():
    """Stops the game clock until enough time has passed to not exceed the desired FPS."""
    return __clock.tick(FPS_CAP)


__current_scene = None


def get_current_scene():
    return __current_scene


def set_current_scene(scene):
    global __current_scene
    __current_scene = scene


__player_object = None


def set_player(player_object):
    global __player_object
    __player_object = player_object


def get_player():
    if __player_object is None:
        raise Exception("Player object has not been set yet")
    return __player_object


def update_events_for_current_tick(events):
    """
    Updates the pyagme events that were triggered during the current tick for other modules to access.
    """
    global __current_tick_events
    __current_tick_events = events


def get_current_tick_events():
    return __current_tick_events


def event_occured_this_tick(event_type):
    """
    True if any of the current tick events are of the specified type.
    e.g. event_has_occured(pygame.KEYDOWN) will return True if any key was pressed

    :param event_type: The type of event to check for, e.g. pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN... (see https://www.pygame.org/docs/ref/event.html)
    """
    global __current_tick_events
    return any(event.type == event_type for event in __current_tick_events)


# Specific to the main game scene


__enemy_manager = EnemyManager()
__collision_manager = CollisionManager()

__current_game_level = 0


def update_current_game_level(level):
    global __current_game_level
    __current_game_level = level


def get_current_game_level():
    return __current_game_level


def get_enemy_manager() -> EnemyManager:
    return __enemy_manager


def get_collision_manager() -> CollisionManager:
    return __collision_manager


__current_game_over_score = 0


def set_current_game_over_score(score):
    global __current_game_over_score
    __current_game_over_score = score


def get_current_game_over_score():
    return __current_game_over_score
