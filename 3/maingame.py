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

# GAME VARIABLES #
word_file = "dictionary.txt"
WORDS = open(word_file).read().splitlines()
word = random.choice(WORDS).upper()[1:-1]
word_display = ""
for char in word:
	word_display += "_ "

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hangman')

def draw(canvas):
	global word, word_display

	canvas.fill(WHITE)

	# create labels for gameplay #

	# word display label #
	myfont2 = pygame.font.SysFont(None, 20)
	label2 = myfont2.render(word_display, 1, BLACK)
	canvas.blit(label2, (WIDTH // 2 - WIDTH // 8, HEIGHT // 2 + HEIGHT // 8))

while True:
	draw(window)

	pygame.display.update()
	fps.tick(60)