import guess_number
import RPS

def main():
    print("Welcome to the Arcade Menu!".center(50, '='))
    while True:
        choice = int(input("Please select a game to play:\n1. Number Guessing Game\n2. Rock Paper Scissors\n\nOr X to exit\n"))
        if choice == 1:
            guess_number.main()
        elif choice == 2:
            RPS.game()
        elif choice == 'X'.upper():
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2 or X to exit.")
if __name__ == "__main__":
    main()