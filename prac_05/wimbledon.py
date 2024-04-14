import csv


def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data


def get_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
        countries.add(row[3])
    return sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")


def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(countries)
    print(countries_str)


def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = get_champions(data)
    countries = get_countries(data)

    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()