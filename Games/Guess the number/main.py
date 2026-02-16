from art import logo, win, lose
import random as rnd

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def select_number():
    """Randomly select a number between 1 and 100"""
    return rnd.randint(1,100)

def choose_difficulty_level(level_choice):
    """Return the number of attempts given the chosen difficulty level"""
    if level_choice == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_number(guess, target, turns):
    """
    Compare the guessed number with the target number.
    Return "win" if the target number is predicted, otherwise return the number of turns left
    """
    if guess == target:
        print(f"{win}")
        return "win"
    else:
        turns -= 1
        # case 1: the guessed number is too high
        if guess > target:
            print("Too high, try again!")
            return turns
        # case 2: the guessed number is too low
        else:
            print("Too low, try again")
            return turns


def play():
    print(logo)
    print("Welcome to guess the number!")

    # the computer choose a number
    print("The computer is thinking of a number between 1 and 100 ...")
    target_number = select_number()

    # the user choose the difficulty level
    level_choice = input("Select the difficulty level: type 'easy' or 'hard' \n").lower()
    turns = choose_difficulty_level(level_choice)

    while turns > 0:
        if turns == 1:
            print("You have ONE LAST ATTEMPT remaining to guess the number!")
        else:
            print(f"You have {turns} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess "))

        check = check_number(guessed_number,target_number,turns)

        if check == "win":
            return  # If the guessed number is the target one, exit the while loop!
        else:
            turns = check
    if turns == 0:
        print(f"{lose}")


play_again = "yes"
while play_again == "yes":
    play()
    play_again = input("If you want to play GUESS THE NUMBER again, press 'yes', otherwise press 'no' ")
    print("\n"*20)
