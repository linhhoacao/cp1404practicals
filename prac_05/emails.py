"""
CP1404: Practical 5
Emails

Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    """Create a dictionary of emails-to-names."""
    email_to_name = {}

    # Prompt the user for emails until a blank one is entered
    email = input("Email: ")
    while email != "":
        # Extract the name from the email
        name = get_name_from_email(email)

        # Ask the user to confirm the name
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        # If the user doesn't confirm with 'Y' or 'y', prompt for the correct name
        if confirmation != "y" and confirmation != "":
            name = input("Name: ")

        # Store the email and name in the dictionary
        email_to_name[email] = name

        # Prompt for another email
        email = input("Email: ")

    # Print out the names and emails
    print("\nEmail and Name List:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract an expected name from the email address."""
    # Split the email address at the '@' symbol to get the prefix
    prefix = email.split('@')[0]

    # Split the prefix at the '.' to separate parts of the name
    parts = prefix.split('.')

    # Join the parts back together with a space and capitalize each word
    name = " ".join(parts).title()

    return name


# Call the main function to run the program
main()

