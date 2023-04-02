#!/usr/bin/python3

#This code calculates the average of heights
#Takes input from user.


height_input = input("Enter heights(in meters) and separate with a comma: ")
height_input.split(",")
print("Entered data is: ", height_input)
first_element_num = (height_input[0])
print("The first element is: ", first_element_num)
for first_element_num in range(0, 9):
    num = 1
    if height_input[num] == "":
        print("No more items in the list")
        break
    first_element_num = first_element_num + int(height_input[num])
    num += 1
    continue
print("The sum of all items is: ", first_element_num)
print("\nCode developed by Masino")
