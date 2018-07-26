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
guess = ""
remaining_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
notice = "Guess a letter"
wrong_guesses_count = 0
end_game = False

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hangman')

def draw(canvas):
	global word, word_display, guess, remaining_letters, notice, wrong_guesses_count, end_game

	# create game canvas #
	canvas.fill(WHITE)
	pygame.draw.line(canvas, BLACK, [0, HEIGHT // 2 + HEIGHT // 4], [WIDTH, HEIGHT // 2 + HEIGHT // 4], 1)

	if guess != "":
		notice = ""
		guess_in_word = False
		if guess in remaining_letters:
			index = 0
			for char in word:
				if guess == char:
					guess_in_word = True
					word_display = word_display[:index * 2] + char + word_display[index * 2 + 1:]
				index += 1
			letter_index = remaining_letters.find(guess)
			remaining_letters = remaining_letters[:letter_index:] + remaining_letters[letter_index + 1::]
			if guess_in_word != True:
				notice = "That letter isn't in the word! Guess a different letter!"
				wrong_guesses_count += 1
			else:
				notice = "Guess another letter!"
		else:
			notice = "You already guessed that letter! Try one of the remaining letters in the alphabet!"
		guess = ""

	# draw hangman #
		# draw hangman tower #
			# baseline #
	pygame.draw.line(canvas, BLACK, [WIDTH // 2 + WIDTH // 16, HEIGHT // 2], [WIDTH // 2 + WIDTH // 4 - WIDTH // 16, HEIGHT // 2], 1)
			# tall pole #
	pygame.draw.line(canvas, BLACK, [WIDTH // 2 + WIDTH // 8, HEIGHT // 2], [WIDTH // 2 + WIDTH // 8, HEIGHT // 6], 1)
			# horizontal line #
	pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6], [WIDTH // 2 + WIDTH // 8, HEIGHT // 6], 1)
			# small pole #
	pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12], [WIDTH // 2, HEIGHT // 6], 1)
		# draw head #
	if wrong_guesses_count >= 1:
		pygame.draw.circle(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 10], 10, 1)
		# draw body #
	if wrong_guesses_count >= 2:
		pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 20], [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 70], 1)
		# draw right arm #
	if wrong_guesses_count >= 3:
		pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 25], [WIDTH // 2 - WIDTH // 32, HEIGHT // 6 + HEIGHT // 12 + 35], 1)
		# draw left arm #
	if wrong_guesses_count >= 4:
		pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 25], [WIDTH // 2 + WIDTH // 32, HEIGHT // 6 + HEIGHT // 12 + 35], 1)
		# draw right leg #	
	if wrong_guesses_count >= 5:
		pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 70], [WIDTH // 2 - WIDTH // 32, HEIGHT // 6 + HEIGHT // 12 + 85], 1)
		# draw left leg #
	if wrong_guesses_count >= 6:
		pygame.draw.line(canvas, BLACK, [WIDTH // 2, HEIGHT // 6 + HEIGHT // 12 + 70], [WIDTH // 2 + WIDTH // 32, HEIGHT // 6 + HEIGHT // 12 + 85], 1)

	# create labels for gameplay #

	# you win display label #
	# if no more _ in word display, the player must have guessed all the letters in the word #
	if "_" not in word_display:
		end_game = True
		canvas.fill(BLACK)
		canvas.fill(BLACK)
		myfont2 = pygame.font.SysFont(None, 60)
		endgame_label = myfont2.render("YOU WON!", 1, WHITE)
		canvas.blit(endgame_label, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2))
		myfont2 = pygame.font.SysFont(None, 30)
		word_label = myfont2.render("Your word was " + word, 1, WHITE)
		canvas.blit(word_label, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 8 + HEIGHT // 16))
		myfont2 = pygame.font.SysFont(None, 30)
		explain = myfont2.render("press any button to exit", 1, WHITE)
		canvas.blit(explain, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 4))

	# you lost display label #
	# if the player guessed wrongly six times then the whole man is hung and they lost #
	if wrong_guesses_count == 6:
		end_game = True
		canvas.fill(BLACK)
		myfont2 = pygame.font.SysFont(None, 60)
		endgame_label = myfont2.render("YOU LOST", 1, WHITE)
		canvas.blit(endgame_label, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2))
		myfont2 = pygame.font.SysFont(None, 30)
		word_label = myfont2.render("Your word was " + word, 1, WHITE)
		canvas.blit(word_label, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 8 + HEIGHT // 16))
		myfont2 = pygame.font.SysFont(None, 30)
		explain = myfont2.render("press any button to exit", 1, WHITE)
		canvas.blit(explain, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 4))

	# word display label #
	myfont2 = pygame.font.SysFont(None, 20)
	label2 = myfont2.render(word_display, 1, BLACK)
	canvas.blit(label2, (WIDTH // 2 - WIDTH // 8, HEIGHT // 2 + HEIGHT // 8))

	# notice label #
	myfont1 = pygame.font.SysFont(None, 20)
	notice1 = myfont1.render(notice, 1, BLACK)
	canvas.blit(notice1, (30, HEIGHT // 2 + HEIGHT // 4 + HEIGHT // 16))

	# remaining letters label #
	myfont1 = pygame.font.SysFont(None, 20)
	alphabet = myfont1.render("Letters: " + remaining_letters, 1, BLACK)
	canvas.blit(alphabet, (30, HEIGHT // 2 + HEIGHT // 4 + HEIGHT // 8))


def keydown(event):
	global guess, end_game

	if end_game == True:
		pygame.quit()
		sys.exit()

	if event.unicode.isalpha():
		guess = event.unicode.upper()

init()

while True:
	draw(window)

	for event in pygame.event.get():

		if event.type == KEYDOWN:
			keydown(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fps.tick(60)