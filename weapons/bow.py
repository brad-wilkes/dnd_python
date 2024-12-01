from dice import D20
from .simple import Simple

class Bow(Simple):
    """A class to represent a bow."""

    def __init__(self, name, damage, weap_range, weight, cost, properties):
        """
        :param name: The name of the weapon.
        :param damage: The damage the weapon deals.
        :param weight: The weight of the weapon.
        :param cost: The cost of the weapon.
        :param properties: The properties of the weapon.
        """
        super().__init__(name, damage, weap_range, weight, cost, properties)
        self.d20 = D20()

    def shoot(self):
        """Return a random value between 1 and 20."""
        return self.d20.roll()

    def __str__(self):
        return f"{self.name} ({self.damage.roll()})"

    def __repr__(self):
        return f"{self.name} ({self.damage.roll()})"