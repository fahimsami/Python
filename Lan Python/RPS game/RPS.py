import random as random

user_win = 0
computer_win = 0
count = 0

USER_WIN = "You win!"
COMPUTER_WIN = "Computer wins!"
TIE = "It's a tie!"


def get_user_choice():
    print("Welcome to Rock, Paper, Scissors Game!".center(50, "="))
    while True:
        user_input = input("Please choose :\n1. Rock\n2. Paper\n3. Scissors\n")
        if user_input == '1':
            return 'Rock'
        elif user_input == '2':
            return 'Paper'
        elif user_input == '3':
            return 'Scissors'
        print("Invalid input. Please choose 1, 2 or 3.")


def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return TIE
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return USER_WIN
    elif user_choice == "Paper" and computer_choice == "Rock":
        return USER_WIN
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return USER_WIN
    return COMPUTER_WIN


def display_score(user_choice, computer_choice, result):
    global user_win, computer_win, count

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    if result == USER_WIN:
        user_win += 1
    elif result == COMPUTER_WIN:
        computer_win += 1

    print(f"Total games played : {count}")
    print(f"Your score : {user_win} | Computer score : {computer_win}")
    percentage_win = percentage(user_win, count)
    print(f"Your winning percentage : {percentage_win}%")

    return count, user_win, computer_win


def percentage(user_win, count):
    return (user_win / count) * 100 if count > 0 else 0


def play_again():
    while True:
        play_again_input = input("Do you want to play again? (y/n)\n")
        if play_again_input.lower() == 'y':
            return True
        elif play_again_input.lower() == 'n':
            return False
        print("Invalid input. Please enter y or n.")


def game():
    global count

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        count += 1
        result = determine_winner(user_choice, computer_choice)
        display_score(user_choice, computer_choice, result)

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    game()
