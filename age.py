#!/usr/bin/python3

age = int(input("Welcome here!\nWhat is your age please ?  "))
if age >= 0 and age <= 5:
    print("Well\nYou should be in the Kindergarteen.")
elif age >= 6 and age <= 17:
    print("You should be in High School now")
elif age > 17 and age <= 25:
    print("You should be in College buddy...")
elif age < 0:
    print("Error in your age!\nCheck again and try again.")
else:
    print("You should be working or retired")
print("Thanks for checking in today...")
print("\nCode developed by Masino")
