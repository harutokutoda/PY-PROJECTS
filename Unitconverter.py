
# unit converter - length, weight, volume

CONVERSIONS = {
    "length": {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "yd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254,
    },
    "weight": {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495,
    },
    "volume": {
        "l": 1.0,
        "ml": 0.001,
        "gal": 3.78541,
        "qt": 0.946353,
        "pt": 0.473176,
        "cup": 0.236588,
        "floz": 0.0295735,
    },
}

def convert(value, from_unit, to_unit, category):
    units = CONVERSIONS[category]

    if from_unit not in units:
        raise ValueError(f"'{from_unit}' isn't a known {category} unit. try: {', '.join(units)}")
    if to_unit not in units:
        raise ValueError(f"'{to_unit}' isn't a known {category} unit. try: {', '.join(units)}")

    base_value = value * units[from_unit]
    return base_value / units[to_unit]

def main():
    print("Unit Converter")
    print("categories: length, weight, volume")
    print("example: length 5 m ft")
    print("type 'quit' to exit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ("quit", "q", "exit"):
            print("goodbye!")
            break

        parts = cmd.split()
        if len(parts) != 4:
            print("expected format: <category> <value> <from_unit> <to_unit>")
            continue

        category, value_str, from_unit, to_unit = parts

        if category not in CONVERSIONS:
            print(f"unknown category '{category}' - pick from: length, weight, volume")
            continue

        try:
            value = float(value_str)
        except ValueError:
            print(f"'{value_str}' doesn't look like a number")
            continue

        try:
            result = convert(value, from_unit, to_unit, category)
            print(f"{value} {from_unit} = {result:.6f} {to_unit}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
