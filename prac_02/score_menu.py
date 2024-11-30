import random


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")
    return score


def show_stars(score):
    print("*" * int(score))


# Main function to handle the menu
def main():
    print("Welcome to the Score Program!")

    # Get a valid score before the menu loop
    score = get_valid_score()

    # Main menu loop
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()

        elif choice == 'P':
            print(f"Score: {score}, Status: {determine_score_status(score)}")

        elif choice == 'S':
            show_stars(score)

        elif choice == 'Q':
            print("Farewell")
            break

        else:
            print("Invalid option. Choose again.")


main()
