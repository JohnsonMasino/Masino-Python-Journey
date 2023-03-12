#!/usr/bin/python3

height = float(input("Enter your height here in m: "))
weight = int(input("Enter your weight here in kg: "))
print("To calculate your body mass index, we divide your weight by the square of your height")
BMI = (weight / (height ** 2))
bmi = round(BMI, 1)
print(f"Your total body mass index is: {bmi}kg/m^2.\nNow we will classify you in our BMI chart.")
if (bmi < 16):
    print("You are underweight (Severe  thinness).")
elif (bmi >= 16 and bmi <= 16.9):
    print("You are underweight (Moderate thinness).")
elif (bmi >= 17 and bmi <= 18.4):
    print("You are underweight (Mild thinness).")
elif (bmi >= 18.5 and bmi <= 24.9):
    print("Cool!\nYour Body Mass Index is at a normal range.\nWatch it closely!!!")
elif (bmi >= 25 and bmi <= 29.9):
    print("Overweight (Pre-Obese).")
elif (bmi >= 30 and bmi <= 34.9):
    print("Obese (Class I).")
elif (bmi >= 35 and bmi <= 39.9):
    print("Obese (Class II).")
else:
    print("You are Obese (Class III).")
print("\nCode developed by Masino")
