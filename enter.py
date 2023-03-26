#!/usr/bin/python3

while True:
    try:
        num = int(input("Enter a number here: "))
        break
    except ValueError:
        print("You did not enter a number")
    except:
        print("An unknown error occurred")
print("Thank you for entereing a number")
print("\nCode developed by Masino")
