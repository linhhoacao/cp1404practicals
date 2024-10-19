"""
CP1404: Practical 5
Hexadecimal colour

Estimate: 20 minutes
Actual:   32 minutes
"""

# Constant dictionary with color names and their hexadecimal codes
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "brown": "#a52a2a",
    "chartreuse": "#7fff00"
}

# Prompt the user for input and continue until a blank input is given
colour_name = input("Enter a colour name (or leave blank to exit): ").lower()

while colour_name != "":
    # Look up the colour name in the dictionary (case-insensitive)
    hex_code = COLOUR_CODES.get(colour_name)

    if hex_code:
        print(f"The code for \"{colour_name}\" is {hex_code}")
    else:
        print(f"Sorry, \"{colour_name}\" is not a valid colour name.")

    # Prompt for another colour name
    colour_name = input("Enter a colour name (or leave blank to exit): ").lower()

print("Program terminated.")
