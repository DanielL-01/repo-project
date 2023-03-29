x, y = input().split()
x, y = float(x), float(y)
if x == 0 and y == 0:
	print("Origem")
else:
	if x > 0 and y > 0:
		if x == 0: 
			print("Eixo Y")
		elif y == 0:
			print("Eixo X")
		else: 
			print("Q1")

	elif x <= 0 and y >= 0:
		if x == 0: 
			print("Eixo Y")
		elif y == 0:
			print("Eixo X")
		else: 
			print("Q2")
	elif x <= 0 and y <= 0:
		if x == 0: 
			print("Eixo Y")
		elif y == 0:
			print("Eixo X")
		else: 
			print("Q3")
	elif x >= 0 and y <= 0:
		if x == 0: 
			print("Eixo Y")
		elif y == 0:
			print("Eixo X")
		else: 
			print("Q4")
