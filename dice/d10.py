from random import randint

class D10:
    """A class representing a single die."""

    def __init__(self, num_sides=10):
        """
        :param num_sides: Assume 10-sided die.
        """
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)