#!/usr/bin/python3

input_numbers = input("Hello!\nEnter some numbers(Only single numbers) here and separate them with a space: ")
sorted_number = input_numbers.split(" ")
print(sorted_number)
sorted_number_set = set(sorted_number)
print(sorted_number_set)
sorted_number_tuple = tuple(sorted_number_set)
print(sorted_number_tuple)
print("Sorry for the much conversions but we will work with this tuple...")
maxx = sorted_number_tuple[0]
new_maxx = max(sorted_number_tuple)
print(f"{maxx} is the first number in this tuple and it is automaticaly the maximum number till we detect another maximum number")
for number in sorted_number_tuple:
    print(number)
    if number == new_maxx:
        print(f"{number} is the new detected maximum in this tuple")
else:
    print("Done with tuple.\nOut of loop block.")
#print(max(sorted_number_tuple))
print("\nCode developed by Masino")
