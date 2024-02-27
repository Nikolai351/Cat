import pygame as pg
import sys

from settings import *
from level import Level


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.level = Level(self.screen)

    def run(self):
        while True:

            self.screen.fill((46, 143, 110))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == NOISE_EVENT_TYPE:
                    self.level.noise -= 1

            self.level.run()

            pg.display.flip()
            self.clock.tick(FPS)


Game().run()
