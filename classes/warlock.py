from .base import Base

class Warlock(Base):
    """A class representing a warlock."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):

        """
        :param name: The warlock's name.
        :param hp: The warlock's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.intelligence = intelligence + 2
        self.intelligence = charisma + 1
        self.attack()

    def corruption(self):
        """Cast a spell."""
        return self.d20.roll() + self.intelligence

    def summon_imp(self):
        """Summon an imp."""
        return self.d20.roll() + self.charisma