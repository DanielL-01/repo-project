import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

d = b**2 - (4 * a * c) 



if d >= 0 and a > 0:
	r1 = (-b + math.sqrt(d))/ (2 * a)
	r2 = (-b - math.sqrt(d))/(2 * a)

	print(f"R1 = {r1:.5f}")
	print(f"R2 = {r2:.5f}")
else:
	print("Impossivel calcular")