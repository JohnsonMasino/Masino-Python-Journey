#!/usr/bin/python3
import random as rd

i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd is: ", i)
    i += 1
print("\nCode developed by Masino")    
