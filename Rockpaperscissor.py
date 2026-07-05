# rock paper scissor game

import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

def get_winner(player, computer):
    if player == computer:
        return "tie"
    return "player" if BEATS[player] == computer else "computer"

def main():
    print("Rock, Paper, Scissors")
    print("choices: rock / paper / scissors")
    print("type 'quit' to stop playing\n")

    wins = 0
    losses = 0
    ties = 0

    while True:
        player = input("your move: ").strip().lower()

        if player in ("quit", "q", "exit"):
            print(f"\nfinal score -> you: {wins}, computer: {losses}, ties: {ties}")
            if wins > losses:
                print("you came out ahead, nice!")
            elif losses > wins:
                print("computer got the better of you this time.")
            else:
                print("all tied up overall.")
            break

        if player not in CHOICES:
            print("didn't catch that - try rock, paper, or scissors")
            continue

        computer = random.choice(CHOICES)
        print(f"computer picked: {computer}")

        result = get_winner(player, computer)

        if result == "tie":
            print("tie game!")
            ties += 1
        elif result == "player":
            print("you win this round!")
            wins += 1
        else:
            print("computer takes it.")
            losses += 1

if __name__ == "__main__":
    main()
