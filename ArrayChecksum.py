#!/usr/bin/env python

from functools import reduce

"""Array Checksum
brayanestive18.py
DATA.lst
"""


def read_file(name_file):
    return open(name_file, 'r').readlines()[1].split(" ")


def calculate_checksum(result=0, element=0):
    result += element
    result *= 113
    result = result % 10000007
    return result


data_list_int = list(map(int, read_file("DATA.lst")))

print(reduce(calculate_checksum, data_list_int, 0))

