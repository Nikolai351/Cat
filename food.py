import pygame as pg

from settings import *


class Food(pg.sprite.Sprite):
    def __init__(self, path, type_food):
        super().__init__()
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=(randint(32, SCREEN_WIDTH - 32), randint(80 + 32, 580 - 32)))
        self.type_food = type_food
