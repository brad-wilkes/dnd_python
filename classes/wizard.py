from .base import Base

class Wizard(Base):
    """A class representing a wizard."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        """
        :param name: The wizard's name.
        :param hp: The wizard's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.intelligence = intelligence + 3
        self.attack()


    def fireball(self):
        """Cast a fireball spell."""
        return self.d20.roll() + self.intelligence