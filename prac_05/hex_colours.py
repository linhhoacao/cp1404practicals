color_codes = {
    "aliceblue": "#f0f8ff",
    "brown": "#a52a2a",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "coffee": "#6f4e37",
    "celeste": "#b2ffff",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "babypink": "#f4c2c2",
    "blue": "#0000ff"
}

while True:
    color_name = input("Enter a color name (or blank to exit): ").lower()
    if color_name == "":
        break

    color_code = color_codes.get(color_name)
    if color_code:
        print(f"The hexadecimal color code for {color_name} is {color_code}")
    else:
        print("Invalid color name.")