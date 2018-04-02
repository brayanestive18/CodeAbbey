#!/usr/bin/env python

""" Linear Fuction
linearFuction.py

Ingrese la cantidad de datos: 12
Ingrese los valores x1 y1 x2 y2:
-521 -17628 533 18208
-948 -29377 -441 -13660
171 5941 796 27816
-30 273 396 -13359
564 -10902 -145 3278
-155 -15312 -494 -47178
655 -51541 -227 18137
463 -29658 711 -45282
244 15337 -96 -4723
463 -2019 -698 3786
-901 66308 -70 4814
-674 3438 746 -3662

Output
(34 86) (31 11) (35 -44) (-32 -687) (-20 378) (94 -742) (-79 204) (-63 -489) (59 941) (-5 296) (-74 -366) (-5 68)

"""

cnt = int(raw_input("Ingrese la cantidad de datos: "))
res = []

print "Ingrese los valores x1 y1 x2 y2: "

for i in range(0, cnt):
	data = raw_input().split()
	x1 = int(data[0])
	y1 = int(data[1])
	x2 = int(data[2])
	y2 = int(data[3])

	a = (y2 - y1) / (x2 - x1)
	b = y1 - (a * x1)

	res.append("("+str(a) + " " + str(b) + ")")

print "los valores encontrados (a b): "
print ' '.join(res)