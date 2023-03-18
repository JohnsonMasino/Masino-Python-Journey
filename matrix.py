#!/usr/bin/python3

lists = [[1, 2, 3, 4], [7, 4, 5, 6], [7, 8, 9, 5], [5, 0, 1, 9], [2, 0, 1, 3]]
print("Welcome to the matrix world...")
lists0 = [1, 2, 3, 4]
lists1 = [7, 4, 5, 6]
lists2 = [7, 8, 9, 5]
lists3 = [5, 0, 1, 9]
lists4 = [2, 0, 1, 3]
print("Below is our matrix stand for today:")
print(f"{lists0}\n{lists1}\n{lists2}\n{lists3}\n{lists4}")
number = input("Enter row and colum(separate with a comma) to hide your money: ")
sort_number = number.split(",")
num0 = int(sort_number[0])
num1 = int(sort_number[1])
matrix = lists[num0 - 1][num1 - 1]
print("The element in this locations is: " + str(matrix))

lists[num0 - 1][num1 - 1] = "^"
print(lists[0])
print(lists[1])
print(lists[2])
print(lists[3])
print(lists[4])

print("\nCode developed by Masino")
