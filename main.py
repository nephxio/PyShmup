import objects
from renderer import *
from settings import Settings

SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms = pygame.USEREVENT + 1, 250


def main():

    run = True
    clock = pygame.time.Clock()
    game_window = Window(Settings.screen_width, Settings.screen_height)
    Settings.load_enemy_sprites()
    Settings.load_boss_sprites()
    game_state = objects.GameState(Settings.screen_background_color)

    pygame.time.set_timer(SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms)

    while run:
        clock.tick(Settings.FPS)
        for event in pygame.event.get():
            if event.type == SPAWN_BACKGROUND_STAR_EVENT:
                game_state.add_new_objects(None, 'background_objects', 'background_stars')

            if event.type == pygame.QUIT:
                run = False
        if len(game_state.entity_list['player']) >= 0:
            for player in game_state.entity_list['player']:
                player.handle_movement(pygame.key.get_pressed())
        game_window.draw_window(game_state)
    pygame.quit()


if __name__ == "__main__":
    main()
