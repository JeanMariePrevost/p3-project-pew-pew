import pygame
import sys
from global_services import event_occured_this_tick, get_screen, BG_COLOR, clock_tick, update_events_for_current_tick
from scenes.base_scene import BaseScene
from scenes.main_game_scene import MainGameScene

current_scene: BaseScene = None


def initial_setup():
    pygame.init()
    change_scene(MainGameScene())


def run_core_game_loop():
    """Main game loop for the entire application"""
    running = True
    while running:
        update_events_for_current_tick(pygame.event.get())
        if event_occured_this_tick(pygame.QUIT):
            print("Quit event detected, exiting game loop")
            running = False

        if current_scene is not None:
            current_scene.tick()
            current_scene.draw(get_screen())

        pygame.display.flip()  # Update the display with the buffer
        clock_tick()  # Cap the frame rate, sleep until it's time for the next frame

    # Game loop has been exited, quit Pygame
    print("Core loop exited, quitting Pygame")
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
