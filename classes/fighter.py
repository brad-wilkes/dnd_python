from .base import Base

class Fighter(Base):
    """A class representing a fighter."""

    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):

        """
        :param name: The fighter's name.
        :param hp: The fighter's hit points.
        """
        super().__init__(name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.strength = strength + 2
        self.constitution = constitution + 1
        self.dexterity = dexterity + 1
        self.attack()

    def battle_shout(self):
        """Shout a battle cry."""
        return self.d20.roll() + self.strength

    def shield_bash(self):
        """Bash with a shield."""
        return self.d20.roll() + self.strength

    def cleave(self):
        """Cleave through enemies."""
        return self.d20.roll() + self.strength