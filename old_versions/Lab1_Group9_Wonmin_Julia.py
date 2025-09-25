import random


def rock_scissors_paper():
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

rock_scissors_paper()
