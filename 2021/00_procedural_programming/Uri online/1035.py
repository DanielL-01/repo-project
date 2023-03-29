a, b, c, d = input().split()

A = int(a)
B = int(b)
C = int(c)
D = int(d)
"""
b > c and d > a
c + d > a + b
c and d >= 0
a $ 2 = 0
"""

if B > C and D > A:
	if C + D > A + B:
		if C >= 0 and D >= 0:
			if A % 2 == 0:
				print("Valores aceitos")
			else:
				print("Valores nao aceitos")
		else:
			print("Valores nao aceitos")
	else:
		print("Valores nao aceitos")
else:
	print("Valores nao aceitos")


