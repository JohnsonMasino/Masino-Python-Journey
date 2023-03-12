#!/usr/bin/python3
print("Welcome to Johnson's BMI calculator!")
print("Here, you will find out your body mass condition")
name = input("Tell us your name please: ")
print("Welcoming " + name + "...")
height = float(input("Enter your height here in m: "))
weight = int(input("Enter your weight here in kg: "))
print("To calculate your body mass index, divide your weight by the square of your height")
BMI = (weight / (height ** 2))
bmi = round(BMI, 1)
print(f"{name}, Your total body mass index is: {bmi}kg/m^2.\nNow we will classify you in our BMI chart.")
if (bmi < 16):
    print(name + ", You are underweight (Severe  thinness).")
elif (bmi >= 16 and bmi <= 16.9):
    print(name + ", You are underweight (Moderate thinness).")
elif (bmi >= 17 and bmi <= 18.4):
    print(name + ", You are underweight (Mild thinness).")
elif (bmi >= 18.5 and bmi <= 24.9):
    print(f"Cool one! {name}\nYour Body Mass Index is at a normal range.\nWatch it closely!!!")
elif (bmi >= 25 and bmi <= 29.9):
    print("You're overweight {name} (Pre-Obese).")
elif (bmi >= 30 and bmi <= 34.9):
    print(f"You're obese {name} (Class I).")
elif (bmi >= 35 and bmi <= 39.9):
    print(f"You're obese {name}. (Class II).")
else:
    print(f"You are Obese {name}. (Class III).")
print("\nCode developed by Masino")
