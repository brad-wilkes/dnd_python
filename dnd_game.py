from dice import D20, D8, D6, D4, D12, D10
from classes import Bard, Fighter, Rogue, Warlock, Wizard, Paladin, Base
from weapons import Axe, Sword, Flail, Bow, Polearm, Simple, Exotic, Quarterstaff, Dagger

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
# Can I move the roll() methods to the dice classes?

# Set up the characters
player_one = Rogue("Player One", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_two = Fighter("Player Two", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_three = Warlock("Player Three", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
enemy = Fighter("Bad Guy", 1500, 18, 12, 18, 16, 10, 6)

# Set up the game loop
running = True
rolls_done = False

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

def draw_screen():
    screen.fill(WHITE)

    # Draw the characters
    player_one_text = [
        f"{player_one.name}: {player_one.hp}",
        f"STR: {player_one.strength}",
        f"DEX: {player_one.dexterity}",
        f"CON: {player_one.constitution}",
        f"INT: {player_one.intelligence}",
        f"WIS: {player_one.wisdom}",
        f"CHA: {player_one.charisma}"
    ]

    # Define the aside area for player text
    aside_x = 600
    aside_y = 150
    y_offset = aside_y
    for line in player_one_text:
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (aside_x, y_offset))
        y_offset += 30  # Adjust the offset for the next line

    enemy_text = font.render(f"{enemy.name}: {enemy.hp}", True, BLACK)
    screen.blit(enemy_text, (600, 50))

    # Draw the Dice
    dice_positions = [
        (dice_results["d20"], "D20"),
        (dice_results["d8"], "D8"),
        (dice_results["d6"], "D6"),
        (dice_results["d4"], "D4"),
        (dice_results["d12"], "D12"),
        (dice_results["d10"], "D10")
    ]

    # Define the aside area for the dice results
    dice_aside_x = 50
    dice_aside_y = 150
    dice_y_offset = dice_aside_y
    for result, label in dice_positions:
        text_surface = font.render(f"{label}: {result}", True, BLACK)
        screen.blit(text_surface, (dice_aside_x, dice_y_offset))
        dice_y_offset += 30 # Adjust the offset for the next line

    # Draw the buttons
    pygame.draw.rect(screen, GREY, (350, 500, 100, 50))
    button_text = font.render("Reroll Dice", True, BLACK)
    screen.blit(button_text, (355, 515))

    pygame.draw.rect(screen, GREY, (500, 500, 100, 50))
    button_text = font.render("Reroll Stats", True, BLACK)
    screen.blit(button_text, (505, 515))

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if 350 <= mouse_pos[0] <= 450 and 500 <= mouse_pos[1] <= 550:
                reroll_dice()
                rolls_done = False
            elif 500 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550:
                reroll_stats(player_one)
                rolls_done = False

    if not rolls_done:
        draw_screen()
        rolls_done = True

    clock.tick(60)

pygame.quit()

# End of file
# dnd_game.py