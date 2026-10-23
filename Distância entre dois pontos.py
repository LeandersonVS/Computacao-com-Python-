from math import hypot

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distancia = hypot(x2 - x1, y2 - y1)

if distancia >= 10:
	print("longe")
else:
	print("perto")
