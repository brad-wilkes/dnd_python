from dice import D20
from .base import Base

class Rogue(Base):
    """A class representing a rogue."""

    def __init__(self, name, hp, strength, dexterity, intelligence, wisdom, charisma, constitution=10):

        """
        :param name: The rogue's name.
        :param hp: The rogue's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.dexterity = dexterity + 3
        self.d20 = D20()

    def attack(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def backstab(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll() + self.dexterity