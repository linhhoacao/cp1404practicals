# Set the minimum length for the password
min_length = 8

while True:
    # Prompt the user to enter a password
    password = input("Enter a password: ")

    # Check the length of the password
    if len(password) < min_length:
        print("Password is too short. Please enter a password with at least", min_length, "characters.")
    else:
        break

# Print asterisks as long as the length of the password
print("*" * len(password))