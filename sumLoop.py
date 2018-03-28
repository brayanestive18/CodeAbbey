#!/usr/bin/env python

""" Suma de varios numeros en ciclo """

cnt = raw_input("Ingrese el total de numeros a sumar: ")
sum = raw_input("Ingrese los numeros a sumar, separados por un espacio: ").split()
total = 0

for i in range(0, int(cnt)):
	total = total + int(sum[i])

print total 