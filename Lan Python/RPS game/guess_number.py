import sys
import random
import argparse
from unicodedata import name

print("Welcome to the Number Guessing Game!".center(50, "="))

parser = argparse.ArgumentParser(description = "A simple number guessing game")
parser.add_argument("--name", type = str, help = "Enter your name", required = True, default = "Player")
args = parser.parse_args()

player_win = 0
computer_win = 0
game_count = 0

def guess_number(name):
    print(f"Hello, {name}! Let's start the game.")
    print("I have selected a number between 1 and 3. Can you guess it?")
    
    number_to_guess = int(input("Enter your guess : \n"))
    while number_to_guess not in [1, 2, 3]:
        print("Invalid input. Please enter a number between 1 and 3.")
        number_to_guess = int(input("Enter your guess : \n"))

    return number_to_guess

def computer_guess():
    default_number = random.randint(1,3)
    return default_number    
    
def check_guess(user_guess, computer_guess):
    global player_win
    global computer_win
    global game_count
    game_count += 1
    if user_guess == computer_guess:
        print(f"Congratulations, {args.name}! You guessed the number {computer_guess} correctly.")
        player_win += 1
        print(f"Your score: {player_win} | Computer score: {computer_win}")
    else:
        print(f"Sorry, {args.name}. The correct number was {computer_guess}. Better luck next time!")
        computer_win += 1
        print(f"Your score: {player_win} | Computer score: {computer_win}")
        print(f"Total games played: {game_count}")
        
    return player_win, computer_win, game_count

def play_again():
    play_again_input = input("Do you want to play again?\n1. Yes \n2 No\n")
    if play_again_input == '1':
        return True
    elif play_again_input == '2':
        return False
    else:
        print("Invalid input. Please enter 1 or 2.")
        return play_again()
    
def display_score(player_win, game_count):
    winnning_percentage = (player_win/game_count)*100
    print(f"Your winning percentage : {winnning_percentage}%")
    return winnning_percentage
    
if __name__ == "__main__":
    while True:
        user_guess = guess_number(args.name)
        computer_number = computer_guess()
        check_guess(user_guess, computer_number)
        score = display_score(player_win, game_count)
        if not play_again():
            print("Thanks for playinng! Goodbye!")
            break
        
    
