#!/usr/bin/python3
print("Python 3 development...")
num = int(input("Hello!\nWelcome to screen tree printer.\nWhat is the height of the tree you want to print ?  "))
print("Okay, Got it!\n")
top_space = num - 1
hashes = 1
stump_spaces = num - 1
while num != 0:
    for i in range(top_space):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print("\n")
    top_space -= 1
    hashes += 2
    num -= 1
for i in range(stump_spaces):
    print(' ', end="")
print("#")
print("\nCode developed by Masino")
