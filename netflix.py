#!/usr/bin/python3
name = input("Hi daer!\nWelcome to netflixson's movie centre.\nLet us know your name please.  ")
print(f"Welcome here {name}...")
fee = 0
age = int(input("Let us know your age " + name + "." + "  "))
if age >= 18:
    print("You can watch in this movie center.")
    sal = int(input("What is your monthly salary in USD ?  "))
    if sal < 500:
        print("Your ticket fee is USD5")
        fee = 5
    elif sal >= 500 and sal < 5000:
        print("Your ticket fee is USD10")
        fee = 10
    else:
        print("Your ticket fee is USD50")
        fee = 50
    popcorn = input("Would you buy a pack of popcorn(USD7) ?\nUse 'Y' for yes and 'N' for no  ")
    if popcorn == 'y' or popcorn == 'Y':
        number = int(input("How many packs would you want please ?  "))
        total = number * 7
        print("Got it!\nThe total cost of your popcorn is: " + str(total) + "USD.")
        grand_total = total + fee
        print("Together with your ticket, your total fee is: USD" + str(grand_total))
    elif popcorn == 'n' or popcorn == 'N':
        print("Okay" + name + "!\nThat is noted")
        print("Your fee is: USD" + str(fee))
    else:
        print("Sorry " + name + ", that is a wrong input.")
else:
    print("Sorry!\nYou are not allowed to watch in Netflixson's movie centre.")
print("Thanks for trusting us!!!")
print("\nCode developed by Masino")
