"""CP1404 Practical - guitar_test
Estimate: 40 minutes
Actual:   45 minutes
"""


from guitar import Guitar


def test_guitar():
    """Test the Guitar class methods get_age() and is_vintage()."""
    # Create test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    # Test get_age()
    print(f"{guitar1.name} get_age() - Expected 102. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 11. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


if __name__ == "__main__":
    test_guitar()
