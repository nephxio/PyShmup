import pygame
import pygame.display
import random

pygame.init()

STARFIELD_SATURATION_MIN = 40
STARFIELD_SATURATION_MAX = 60

STAR_SIZE_MIN = 1
STAR_SIZE_MAX = 3

class Background_Star:

    def __init__(self, layer, radius, vel, coord_x, coord_y):
        self.draw_layer = layer
        self.star_radius = radius
        self.velocity = vel
        self.position_x = coord_x
        self.position_y = coord_y
        self_color = (255, 255, 255)

class Window:

    def __init__(self, window_w, window_h, background_art):
        self.width, self.height = window_w, window_h
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.entity_list = { 'background': background_art, 'background_objects': [], 'enemy': [], 'boss': None, 'projectiles': [], 'player': None, 'ui_elements': [] }

        for i in range(random.randint(STARFIELD_SATURATION_MIN, STARFIELD_SATURATION_MAX)):
            self.entity_list['background_objects'].append(Background_Star(random.randint(1, 3), random.randint(STAR_SIZE_MIN, STAR_SIZE_MAX), 3, random.randint(0, self.width), random.randint(0, self.height)))

    def draw_window(self):
        self.WIN.fill((self.entity_list['background']))
        self.draw_stars(self.entity_list['background_objects'])
        pygame.display.update()
        self.remove_old_stars()

    def draw_stars(self, star_list):
       for star in star_list:
            pygame.draw.circle(self.WIN,(255, 255, 255), (star.position_x, star.position_y), star.star_radius)
            star.position_x -= star.velocity

    def add_new_stars(self):
        for i in range(random.randint(1, 4)):
            layer = random.randint(1, 3)
            self.entity_list['background_objects'].append(Background_Star(layer, random.randint(STAR_SIZE_MIN, STAR_SIZE_MAX), layer*2, self.width + 10, random.randint(0, self.height)))


    def remove_old_stars(self):
        for obj in self.entity_list['background_objects']:
            if obj.position_x < 0:
                self.entity_list['background_objects'].remove(obj)


