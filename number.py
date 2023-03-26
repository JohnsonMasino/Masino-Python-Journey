#!/usr/bin/python3

number = int(input("Enter the height of your pine tree here: "))
space = number - 1
star = 1
stump = number - 1
while number != 0:
    for i in range(space):
        print(" ", end="")
    for i in range(star):
        print("*", end="")
    print("\n")    
    space -= 1
    star += 2
    number -= 1
for i in range(stump):
    print(" ", end="")
print("*")    
print("\nCode developed by Masino")    
