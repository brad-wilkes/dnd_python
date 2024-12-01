from classes.base import Base
from dice import D20, D8, D6, D4, D12

import pygame

'''
This is the main game file. It will handle the game loop, and the game logic.
Use dice.py to create a dice object, and use classes/base.py to create a character object.
The weapons are constituted in weapons package
'''

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("D&D Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the dice
d20 = D20()
d8 = D8()
d6 = D6()
d4 = D4()
d12 = D12()

# Set up the characters
player = Base("Player", 100)
enemy = Base("Enemy", 100)

# Set up the weapons
player_weapon = None
enemy_weapon = None

# Set up the game loop
running = True

while running:
    screen.fill(WHITE)



    pygame.display.flip()

pygame.quit()

# End of file
# dnd_game.py
