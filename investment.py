#!/usr/bin/python3

invest = int(input("Hi there!\nWhat is your investment amount ?  "))
rate = int(input("Got it!\nNow tell us your expected interest rate(in percentage):  "))
print(f"Your investment is: USD{invest}.\nYour interest rate is: {rate}%.")
year = int(input("Calculate profit after how many years ?  "))
profit = invest + (invest * rate)
print(f"Your profit after {year} years is: USD{profit}")
print("\nCode developed by Masino")
