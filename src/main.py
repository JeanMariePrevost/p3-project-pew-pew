import pygame
import sys
from game import memory_debugger
import global_events
from global_services import event_occured_this_tick, get_screen, clock_tick, update_events_for_current_tick
from menu.main_menu_scene import MainMenuScene
from scenes.base_scene import BaseScene
from scenes.main_game_scene import MainGameScene

current_scene: BaseScene = None


def initial_setup():
    print("Initial setup")
    pygame.init()
    pygame.mixer.init()
    # change_scene(MainGameScene())
    # change_scene(MainMenuScene())
    start_scene_transition(None, MainMenuScene, fadeout_ms=0, pause_ms=0, fadein_ms=300)
    print("Initial setup complete")


def run_core_game_loop():
    """Main game loop for the entire application"""
    running = True
    while running:
        update_events_for_current_tick(pygame.event.get())
        if event_occured_this_tick(pygame.QUIT):
            print("Quit event detected, exiting game loop")
            running = False

        # DEBUG - press F1 to print all objects using gc
        if event_occured_this_tick(pygame.KEYDOWN) and pygame.key.get_pressed()[pygame.K_F1]:
            memory_debugger.print_debug_info()

        if current_scene is not None:
            current_scene.tick()
            current_scene.draw(get_screen())

        global_events.tick_signal.trigger()  # Global "unsafe" ticking signal
        global_events.draw_signal.trigger(get_screen())  # Global "unsafe" drawing signal

        pygame.display.flip()  # Update the display with the buffer
        clock_tick()  # Cap the frame rate, sleep until it's time for the next frame

    # Game loop has been exited, quit Pygame
    print("Core loop exited, quitting Pygame")
    pygame.quit()
    sys.exit()


def start_scene_transition(from_scene: BaseScene | None, target_scene_class: type, fadeout_ms: int = 300, pause_ms=300, fadein_ms: int = 300):
    assert isinstance(from_scene, BaseScene) or from_scene is None
    assert isinstance(target_scene_class, type)
    if from_scene is not None:
        from_scene.fade_out_complete_signal.add_once(lambda: finish_scene_transition(target_scene_class, pause_ms, fadein_ms))
        from_scene.fade_out_then_destroy(fadeout_ms)
    else:
        finish_scene_transition(target_scene_class, pause_ms, fadein_ms)


def finish_scene_transition(target_scene_class, pause_ms, fadein_ms):
    # Pause for a moment before fading in
    pygame.time.wait(pause_ms)
    target_scene = target_scene_class()
    change_scene(target_scene)
    target_scene.fade_in(fadein_ms)


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
