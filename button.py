import pygame as pg


class Button:
    def __init__(self, x, y, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (100, 100))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pg.image.load(hover_image_path)
            self.hover_image = pg.transform.scale(self.hover_image, (100, 100))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)
        self.is_hovered = False

    def render(self, surface):
        current_image = self.hover_image if self.is_hovered else self.image
        surface.blit(current_image, self.rect.topleft)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
