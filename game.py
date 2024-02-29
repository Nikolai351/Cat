import pygame as pg
import sys

from settings import *
from level import Level
from button import Button


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

    def run(self):
            self.main_menu()

            pg.quit()
            sys.exit()

    def main_menu(self):
        pg.mouse.set_visible(True)
        pg.display.set_caption('Главное меню')

        font = pg.font.Font(None, 72)
        text_surface = font.render('ГЛАВНОЕ МЕНЮ', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

        play_button = Button(SCREEN_WIDTH // 2 - 50, 100, 'images/buttons/PlayIcon.png',
                             'images/buttons/PlayIconClick.png')
        option_button = Button(SCREEN_WIDTH // 2 - 50, 250, 'images/buttons/OptIcon.png',
                               'images/buttons/OptIconClick.png')
        exit_button = Button(SCREEN_WIDTH // 2 - 50, 400, 'images/buttons/ExitIcon.png',
                             'images/buttons/ExitIconClick.png')

        running = True
        while running:
            self.screen.fill((255, 234, 12))

            self.screen.blit(text_surface, text_rect)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.USEREVENT and event.button == exit_button:
                    running = False
                if event.type == pg.USEREVENT and event.button == option_button:
                    self.settings_menu()
                if event.type == pg.USEREVENT and event.button == play_button:
                    self.play()

                for btn in [play_button, option_button, exit_button]:
                    btn.handle_event(event)

            for btn in [play_button, option_button, exit_button]:
                btn.check_hover(pg.mouse.get_pos())
                btn.render(self.screen)

            pg.display.flip()
            self.clock.tick(FPS)

    def settings_menu(self):
        pg.mouse.set_visible(True)
        pg.display.set_caption('Настройки')

        font = pg.font.Font(None, 72)
        text_surface = font.render('НАСТРОЙКИ',True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

        back_button = Button(SCREEN_WIDTH // 2 - 50, 400, 'images/buttons/BackIcon.png',
                             'images/buttons/BackIconClick.png')

        running = True
        while running:
            self.screen.fill((255, 234, 12))
            self.screen.blit(text_surface, text_rect)

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

            pg.display.flip()
            self.clock.tick(FPS)

    def play(self):
        pg.mouse.set_visible(False)
        pg.display.set_caption('Название игры')

        level = Level(self.screen)

        running = True
        while running:

            self.screen.fill((223, 123, 123))

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

            pg.display.flip()
            self.clock.tick(FPS)


Game().run()
