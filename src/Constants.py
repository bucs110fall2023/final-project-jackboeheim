import pygame
from math import pi

WOLRD_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 3, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

#Colors:
DARK_GREY = pygame.Color(96,96,96)
LIGHT_GRAY = pygame.Color(160,160,160)
BLUE = pygame.Color(0,0,255)
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)

WALL_COLOR = [0,BLUE, RED, GREEN]

MAP_SIZE = (len(WOLRD_MAP[0]), len(WOLRD_MAP))
SCREEN_SIZE = (800,800)
SCREEN_HEIGHT = SCREEN_SIZE[1]
SCREEN_WIDTH = SCREEN_SIZE[0]
CLOCK = pygame.time.Clock()
MAP_LEGEND = [LIGHT_GRAY,DARK_GREY]
SQUARE_LENGTH = SCREEN_WIDTH / MAP_SIZE[0]
NUM_RAYS = 200
FOV = pi/3
DELTA_THETA = FOV / NUM_RAYS
LINE_WIDTH = int(SCREEN_WIDTH / NUM_RAYS)
ROT_SPEED = .12
MOVEMENT_SPEED = .06
