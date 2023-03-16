#!/usr/bin/python3

import random as rd

print("Code execution starts here...")
num0 = rd.randint(0, 3)
print(num0)
num1 = rd.randrange(3, 5)
print(num1)
num2 = rd.random()
print(num2)
num3 = rd.uniform(1,3)
print(num3)
nums = [2, 4, 9, 0, 30, 45]
num4 = rd.choice(nums)
print(nums)
print(num4)
rd.shuffle(nums)
print(nums)
a = rd.choice(nums)
print(a)
print("Code execution ended here...")
print("\nCode developed by Masino")
