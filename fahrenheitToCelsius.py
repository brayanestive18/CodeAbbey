#!/usr/bin/env python

""" Fahrenheit To Celsius 
python fahrenheitToCelsius.py

Ingrese los datos:
Input:
38 73 587 59 106 290 359 224 340 414 192 476 575 210 75 437 309 403 218 
491 62 47 521 96 340 41 517 347 235 275 381 97 317 368 125 391 57 452 584

Output
23 308 15 41 143 182 107 171 212 89 247 302 99 24 225 154 206 103 255 17 
8 272 36 171 5 269 175 113 135 194 36 158 187 52 199 14 233 307

"""

fahre = raw_input("Ingrese los datos: ").split()
cel = []

for i in range(1, int(fahre[0]) + 1):
	cel.append(str(int(round((int(fahre[i])-32)/1.8))))

print "Grados Celsius: "
print ' '.join(cel)