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
player_one = Bard("Player One", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_two = Fighter("Player Two", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_three = Rogue("Player Three", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())
player_four = Warlock("Player Four", 100, d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum(), d6.stat_roll_sum())

enemy = Base("Bad Guy", 1500, 18, 12, 18, 16, 10, 6)

# Set up the weapons
player_one_weapon = Bow("Bow", 1, 8, 2, 25, "Ranged")
player_two_weapon = Axe("Axe", 1, 12, 5, 15, "Melee")
player_three_weapon = Sword("Sword", 1, 6, 3, 10, "Melee")
player_four_weapon = Flail("Flail", 1, 10, 2, 10, "Melee")
enemy_weapon = Polearm("Polearm", 1, 10, 6, 20, "Melee")

# Set up the game loop
running = True
rolls_done = False

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

    # Define the aside area for player_one_text
    aside_x = 600
    aside_y = 150
    y_offset = aside_y
    for line in player_one_text:
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (aside_x, y_offset))
        y_offset += 30  # Adjust the offset for the next line

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

    # Draw the button
    pygame.draw.rect(screen, GREEN, (350, 500, 100, 50))
    button_text = font.render("Reroll", True, BLACK)
    screen.blit(button_text, (365, 515))

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if 350 <= mouse_pos[0] <= 450 and 500 <= mouse_pos[1] <= 550:
                rolls_done = False

    if not rolls_done:
        draw_screen()
        rolls_done = True

    clock.tick(60)

pygame.quit()

# End of file
# dnd_game.py
