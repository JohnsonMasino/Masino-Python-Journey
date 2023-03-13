#!/usr/bin/python3
print("Welcome to our snooker camp champ!")
age = int(input("Enter age here:  "))
if age >= 18:
    print("You can play snooker here!")
    sal = int(input("Enter 1 if employed and 0 if not  "))
    if sal == 1:
        print("You have to pay some amount to play snooker here.")
        amount = int(input("Enter your monthly salary in USD  "))
        if amount <= 1000:
            print("You have to pay USD10 to play here\nThank you!")
        elif amount > 1000 and amount <= 5000:
            print("You have to pay USD25 to play snooker here.\nThank you.")
        elif amount > 5000 and amount <= 10000:
            print("Your fee is USD50.\nThank you!")
        else:
            print("Wow you are rich$\nYour fee is USD100.\nThank you!")
    else:
        print("You can play for free\nThank you.")
else:
    print("Sorry!\nYou can not play here.")
print("Have fun!!!")    
print("\nCode developed by Maino")
