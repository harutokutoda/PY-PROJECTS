
# guess the number game

import random

def main():
    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    print("(type 'quit' anytime to give up)\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess_input = input("your guess: ").strip()

        if guess_input.lower() in ("quit", "q"):
            print(f"aw, giving up? the number was {secret}.")
            break

        if not guess_input.lstrip("-").isdigit():
            print("that's not a number, try again")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < secret:
            print("too low!")
        elif guess > secret:
            print("too high!")
        else:
            if attempts == 1:
                print("wow, got it in one guess!")
            else:
                print(f"yes! you got it in {attempts} tries.")
            break

if __name__ == "__main__":
    main()
