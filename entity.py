import pygame
from settings import Settings

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
        pygame.draw.circle(surface, self.color, (self.position_x, self.position_y), self.obj_radius)
