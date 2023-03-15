#!/usr/bin/python3

print("Welcome!\nWorkings starts here: ")
lists = [2, 0, 3, 12, 90, 0, 7, 0, 5, 5]
print(lists)
print(lists[0:3])
print(lists[:5])
print(lists[1:3:1])
print("To sort these numbers: ")
lists.sort()
print(lists)
print("To reverse these numbers: ")
lists.reverse()
print(lists)
print("To print maximum number: " + str(max(lists)))
print("To print minimum number: " + str(min(lists)))
print("End of execution!")
print("\nCode developed by Masino")
