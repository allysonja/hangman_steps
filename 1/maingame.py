import random
import pygame
import sys
from pygame import *

pygame.init()
fps = pygame.time.Clock()

# CONSTANTS #
# DIMENSIONS #
WIDTH = 600
HEIGHT = 400

# COLORS #
WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hangman')

def draw(canvas):
	canvas.fill(WHITE)

while True:
	draw(window)

	pygame.display.update()
	fps.tick(60)