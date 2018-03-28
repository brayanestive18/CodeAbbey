#!/usr/bin/env python

""" Minimum Of Two 
python minimumOfTwo.py

Ingrese el total de numeros de datos:
input 26

Ingrese los numeros:
Input:
464862 9550997
8302993 -9222100
-6297047 9626674
6187003 1652463
-294137 8920514
-9623151 -8958034
-3176737 -1676845
-3401419 7270660
-9613625 -6432657
1324564 -7334353
-4303307 -7370117
1235887 -7162362
-2955630 -9784534
9366482 6588609
7143866 6103967
-1211845 -2391272
5654965 -2908851
-1613372 9357917
-3282177 -5426368
1010380 6423686
-6505854 1387228
7465651 317409
9710383 -5935768
-2411931 -9903241
-2368425 8912633
-7237595 3328267

Output
464862 -9222100 -6297047 1652463 -294137 -9623151 -3176737 -3401419 -9613625 -7334353 -7370117 -7162362 -9784534 
6588609 6103967 -2391272 -2908851 -1613372 -5426368 1010380 -6505854 317409 -5935768 -9903241 -2368425 -7237595
"""

maxi = []

cnt = raw_input("Ingrese el total de numeros de datos: ")
print "Ingrese los numeros: "
for i in range(0, int(cnt)):
	data = raw_input().split()
	if int(data[0]) < int(data[1]):
		maxi.append(data[0])
	else: 
		maxi.append(data[1])

print ' '.join(maxi)