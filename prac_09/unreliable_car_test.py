"""
CP1404/CP5632 Practical
Unreliable car test
Estimate: 25 minutes
Actual:   30 minutes

"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create some UnreliableCar instances
    reliable_car = UnreliableCar("Reliable Car", 100, 90)  # High reliability
    unreliable_car = UnreliableCar("Unreliable Car", 100, 10)  # Low reliability

    print("Starting tests for UnreliableCar")

    for i in range(1, 6):  # Simulate 5 driving attempts for each car
        distance = 20
        print(f"\nAttempt {i}: Trying to drive {distance} km")

        reliable_distance = reliable_car.drive(distance)
        print(f"{reliable_car.name} drove {reliable_distance} km. Remaining fuel: {reliable_car.fuel}")

        unreliable_distance = unreliable_car.drive(distance)
        print(f"{unreliable_car.name} drove {unreliable_distance} km. Remaining fuel: {unreliable_car.fuel}")


if __name__ == "__main__":
    main()
