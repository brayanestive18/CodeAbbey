#!/usr/bin/env python

""" Sum of digits
sumOfDigits.py

Ingrese la cantidad de datos: 15
Ingrese los datos:
31 135 9
235 28 65
28 105 172
64 11 98
179 48 136
325 203 65
360 256 28
43 9 144
302 171 17
263 187 128
250 203 18
266 77 36
392 91 106
339 133 114
140 262 145

Output
18 21 7 10 25 16 28 9 26 25 26 16 30 12 24

"""

cnt = int(raw_input("Ingrese la cantidad de datos: "))
print "Ingrese los datos: "
sums = []

for i in range(0, cnt):
	data = raw_input().split()
	a = int(data[0])
	b = int(data[1])
	c = int(data[2])

	dig = a * b + c
	res = 0
	while dig >= 10:
		res += dig % 10
		dig = dig / 10

		if dig < 10:
			res += dig

	sums.append(str(res))

print "Los resultados son: "
print ' '.join(sums)