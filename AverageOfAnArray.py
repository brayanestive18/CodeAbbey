#!/usr/bin/env python

""" Average of an array
python AverageOfAnArray.py
Ingrese el numero de vectores:
input 11

Ingrese los vectores:
13618 4500 2908 8510 3484 11444 15543 0
25 142 95 49 113 0
628 1093 678 225 1118 1240 1703 476 821 1370 1246 1371 0
5256 7252 619 6710 3315 0
724 658 1161 923 1787 1920 1311 635 0
316 68 260 372 347 58 286 466 263 116 265 0
163 423 85 202 330 292 349 0
39 11919 6107 14329 10889 206 0
97 410 202 357 270 36 415 0
5290 5047 8117 8283 9623 0
770 212 997 329 910 137 249 912 882 631 784 539 644 0

output:
8572 85 997 4630 1140 256 263 7248 255 7272 615

"""
arr = []
result = []
cnt = input("Ingrese el numero de vectores: ")
print("Ingrese los vectores")
for i in range(0, int(cnt)):
    arr.append(input().split())

for el in arr:
    sum = 0
    avg = 0
    for n in el:
        if n != '0':
            sum += int(n)
    avg = sum / (len(el) - 1)
    result.append(str(round(avg)))

print(' '.join(result))