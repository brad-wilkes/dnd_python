from random import randint

class D20:
    """A class representing a single die."""

    def __init__(self, num_sides=20):
        """
        :param num_sides: Assume 20-sided die.
        """
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def roll_two(self):
        rolls = [self.roll() for _ in range(2)]
        return rolls

    def roll_three(self):
        rolls = [self.roll() for _ in range(3)]
        return rolls