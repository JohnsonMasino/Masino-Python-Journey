#!/usr/bin/python3
print("Welcome to our snooker camp champ!")
age = int(input("Enter age here:  "))
if age >= 18:
    print("You can play snooker here!")
    sal = int(input("Enter your salary here in USD  "))
    if sal <= 1000:
        print("You can play for free")
    else:
        print("You have to pay $10 to play\nThank you.")
else:
    print("Sorry!\nYou can not play here.")
print("Thanks for choosing us")    
print("\nCode developed by Maino")
