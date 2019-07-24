#!/usr/bin/env python

"""Array Checksum
ArrayChecksum.py
Inpunt array size: 26
Input array: 59 8 58098721 4 515 3912 1588 902 3464646 401 16293 54579 86101 74 157 493 3596066 530 260883011 230772011 2351597 155846 9345 3 328367456 4377787

Output
2236682
"""
array = []
result = 0
cnt = input("Inpunt array size: ")
data = input("Input array: ")
array = data.split(" ")

for num in array:
    result += int(num)
    result *= 113
    result = result % 10000007

print("Result is: " + str(result))