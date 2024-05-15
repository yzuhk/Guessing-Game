import random
from colorama import Fore, Style


def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)


def print_green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_blue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)


def guess():
    while True:  # Loop for starting a new game
        print("----------------------------------------------------------------------")
        print("This is the Guessing Game!")
        print("I've picked a number between 1 and 100. You have to try to guess it!")
        print("----------------------------------------------------------------------")

        number_to_guess = random.randint(1, 100)
        attempts = 0
        max_attempts = 10

        while attempts < max_attempts:
            user_input = input("Enter your guess: ")

            # Check if input is empty
            if not user_input:
                print_red("Please enter a number.")
                continue  # Skip the rest of the loop iteration

            guess = int(user_input)
            attempts += 1

            if guess < number_to_guess:
                if number_to_guess - guess <= 10:
                    print_green("Almost! Try a little higher.")
                else:
                    print_blue("Too low! Try again.")
            elif guess > number_to_guess:
                if guess - number_to_guess <= 10:
                    print_green("Almost! Try a little lower.")
                else:
                    print_blue("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number ({number_to_guess}) in {attempts} attempts!"
                )
                break
            
            if attempts == 5:
               hint_choice = input("Do you want a hint? (yes/no): ")
               if hint_choice.lower() == 'yes':
                   print(f"The number is between {number_to_guess - 10} and {number_to_guess + 10}.")

        else:
            print(
                f"Sorry, you've run out of attempts. The number was {number_to_guess}."
            )

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break  # Exit the loop if the player chooses not to play again


if __name__ == "__main__":
    guess()