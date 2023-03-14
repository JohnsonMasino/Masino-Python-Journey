#!/usr/bin/python3

print("Welcome to our love rate calculation.")
print('Our checker(Key) value is "TRUE LOVE" = 7 letters')
print("'t','r','u','e','l','o','v'.\nLetter 'e' appeared 'twice' so we will count it only once.")
print("We will find out how many times these letters appeard in both your names")
print("We will find out the percentage of the total letters that appeard and rate your love\nLet's do this!!!")
names0 = input("Enter your full name here:  ")
names1 = input("Enter your partner's full name here:  ")
names = names0 + " " + names1
edited_names = names.lower()
count0 = edited_names.count("t")
print("The total number of letter 't' in both your names is: " + str(count0))
count1 = edited_names.count("r")
print("The total number of letter 'r' in both your names is: " + str(count1))
count2 = edited_names.count("u")
print("The total number of letter 'u' in both your names is: " + str(count2))
count3 = edited_names.count("e")
print("The total number of letter 'e' in both your names is: " + str(count3))
count4 = edited_names.count("l")
print("The total number of letter 'l' in both your names is: " + str(count4))
count5 = edited_names.count("o")
print("The total number of letter 'o' in both your names is: " + str(count5))
count6 = edited_names.count("v")
print("The total number of letter 'v' in both your names is: " + str(count6))
total_count = count0 + count1 + count2 + count3 + count4 + count5 + count6
print(f"The total occurence of these letters is: {total_count}")
percent = float((total_count * 100) / 7)
final_percent = round(percent, 2)
print(f"The percentage occurence is: {final_percent}%")
if final_percent < 50:
    print("Love exists between the two of you.\nEnjoy!!!")
elif final_percent >= 50 and final_percent < 100:
    print("Wow!\nThere's so much love between you two. Have fun!!!")
elif final_percent >= 100 and final_percent < 150:
    print("Awesome!\nThe bond is strong!\nKeep it tight")
elif final_percent >= 150 and final_percent < 200:
    print("This type of love is rare!\nOnly 5% in existence.\nPlease keep this bond strong")
else:
    print("Hmm...\nThis love suparceeds that of Romeo and Julieth.\nDon't let it die please! Keep the bond stronger than a rock.")
feedback = input("Leave us a feedback please!\nAre you satisfied ?\nUse 'Y' for yes and 'N' for no:  ")
if feedback == 'Y' or feedback == 'y':
    print("Thank you for this positive feedback!")
elif feedback == 'N' or feedback == 'n':
    print("Oh well! We will improve. Thank you!")
else:
    print("Sorry!\nWrong input")
print("Take care, stay safe and be fine!!!")    
print("\nCode developed by Masino")
