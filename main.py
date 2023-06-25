import random

def guess_game():
    random_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < random_number:
            print("uhh, Try again")
        elif guess > random_number:
            print("Oopss, try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_game()
