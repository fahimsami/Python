print("Welcome to Rock, Paper, Scissors Game!".center(50, "="))  
import random as random
      
 
def game():
    def get_user_choice():
        user_input = input("Please choose :\n1. Rock\n2. Paper\n3. Scissors\n")
        if user_input not in ['1', '2', '3']:
            print("Invalid Input. Please choose 1, 2 or 3.")
            return get_user_choice()
        if user_input == '1':
            return 'Rock'
        elif user_input == '2':
            return 'Paper'
        elif user_input == "3":
            return "Scissors"
    
    def get_computer_choice():
        choices = ['Rock', 'Paper', "Scissors"]
        return random.choice(choices)
    
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif user_choice == "Rock" and computer_choice == "Scissors":
            return "You win!"
        elif user_choice == "Paper" and computer_choice == "Rock":
            return "You win!"
        elif user_choice == "Scissors" and computer_choice == "Paper":
            return "You win!"
        else:
            return "Computer wins!"
        
    def play_again():
        play_again_input = input("Do you want to play again? (y/n)\n")
        if play_again_input.lower() == 'y':
            return True
        elif play_again_input.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter y or n.")
            return play_again()
        
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    if play_again():
        game()
    else:
        print("Thanks for playing! Goodbye!")
        
if __name__ == "__main__":
    game()
    