# Lab 1
# Group 9
# Authors: Julia Mirani, Wonmin Song
# Date: 9/24/2025

import random

def guessing_game():
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

if __name__ == "__main__":
    guessing_game()
            
                             
