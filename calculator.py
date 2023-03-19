#!/usr/bin/python3

expression = input("Hi there!\nWelcome to calculate.com.\nEnter your mathematical expression here.\nSeparate each character with a single space: ")
sort = expression.split(" ")
if sort[1] == '+':
    print(int(sort[0]) + int(sort[2]))
elif sort[1] == '-':
    print(int(sort[0]) - int(sort[2]))
elif sort[1] == '*':
    print(int(sort[0]) * int(sort[2]))
elif sort[1] == '/':
    print(int(sort[0]) / int(sort[2]))
elif sort[1] == '%':
    print(int(sort[0]) % int(sort[2]))
else:    
    print("Wrong input!\nTry reading instructions and try again.")
print("\nCode developed by Masino")    
