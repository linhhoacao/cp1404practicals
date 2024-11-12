"""
CP1404/CP5632 Practical
My_guitars
"""

from guitar import Guitar


def read_guitars_from_file(file_name):
    guitars = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, year, cost = line.split(",")
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def main():
    file_name = "guitars.csv"
    guitars = read_guitars_from_file(file_name)
    display_guitars(guitars)


if __name__ == "__main__":
    main()
