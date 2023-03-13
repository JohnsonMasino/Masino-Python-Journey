#!/usr/bin/python3
print("Welcome to Johnson's printing press  ")
enter = input("Enter a single input here:  ")
if enter >= 'a' and enter <= 'z':
    print(f'You have entered a lower case letter.\nYour input is: "{enter}".\nThank you!')
elif enter >= 'A' and enter <= 'Z':
    print(f'You have entered an upper case letter.\nYour input is: "{enter}".\nThank you!')
else:
    print("Your input is a number.\nYou entered " + '"' + str(enter) + '"' + ".\nThank you!")
#enter1 = int(enter)
#print("The number you entered is: {enter1}.\nThank you!")
print("Have fun!!!")
print("\nCode developed by Masino")
