import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # создание слоя игрока
        self.image = pg.image.load('images/player.png')
        self.rect_player = self.image.get_rect()
        # создание коллизии для игрока
        self.player_collision = pg.Surface((42, 42))
        self.rect_player_collision = self.player_collision.get_rect()

    def draw_paw(self, surface):
        # отображение героя на экране
        surface.blit(self.player_collision, self.rect_player_collision)
        surface.blit(self.image, self.rect_player)



    def update(self, pos):
        # обновление координат героя
        self.rect_player_collision.center = pos
        self.rect_player.top = self.rect_player_collision.top - 25
        self.rect_player.right = self.rect_player_collision.right + 26


