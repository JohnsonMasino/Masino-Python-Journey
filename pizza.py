#!/usr/bin/python3
cost = 0
name = input("Hi dear!\nWelcome to The Pizza House.\nWhat is your name please ?  ")
pizza = input(f"Welcome here {name}...\nDo you need pizza today ?\nUse 'Y' for yes and 'N' for no... ")
if pizza == 'y' or pizza == 'Y':
    print(f"Got it {name}!\nOur pizza sizes and prices include:")
    print("1. Small(2.8kg) >>> NGN800.\n2. Medium(4.2kg) >>> NGN1200.\n3. Large(7.3kg) >>> NGN2200.")
    number = int(input("Enter 1, 2 or 3 for your preferred pizza. "))
    if number == 1:
        print("Got it!\nYou will pay NGN800 for this pizza")
        cost = 800
    elif number == 2:
        print("Got it!\nYou will pay NGN1200 for this pizza")
        cost = 1200
    elif number == 3:
        print("Got it!\nYou will pay NGN2200 for this pizza")
        cost = 2200
    else:
        print(f"Sorry {name}!\nThat's a wrong input. Try again")
    sadine = input("Would you want some sardine(NGN300 per cup) with your pizza ?\nY / N  ? ")
    if sadine == 'Y' or sadine == 'y':
        sadine_number = int(input("How many cups of sadine would do ? "))
        sadine_cost = sadine_number * 300
        print(f"Your ordered sadine will cost {sadine_cost}.")
        total = sadine_cost + cost
        print(f"Your total expenditure is {total}.")
    elif sadine == 'n' or sadine == 'N':
        print(f"Alright {name}! that is noted.")
        print(f"Your expenditure is {cost}.\nThank you!")
    else:
        print("That is a wrong input.\nTry again")
    sauce = input("How about a sauce for your pizza(NGN200 per spatula) ?\nY / N ?  ")
    if sauce == 'y' or sauce == 'Y':
        sauce_number = int(input("How many spatula measures will do ?  "))
        sauce_cost = sauce_number * 200
        print(f"The cost of your ordered sauce is {sauce_cost}.")
        grand_total = sauce_cost + total
        print(f"Well shopped {name}!\nYour grand total for this session is: {grand_total}")
        print("Thanks for your session.\nWe expect you next time please...\nEnjoy!!!")
    elif sauce == 'n' or sauce == 'N':
        print(f"Alright {name}.\nNo sauce at all okay? Right!")
    else:
        print("So sorry!\nWrong input there.\nTry again.")
elif pizza == 'n' or pizza == 'N':
    print(f"Okay {name}!\nThanks for reaching out today.")
else:
    print(f"Sorry!\nThis is a wrong input.\nTry again {name}")
print(f"Have a nice day {name}...")
print("\nCode developed by Masino")
