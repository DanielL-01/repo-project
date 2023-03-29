def triangle(n1, n2):
		return n1 * n2 / 2
def circle(c):
		return 3.14159 * c**2
def trapezium(a, b, c):
		return (a + b)* c/ 2
def square(n7):
		return n7**2
def rectangle(n8, n9):
		return n8 * n9




a, b, c = input().split()

print(f"TRIANGULO: {triangle(float(a), float(c)):.3f}")
print(f"CIRCULO: {circle(float(c)):.3f}")
print(f"TRAPEZIO: {trapezium(float(a), float(b), float(c)):.3f}")
print(f"QUADRADO: {square(float(b)):.3f}")
print(f"RETANGULO: {rectangle(float(a), float(b)):.3f}")

