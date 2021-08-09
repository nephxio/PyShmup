import pygame
import objects

WIDTH, HEIGHT = int(pygame.display.Info().current_w*.75), int(pygame.display.Info().current_h*.75)
FPS = 60

SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms = pygame.USEREVENT + 1, 250

def main():

    run = True
    clock = pygame.time.Clock()
    game_window = objects.Window(WIDTH, HEIGHT, (0, 0, 0))
    pygame.time.set_timer(SPAWN_BACKGROUND_STAR_EVENT, tick_interval_ms)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == SPAWN_BACKGROUND_STAR_EVENT:
                game_window.add_new_background_objects()

            if event.type == pygame.QUIT:
                run = False

        game_window.entity_list['player'].handle_movement(pygame.key.get_pressed())
        game_window.draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
