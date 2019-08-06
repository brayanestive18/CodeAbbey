#!/usr/bin/env python
"""Array Checksum
brayanestive18.py
DATA.lst
"""


class ArrayChecksum:

    def __init__(self):
        file = open("DATA.lst", 'r')
        data_file = file.readlines()
        self.calculate_checksum(data_file)

    def calculate_checksum(self, data):
        result = 0
        cnt = data[0]
        array = data[1].split(" ")
        for num in array:
            result += int(num)
            result *= 113
            result = result % 10000007

        print("Result is: " + str(result))


ArrayChecksum()
