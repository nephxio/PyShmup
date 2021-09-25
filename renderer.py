import pygame
from settings import Settings
from spritesheet import SpriteSheet

pygame.init()


class Window:

    def __init__(self, window_w: int, window_h: int):
        self.WIN = pygame.display.set_mode((window_w, window_h))
        self.sheet = SpriteSheet(Settings.weapon_sprite_assets)

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
        weapon_rect = (0, 0, 60, 90)
        weapon_img = self.sheet.load_strip(weapon_rect, 4)
        self.WIN.blit(weapon_img[0], 50, 500)

        # for x, bullet in enumerate(weapon_img):
        #     self.WIN.blit(bullet, (x*50 + 500, 500))

    def draw_layer(self, obj_list: list):
        for obj in obj_list:
            obj.draw(self.WIN)
            if obj.draw_layer > 4:
                obj.position_x -= obj.velocity
