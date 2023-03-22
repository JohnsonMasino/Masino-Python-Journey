#!/usr/bin/python3
import random as rd

print("Helloe dear!\nWelcome to our Rock Paper Scissors challange.\nHeere you will be playing with the computer.\nDo not worry as the computer can not see the option you chose.")
user_choice = int(input("This game is totally free and fair!!!\n0. Rock.\n1. Paper.\n2. Scissors.\nPlease select your choice: "))
computer_choice = rd.randint(0,2)
print(str(user_choice) + "\n" + str(computer_choice))
print("\nCode developed by Masino")
