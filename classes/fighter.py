from dice.d20 import D20
from .base import Base

class Fighter(Base):
    """A class representing a fighter."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):

        """
        :param name: The fighter's name.
        :param hp: The fighter's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.d20 = D20()

    def attack(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def battle_shout(self):
        """Shout a battle cry."""
        return self.d20.roll() + self.strength

    def shield_bash(self):
        """Bash with a shield."""
        return self.d20.roll() + self.strength

    def cleave(self):
        """Cleave through enemies."""
        return self.d20.roll() + self.strength