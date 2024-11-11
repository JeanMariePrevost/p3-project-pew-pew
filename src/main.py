import pygame
import sys
import typing
from game.player_ship import PlayerShip
from global_services import get_screen, BG_COLOR, clock_tick
from scenes.base_scene import BaseScene
from scenes.main_game_scene import MainGameScene

current_scene = None


def initial_setup():
    pygame.init()
    change_scene(MainGameScene())


def run_core_game_loop():
    """Main game loop for the entire application"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_scene is not None:
            current_scene.tick()
            current_scene.draw(get_screen())

        pygame.display.flip()  # Update the display with the buffer
        clock_tick()  # Cap the frame rate, sleep until it's time for the next frame

    # Game loop has been exited, quit Pygame
    pygame.quit()
    sys.exit()


def change_scene(new_scene: BaseScene):
    global current_scene
    if current_scene is not None:
        print(f"Changing scene from [{current_scene}] to [{new_scene}]")
        current_scene.destroy()
    else:
        print(f"Changing from [no scene] to [{new_scene}]")
    current_scene = new_scene


if __name__ == "__main__":
    initial_setup()
    run_core_game_loop()
