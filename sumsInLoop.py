#!/usr/bin/env python

""" Sum In Loop """

total = []

cnt = raw_input("Ingrese el total de numeros de datos: ")
print "Ingrese los numeros a sumar: "
for i in range(0, int(cnt)):
	data = raw_input().split()
	total.append(str(int(data[0]) + int(data[1])))

print ' '.join(total)
