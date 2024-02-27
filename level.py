import pygame as pg

from copy import deepcopy
from player import Player
from food import Food
from noise_bar import Noise

from settings import *


class Level:
    def __init__(self, surface):
        self.surface = surface
        # создаёт задержку до события
        self.delay = 20
        pg.time.set_timer(NOISE_EVENT_TYPE, self.delay)
        # настраивает уровень
        self.setup_level()

    def setup_level(self):
        pos_foods = deepcopy(attribute_food['pos'])
        self.noise = 0
        self.player = Player()
        self.foods = pg.sprite.Group()
        self.noise_bar = Noise()

        for _ in range(15):
            type_food = get_type_food()
            path = get_path(type_food)
            pos = pos_foods.pop(randint(0, len(pos_foods) - 1))
            self.foods.add(Food(path, pos, type_food))

    def update(self):
        # обновляет координаты героя
        self.player.update(pg.mouse.get_pos())

        # обновляет координаты спрайтов еды
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

        # обновляет спрайт шума
        self.noise = 0 if self.noise < 0 else self.noise
        self.noise = 100 if self.noise > 100 else self.noise
        self.noise_bar.update(self.noise)

    def run(self):
        # вызывает функции обновления всех объектов
        self.update()

        # отрисовывает спрайты еды
        self.foods.draw(self.surface)
        # отрисовывает героя
        self.player.render(self.surface)
        # отрисовывает спрайт шума
        self.noise_bar.render_noise(self.surface)


