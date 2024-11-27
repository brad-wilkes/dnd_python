from dice.d20 import D20
from base import Base

class Wizard(Base):
    """A class representing a wizard."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        """
        :param name: The wizard's name.
        :param hp: The wizard's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.d20 = D20()

    def attack(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def fireball(self):
        """Cast a fireball spell."""
        return self.d20.roll() + self.intelligence