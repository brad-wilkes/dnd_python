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

    def __str__(self):
        return f"{self.name} ({self.hp})"

    def __repr__(self):
        return f"{self.name} ({self.hp})"