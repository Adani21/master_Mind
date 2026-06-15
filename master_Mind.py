#!/bin/python3
print("MasterMind")

import random

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def generate_Color_Code(length=4):
    options = ['R', 'G', 'B', 'Y', 'O', 'P']
    return [random.choice(options) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)

    return black_Pegs, white_Pegs

def play_Mastermind():
    mode = input("Select mode: n = numbers, c = colors: ").lower()
    attempts = 10

    if mode == 'c':
        options = ['R', 'G', 'B', 'Y', 'O', 'P']
        secret_Code = generate_Color_Code()

        print("Welcome to Mastermind with colors!")
        print("Use: R, G, B, Y, O, P")
        print("Example: RGBY")

    else:
        options = ['1', '2', '3', '4', '5', '6']
        secret_Code = generate_Code()

        print("Welcome to bij Mastermind with numbers!")
        print("Use digits from 1 to 6")
        print("Example: 1234")

    for attempt in range(1, attempts + 1):
        valid_Guess = False

        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").upper().strip()
            valid_Guess = len(guess) == 4 and all(c in options for c in guess)

            if not valid_Guess:
                print("Invalid input. Enter 4 correct characters.")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs: {black}, White pegs: {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()