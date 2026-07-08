# dice roller - with custom sides/count and dice notation

import random
import argparse

def roll_dice(sides=6, count=1):
    return [random.randint(1, sides) for _ in range(count)]

def parse_notation(text):
    """parse something like '2d6' into (count, sides)"""
    if "d" not in text:
        raise ValueError("missing 'd' - format is <count>d<sides>, e.g. 2d6")

    count_str, sides_str = text.split("d", 1)
    count = int(count_str)
    sides = int(sides_str)

    if count < 1 or sides < 2:
        raise ValueError("count must be at least 1 and sides at least 2")

    return count, sides

def main():
    parser = argparse.ArgumentParser(description="roll some dice")
    parser.add_argument("-s", "--sides", type=int, default=6, help="sides per die (default: 6)")
    parser.add_argument("-c", "--count", type=int, default=1, help="number of dice (default: 1)")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive mode")

    args = parser.parse_args()

    if not args.interactive:
        results = roll_dice(args.sides, args.count)
        print(f"rolled {args.count}d{args.sides}: {results}")
        print(f"total: {sum(results)}")
        return

    print("Dice Roller (interactive)")
    print("enter dice notation like '2d6' or '3d20', 'quit' to exit\n")

    while True:
        user_input = input("roll: ").strip().lower()

        if user_input in ("quit", "q", "exit"):
            print("goodbye!")
            break

        try:
            count, sides = parse_notation(user_input)
        except ValueError as e:
            print(f"nope - {e}")
            continue

        results = roll_dice(sides, count)
        total = sum(results)

        print(f"rolled: {results}")
        if count > 1:
            print(f"total: {total}")

        if sides >= 20 and total == sides * count:
            print("max roll! lucky.")
        elif sides >= 20 and total == count:
            print("ouch, lowest possible roll.")

        print()
