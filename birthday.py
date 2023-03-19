#!/usr/bin/python3

name = input("Welcome to birthday authenticator!\nWhat is your name please ?  ")
country = input(f"Great to have you here {name}.\nWhat is your country please ?  ")
birthday = input(f"Got it {name}! Tell us your birthday.\nUse '/' to separate them in the order of\ndd/mm/yyyy  ")
sort_birth = birthday.split("/")
sort_birthday = int(sort_birth[2])
if (2023 - sort_birthday) <= 18:
    print("Your birthday is important!!!")
elif (2023 - sort_birthday) > 18 and (2023 - sort_birthday) < 65:
    print("Sorry!\nYour birthday is unimportant.")
else:
    print("Your birthday is important")
print("\nCode developed by Masino")
