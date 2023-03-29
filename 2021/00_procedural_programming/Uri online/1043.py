x, y, z = input().split()
x, y, z = float(x), float(y), float(z)

if x + y > z and x + z > y and y + z > x:
	print(f"Perimetro = {(x + y + z):.1f}")
else:
	tra = ((x + y)*z)/2
	print(f"Area = {tra:.1f}") 