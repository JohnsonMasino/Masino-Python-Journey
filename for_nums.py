#!/usr/bin/python3

numbers = [2, -1, 0, 3, 5, 3, 3]
for number in numbers:
    print(number)
    if number == 0:
        print("0 detected...\nExited")
        break
else:
    print("Successfully exited!")
print("\nCode developed by Masino")    
