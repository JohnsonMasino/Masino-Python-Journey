#!/usr/bin/python3

seta = {3, 4, 1, 0, 9, -9, -5}
setb = {0, 7, 8, 6, 9, -3, -1}
print(seta)
print(setb)
seta = setb
print(seta)
print(seta.intersection(setb))
print(seta & setb)
seta = {3, 4, 1, 0, 9, -9, -5}
seta.intersection_update(setb)
print(seta)
print("\ncode developed by Masino")
