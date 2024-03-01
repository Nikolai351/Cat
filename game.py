import pygame as pg
import sys

from settings import *
from level import Level
from button import Button


class Game:
    def __init__(self):
        pg.init()
        self.music = pg.mixer.Sound('sound/1.mp3')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.bg_x = 0
        self.bg_color_menu = pg.Color((238, 195, 154))
        pg.display.set_caption('NOISE CAT')

        self.win = False
        self.game_over = False

    def run(self):
            self.music.play(-1)
            self.main_menu()
            pg.quit()
            sys.exit()

    def scrool_bg_x(self):
        self.bg_x -= 1
        if self.bg_x <= -1570:
            self.bg_x = 0

    def main_menu(self):
        pg.mouse.set_visible(True)

        title_game = pg.image.load('images/title_game.png')

        image_table = pg.image.load('images/table.png')
        rect_image_title = image_table.get_rect(topleft=(SCREEN_WIDTH // 2 - 300, 20))

        font = pg.font.Font(None, 30)

        play_button = Button(SCREEN_WIDTH // 2 - 50, 170, 'images/buttons/PlayIcon.png',
                             'images/buttons/PlayIconClick.png')
        option_button = Button(SCREEN_WIDTH // 2 - 50, 300, 'images/buttons/OptIcon.png',
                               'images/buttons/OptIconClick.png')
        exit_button = Button(SCREEN_WIDTH // 2 - 50, 430, 'images/buttons/ExitIcon.png',
                             'images/buttons/ExitIconClick.png')

        running = True
        while running:
            window_event = pg.surface.Surface((150, 100))
            window_event.fill(self.bg_color_menu)
            rect_window_event = window_event.get_rect(topleft=(100, 200))

            self.screen.fill(self.bg_color_menu)

            self.screen.blit(title_game, rect_image_title)

            self.screen.blit(image_table, (self.bg_x, 150))
            self.screen.blit(image_table, (self.bg_x + 1570, 150))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.USEREVENT and event.button == exit_button:
                    running = False
                if event.type == pg.USEREVENT and event.button == option_button:
                    self.settings_menu()
                if event.type == pg.USEREVENT and event.button == play_button:
                    self.win = False
                    self.game_over = False

                    self.play()

                for btn in [play_button, option_button, exit_button]:
                    btn.handle_event(event)

            for btn in [play_button, option_button, exit_button]:
                btn.check_hover(pg.mouse.get_pos())
                btn.render(self.screen)

            self.scrool_bg_x()

            if self.win:
                image = pg.image.load('images/emotion_cat/win.png')
                rect_image = image.get_rect(topleft=(50, 40))
                text = font.render('ПОБЕДА!!!', True, (255, 255, 255))
                rect_text = text.get_rect(topleft=(20, 10))
            elif self.game_over:
                image = pg.image.load('images/emotion_cat/lose.png')
                rect_image = image.get_rect(topleft=(50, 40))
                text = font.render('ПРОИГРЫШ!!!', True, (255, 255, 255))
                rect_text = text.get_rect(topleft=(5, 10))

            if self.game_over or self.win:
                window_event.blit(text, rect_text)
                window_event.blit(image, rect_image)
                self.screen.blit(window_event, rect_window_event)

            pg.display.flip()
            self.clock.tick(FPS)

    def settings_menu(self):
        pg.mouse.set_visible(True)

        font = pg.font.Font(None, 72)
        text_surface = font.render('не сделал настройки', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

        image_table = pg.image.load('images/table.png')

        back_button = Button(SCREEN_WIDTH // 2 - 50, 430, 'images/buttons/BackIcon.png',
                             'images/buttons/BackIconClick.png')

        running = True

        while running:
            self.screen.fill(self.bg_color_menu)

            self.screen.blit(text_surface, text_rect)

            self.screen.blit(image_table, (self.bg_x, 150))
            self.screen.blit(image_table, (self.bg_x + 1570, 150))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                if event.type == pg.USEREVENT and event.button == back_button:
                    running = False

                back_button.handle_event(event)

            back_button.check_hover(pg.mouse.get_pos())
            back_button.render(self.screen)

            self.scrool_bg_x()

            pg.display.flip()
            self.clock.tick(FPS)

    def play(self):
        pg.mouse.set_visible(False)

        table_image = pg.image.load('images/table_for_game.png')
        rect_table_image = table_image.get_rect(topleft=(0, 80))

        level = Level(self.screen)

        running = True
        while running:

            self.screen.fill(self.bg_color_menu)

            self.screen.blit(table_image, rect_table_image)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.mouse.set_visible(True)
                        running = False
                if event.type == NOISE_EVENT_TYPE:
                    level.noise -= 1

            level.run()

            if level.win or level.game_over:
                self.win = level.win
                self.game_over = level.game_over
                running = False
                pg.mouse.set_visible(True)

            pg.display.flip()
            self.clock.tick(FPS)


Game().run()
