import pygame as pg
from copy import deepcopy

from player import Player
from food import Food
from noise_bar import Noise

from settings import *


class Level:
    def __init__(self, surface):
        self.surface = surface

        self.delay = 20
        pg.time.set_timer(NOISE_EVENT_TYPE, self.delay)

        self.setup_level()

    def setup_level(self):
        # настройка уровня
        self.noise = 0
        pos_foods = deepcopy(attribute_food['pos'])
        self.player = Player()
        self.foods = pg.sprite.Group()
        self.noise_bar = Noise()

        for _ in range(15):
            type_food = get_type_food()
            path = get_path(type_food)
            pos = pos_foods.pop(randint(0, len(pos_foods) - 1))
            self.foods.add(Food(path, pos, type_food))

    def update(self):
        # обновление координат героя
        self.player.update(pg.mouse.get_pos())

        # обновление координат спрайтов еды
        for food in self.foods:
            if self.player.rect_player_collision.collidepoint(food.rect.midright):
                food.rect.centerx -= 1
            if self.player.rect_player_collision.collidepoint(food.rect.midleft):
                food.rect.centerx += 1
            if self.player.rect_player_collision.collidepoint(food.rect.midtop):
                food.rect.centery += 1
            if self.player.rect_player_collision.collidepoint(food.rect.midbottom):
                food.rect.centery -= 1
            if self.player.rect_player_collision.colliderect(food.rect):
                self.noise += 1

        # обновление спрайта шума
        if self.noise < 0:
            self.noise = 0
        elif self.noise > 100:
            self.noise = 100
        self.noise_bar.update(self.noise)

    def run(self):
        # обновление всех объектов на уровне
        self.update()

        # отрисовка спрайтов еды
        self.foods.draw(self.surface)
        # отрисовка героя
        self.player.draw_paw(self.surface)
        # отрисовка спрайта шума
        self.noise_bar.draw_noise_bar(self.surface)


