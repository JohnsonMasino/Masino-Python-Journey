#!/usr/bin/python3
leap = int(input("Enter a year here:  "))
if (leap % 4) == 0:
    print("Let us find out yet")
    if (leap % 100) == 0:
        print("This is the final verification step")
        if (leap % 400) == 0:
            print(f"Got it!\n{leap} is a leap year")
        else:
            print("Oh no!\nSadly, " + str(leap) + "is not a leap year")
    else:
        print(f"{leap} is a leap year")
else:
    print("Not a leap year")
print("Thanks for verifying wih us")
print("\nCode developed by Masino...")
