#!/usr/bin/python3

import random as rn

print("Hello!\nWelcome to Random_Select AI\nLet's get started...")
names = input("Enter only your individual nicknames and separate them with a space only please:\n")
print("A list of entered names below:")
split = names.split(" ")
print(split)
print("Now, we will pick a name randomly...")
win = rn.choice(split)
print(f"Congratulations!!!\nWe got a name and that is: {win}.")
#choice = rn.random()
#print(choice)
print("\nCode developed by Masino")
