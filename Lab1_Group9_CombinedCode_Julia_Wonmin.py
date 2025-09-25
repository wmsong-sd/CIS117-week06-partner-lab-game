# Lab 1
# Group 9
# Authors: Julia Mirani, Wonmin Song
# Date: 9/24/2025

import random

def guessing_game():

    """

    Function: guessing_game
    Author: Julia Mirani

    This function runs a number guessing game.
    - It comes up with a random number between 1 and 100.
    - The player has 5 tries to guess the correct number.
    - After each guess, the program tells the player if the number is too low/high.
    - If the player guesses correctly, the game ends with a message saying they guessed correctly.
    - If the player runs out of tries, the program reveals the number at the end.
    - After the round is over, the program askes if they would like to play again.

    """

    
    play_again = "y"
    while play_again == "y":
        secret_number = random.randint(1,100)
        tries = 5
        print("I'm thinking of a number between 1 and 100.", end="")
        print(" You have", tries, "tries!")

        while tries > 0:
            guess = input("Enter your guess: ")

            # Checking if the guess is a digit
            if guess.isdigit():
                guess = int(guess)
                if guess == secret_number:
                    print("You got it!")
                    break
                elif guess < secret_number:
                    tries -= 1
                    if tries > 0:
                        print("Nope! Too Low. You have", tries, "tries left.")
                else:
                    tries -= 1
                    if tries > 0:
                        print("Nope! Too high. You have", tries, "tries left.")
            else:
                print("Please enter a valid number.")
                
        if tries == 0 and guess != secret_number:
            print("Nope! You lost. The number was", secret_number)
            
        play_again = input("Do you want to play again? (y/n): ").lower()






import random


def rock_scissors_paper():

    """

    Function: rock_scissors_paper
    Author: Wonmin Song

    This function runs a Rock-Paper-Scissors game.
    - The program chooses rock, paper, or scissors at random.
    - The player makes their move by selecting 1 (paper), 2 (scissors), or 3 (rock).
    - The program tells the player if they have won, lost, or tied.
    - After the round is over, the player can choose to play again or not
    
    """
    
    print("Do you want to play? (yes/no)")
    answer = input()

    if answer == "yes":
        while True:
            choices = {1: "paper", 2: "scissors", 3: "rock"}
            computer_choice = random.randint(1, 3)
            user_choice = int(input("Enter your choice: 1. paper, 2. scissors, 3. rock: "))

            if user_choice == computer_choice:
                print(f"It's a tie! You both chose {choices[user_choice]}.")
            elif (user_choice == 1 and computer_choice == 3):
                print(f"You win! {choices[user_choice]} beats {choices[computer_choice]}.")

            elif (user_choice == 2 and computer_choice == 1):
                print (f"You win! {choices[user_choice]} cut {choices[computer_choice]}.")
            elif (user_choice == 3 and computer_choice == 2):
                print(f"You win! {choices[user_choice]} breaks {choices[computer_choice]}.")
            elif (user_choice == 3 and computer_choice == 1):
                print(f"You lose! {choices[computer_choice]} beats {choices[user_choice]}.")
            elif (user_choice == 1 and computer_choice == 2):
                print(f"You lose! {choices[computer_choice]} cut {choices[user_choice]}.")
            elif (user_choice == 2 and computer_choice == 3):
                print(f"You lose! {choices[computer_choice]} breaks {choices[user_choice]}.")
                
            play_again = input("Do you want to play again? (yes/no)")
            if play_again != "yes":
                print("Bye!")
                break

    else:
        print("Okay, maybe next time!")




# Main program

if __name__ == "__main__":
    
    while True:
        print("Which game would you like to play?")
        print("1. Guessing Game, 2. Rock-Paper-Scissors, or 3. Quit")

        choice = input("Enter your choice (1, 2, or 3)")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            rock_scissors_paper()
        elif choice == "3":
            print("Thanks for playing! Goodbye :)")
            break
        else:
            Print("Invalid choice. Choose either 1, 2, or 3")

