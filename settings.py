import os
import pygame
import pygame.image
import pathlib
from pathlib import Path

pygame.init()


class Settings:
    # Window Settings
    screen_width, screen_height = int(pygame.display.Info().current_w * .75), \
                                  int(pygame.display.Info().current_h * .75)
    FPS = 60
    screen_background_color = (0, 0, 0)

    # Directories
    asset_directory = Path(pathlib.PurePath(Path.cwd(), "assets"))
    ship_assets = Path(pathlib.PurePath(Path.cwd(), "assets", "ships"))
    enemy_ship_assets = Path(pathlib.PurePath(Path.cwd(), "assets", "ships", "enemies"))
    boss_ship_assets = Path(pathlib.PurePath(Path.cwd(), "assets", "ships", "boss"))
    weapon_sprite_assets = Path(pathlib.PurePath(Path.cwd(), "assets", "weapons", "M484BulletCollection1.png"))

    # Background Object Settings
    bg_star_color = (255, 255, 255)
    bg_star_saturation_min = 40
    bg_star_saturation_max = 60
    bg_star_size_min = 1
    bg_star_size_max = 3
    bg_star_vel_modifier = 21

    # Player Settings
    player_ship_image = pygame.image.load(os.path.join(ship_assets, 'player', 'player.png'))
    player_ship_sprite = pygame.transform.scale(player_ship_image,
                                                (round(player_ship_image.get_width() * .5),
                                                 round(player_ship_image.get_height() * .5)))
    player_sprite_width = player_ship_sprite.get_width()
    player_sprite_height = player_ship_sprite.get_height()
    player_ship_initial_x = 50
    player_ship_initial_y = (screen_height / 2) - (player_ship_sprite.get_height() / 2)
    player_velocity = 6
    player_hp = 100

    # Sprite Game Data
    enemy_sprite_list = []
    boss_sprite_list = []


    @classmethod
    def load_enemy_sprites(cls):
        for file in os.scandir(cls.enemy_ship_assets):
            temp_sprite = pygame.image.load(os.path.join(cls.enemy_ship_assets, file.name))
            cls.enemy_sprite_list.append(
                pygame.transform.rotate(pygame.transform.scale(temp_sprite,
                                                              (round(temp_sprite.get_width() * 2),
                                                               round(temp_sprite.get_height() * 2))), 270))

    @classmethod
    def load_boss_sprites(cls):
        for file in os.scandir(cls.boss_ship_assets):
            temp_sprite = pygame.image.load(os.path.join(cls.boss_ship_assets, file.name))
            cls.boss_sprite_list.append(pygame.transform.rotate(pygame.transform.scale(temp_sprite,
                                                              (round(temp_sprite.get_width() * 2),
                                                               round(temp_sprite.get_height() * 2))), 270))