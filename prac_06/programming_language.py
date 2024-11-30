"""CP1404 Practical - Programming language
Estimate: 30 minutes
Actual:   35 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language with its typing, reflection, and year of creation."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
