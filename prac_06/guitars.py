"""CP1404 Practical - guitars
Estimate: 40 minutes
Actual:   45 minutes
"""


from guitar import Guitar


def main():
    """Collect guitar information from the user and display it."""
    guitars = []

    print("My guitars!")
    # Collect guitar details from the user
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

        # Prompt for the next guitar
        name = input("Name: ")

    # Display all guitars entered
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
