#!/usr/bin/env python

""" Rounding 
python rounding.py

Ingrese el total de numeros de datos:
input 14

Ingrese los numeros:
Input:
9862220 -2676295
-4457028 4975858
4497 714
4813335 4289435
-7428849 2570543
5551989 844
16233 1700
19343 2000
18663 1880
6562957 -934214
9011 1040
7149374 677
4179220 708
9398113 449

Output
-4 -1 6 1 -3 6578 10 10 10 -7 9 10560 5903 20931

"""

div = []

cnt = raw_input("Ingrese el total de numeros de datos: ")
print "Ingrese los numeros: "
for i in range(0, int(cnt)):
	data = raw_input().split()

	d = float(data[0]) / float(data[1])
	d_i = d - int(d)

	if d_i >= 0.5:
		div.append(str(int(d) + 1))
	elif d_i >= 0 and d_i < 0.5:
		div.append(str(int(d)))
	else:
		if d_i >= -0.5:
			div.append(str(int(d)))
		else:
			div.append(str(int(d) - 1))

print ' '.join(div)