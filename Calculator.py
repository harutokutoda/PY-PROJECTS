# Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("can't divide by zero")
    return a / b

def main():
    print("CLI Calculator")
    print("supports: + - * /")
    print("type 'quit' to exit\n")

    while True:
        expr = input("enter expression (e.g. 5 + 3): ").strip()

        if expr.lower() in ("quit", "exit", "q"):
            print("bye!")
            break

        parts = expr.split()
        if len(parts) != 3:
            print("format should be: number operator number")
            continue

        a, op, b = parts

        try:
            a, b = float(a), float(b)
        except ValueError:
            print(f"'{a}' or '{b}' isn't a valid number")
            continue

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print(f"don't recognize operator '{op}'")
                continue

            print(f"= {result}")

        except ValueError as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()
