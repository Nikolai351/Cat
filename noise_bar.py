import pygame as pg


class Noise(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('images/noise_bar/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(10, 10))

    def render_noise(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, noise):
        self.image = pg.image.load((f'images/noise_bar/{noise // 10}.png')).convert_alpha()
