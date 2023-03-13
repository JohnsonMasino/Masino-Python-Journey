#!/usr/bin/python3
print("Welcome to our snooker camp champ!")
age = int(input("Enter age here:  "))
if age >= 18:
    print("You can play snooker here!")
    sal = int(input("Enter 1 if employed and 0 if not  "))
    if sal == 1:
        print("You have to pay $10 to play\nThank you.")
    else:
        print("You can play for free\nThank you.")
else:
    print("Sorry!\nYou can not play here.")
print("Have fun!!!")    
print("\nCode developed by Maino")
