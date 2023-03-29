value = input().split()
numbers = []
for number in value:
	numbers.append(float(number))
numbers.sort(reverse=True)
a, b, c = float(numbers[0]), float(numbers[1]), float(numbers[2])



if a >= b + c:
	print("NAO FORMA TRIANGULO")
elif a **2 == b**2 + c**2:
	print("TRIANGULO RETANGULO")
elif a**2 > (b**2 + c**2):
	print("TRIANGULO OBTUSANGULO")
elif a **2 < (b**2 + c**2):
	print("TRIANGULO ACUTANGULO")
if a == b == c:
	print("TRIANGULO EQUILATERO")
if a == b != c or a == c != b  or b == c != a:
	print("TRIANGULO ISOSCELES")