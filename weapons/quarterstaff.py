from .simple import Simple

class Quarterstaff(Simple):
    """A class to represent quarterstaffs."""

    def __init__(self, name, damage, weap_range, weight, cost, properties):
        """
        :param name: The name of the weapon.
        :param damage: The damage the weapon deals.
        :param weight: The weight of the weapon.
        :param cost: The cost of the weapon.
        :param properties: The properties of the weapon.
        """
        super().__init__(name, damage, weap_range, weight, cost, properties)

    def __str__(self):
        return f"{self.name} ({self.damage.roll()} bludgeoning)"

    def __repr__(self):
        return f"{self.name} ({self.damage.roll()} bludgeoning)"