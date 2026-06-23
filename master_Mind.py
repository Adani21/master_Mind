#!/bin/python3
import random

print("MasterMind")

def admin_Login(secret_Code):
    with open("admin.env") as f:
        regels = f.read().splitlines()

    stukken_user = regels[0].split("=")
    juiste_user = stukken_user[1]

    stukken_pass = regels[1].split("=")
    juiste_pass = stukken_pass[1]

    user = input("Gebruikersnaam: ")
    wachtwoord = input("Wachtwoord: ")

    if user == juiste_user and wachtwoord == juiste_pass:
        print("Ingelogd als admin!")
        print(secret_Code)
        return True
    else:
        print("Onjuiste gegevens.")
        return False

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
    print("Welcome to Mastermind!")
   
    attempts = 10
    
    # Standaard opties (vallen we op terug als invoer ongeldig is)
    options = ['1', '2', '3', '4', '5', '6']
    secret_Code = generate_Code()

    
    mode = input("Choose a mode (c for colors | n for numbers): ").strip().lower()

    if mode == 'c':
        options = ['R', 'G', 'B', 'Y', 'O', 'P']
        secret_Code = generate_Color_Code()

        print("\nWelcome to Mastermind with colors!")
        print("Use: R, G, B, Y, O, P")
        print("Example: RGBY")

    else:
        # We pakken automatisch 'n' (numbers) als standaard
        options = ['1', '2', '3', '4', '5', '6']
        secret_Code = generate_Code()

        print("\nWelcome to Mastermind with numbers!")
        print("Use digits from 1 to 6")
        print("Example: 1234")
    
    print(f"Guess the 4-digit/color code. You have {attempts} attempts.")
    admin_Login(secret_Code)
    
    for attempt in range(1, attempts + 1):
        valid_Guess = False

        while not valid_Guess:
            # .upper() zorgt ervoor dat 'rgby' automatisch 'RGBY' wordt
            user_input = input(f"Attempt {attempt}: ").strip().upper()
            guess = user_input.replace(" ", "").replace(",", "")
            
            # Controleer of de lengte 4 is EN of elk karakter in de actieve opties zit
            valid_Guess = len(guess) == 4 and all(c in options for c in guess)
            
            if not valid_Guess:
                print(f"Invalid input. Enter 4 items using only: {', '.join(options)}")
        
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
        again = input("Play again (Y/N)? ").upper().strip()