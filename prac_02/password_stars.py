def get_valid_password(min_length):
    while True:
        password = input(f"Enter a password (at least {min_length} characters): ")
        if len(password) < min_length:
            print(f"Password is too short. Please enter a password with at least {min_length} characters.")
        else:
            return password


def main():
    min_length = 8
    password = get_valid_password(min_length)
    print("Password accepted.")
    print("*" * len(password))  # Show stars for the password length


main()
