"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

Estimate: 20 minutes
Actual:   25 minutes
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" initialized with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to the limo
    limo.add_fuel(20)

    # Print the amount of fuel in the limo
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km.")

    # Print the limo object to show __str__ method functionality
    print(limo)


main()
