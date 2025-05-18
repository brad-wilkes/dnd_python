from .base import Base

class Bard(Base):
    """A class representing a bard."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        """
        :param name: The bard's name.
        :param hp: The bard's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.charisma = charisma + 3
        self.attack()

    def sing_praise(self):
        """Sing a song of praise."""
        return self.d20.roll() + self.charisma

    def inspire(self):
        """Inspire allies."""
        return self.d20.roll() + self.charisma

    def lullaby(self):
        """Sing an enemy to sleep."""
        return self.d20.roll() + self.charisma