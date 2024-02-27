import pygame as pg


class Food(pg.sprite.Sprite):
    def __init__(self, path, pos, type_food):
        super().__init__()
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=pos)
        self.type_food = type_food
