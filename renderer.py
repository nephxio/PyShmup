import pygame

pygame.init()


class Window:

    def __init__(self, window_w: int, window_h: int):
        self.WIN = pygame.display.set_mode((window_w, window_h))

    def draw_window(self, game_state):
        self.draw_all_objects(game_state)
        pygame.display.update()
        game_state.remove_old_objects()

    def draw_all_objects(self, game_state):
        self.WIN.fill(game_state.entity_list['background'])
        self.draw_layer(game_state.entity_list['background_objects'])
        self.draw_layer(game_state.entity_list['enemy'])
        self.draw_layer(game_state.entity_list['boss'])
        self.draw_layer(game_state.entity_list['projectiles'])
        self.draw_layer(game_state.entity_list['player'])
        self.draw_layer(game_state.entity_list['ui_elements'])

    def draw_layer(self, obj_list: list):
        for obj in obj_list:
            obj.draw(self.WIN)
            if obj.draw_layer > 4:
                obj.position_x -= obj.velocity
