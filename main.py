import pygame
import objects
from settings import Settings

SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms = pygame.USEREVENT + 1, 250


def main():

    run = True
    clock = pygame.time.Clock()
    game_window = objects.Window(Settings.screen_width, Settings.screen_height)
    game_data = objects.GameData()
    game_state = objects.GameState(Settings.screen_background_color)

    pygame.time.set_timer(SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms)

    while run:
        clock.tick(objects.Settings.FPS)
        for event in pygame.event.get():
            if event.type == SPAWN_BACKGROUND_STAR_EVENT:
                game_state.add_new_background_objects('background_objects','background star')

            if event.type == pygame.QUIT:
                run = False

        game_state.entity_list['player'].handle_movement(pygame.key.get_pressed())
        game_window.draw_window(game_state)
    pygame.quit()


if __name__ == "__main__":
    main()
