from martial import Martial

class Flail(Martial):
    """A class to represent a flail weapon."""

    def __init__(self, properties, name="Flail", damage="1d8", weap_range="Melee", weight=2, cost=10):
        """
        :param name: The name of the weapon.
        :param damage: The damage the weapon deals.
        :param weight: The weight of the weapon.
        :param cost: The cost of the weapon.
        :param properties: The properties of the weapon.
        """
        super().__init__(name, damage, weap_range, weight, cost, properties)

    def __str__(self):
        return f"{self.name} ({self.damage.roll()} martial)"

    def __repr__(self):
        return f"{self.name} ({self.damage.roll()} martial)"