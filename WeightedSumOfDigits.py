#!/usr/bin/env python

""" Weighted Sum Of Digits
python WeightedSumOfDigits.py

Ingrese la cantidad de datos: 36
Ingrese los numeros: 
30795 24153022 26815372 252 14 775595201 190 392826624 22444 12153460 370031539 
110384 24 322976725 2620239 72 0 4 31822150 1327799 208439 7938402 47928620 595 
677 1 11605351 7674 3 113872 12386 29 2625317 630 110196 227228

Output
85 78 150 18 9 154 19 199 54 109 178 79 10 230 111 11 0 4 88 193 111 100 143 
38 41 1 107 56 3 91 76 20 110 12 88 93
"""

cnt = raw_input("Ingrese la cantidad de datos: ")

data = raw_input("Ingrese los numeros: ").split()

sumDig = []

for i in range(0, int(cnt)):
	num = int(data[i])
	suma = 0 
	num = 1
	for j in data[i]:
		suma += int(j) * num
		num += 1
	
	sumDig.append(str(suma))


print "Resultados: "
print " ".join(sumDig)
