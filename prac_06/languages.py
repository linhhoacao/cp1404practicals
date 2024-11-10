"""CP1404 Practical - Languages
Estimate: 30 minutes
Actual:   35 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    # Create instances of ProgrammingLanguage
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print details of the Python object to check __str__ method
    print(python)

    # Store languages in a list
    languages = [python, ruby, visual_basic]

    # Filter and print names of dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


# Run the main function
if __name__ == "__main__":
    main()
