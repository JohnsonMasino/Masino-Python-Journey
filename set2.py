#!/usr/bin/python3

set_1 = {'Masino', 'Chuks', "King's web", 'Chike'}
set_2 = {'Joy', 'Alex', 'Ginika', 'Uju', 'Masino'}
print('Difference is: ' + str(set_1.difference(set_2)))
print(set_1 - set_2)
set_1.difference_update(set_2)
print(set_1)
print(set_1 ^ set_2)
print(set_1.symmetric_difference(set_2))
print(set_1.isdisjoint(set_2))
set_1.clear
print(set_1)
#set_2.del
print(set_2)
print("\nCode developed by Masino")
