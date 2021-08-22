import pygame
import pygame.display
import random
from settings import Settings
from spritesheet import SpriteSheet

pygame.init()


class GameObject:

    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, image=None):
        self.image = image
        self.position_x = coord_x
        self.position_y = coord_y
        self.velocity = vel
        self.draw_layer = layer
        self.obj_type = obj_tag


class Entity(GameObject):

    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, hp: int, image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, image)
        self.hitpoints = hp

    def handle_movement(self, keys_pressed):
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and (self.position_y - self.velocity >= 0):
            self.position_y -= self.velocity
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and (self.position_y + self.velocity +
                                                                          Settings.player_ship_sprite.get_height() <=
                                                                          pygame.display.get_surface().get_height()):
            self.position_y += self.velocity
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and (self.position_x - self.velocity >= 0):
            self.position_x -= self.velocity
        if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and (self.position_x + self.velocity +
                                                                           Settings.player_sprite_width) <= \
                                                                           pygame.display.get_surface().get_width():
            self.position_x += self.velocity

    def draw(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))


class Player(Entity):
    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, hp: int, image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, hp, image)


class Enemy(Entity):
    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, hp: int, image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, hp, image)


class Boss(Entity):
    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, hp: int, image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, hp, image)


class BackgroundObject(GameObject):

    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, image)


class BackgroundStar(BackgroundObject):

    def __init__(self, coord_x: int, coord_y: int, vel: int, layer: int, obj_tag: str, radius: int,
                 obj_color: tuple[int, int, int], image=None):
        super().__init__(coord_x, coord_y, vel, layer, obj_tag, image)
        self.obj_radius = radius
        self.color = obj_color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color , (self.position_x, self.position_y), self.obj_radius)


class GameData:

    def __init__(self):
        self.enemy_ship_sprites = Settings.load_enemy_sprites()


class GameState:

    def __init__(self, background_art):
        self.entity_list = {'background': background_art, 'background_objects': [], 'enemy': [],
                            'boss': None, 'projectiles': [], 'player': None, 'ui_elements': []}
        self.entity_list['player'] = Player(50, (Settings.screen_height / 2) -
                                            (Settings.player_sprite_height / 2),
                                            Settings.player_velocity,
                                            1,
                                            'player',
                                            Settings.player_hp, image=Settings.player_ship_sprite)

        for i in range(random.randint(Settings.bg_star_saturation_min, Settings.bg_star_saturation_max)):
            self.entity_list['background_objects'].append(BackgroundStar(random.randint(0, Settings.screen_width),
                                                                         random.randint(0, Settings.screen_height),
                                                                         3,
                                                                         random.randint(1, 3),
                                                                         'background_stars',
                                                                         random.randint(Settings.bg_star_size_min,
                                                                                        Settings.bg_star_size_max),
                                                                         Settings.bg_star_color))

    def add_new_objects(self, object_type: str, object_tag: str):
        if object_tag == 'background_stars':
            for _ in range(random.randint(1, 4)):
                layer = random.randint(1, 3)
                self.entity_list['background_objects'].append(
                    BackgroundStar(Settings.screen_width + 10,
                                   random.randint(0, Settings.screen_height),
                                   layer * Settings.bg_star_vel_modifier,
                                   layer,
                                   object_tag,
                                   random.randint(Settings.bg_star_size_min, Settings.bg_star_size_max),
                                   Settings.bg_star_color))

    def remove_old_objects(self):
        for obj in self.entity_list['background_objects']:
            if obj.position_x < 0:
                self.entity_list['background_objects'].remove(obj)


class Window:

    def __init__(self, window_w: int, window_h: int):
        self.WIN = pygame.display.set_mode((window_w, window_h))

    def draw_window(self, game_state):
        self.WIN.fill(game_state.entity_list['background'])
        self.draw_background_objects(game_state.entity_list['background_objects'])
        game_state.entity_list['player'].draw(self.WIN)
        pygame.display.update()
        game_state.remove_old_objects()

    def draw_background_objects(self, obj_list: list):
        for obj in obj_list:
            obj.draw(self.WIN)
            obj.position_x -= obj.velocity

    def draw_enemies(self, enemy_list: list):
        for enemy in enemy_list:
            enemy.draw()
