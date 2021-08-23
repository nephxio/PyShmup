import math
import random
from entity import *
from settings import Settings

class GameState:

    def __init__(self, background_art):
        self.entity_list = {'background': background_art, 'background_objects': [], 'enemy': [],
                            'boss': [], 'projectiles': [], 'player': [], 'ui_elements': []}
        self.entity_list['player'].append(Player(50, (Settings.screen_height / 2) -
                                                 (Settings.player_sprite_height / 2),
                                                 Settings.player_velocity,
                                                 1,
                                                 'player',
                                                 Settings.player_hp, image=Settings.player_ship_sprite))

        for i in range(random.randint(Settings.bg_star_saturation_min, Settings.bg_star_saturation_max)):
            layer = random.randint(5, 7)
            self.entity_list['background_objects'].append(BackgroundStar(random.randint(0, Settings.screen_width),
                                                                         random.randint(0, Settings.screen_height),
                                                                         math.ceil(Settings.bg_star_vel_modifier / layer),
                                                                         layer,
                                                                         'background_stars',
                                                                         random.randint(Settings.bg_star_size_min,
                                                                                        Settings.bg_star_size_max),
                                                                         Settings.bg_star_color))

    def add_new_objects(self, obj, object_type: str, object_tag: str):
        if not object_type == 'background_objects':
            self.entity_list[object_type].append(obj)
        else:
            if object_tag == 'background_stars':
                for _ in range(random.randint(1, 4)):
                    layer = random.randint(5, 7)
                    self.entity_list['background_objects'].append(
                        BackgroundStar(Settings.screen_width + 10,
                                       random.randint(0, Settings.screen_height),
                                       math.ceil(Settings.bg_star_vel_modifier / layer),
                                       layer,
                                       object_tag,
                                       random.randint(Settings.bg_star_size_min, Settings.bg_star_size_max),
                                       Settings.bg_star_color))

    def remove_old_objects(self):
        for obj in self.entity_list['background_objects']:
            if obj.position_x < 0:
                self.entity_list['background_objects'].remove(obj)
