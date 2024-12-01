from dice.d12 import D12

class Exotic:
    """A class to represent all kinds of martial weapons."""

    def __init__(self, name, damage, weap_range, weight, cost, properties):
        """
        :param name: The name of the weapon.
        :param damage: The damage the weapon deals.
        :param weight: The weight of the weapon.
        :param cost: The cost of the weapon.
        :param properties: The properties of the weapon.
        """
        self.name = name
        self.damage = D12()
        self.range = weap_range
        self.weight = weight
        self.cost = cost
        self.properties = "Abnormal weapon requiring specific proficiency."

    def __str__(self):
        return f"{self.name} ({self.damage.roll()})"

    def __repr__(self):
        return f"{self.name} ({self.damage.roll()})"