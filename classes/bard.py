from dice.d20 import D20
from base import Base

class Bard(Base):
    """A class representing a bard."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        """
        :param name: The bard's name.
        :param hp: The bard's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.d20 = D20()

    def attack(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def sing_praise(self):
        """Sing a song of praise."""
        return self.d20.roll() + self.charisma