#!/usr/bin/python3

import random as rd
print("Hi!\nWelcome to randon name selector...")
names = input("Enter your names separated by comma:\n")
sort_names = names.split(",")
#print("Entered names are:")
#print(sort_names)
lenght = len(sort_names)
print("The number of names entered is: " + str(lenght))
print("Entered names are:")
print(sort_names)
select = rd.randint(0, (lenght - 1))
print("Congratulations!!!")
print(sort_names[select] + " is selected!")
print("\nCode developed by Masino")
