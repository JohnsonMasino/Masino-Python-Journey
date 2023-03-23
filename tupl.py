#!/usr/bin/python3

tupl1 = (1, 8, 0, -8, -35, 77, 99)
tupl2 = (77, 0, 0, 22, 44, -9, 3)
tupl3 = (tupl1, tupl2)
number0 = tupl2.count(0)
print("The number of '0' in tuple 2 is: " + str(number0))
print(tupl3)
print(f"Tuple 1 is: {tupl1}.\nConverting to list is:")
print(list(tupl1))
print("The index of '0' is: " + str(tupl1.index(0)))

print("\nCode developed by Masino")
