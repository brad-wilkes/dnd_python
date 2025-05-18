from dice import D20

class Base:
    """Base class for all classes"""
    def __init__(self, name, hp, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.d20 = D20()

    def attack(self):
        return self.d20.roll()

    def __str__(self):
        return f"{self.name} ({self.hp})"

    def __repr__(self):
        return f"{self.name} ({self.hp})"