"""
CP1404/CP5632 Practical
Unreliable car
Estimate: 25 minutes
Actual:   30 minutes

"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that may not always drive reliably."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability  # A percentage value between 0 and 100

    def drive(self, distance):
        """
        Drive the car a given distance, but only if it is reliable enough.

        Generate a random number between 0 and 100. If it's less than the reliability,
        drive the car as normal. Otherwise, the car does not move.
        """
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            # Car drives normally
            return super().drive(distance)
        else:
            # Car doesn't drive
            return 0
