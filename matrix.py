#!/usr/bin/python3

print("Welcome to the matrix world...")
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Below is our matrix stand for today:")
print(lists[0])
print(lists[1])
print(lists[2])
number = input("Enter row and colum(separate with a comma) of a number to access it: ")
sort_number = number.split(",")
num00 = sort_number[0]
num01 = sort_number[1]
num0 = int(num00)
num1 = int(num01)
matrix = lists[num0 - 1][num1 - 1]
print(matrix)
#print("Tha value in that position is: " + str(matrix))
print("\nCode developed by Masino")
