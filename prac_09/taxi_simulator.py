from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def choose_taxi(taxis):
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    try:
        choice = int(choice)
        if choice < 0 or choice >= len(taxis):
            raise ValueError
        return taxis[choice]
    except ValueError:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    fare = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, fare))
    return fare


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.00

    print("Let's drive!")
    display_menu()

    while True:
        choice = input(">>> ").lower()

        if choice == "q":
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
            if current_taxi is not None:
                print("Bill to date: ${:.2f}".format(total_bill))
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                total_bill += fare
                print("Bill to date: ${:.2f}".format(total_bill))
        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(total_bill))

        display_menu()


if __name__ == "__main__":
    main()  