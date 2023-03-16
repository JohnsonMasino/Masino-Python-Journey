#!/usr/bin/python3
import random
print("Hello Guys!\nWelcome to our 'head' and 'tail' random selection.")
print("Here, we will take:\n0 for Head\n1 for tail.\nLet's Goo!!!")
numbers = (0, 1)
num = random.choice(numbers)
name = input("Please type 'toss' to toss the coin:  ")
print("Good toss!\nPrinting the result now.")
print(num)
if num == 0:
    print("Congratulations!\nWe got a HEAD!")
else:
    print("Congratulations!\nWe got a TAIL!")
print("\nCode developed by Masino")
