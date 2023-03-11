#!/usr/bin/python3
print("Welcome to the land of the SPIRITS!!!")
print("Here, we only live not below and not more than 90 years...")
print("I am sorry but we all die at our 90th birthdays.\nHAHA! HAHA!! HAHA!!!")
print("Don't be afraid of death so you don't die multiple times...")

cur_age = input("What is your current age in years  ")
your_cur_day = (int(cur_age) * 365)
your_cur_week = (int(cur_age) * 52)
your_cur_month = (int(cur_age) * 12)

#90yrs in days is 90 * 365 = 32850
#90yrs in weeks is 90 * 52 = 4680
#90yrs in months is 90 * 12 = 1080

left_day = (32850 - your_cur_day)
left_week = (4680 - your_cur_week)
left_month = (1080 - your_cur_month)
left_year = (90 - int(cur_age))
print(f"You have:\n{left_day} days to live\n{left_week} weeks to live or\n{left_month} months to live.")
print("That is to say that you have " + str(left_year) + " year(s) to live so get ready as you age")

print("\nCode developed by Masino")
