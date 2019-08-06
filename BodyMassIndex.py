#!/usr/bin/env python
"""
python brayanestive18.py
Class for calculate the body mass index
DATA.lst is necessary that are the next data
first the total data, a continuation for row
the weight and height
Where weight is taken in kilograms and height in meters.
"""


class BodyMassIndex(object):
    """
    This is a class for calculate body mass index.
    data is array with data is reading in file DATA.lst
    """
    def __init__(self):
        """ The constructor for BodyMassIndex class. """
        self.data = self.get_data()
        self.calculate_body_mass_index()

    def calculate_body_mass_index(self):
        """ The function for calculate the boddy mass index"""
        result = []
        for x in self.data:
            result.append(float(x[0]) / pow(float(x[1]), 2))
        self.printResult(result)

    def printResult(self, result):
        """ The function for print the result. """
        index = []
        for mass in result:
            if mass < 18.5:
                index.append("under")
            elif 18.5 <= mass < 25.0:
                index.append("normal")
            elif 25.0 <= mass < 30.0:
                index.append("over")
            else:
                index.append("obese")

        print(' '.join(index))

    def get_data(self):
        """ The function for read file. """
        data_in_file = open("DATA.lst", 'r').readlines()
        size_data = int(data_in_file[0])
        array = []
        for i in range(1, size_data + 1):
            array.append(data_in_file[i].replace('\n', '').split(' '))
        return array


BodyMassIndex()
