"""
CP1404/CP5632 Practical
State names in a dictionary

"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}


def main():
    """Main function to handle state code input and display state names."""
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    # Print all states and names neatly aligned
    print("\nAll states and their names:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code} is {name}")


main()

