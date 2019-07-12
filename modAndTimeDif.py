#!/usr/bin/env python

""" Module and time difference
python modAndTimeDif.py

Ingrese la cantidad de datos: 12
Ingrese las fechas:
0 20 40 57 13 18 29 37
12 13 23 22 19 20 43 4
3 8 50 2 8 19 48 6
15 21 27 39 16 17 14 1
8 11 59 33 20 2 16 56
11 7 56 40 27 18 59 34
25 20 9 6 29 14 57 22
10 12 40 7 28 17 29 5
18 15 26 51 29 7 1 38
10 7 48 56 13 0 56 15
4 16 23 20 21 0 2 57
12 14 0 2 17 14 49 52

Output
(12 21 48 40) (7 7 19 42) (5 10 58 4) (0 19 46 22) (11 14 17 23) (16 11 2 54) 
(3 18 48 16) (18 4 48 58) (10 15 34 47) (2 17 7 19) (16 7 39 37) (5 0 49 50)

"""
from pip._vendor.distlib.compat import raw_input

cnt = int(raw_input("Ingrese la cantidad de datos: "))

print("Ingrese las fechas: ")
res = []

for i in range(0, cnt):
	data = raw_input().split()
	
	d1 = int(data[0])
	h1 = int(data[1])
	m1 = int(data[2])
	s1 = int(data[3])
	d2 = int(data[4])
	h2 = int(data[5])
	m2 = int(data[6])
	s2 = int(data[7])

	# Pasamos todo a segundos
	ts1 = (d1 * 86400) + (h1 * 3600) + (m1 * 60) + s1
	ts2 = (d2 * 86400) + (h2 * 3600) + (m2 * 60) + s2

	dif = ts2 - ts1
	
	# Volvemos la diferencia a su respectivas unidades
	s1 = int(dif % 60)
	dif /= 60
	m1 = int(dif % 60)
	dif /= 60
	h1 = int(dif % 24)
	dif /= 24
	d1 = int(dif)

	res.append('(' + str(d1) + ' ' + str(h1) + ' ' + str(m1) + ' ' + str(s1) + ')')

print("Resultados: ")
print(' '.join(res))
