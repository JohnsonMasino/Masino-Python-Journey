#!/usr/bin/python3
import random as rd

print("Helloe dear!\nWelcome to our Rock Paper Scissors challange.\nHere you will be playing with the computer.\nDo not worry as the computer can not see the option you chose.")
print("Hints:\n>Rock     WINS Scissors.\n>Scissors WINS Paper.\n>Paper    WINS Rock.")
user_choice = int(input("This game is totally free and fair!!!\n0. Rock.\n1. Paper.\n2. Scissors.\nPlease use 0, 1 or 2 to select your choice: "))
computer_choice = rd.randint(0,2)
print(f"The computer has selected {computer_choice}.\nCompiling the results...\n>>>\n>>\n>")
if user_choice >= 0 and user_choice <= 2:
    if computer_choice == 2 and user_choice == 0:
        print("Congratulations!!!\nYou win!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer Wins!")
    elif computer_choice == user_choice:
        print("Same Output!\nNo Winner.\nPlay again...")
    elif user_choice > computer_choice:
        print("You win!\nCongratulations...")
    else:
        print("Computer Wins!")
else:
    print("Sorry!\nWrong input. Check well and try again.")
print("\nCode developed by Masino")
