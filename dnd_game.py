from dice import D20, D8, D6, D4, D12
from classes import Bard, Fighter, Rogue, Warlock, Wizard, Paladin, Base
from weapons import Axe, Sword, Flail, Bow, Polearm, Normal, Martial

import pygame
import sys


'''
This is the main game file. It will handle the game loop, and the game logic.
Use dice.py to create a dice object, and use classes/base.py to create a character object.
The weapons are constituted in weapons package
'''

# Initialize the game
pygame.init()

# Set up the clock
clock = pygame.time.Clock()

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
secondary_font = pygame.font.Font(None, 36)
alt_font = pygame.font.Font(None, 24)
font = pygame.font.Font(None, 18)

# Set up the dice
d20 = D20()
d8 = D8()
d6 = D6()
d4 = D4()
d12 = D12()

# Set up the characters
player_one = Bard("Player One", 100, 10, 10, 10, 10, 10, 10)
player_two = Fighter("Player Two", 100, 10, 10, 10, 10, 10, 10)
player_three = Rogue("Player Three", 100, 10, 10, 10, 10, 10, 10)
player_four = Warlock("Player Four", 100, 10, 10, 10, 10, 10, 10)
player_five = Wizard("Player Five", 100, 10, 10, 10, 10, 10, 10)

enemy = Base("Bad Guy", 1500, 18, 12, 18, 16, 10, 6)

# Set up the weapons
player_one_weapon = Bow("Bow", 1, 8, 2, 25, "Ranged")
player_two_weapon = Axe("Axe", 1, 12, 5, 15, "Melee")
player_three_weapon = Sword("Sword", 1, 6, 3, 10, "Melee")
player_four_weapon = Flail("Flail", 1, 10, 2, 10, "Melee")
player_five_weapon = Polearm("Polearm", 1, 10, 6, 20, "Melee")
enemy_weapon = Polearm("Polearm", 1, 10, 6, 20, "Melee")

# Set up the game loop
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the characters
    player_text = font.render(f"{player_one.name}: {player_one.hp}", True, BLACK)
    screen.blit(player_text, (50, 50))

    enemy_text = font.render(f"{enemy.name}: {enemy.hp}", True, BLACK)
    screen.blit(enemy_text, (600, 50))

    # Draw the weapons
    if player_one_weapon:
        player_weapon_text = font.render(f"{player_one_weapon.name}: {player_one_weapon.damage.roll()}", True, BLACK)
        screen.blit(player_weapon_text, (50, 100))

    if enemy_weapon:
        enemy_weapon_text = font.render(f"{enemy_weapon.name}: {enemy_weapon.damage.roll()}", True, BLACK)
        screen.blit(enemy_weapon_text, (600, 100))

    # Draw the dice
    d20_text = font.render(f"D20: {d20.roll()}", True, BLACK)
    screen.blit(d20_text, (50, 150))

    d8_text = font.render(f"D8: {d8.roll()}", True, BLACK)
    screen.blit(d8_text, (50, 200))

    d6_text = font.render(f"D6: {d6.roll()}", True, BLACK)
    screen.blit(d6_text, (50, 250))

    d4_text = font.render(f"D4: {d4.roll()}", True, BLACK)
    screen.blit(d4_text, (50, 300))

    d12_text = font.render(f"D12: {d12.roll()}", True, BLACK)
    screen.blit(d12_text, (50, 350))

    pygame.display.flip()

pygame.quit()

# End of file
# dnd_game.py
