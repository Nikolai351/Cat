from random import randint


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
NOISE_EVENT_TYPE = 30


def get_path(type):
    return f'images/{type}_food/{randint(1, 19)}.png'


def get_type_food():
    return ['good', 'bad'][randint(0, 1)]
