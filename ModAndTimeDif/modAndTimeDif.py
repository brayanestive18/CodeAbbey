#!/usr/bin/env python

""" Module and time difference
Solution problem # 12 - Module and time difference

"""

cnt = int(raw_input("Ingrese la cantidad de datos: "))

print "Ingrese las fechas: "
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
	s1 = dif % 60
	dif /= 60
	m1 = dif % 60
	dif /= 60
	h1 = dif % 24
	dif /= 24
	d1 = dif

	res.append('(' + str(d1) + ' ' + str(h1) + ' ' + str(m1) + ' ' + str(s1) + ')')

print "Resultados: "
print ' '.join(res)

"""
python modAndTimeDif.py
"""
