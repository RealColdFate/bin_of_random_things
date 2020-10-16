import pygame
import os

FRAME_RATE = 60
BLOCK_SIZE = 25
GAME_CLOCK_SPEED = 7
SCORE_INCREMENT = 10
PIXEL_BOARDER = 10

WIN_WIDTH = 625
WIN_HEIGHT = 625

SNAKE_START_X = 300
SNAKE_START_Y = 300

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

SNAKE_IMGS = [pygame.image.load(os.path.join("images", 'SnakeBody.png')),
              pygame.image.load(os.path.join("images", 'SnakeHead.png')),
              pygame.image.load(os.path.join("images", 'SnakeTail.png')),
              pygame.image.load(os.path.join("images", 'SnakeBend.png'))]
APPLE_IMG = pygame.image.load(os.path.join("images", 'apple.png'))
