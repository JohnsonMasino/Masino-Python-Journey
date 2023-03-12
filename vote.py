#!/usr/bin/python3

print("Hello! Welcome here.")
name = input("Tell us your name please... ")
print(f"Welcome here {name}. We are happy to have you here")
age = int(input("Enter your age here... "))
if (age < 12):
    print("Sorry!\nYou can't vote yet")
elif (age >= 12 and age <= 17):
    print("Sorry\nYou are still a middle teenager and you can not vote")
else:
    print("Yes!\nYou can vote")
print("Thanks for verifying age with us")
print("\nCode developed by Masino")
