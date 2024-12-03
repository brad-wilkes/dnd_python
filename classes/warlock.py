from dice import D20
from .base import Base

class Warlock(Base):
    """A class representing a warlock."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):

        """
        :param name: The warlock's name.
        :param hp: The warlock's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.d20 = D20()

    def attack(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def corruption(self):
        """Cast a spell."""
        return self.d20.roll() + self.intelligence

    def summon_imp(self):
        """Summon an imp."""
        return self.d20.roll() + self.charisma