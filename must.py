#!/usr/bin/python3

#This program forces you to enter a number.
#Code devloped by Masino.

while True:

    try:

        number = int(input("Please enter a number here:"))
        
        break

    except ValueError:
        print("You did not enter a number")
    
    except:

        print("An unknown error occurred")
print("You Obeyed the rule")        
print("\nCode developed by Masino")        
