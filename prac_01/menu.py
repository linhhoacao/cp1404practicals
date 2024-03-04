name = input("Enter name: ")

def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def greet_hello(name):
    print("Hello", name)

def greet_goodbye(name):
    print("Goodbye", name)

choice = ''
while choice != 'Q':
    display_menu()
    choice = input(">>> ").upper()

    if choice == 'H':
        greet_hello(name)
    elif choice == 'G':
        greet_goodbye(name)
    elif choice == 'Q':
        print("Finished.")
    else:
        print("Invalid choice")