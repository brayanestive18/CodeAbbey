#!/usr/bin/env python

""" Triangles
python triangles.py

Ingrese el numero de triangulos: 24
Ingrese las longitudes de los lados A, B, C: 
507 1921 812
217 304 196
805 502 424
1510 2119 888
484 265 358
1974 1695 929
1563 572 949
2030 1537 997
507 824 1863
754 1306 2006
592 698 1032
396 1121 675
676 344 1252
706 1201 2896
1611 636 853
900 324 376
1570 1043 905
958 2896 1479
988 2392 593
814 736 411
260 134 253
551 949 293
701 676 1373
1190 2611 616

Output
0 1 1 1 1 1 0 1 0 1 1 0 0 0 0 0 1 0 0 1 1 0 1 0

"""
res = []
cnt = raw_input("Ingrese el numero de triangulos: ")
print "Ingrese las longitudes de los lados A, B, C: "
for i in range(0, int(cnt)):
	a, b ,c = raw_input().split()
	a = int (a)
	b = int (b)
	c = int (c)
	# Area = 0.25 * sqrt ((a + b - c) * (a - b + c) * (-a + b + c) * (a + b + c))
	# Si el argumento de la raiz es negativo, No se puede construir el triangulo
	arg = ((a + b - c) * (a - b + c) * (-a + b + c) * (a + b + c))

	if arg > 0:
		res.append("1")
	else:
		res.append("0")

print "Resultados: "
print " ".join(res)