"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When users enter a value that can't be converted to integer
2. When will a ZeroDivisionError occur?
    When user enters a denominator with value 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Denominator cannot be zero. Please try again.")
        else:
            fraction = numerator / denominator
            print(fraction)
            break
    except ValueError:
        print("Numerator and denominator must be valid numbers. Please try again.")

print("Finished.")
