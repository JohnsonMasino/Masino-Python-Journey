#!/usr/bin/python3

nums = input("Hi there!\nEnter two numbers(separate them with a space) please:  ")
sort_nums = nums.split(" ")
nums0 = int(sort_nums[0])
nums1 = int(sort_nums[1])
operator = input("Please select an operator(+, -, /, or *): ")
if operator == '+':
    print(f"{nums0} {operator} {nums1} = " + str(nums0 + nums1))
elif operator == '-':
    print(f"{nums0} {operator} {nums1} = " + str(nums0 - nums1))
elif operator == '/':
    print(f"{nums0} {operator} {nums1} = " + str(nums0 / nums1))
elif operator == "*":
    print(f"{nums0} {operator} {nums1} = " + str(nums0 * nums1))
else:
    print("Sorry!\nWrong input. Read instructions and try again.")
print("Thanks for calculating with us!")
print("\nCode developed by Masino")
