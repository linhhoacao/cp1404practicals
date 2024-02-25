
min_length = 8

while True:

    password = input("Enter a password: ")
    if len(password) < min_length:
        print("Password is too short. Please enter a password with at least", min_length, "characters.")
    else:
        break

print("*" * len(password))