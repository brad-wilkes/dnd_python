from dice import D20, D8, D6, D4, D12, D10
from classes import Bard, Fighter, Rogue, Warlock, Wizard, Paladin, Base
from weapons import Axe, Sword, Flail, Bow, Polearm, Simple, Exotic, Quarterstaff, Dagger
from ui.game_ui import GameUI

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
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
VIOLET = (148, 0, 211)
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
d10 = D10()
dice_results = {
    "d20": d20.roll(),
    "d8": d8.roll(),
    "d6": d6.roll(),
    "d4": d4.roll(),
    "d12": d12.roll(),
    "d10": d10.roll()
}

# Set up the characters
player_one = Rogue("Player One", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_two = Fighter("Player Two", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_three = Warlock("Player Three", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
enemy = Fighter("Bad Guy", 1500, 18, 12, 18, 16, 10, 6)

def reroll_stats(player):
    player.strength = d6.stat_roll_sum()
    player.dexterity = d6.stat_roll_sum()
    player.constitution = d6.stat_roll_sum()
    player.intelligence = d6.stat_roll_sum()
    player.wisdom = d6.stat_roll_sum()
    player.charisma = d6.stat_roll_sum()

def reroll_dice():
    dice_results["d20"] = d20.roll()
    dice_results["d8"] = d8.roll()
    dice_results["d6"] = d6.roll()
    dice_results["d4"] = d4.roll()
    dice_results["d12"] = d12.roll()
    dice_results["d10"] = d10.roll()

def main():
    game_ui = GameUI()
    running = True
    rolls_done = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                action = game_ui.check_button_clicks(event.pos)
                if action == "reroll_dice":
                    reroll_dice()
                    rolls_done = False
                elif action == "reroll_stats":
                    reroll_stats(player_one)
                    rolls_done = False

        if not rolls_done:
            game_ui.draw_screen(player_one, enemy, dice_results)
            rolls_done = True

        game_ui.tick()

    game_ui.quit()

if __name__ == "__main__":
    main()

# End of file
# dnd_game.py