def extract_name(email):
    parts = email.split("@")
    name = parts[0]
    name_parts = name.split(".")
    capitalized_name = " ".join(part.title() for part in name_parts)
    return capitalized_name


def prompt_name(email, extracted_name):
    while True:
        choice = input(f"Is your name {extracted_name}? (Y/n) ").lower()
        if choice == "" or choice == "y":
            return extracted_name
        elif choice == "n":
            return input("Name: ").title()


user_data = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)
    verified_name = prompt_name(email, name)
    user_data[email] = verified_name

print()

for email, name in user_data.items():
    print(f"{name} ({email})")