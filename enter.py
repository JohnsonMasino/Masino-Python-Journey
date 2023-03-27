#!/usr/bin/python3

while False:
    try:
        num = int(input("Enter '0' here: "))
        break
    except ValueError:
        print("You did not enter '0'")
    except:
        print("An unknown error occurred")
print("Thank you for entering a '0'")
print("\nCode developed by Masino")
