#!/usr/bin/python3

#letter = input("Please enter a letter here")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for letter in letters:
#    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letter = input("Enter an upper case letter here: ")
    """if letter in letters:
        print("You have entered an upper case  letter")
        break
        """
    if letter == 'C' or letter == "F" or letter == 'A':
        print("Sorry...\nThis is an upper case letter but it is not supported.")
        continue
    elif letter in letters:
        print("You have entered an upper case  letter")
        break
    else:
        print("You have not entered an upper case letter")
        continue
else:
    print("Thank you for obeying the rule")
print("\nCode developed by Masino")
