"""
CP1404/CP5632 Practical
Silver service taxi test
Estimate: 30 minutes
Actual:   38 minutes

"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""

    # Create a SilverServiceTaxi with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    fancy_taxi.start_fare()
    distance_driven = fancy_taxi.drive(18)

    # Print details of the taxi
    print(fancy_taxi)

    # Calculate and print the fare
    fare = fancy_taxi.get_fare()
    print(f"Distance driven: {distance_driven} km")
    print(f"Fare: ${fare:.2f}")

    # Assert tests to validate the implementation
    assert distance_driven == 18, "The taxi should have driven 18 km"
    assert abs(fare - 48.78) < 0.01, f"Expected fare: $48.78, got {fare:.2f}"


if __name__ == "__main__":
    main()
