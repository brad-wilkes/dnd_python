import pygame

class GameUI:
    def __init__(self):
        # Colors
        self.WHITE = (255, 255, 255)
        self.GREY = (128, 128, 128)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.VIOLET = (148, 0, 211)
        self.BLUE = (0, 0, 255)

        # Initialize pygame and create window
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("D&D Game")
        
        # Set up the fonts
        self.secondary_font = pygame.font.Font(None, 36)
        self.alt_font = pygame.font.Font(None, 24)
        self.font = pygame.font.Font(None, 18)
        
        # Set up the clock
        self.clock = pygame.time.Clock()

    def draw_screen(self, player_one, enemy, dice_results):
        self.screen.fill(self.WHITE)

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
            text_surface = self.font.render(line, True, self.BLACK)
            self.screen.blit(text_surface, (aside_x, y_offset))
            y_offset += 30

        enemy_text = self.font.render(f"{enemy.name}: {enemy.hp}", True, self.BLACK)
        self.screen.blit(enemy_text, (600, 50))

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
            text_surface = self.font.render(f"{label}: {result}", True, self.BLACK)
            self.screen.blit(text_surface, (dice_aside_x, dice_y_offset))
            dice_y_offset += 30

        # Draw the buttons
        pygame.draw.rect(self.screen, self.GREY, (350, 500, 100, 50))
        button_text = self.font.render("Reroll Dice", True, self.BLACK)
        self.screen.blit(button_text, (355, 515))

        pygame.draw.rect(self.screen, self.GREY, (500, 500, 100, 50))
        button_text = self.font.render("Reroll Stats", True, self.BLACK)
        self.screen.blit(button_text, (505, 515))

        pygame.display.flip()

    def check_button_clicks(self, mouse_pos):
        if 350 <= mouse_pos[0] <= 450 and 500 <= mouse_pos[1] <= 550:
            return "reroll_dice"
        elif 500 <= mouse_pos[0] <= 600 and 500 <= mouse_pos[1] <= 550:
            return "reroll_stats"
        return None

    def tick(self):
        self.clock.tick(60)

    def quit(self):
        pygame.quit()