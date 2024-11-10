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


# Constants
INTERNAL_WIDTH, INTERNAL_HEIGHT = 700, 800
BG_COLOR = (0, 0, 0)

# Set up the display
__screen = pygame.display.set_mode((INTERNAL_WIDTH, INTERNAL_HEIGHT))
pygame.display.set_caption("P3 - Project Pew Pew")


def get_screen():
    """Return the main display surface."""
    return __screen
