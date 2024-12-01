"""
CP1404/CP5632 Practical
Taxi simulator
Estimate: 45 minutes
Actual:   52 minutes

"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    current_taxi = None
    total_bill = 0.0
    choice = None

    print("Let's drive!")
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()

        if choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input; please enter a number.")
        elif choice == "d":
            if current_taxi:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    total_bill += trip_cost
                    print(
                        f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}"
                    )
                except ValueError:
                    print("Invalid input; please enter a number.")
            else:
                print("You need to choose a taxi before you can drive")
        elif choice == "q":
            break
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
