#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$ pylint brayanestive18.py
$ python brayanestive18.py
Calculate the body mass index
DATA.lst is necessary that are the next data
first the total data, a continuation for row
the weight and height
Where weight is taken in kilograms and height in meters.
"""


def get_data():
    """ The function for read file. """
    return open("DATA.lst", 'r').readlines()


def normalize_data(element):
    """ Function for normaize data of list. """
    return element.replace('\n', '').split(' ')


def convert_list_str_to_list_float(list_str):
    """ Funtion for conver str list to int list. """
    return [float(list_str[0]), float(list_str[1])]


def calculate_body_mass_index(item):
    """ The function for calculate the boddy mass index. """
    return item[0] / pow(item[1], 2)


def filter_list_size(item):
    """ Function validate that size the item is equals two. """
    return len(item) == 2


def print_result(mass):
    """ The function for print the result. """
    if mass < 18.5:
        return "under"
    elif 18.5 <= mass < 25.0:
        return "normal"
    elif 25.0 <= mass < 30.0:
        return "over"
    elif mass >= 30.0:
        return "obese"
    else:
        raise RuntimeError()


result = list(map(normalize_data, get_data()))
result = list(filter(filter_list_size, result))
result = list(map(convert_list_str_to_list_float, result))
result = list(map(calculate_body_mass_index, result))
result = list(map(print_result, result))
print(' '.join(result))
