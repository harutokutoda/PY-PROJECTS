# temperature converter - celsius, fahrenheit, kelvin

def c_to_f(c):
    return (c * 9 / 5) + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5 / 9

def f_to_k(f):
    return f_to_c(f) + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return c_to_f(k_to_c(k))

CONVERTERS = {
    ("c", "f"): c_to_f,
    ("c", "k"): c_to_k,
    ("f", "c"): f_to_c,
    ("f", "k"): f_to_k,
    ("k", "c"): k_to_c,
    ("k", "f"): k_to_f,
}

VALID_SCALES = ("c", "f", "k")

def convert(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value

    func = CONVERTERS.get((from_scale, to_scale))
    if not func:
        raise ValueError(f"can't convert {from_scale} to {to_scale}")
    return func(value)

def main():
    print("Temperature Converter")
    print("scales: c (celsius), f (fahrenheit), k (kelvin)")
    print("example: 100 c f")
    print("type 'quit' to exit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd in ("quit", "q", "exit"):
            print("goodbye!")
            break

        parts = cmd.split()
        if len(parts) != 3:
            print("expected format: <value> <from_scale> <to_scale>")
            continue

        value_str, from_scale, to_scale = parts

        if from_scale not in VALID_SCALES or to_scale not in VALID_SCALES:
            print("scales must be c, f, or k")
            continue

        try:
            value = float(value_str)
        except ValueError:
            print(f"'{value_str}' doesn't look like a number")
            continue

        result = convert(value, from_scale, to_scale)
        print(f"{value:.2f}°{from_scale.upper()} = {result:.2f}°{to_scale.upper()}")

if __name__ == "__main__":
    main()
