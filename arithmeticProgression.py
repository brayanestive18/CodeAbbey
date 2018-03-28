#!/usr/bin/env python

""" Arithmetic Progression
python arithmeticProgression.py

Ingrese el numero de progresiones a realizar: 11
Ingrese los datos: 
15 1 78
5 19 18
29 9 86
8 0 58
7 14 30
17 20 15
2 6 95
12 16 67
23 13 73
6 0 88
2 10 94

Output
4173 2997 35389 464 6300 2355 26980 36180 35843 528 43898

"""
prg = []
cnt = raw_input("Ingrese el numero de progresiones a realizar: ")
print "Ingrese los datos: "
for i in range(0, int(cnt)):
	a, b, n = raw_input().split()
	flag = 0
	for j in range(0, int(n)):
		flag += int(a) + (int(b) * j)
	prg.append(str(flag))

print "Resultados: "
print " ".join(prg)