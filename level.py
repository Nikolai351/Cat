import pygame as pg

from player import Player
from food import Food
from noise_bar import Noise

from settings import *


class Level:
    def __init__(self, surface):
        self.surface = surface
        self.win = False
        self.game_over = False
        self.good_sound = pg.mixer.Sound('sound/good.mp3')
        self.bad_sound = pg.mixer.Sound('sound/bad.mp3')
        # создаёт задержку до события
        self.delay = 50
        pg.time.set_timer(NOISE_EVENT_TYPE, self.delay)
        # настраивает уровень
        self.setup_level()

    def setup_level(self):
        self.noise = 0
        self.count_smile_cat = 0

        self.player = Player()
        self.foods = pg.sprite.Group()
        self.noise_bar = Noise()

        count_good_food = 0
        for _ in range(25):
            # определяет минимальное количество "хорошей" еды
            type_food = get_type_food()
            if count_good_food < 5:
                type_food = 'good'
                count_good_food += 1
            # определяет путь к изображению в зависимости от типа еды
            path = get_path(type_food)
            # создаёт экземпляр класса еды
            new_food = Food(path, type_food)
            # получение списка атрибутов rect класса food
            rect_foods = [food.rect for food in self.foods]
            # проверка на пересечение с другой едой
            while new_food.rect.collidelistall(rect_foods):
                new_food = Food(path, type_food)

            self.foods.add(new_food)

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

    def check_win(self):
        # создание изображения для эмоции кота
        image_cat = pg.image.load(f'images/emotion_cat/{self.count_smile_cat}.png')
        rect_image_cat = image_cat.get_rect(topleft=(730, 10))
        # отрисовывает коллизию внизу экрана для проверки съеденной еды
        collision_for_food = pg.surface.Surface((800, 20))
        collision_for_food.fill((238, 195, 154))
        rect_collision_for_food = collision_for_food.get_rect(topleft=(0, 580))
        # проверка касания спрайтов коллизии
        for food in self.foods:
            if rect_collision_for_food.colliderect(food.rect):
                if food.type_food == 'good':
                    self.count_smile_cat += 1
                    self.good_sound.play()
                else:
                    self.bad_sound.play()
                food.kill()
        # отрисовывает лицо котика
        self.surface.blit(image_cat, rect_image_cat)

        self.win = True if self.count_smile_cat >= 5 else False

    def run(self):
        # вызывает функции обновления всех объектов
        self.update()

        # отрисовывает спрайты еды
        self.foods.draw(self.surface)
        # отрисовывает героя
        self.player.render(self.surface)
        # отрисовывает спрайт шума
        self.noise_bar.render_noise(self.surface)
        # проверяет условие победы
        self.check_win()
        # проверяет условие проигрыша
        if self.noise >= 100:
            self.game_over = True







