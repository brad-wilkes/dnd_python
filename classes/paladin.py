from .base import Base

class Paladin(Base):
    """A class representing a paladin."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):

        """
        :param name: The paladin's name.
        :param hp: The paladin's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.constitution = constitution + 1
        self.wisdom = wisdom + 2
        self.attack()

    def smite(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll() + self.wisdom